# using a dictionary comprehension create a dictionary containing only key value pairs using an existing dictionary where the key is string and the length of the string is greater than 3 .Given dict={'apple':3,'banana':5,'kiwi':2,'orange':6}

dict1 = {'app': 3, 'banana': 5, 'kiwi': 2, 'orange': 6}
dict2={}
dict2 = {key: value for key, value in dict1.items() if len(key) > 3}

# for key,value in dict1.items():
#     if len(key)>3:
#         dict2.

print("Filtered dictionary:", dict2)
