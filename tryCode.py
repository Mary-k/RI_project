#files into list if lists

from collections import defaultdict
myList=[]


fileList=['D1','D2','D3','D4','D5']

for fichier in fileList:
    with open('/home/mimi/Desktop/RI_Lab/lab01/'+fichier+'.txt') as f:
        myList.append(list(f))
        
ListOfLists=[]

for target_list in myList:    
    ListOfLists.append(target_list[0].split(' '))
    
inv_indx = defaultdict(list)
for idx, text in enumerate(ListOfLists):
    for word in text:
        inv_indx[word].append(idx)
         

print(inv_indx.keys(),inv_indx.values())