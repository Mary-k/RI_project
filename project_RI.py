    
#Création d’un fichier inverse de fréquences
import re
import string
import math
import nltk
from nltk.stem.snowball import FrenchStemmer #import the French stemming library

#ps:language is french

def punctuation_removal_funct(textBrute):
    translator = str.maketrans('', '', string.punctuation)
    return bruteText.translate(translator)
def tokenize_Funct(text):
        return  nltk.word_tokenize(text) #tokenize the raw UTF-8 text
def filter_stopWords_Funct(stopWords_path,tokenes_List):
        from nltk import FreqDist
        stopword_list=open(stopWords_path, 'r')
        filtered_words = [] #declare an empty list to hold our filtered words
        for word in tokenes_List: #iterate over all words from the text
          if word not in stopword_list and word.isalpha() and len(word) > 1: #only add words that are not in the French stopwords list, are alphabetic, and are more than 1 character
                 filtered_words.append(word) #add word to filter_words list if it meets the above conditions
        return filtered_words
def stemming_Function(filtered_words):
        stemmed_words = [] #declare an empty list to hold our stemmed words
        stemmer = FrenchStemmer() #create a stemmer object in the FrenchStemmer class
        for word in filtered_words:
         stemmed_word=stemmer.stem(word) #stem the word
         stemmed_words.append(stemmed_word) #add it to our stemmed word list
        
        freqdist = nltk.FreqDist(stemmed_words)
        return freqdist
def invertedIndeces_Funct(outputFile_path):
        FileSave=open(outputFile_path+'invertedIndeces.txt','w')
        #for each file freqDist
        docIndex=1
        for target_freqdistr in stems_list:
                for token in target_freqdistr:                      
                        string='['+str(token)+','+str(docIndex)+']->'+str(target_freqdistr[token])+'\n'                       
                        frequency_file_list.append([token,docIndex-1,target_freqdistr[token]])
                        FileSave.write(string)
                docIndex +=1 
        FileSave.close
def getFrequency_Funct(term,documentId):
        freq=0
        for index_list in frequency_file_list :
                if index_list [0]== term and index_list [1]==documentId-1: 
                        freq=index_list[2]
        return freq
def get_max_Frequency_Funct(term,documentId):
        maxFreq=0
        for target_list in frequency_file_list:
                if target_list[0]==term and target_list[2]>maxFreq:
                        maxFreq=target_list[2]
        return maxFreq
def compute_ni_Funct(term):
        ni_count=0
        for target_list in frequency_file_list:
                
                if target_list[0]==term :
                       ni_count+=1 
                         
        return  ni_count
def tfIdf_function(term,documentId,nbDocs):
        #poids(ti, dj)=(freq(ti,dj)/Max(freq(t, dj))*Log((N/ni) +1)
        nb_docs_containt_ti=compute_ni_Funct(term)
        maxFreq=get_max_Frequency_Funct(term,documentId)
        freq_ti=getFrequency_Funct(term,documentId)
        return freq_ti/(maxFreq*math.log10((nbDocs/nb_docs_containt_ti)+1))      
def weighted_invertedIndeces_Funct(Nb_docs,invertedIndeces_file_path):
        FileSave=open(invertedIndeces_file_path+'weightedinvertedIndeces.txt','w')
        docIndex=1
       # weight=tfIdf_function(term,documentId)
        for target_freqdistr in stems_list:
                
                for token in target_freqdistr:       
                        weight=tfIdf_function(token,docIndex,Nb_docs)
                        string='['+token+','+str(docIndex)+']->'+str(weight)+'\n'                       
                        FileSave.write(string)
                docIndex +=1 
        FileSave.close

files_path='/home/mimi/Desktop/RI_Lab/corpus/'
stopWords_path='/home/mimi/Desktop/RI_Lab/lab01/stopwords_fr.txt'
filesList=['D1','D2','D3']
noPunct=[]
tokenes_List=[]
filtered_List=[]
stems_list=[]
freqDicts_list=[]
invertedIndeces=[]
frequency_file_list=[]
invertedIndeces_file_list=dict
for fileName in filesList:  
    with open(files_path+fileName+'.txt',) as myfile:
        bruteText=myfile.read().replace('\n', '')
        bruteText=bruteText.lower()
        myfile.close
        noPunct.append(punctuation_removal_funct(bruteText))

for target in noPunct:
        tokenes_List.append(tokenize_Funct(target))

for toks_list in tokenes_List:
        filtered_List.append(filter_stopWords_Funct(stopWords_path,toks_list))

for target in filtered_List:
        stems_list.append(stemming_Function(target))

invertedIndeces_Funct(files_path)

weighted_invertedIndeces_Funct(3,files_path)