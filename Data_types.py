# Data Types
# 1. Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
given_string=str(input('Enter the string?'))
result_dict={}
for character in given_string:
    keys=result_dict.keys()
    if character in keys:
        result_dict[character]+=1
    else:
        result_dict[character]=1
print(result_dict)
# 2. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.
# Sample String : 'Python'
# Expected Result : 'Pyon'
# Sample String : 'Py'
# Expected Result : 'PyPy'
# Sample String : ' w'
# Expected Result : Empty String
given_string=str(input('Enter the string?'))
if len(given_string)>4:
    result_string=given_string[0:2]+given_string[-2:]
elif len(given_string)==2:
    result_string=given_string*2
else:
    result_string='Empty String'
print(result_string)
# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
given_string=str(input('Enter the string?'))
first_char=given_string[0]
resulting_string=''
count=0
for char in given_string:
    if char==first_char and count!=0 :
        resulting_string+='$'
    else:
        resulting_string+=char
    count+=1
print(resulting_string)
        
# 4. Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
given_string_1=str(input('Enter the string1?'))
given_string_2=str(input('Enter the string2?'))
result_string= given_string_2[0:2]+given_string_1[2:]+' '+given_string_1[0:2]+given_string_2[2:]
print(result_string)
# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
given_string=str(input('Enter the string?'))
ing='ing'
if len(given_string)>2 and ing not in given_string:
    given_string=given_string+ing
elif len(given_string)>2 and ing in given_string:
    given_string=given_string+'ly'
print(given_string)
# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
given_string=str(input('Enter the string?'))
new_str=''
res_str=''
if 'not' in given_string and 'poor' in given_string and given_string.find('not')<given_string.find('poor'):
    new_str=given_string.replace('not','')
    res_str=new_str.replace('poor','good')
print(res_str)
# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.
def returning_longest_one(my_list):
    max_len=0
    longest_item=''
    for item in my_list:
        if len(item)>max_len:
            longest_item=item
            max_len=len(item)
    return longest_item
 print(returning_longest_one(['asdf','dfsdfs','fsdfsfs','gdgd']))
# 8. Write a Python program to remove the nth
# index character from a nonempty
# string.
given_string=str(input('Enter the string?'))
given_index=int(input("Enter the index?"))
index=0
result_string=''
for char in given_string:
    index+=1
    if index==given_index:
        pass
    else:
        result_string+=char
    
print(result_string)
# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.
given_string=str(input('Enter the string?'))
new_string=given_string[-1]+given_string[1:-2]+given_string[0]
print(new_string)
# 10. Write a Python program to remove the characters which have odd index
# values of a given string.
given_string=str(input('Enter the string?'))
index=0
new_string=''
for character in given_string:
    index+=1
    if index%2!=0:
        pass
    else:
        new_string+=character
    
print(new_string)
# 11. Write a Python program to count the occurrences of each word in a given
# sentence.

given_string=str(input('Enter the string?'))
word_list=[]
word_item=''
for char in given_string:
    if char==' ':
        word_list.append(word_item)
        word_item=''
    else:
        word_item+=char
print(word_list)
words_dict={}
for item in word_list:
    keys=words_dict.keys()
    if item in keys:
        words_dict[item]+=1
    else:
        words_dict[item]=1
print(words_dict)
# 12. Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.
given_string=str(input('Enter the string?'))
print(given_string.upper())
print(given_string.lower())
# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white
given_string=str(input('Enter the string?'))
word_list=[]
word_item=''
for char in given_string:
    if char==' ':
        if word_item  not in word_list:
            word_list.append(word_item)
            word_item=''
        word_item=''
            
    else:
        word_item+=char
print(sorted(word_list))
# 14. Write a Python function to create the HTML string with tags around the
# word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(given_tag,word):
    string_tag= '<'+given_tag+'>'+ word+'</'+given_tag+'>'
    return string_tag
print(add_tags('i','hello'))
# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_sting_middle(line,word):
    index=int(len(line)/2)
    output_line = line[:index] + word + line[index:]
    return output_line
print(insert_sting_middle('this is a string','middle word'))
 # 16. Write a Python program to sum all the items in a list. 

given_string=[1,2,3,4,5]
sum=0
for item in given_string:
     sum=sum+int(item)
print(sum)
# 17. Write a Python program to multiplies all the items in a list.
 given_string=[1,2,3,4,5]
 product=1
for item in given_string:
    product=product*item
print(product)
# 18. Write a Python program to get the largest number from a list.
given_list=[12,32,4,53,6,78,9,45,14]
given_list.sort()
largest_num=given_list[-1]
print(largest_num)
# 19. Write a Python program to get the smallest number from a list.
given_list=[12,32,4,53,6,78,9,45,14]
given_list.sort()
largest_num=given_list[0]
print(largest_num) 
# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2  
words=['abc', 'xyz', 'aba', '1221']
count = 0
for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      count += 1
print(count)
# 21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
given_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result_dict={}
mylist=[]
for item in given_list:
    result_dict[item[1]]=item[0]
for i in sorted(result_dict):
    mylist+=list(tuple(result_dict[i],i))
print(mylist)
#22. Write a Python program to remove duplicates from a list.
given_string=str(input('Enter the string?'))# e.g.abc,abc,aaa,aaa,hello,
word_list=[]
word_item=''
for char in given_string:
    if char==',':
        if word_item  not in word_list:
            word_list.append(word_item)
            word_item=''
        word_item=''
            
    else:
        word_item+=char
print(word_list)

#23. Write a Python program to check a list is empty or not.

given_list=list(input("given list"))
if len(given_index ) == 0:
    print('empty')
# 24. Write a Python program to clone or copy a list.
given_list=[1,2,3,4,5,6]
new_list=given_list
print(new_list)
# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
given_list=[{},{},{1,2},{}]
value=True
for item in given_list:
    if (not item):
        value=value and True
    else:
        value=False
print(value)
# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
string=str(input('string'))
my_list=list(input('List'))
for item in my_list:
    item=item+string
print(my_list)
# 27. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
list1=list(input('list1'))
list2=list(input('list2'))
list1=list1[0:-2]+list2
print(list2)
# 28. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
def add_a_key_in_dict(given_dict,key_value):
    given_dict.update(key_value)
    return given_dict
# 29. Write a Python script to concatenate following dictionaries to create a new
# one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict4={}
for dic in (dict1,dict2,dict3):
    dict4.update(dic)
print(dict4)


# 30. Write a Python script to check whether a given key already exists in a
# dictionary.
dicts={}
keys=dicts.keys()
given_key=str(input('given key'))
if given_key in keys:
    print('key exists')
# 31. Write a Python program to iterate over dictionaries using for loops.

for key,value in dictonary.items()
    print(key,value)
# 32. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
def Sample_dictornary(n):
    res_dec={x:x*x for x in range(1,n+1)}
    return res_dec
# 33. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144,
# 13: 169, 14: 196, 15: 225}
res_dec={x:x*x for x in range(1,16)}
print(res_dec)
# 34. Write a Python script to merge two Python dictionaries.
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res    
print(Merge(dict1,dict2))
# 35. Write a Python program to iterate over dictionaries using for loops.
for key,value in dictonary.items()
    print(key,value)
# 36. Write a Python program to sum all the items in a dictionary.
my_dict=dict(intput('my_dict'))
print(sum(my_dict.values()))
 #37. Write a Python program to multiply all the items in a dictionary.
 product=1
 for numbers in my_dict.values():
     product=product*numbers
print(product)
# 38. Write a Python program to remove a key from a dictionary.
delteing_key=input('key to be deleted')
del my_dict[delteing_key]
print(my_dict)
# 39. Write a Python program to unpack a tuple in several variables.
x, *y, z = given_tuple
print(x,y,z)
 #40. Write a Python program to add an item in a tuple.
given_tuple= ('2',)
item = 'z'
new_tuple = given_tuple + (item,)
# 41. Write a Python program to convert a tuple to a string.
given_tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
string =  ''.join(given_tuple)
str(string)
print(string)
# 42. Write a Python program to convert a list to a tuple.
list(given_tuple)
print(given_tuple)
# 43. Write a Python program to remove an item from a tuple.

given_tuple=input('this is input tuple')
list(given_tuple)
given_tuple.remove(item)
tuple(given_tuple)
print(given_tuple)
# 44. Write a Python program to slice a tuple.
given_tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
start= 3
stop= 7
my_new_tuple= given_tuple[start:stop]
print(my_new_tuple)
# 45. Write a Python program to find the index of an item of a tuple.
item=input('index')
index_of_item=my_tuple.index(item)
print(index_of_item)
#46. Write a Python program to find the length of a tuple
print(len(given_tuple))








    







        




