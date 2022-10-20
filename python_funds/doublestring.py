test_list = ["the", "name","of", "the", "rose", "the","english", "patient", "the","greatest", "person", "in", "the", "world", "test", "the", "person","hello"]

# def count_words(list):
#     list2= []
#     # counter = 0
#     counter2 = 0
#     for i in range(0, len(list)-1):
#         for j in range(1, len(list)-1):
#             if list[i]==list[j]:
#                 if i != j:
#                     list2.append(list[i])
#                 return list2
# import pandas as pd 
# print(pd.Series(test_list).value_counts())
# print(pd.Series(test_list))


# dict_count = {key: test_list.count(key) for key in set(test_list)}
# print(dict_count)

# dict1 = {}

# for i in test_list:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1

# print(dict1)


dict1 = {}

for i in test_list:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

print(dict1)



    
                    
                
                
    



