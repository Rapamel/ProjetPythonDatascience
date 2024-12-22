import requests
import pandas as pd
import json
import os
from dotenv import load_dotenv
from functools import partial
import shutil
import tarfile

def load_credentials():
    load_dotenv()
    url="https://huggingface.co/api/datasets/dell-research-harvard/AmericanStories"
    token=os.getenv("HuggingFaceToken")
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    return headers


def download_targz(years):
    if isinstance(years, str):
        years=[years]
    os.makedirs("ArticlesTarGz", exist_ok=True)
    headers=load_credentials()
    for i in years:
        print(i, end=" ")
        file=f"faro_{i}.tar.gz"
        url=f"https://huggingface.co/datasets/dell-research-harvard/AmericanStories/resolve/main/{file}"
        wb=requests.get(url, headers=headers)
        print(wb.status_code)
        if wb.ok:
            with open("ArticlesTarGz/"+file, "wb") as f:
                f.write(wb.content)
        else:
            print(f"Error {wb.status_code} downloading {file}")


def extract_targz(years):
    if isinstance(years, str):
        years=[years]
    for i in years:
        print(i, end=" ")
        try :
            with tarfile.open(f"ArticlesTarGz/faro_{i}.tar.gz", "r:gz") as tar:
                tar.extractall(path=f"ArticlesTarGz/faro_{i}")
        except FileNotFoundError:
            print(f"Error extracting {i} The file is not found")

def fold_left_local(fonction, acc, years):
    if isinstance(years, str):
        years=[years]
    for i in years:
        print(i, end=" ")
        files=os.listdir(f"ArticlesTarGz/faro_{i}/mnt\\122a7683-fa4b-45dd-9f13-b18cc4f4a187/ca_rule_based_fa_clean/faro_{i}")
        for j in files:
            with open(f"ArticlesTarGz/faro_{i}/mnt\\122a7683-fa4b-45dd-9f13-b18cc4f4a187/ca_rule_based_fa_clean/faro_{i}/{j}") as f:
                data = json.load(f)
            acc=fonction(data, acc, (data["lccn"]["title"],data['edition']['date'],data['full articles']))
    return acc


def map_local(fonction,years):
    if isinstance(years, str):
        years=[years]
    acc=[]
    for i in years:
        print(i, end=" ")
        files=os.listdir(f"ArticlesTarGz/faro_{i}/mnt\\122a7683-fa4b-45dd-9f13-b18cc4f4a187/ca_rule_based_fa_clean/faro_{i}")
        for j in files:
            with open(f"ArticlesTarGz/faro_{i}/mnt\\122a7683-fa4b-45dd-9f13-b18cc4f4a187/ca_rule_based_fa_clean/faro_{i}/{j}") as f:
                data = json.load(f)
            if data['full articles']!=[]:
                try :
                    acc.append(fonction(data["lccn"]["title"],data['edition']['date'][:-3],data['full articles']))
                except:
                    acc.append(fonction("No titles found",data['edition']['date'][:-3],data['full articles']))
    return acc



def filter_and_freq(df,isInflation,title,date,articles):
    if not (date in df.keys()):
        df[date]=0,0
    for i in range(len(articles)): 
        f,n=df[date]
        if isInflation(articles[i]['article']):            
            df[date]=(f+1,n+1)
        else :
            df[date]=(f,n+1)
            articles[i]=None
    articles=[i for i in articles if i is not None]
    return (title,date,articles)

def get_freq_and_articles(isInflation,years):
    df={}
    f_f=partial(filter_and_freq,df,isInflation)
    df=pd.DataFrame(df).T
    return map_local(f_f,years),df

def slice_list(l,step):
    return [l[i:i+step] for i in range(0,len(l),step)]

def delete_files(years):
    if isinstance(years, str):
        years=[years]
    for i in years:
        try:
            os.remove(f"ArticlesTarGz/faro_{i}.tar.gz")
            shutil.rmtree(f"ArticlesTarGz/faro_{i}")
        except FileNotFoundError:
            print(f"Error deleting {i} The file is not found")

def get_freq_and_articles_global(isInflation,years,step):
    if isinstance(years, str):
        years=[years]
    chunks=slice_list(years,step)
    frequences=pd.DataFrame()
    for i in chunks:
        download_targz(i)
        extract_targz(i)
        articles,freq=get_freq_and_articles(isInflation,i)
        frequences=pd.concat([frequences,freq],axis=1)
        articles=[i for i in articles if i[2]!=[]]
        delete_files(i)
        df=[]
        for j in articles:
            a,b,c=j
            for k in c:
                df.append((a,b,k))
        df=pd.DataFrame(df,columns=["Title","Date","Article"])
        df.to_parquet(f"ArticlesParquet/{i[0]}-{i[-1]}.parquet")
    return frequences

def isInflation(article):
    return article.lower().find("inflation")!=-1
get_freq_and_articles_global(isInflation,[i for i in range(1918,1963)],3)