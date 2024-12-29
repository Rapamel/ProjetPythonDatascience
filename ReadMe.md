Pour s'assurer d'avoir toutes les bibliotheques il est recommandé d'utiliser "pip install -r requirements.txt" dans la console

Nous avons ajouté le .env au repo GitHub pour des raisons de simplicité et le repo est privé de toute manière mais nous sommes conscients que ce n'est pas une bonne pratique
Concernant le fichier .env les clés AWS sont les miennes et expire après une semaine donc il peut être nécessaire de contacter raphael.pereira@ensae.fr ou simplement d'utiliser vos propre clés AWS SSP Cloud 
Tout les fichiers de données sont déjà uploader sur SSP Cloud

Le fichier getNews.py sert à récuperer les articles parlant de prêt ou de loin d'inflation il faut le lancer dans la console avec les arguments suivant :
    - Année de début
    - Année de fin
    - Le nombre d'années à télécharger à chaque étape
Le code va télécharger des fichiers targz à l'aide l'API puis les décompresser, les lire puis les effacer et recommencer jusqu'à avoir fait toutes les années. Je recommande de mettre 3 années à la fois et sur mon pc cela prend quelques heures.


Main_Inflation est le notebook principal


Analyse_NLP_frequentielle est le notebook qui sert à calculer les csv de fréquences qui sont upload sur SSP Cloud (le notebook ne les upload pas, tout avait été fait en local et on a upload à la main)