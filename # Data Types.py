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
result_string=''
empty=''
for character in given_string:
    if character in empty:
        count[character]+=1
    else:
        count[character]=1
for character in given_string:
    if count[character]>2:
        result_string+='$'
    else:
        result_string+=character
print(result_string)
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
if len(given_string)>3 and ing not in given_string:
    given_string=given_string+ing
elif len(given_string)>3 and ing in given_string:
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
if 'not' in given_string and 'poor' in given_string and given_string.find('not')<given_string.find('poor'):
    given_string.replace('not','')
    given_string.replace('poor',good)
print(given_string)
# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.
def returning_longest_one(my_list):
    max_len=0
    
    for item in my_list:
        if len(item)>max_len:
            longest_item=item
    return longest_item
# 8. Write a Python program to remove the nth
# index character from a nonempty
# string.
given_string=str(input('Enter the string?'))
given_index=int(input("Enter the string?"))
given_string[given_index]=''
print(given_string)
# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.
given_string=str(input('Enter the string?'))
new_string=given_string[-1]+given_string[1:-2]+given_string[0]
print(new_string)
# 10. Write a Python program to remove the characters which have odd index
# values of a given string.
given_string=str(input('Enter the string?'))
index=0
for character in given_string:
    if index%2!=0:
        given_string[index]=''
        index+=1
print(given_string)
# 11. Write a Python program to count the occurrences of each word in a given
# sentence.
given_string=str(input('Enter the string?'))
word_list=list(given_string)
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
# Expected Result : black, green, red, white,red
given_string=set(input('Enter the string?'))
given_string.sort()
print(given_string)
# 14. Write a Python function to create the HTML string with tags around the
# word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(given_tag,word):
    string_tag= '<'+given_tag+'>'+ word+'</'+given_tag+'>'
    return string_tag
# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_sting_middle(string_given,word):
    index=len(string_given)/2
     output_line = line[:index] + word + line[index:]
    return output_line
 # 16. Write a Python program to sum all the items in a list. 
 given_string=list(input("list of numbers?")) 
 sum=0
 for item in given_string:
     sum=sum+int(item)
print(sum)
# 17. Write a Python program to multiplies all the items in a list.
 given_string=list(input("list of numbers?")) 
 product=1
for item in given_string:
    product=product*item
print(product)
# 18. Write a Python program to get the largest number from a list.
given_list=list(int(input("given list")))
given_list.sort()
largest_num=given_list[-1]
print(largest_num)
# 19. Write a Python program to get the smallest number from a list.
 given_list=list(int(input("given list")))
given_list.sort()
largest_num=given_list[0]
print(largest_num) 
# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2  
count = 0
for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      count += 1
print(count)
# 21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
given_list=list("given list")
result_dict={}
mylist=[]
for item in given_list:
    result_dict[item[1]]=item[0]
for i in sorted(result_dict):
    mylist+=list(tuple(result_dict[i],i))
print(mylist)
#22. Write a Python program to remove duplicates from a list.
given_list=list(input("given list"))
set(given_list)
list(given_list)
print(given_list)
#23. Write a Python program to check a list is empty or not.

given_list=list(input("given list"))
if len(given_index ) == 0:
    print('empty')
# 24. Write a Python program to clone or copy a list.
given_list=list(input("given list"))
new_list=given_list
print(new_list)
# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
given_list=list(input("given list"))
for item in given_list:
    if (not item):
        value=True
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
for i in range(len(dict3)):
    dict3.key[i]=dict2.key[i]+dict1.key[i]
     dict3.value[i]=dict2.value[i]+dict1.value[i]

    









    







        




