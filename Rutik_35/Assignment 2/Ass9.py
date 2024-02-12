# Given list of string create a new list using list comprehension that contains the length of each string in the original list but exclude string that has an odd length.

list1 = ["apple", "banan", "orange", "kiw", "pear"]

list2=[]
for word in list1:
    if len(word)%2==0:
        list2.append(len(word))
print("Filtered lengths:", list2)
