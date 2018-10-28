

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





















'''
    for sent in sents:
        i += 1
        freq_dict = {}
        words = word_tokenize(sent)
        for word in words:
            freq_dict[word] += 1
        else:
'''