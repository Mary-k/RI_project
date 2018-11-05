dict = {'key': ['v1']}



dict['key'].append(1)

print(dict)

dict = {}
some_dict=[]
some_dict.append(['dan',1,2])
some_dict.append(['dan',3,5])
some_dict.append(['fil',1,4])
some_dict.append(['fil',2,2])
some_dict.append(['fil',3,1])
        
for target_list in some_dict:
        if some_dict[0][0] in dict.keys():
                dict[target_list[0]].append(target_list[0])
        else:
                dict[target_list[0]]=[target_list[1],target_list[2]]
print(dict)