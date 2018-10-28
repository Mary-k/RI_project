    
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
def tokenize_Funct(text):
        return  nltk.word_tokenize(text) #tokenize the raw UTF-8 text
def filter_stopWords_Funct(stopWords_path,tokenes_List):
        stopword_list=open(stopWords_path, 'r')
        filtered_words = [] #declare an empty list to hold our filtered words
        for word in tokenes_List: #iterate over all words from the text
          if word not in stopword_list and word.isalpha() and len(word) > 1: #only add words that are not in the French stopwords list, are alphabetic, and are more than 1 character
                 filtered_words.append(word) #add word to filter_words list if it meets the above conditions
        filtered_words.sort() #sort filtered_words list
        return filtered_words
def stemming_Function(filtered_words):
        stemmed_words = [] #declare an empty list to hold our stemmed words
        stemmer = FrenchStemmer() #create a stemmer object in the FrenchStemmer class
        for word in filtered_words:
         stemmed_word=stemmer.stem(word) #stem the word
         stemmed_words.append(stemmed_word) #add it to our stemmed word list
        stemmed_words.sort() #sort the stemmed_words
        return stemmed_words 


files_path='/home/mimi/Desktop/RI_Lab/corpus/'
stopWords_path='/home/mimi/Desktop/RI_Lab/lab01/stopwords_fr.txt'
filesList=['D1','D2','D3']
noPunct=[]
tokenes_List=[]
filtered_words=[]
stems_list=[]
for fileName in filesList:  
    with open(files_path+fileName+'.txt',) as myfile:
        bruteText=myfile.read().replace('\n', '')
        bruteText=bruteText.lower()
        myfile.close
        noPunct.append(punctuation_removal_funct(bruteText))

for target in noPunct:
        tokenes_List.append(tokenize_Funct(target))

for toks_list in tokenes_List:
        filtered_words.append(filter_stopWords_Funct(stopWords_path,toks_list))

#call stemming function
'''
for target_list in words:
        print(target_list)
        print( )
'''
