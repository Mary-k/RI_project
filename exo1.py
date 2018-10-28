def readFilesIntoListFunct(filesList,path):
    myList=[]
    listOfLists=[]
    for fichier in filesList:
        with open(path+fichier+'.txt') as f:
            myList.append(list(f))
    
    for target_list in myList:    
        listOfLists.append(target_list[0])
    return listOfLists

def punctuationREmovalFunct(list_of_texts):
    import string
    NoPunctList=[]
    for text in list_of_texts:       
        translator = str.maketrans('', '', string.punctuation)
        noPunctString=text.translate(translator)
        NoPunctList=noPunctString.split(' ')
    
    return NoPunctList

def indexationFunction(no_Punct_List):
    from collections import defaultdict        
    inv_indx = defaultdict(list)
    for idx, text in enumerate(no_Punct_List):
        for word in text:
            inv_indx[word].append(idx)        
    return inv_indx
def frequencyFunction(no_Punct_List):
    return liste_de_frequence

'''
def frequencyFunction(no_Punct_List):
    return liste_de_frequence

def max_frequency(frequencies_list):


    return the_max

def calcul_Poids(mot,Id_doc):
    import math
    nb_terms_doc=0
    nb_docs_of_term=0
    frequence=
    maxfrequenc=max_frequency(frequencies_list)
    return frequence/maxfrequenc*math.log10((Nb_docs/nb_docs_of_term)+1)

Nb_docs=len(files_List)
dictionnary=frequencyFunction(no_Punct_List)
'''
files_List=['D1','D2','D3']
pathVariable='/home/mimi/Desktop/RI_Lab/corpus/'
listOfLists=[]
listOfLists=readFilesIntoListFunct(files_List,pathVariable)
NoPunctList=punctuationREmovalFunct(listOfLists)
#print(indexationFunction(NoPunctList))


