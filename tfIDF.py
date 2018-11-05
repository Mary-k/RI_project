

'''     
#tokenizing
tokens = nltk.word_tokenize(noPunct) #tokenize the raw UTF-8 text
stopword_list=open('/home/mimi/Desktop/RI_Lab/lab01/stopwords_fr.txt', 'r')
#remove stopWords

filtered_words = [] #declare an empty list to hold our filtered words
for word in tokens: #iterate over all words from the text
    if word not in stopword_list and word.isalpha() and len(word) > 1: #only add words that are not in the French stopwords list, are alphabetic, and are more than 1 character
        filtered_words.append(word) #add word to filter_words list if it meets the above conditions
filtered_words.sort() #sort filtered_words list

#print(filtered_words)

stemmed_words = [] #declare an empty list to hold our stemmed words
stemmer = FrenchStemmer() #create a stemmer object in the FrenchStemmer class
for word in filtered_words:
    stemmed_word=stemmer.stem(word) #stem the word
    stemmed_words.append(stemmed_word) #add it to our stemmed word list
stemmed_words.sort() #sort the stemmed_words
#print(stemmed_words)

from nltk.tokenize import word_tokenize, sent_tokenize 
import nltk
i=0

from nltk import defaultdict
freq_dict = defaultdict(int)
for word in stemmed_words:
    freq_dict[word] += 1

print(freq_dict.items())
'''

print("********** INDEX DE FREQUENCES DU DOCUMENT ", k, " **********")
    f = open('D' + str(k), 'r')
    t = f.read()
    t = t.lower()
    i = 0
    while i < len(t):
        if t[i] in listCar:
            t = t.replace(t[i], "")
        i += 1
    a = t.split()
    nb = len(a)
    for w in a:
        if not w in stoplist and len(w) > 1:
            if not (w, k) in freq:
                freq[w, k] = a.count(w)
                print(w, freq[w, k])
    k += 1
f.close()
print("Le fichier inverse de la collection")
print(freq)

def weighted_invertedIndeces_Funct(Nb_docs,invertedIndeces_file_path):
        #poids(ti, dj)=(freq(ti,dj)/Max(freq(t, dj))*Log((N/ni) +1)
        #poids[w, d] = (float(
        # freq[w, d])/max[d]) * log10((float(Nb_docs))/ni[w]+1)
        #creationOf
        return 0

'''
    for sent in sents:
        i += 1
        freq_dict = {}
        words = word_tokenize(sent)
        for word in words:
            freq_dict[word] += 1
        else:
'''
 string='['+str(token)+','+str(docIndex)+']->'+str(target_freqdistr[token])+'\n'
                        tempList.append(token)
                        tempList.append(docIndex-1)
                        tempList.append(target_freqdistr[token])
                        print(tempList)
                        print( )
                        frequencies_file_list.append(tempList)
                      #  FileSave.write(string)
                
for list_index_1 in frequency_file_list:
        temp=list_index_1
        frequency_file_list.remove(list_index_1)
        temp2.append(temp[0])
        temp2.append(temp[2])
        for list_index_2 in frequency_file_list:
                if list_index_2[0]==temp[0]:
                        temp2.append(list_index_2[2])
                        frequency_file_list.remove(list_index_2)
        invertedIndeces_file_list.append(temp2)

some_dict=dict()
for lines in some_list:
    if lines[0] in some_dict:
        some_dict[lines[0]].append(lines[1])
        pass