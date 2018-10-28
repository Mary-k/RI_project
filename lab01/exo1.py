import math
import string

numDocs=4
corpus=[]
path='/home/mimi/Desktop/RI_Lab/corpus/'
listFichier=['D1','D2','D3']

def filesToCorpus_func(corpus,path,listFichier):
    for file_index in listFichier:
        corpus.append(open(path+file_index+'.txt','r').readlines()) 

def remove_Punct_funct(corpus,no_punct_list):


    translator = str.maketrans('', '', string.punctuation)
    noPunct.append()
    
    