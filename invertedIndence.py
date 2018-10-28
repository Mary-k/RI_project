    
import InvertedIndex
import InvertedIndexQuery

i = InvertedIndex.Index()

filename = '/home/mimi/Desktop/RI tp/D1.txt'
file_to_index = open(filename).read() 
document_key = filename

    # index the document, using document_key as the document's
    # id.
i.index(file_to_index, document_key)
    

'''
    filename = 'document2.txt'
    file_to_index = open(filename).read()
    document_key = filename

    i.index(file_to_index, document_key)

    search_results = InvertedIndexQuery.query('Python and spam', i)
    search_results.sort()

    cnt = 0
    for document in search_results:
      cnt = cnt + 1
      print '%d) %s' % (cnt, document[1])
      '''