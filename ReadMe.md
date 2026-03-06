# Media Coverage and Inflation (1919–1963)

## Project Overview

In recent years, inflation and purchasing power have been central topics in political and media discussions. This project investigates the relationship between **actual inflation rates** and **media coverage of inflation**.

Specifically, we study whether periods of **high inflation coincide with increased media attention** to the topic.

The project is inspired by the research paper from the Banque de France titled *"Using the press to construct a new indicator of inflation perception in France"* (Working Paper No. 921, 2023). While this research focuses on France and recent data, this project applies a similar approach to a **historical context in the United States**.

We analyze the relationship between inflation and press coverage between **1919 and 1963** using a large historical newspaper corpus.

---

## Research Question

**Do periods of high inflation coincide with increased media coverage of inflation?**

---

## Data

Two main data sources are used:

- **Inflation data** from the Federal Reserve Bank of St. Louis (FRED database)
- **Historical newspapers** from the Library of Congress

The newspaper dataset includes **national and local US newspapers published between 1919 and 1963**, representing **more than 20GB of text data**.

---

## Methodology

The analysis is conducted in several steps:

### 1. Inflation Data Analysis

- Download inflation data from FRED
- Clean and process the time series
- Identify periods of high inflation

### 2. Newspaper Corpus Analysis

- Identify articles related to inflation using lexical keywords
- Process and structure the newspaper data
- Compute frequencies of inflation-related terms over time
- Visualize media attention to inflation

### 3. Comparison Between Inflation and Media Coverage

- Aggregate frequency indicators
- Compare media coverage with inflation dynamics

### 4. Modeling

- Linear regression analysis
- Sentiment analysis of inflation-related articles

---

## Main Results

Preliminary results suggest a **strong correlation between inflation levels and media coverage**, although the relationship varies across historical periods and economic contexts.

These findings highlight the interaction between **economic reality** and **media representation of economic issues**.

---



The main analysis is available in: Main_Inflation.ipynb




---
## How to use
The two notebooks are used to download the articles and to compute the csv of frequency later used in the main notebook

---

## Technologies Used

- Python
- Pandas
- NLP methods for text processing
- Data visualization libraries

---

## References

- Banque de France Working Paper 921 (2023)  
- Library of Congress Historical Newspaper Archive  
- FRED – Federal Reserve Economic Data