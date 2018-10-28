from collections import defaultdict

listOflists=[['a', 'b'], ['a', 'c']]

inv_indx = defaultdict(list)
for idx, text in enumerate(listOflists):
    for word in text:
        inv_indx[word].append(idx)
         

print(inv_indx.keys(),inv_indx.values())