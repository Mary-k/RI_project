    
#Création d’un fichier inverse de fréquences
import re
import string
import math
import nltk
from nltk.stem.snowball import FrenchStemmer #import the French stemming library

#ps:language is french


'''
1--Création d’un fichier inverse de fréquences :
[Mot, document]->fréquences

2-- Création d’un fichier inverse de poids : [Mot, document]->poids ----- TF*IDF: poids(ti, dj)=(freq(ti,dj)/Max(freq(t, dj))*Log((N/ni) +1)

3-- Fonctions d’accès
programmer deux fonctions d’accès de base.
1st : accepte un numéro de document, et retourne sa liste des mots avec leurs fréquences et leurs poids.
2nd :  accepte un mot, et retourne la liste des documents contenant ce mot avec sa fréquence et son poids dans chaque
document.
'''


'''
loop of the documents
filesList=['D1','D2','D3']
for fileName in filesList:   

'''
def punctuation_removal_funct(textBrute):
    translator = str.maketrans('', '', string.punctuation)
    return bruteText.translate(translator)

path='/home/mimi/Desktop/RI_Lab/corpus/'
noPunct=''
filesList=['D1','D2','D3']


for fileName in filesList:  
    with open(path+fileName+'.txt',) as myfile:
        bruteText=myfile.read().replace('\n', '')
        bruteText=bruteText.lower()
        myfile.close
        noPunct=punctuation_removal_funct(bruteText)
        print('\n')
        print(noPunct)
