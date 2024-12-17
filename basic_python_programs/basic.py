'''
#1.Calculate string length.
str="kolla rakshitha"
print(len(str))
count=0
for char in str:
    count+=1
print(count)
'''

'''
# 2 Count character frequency in a string.

Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''
'''
str="google.com"
dict={}
for i in range(len(str)):
    dict.update({str[i]:str.count(str[i])})
print(dict)
'''
'''
3. Get string of first and last 2 chars.

Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String 
'''
'''
str=input("enter string: ")
if len(str)<2:
    print("empty string")
else:
    print(str[:2:1]+str[-2::])
'''

'''
4. Replace first char occurrences with $.

Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''
'''
str=input("Enter string: ")
f=str[0]
for i in range(1,len(str)):
    if str[i]==f:
        str=str[:i:]+"$"+str[i+1::]
print(str)
str2=input("enter str:")
char=str2[0]
str2=str2.replace(char,"$")
str2=char+str2[1::]
print(str2)
'''
'''
5.Swap first 2 chars of 2 strings.

Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''
'''
str1="rakshi"
str2="kolla"
str=str2[:2:]+str1[2::]+" "+str1[:2:]+str2[2::]
print(str)
'''
'''
6. Add ing or ly to a string.

Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''
'''
str=input("Enter string: ")
if len(str)<3:
    pass
else:
    if str[-3::]=="ing":
        str+="ly"
    else:
        str+="ing"
print(str)
'''
'''
7. Replace 'not'...'poor' with 'good'.

Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''
'''
str=input("enter: ")
idx=str.find("not")
idx1=str.find("poor")
if idx != -1 and idx1 != -1:
    str=str.replace(str[idx:idx1+4:],"good")
print(str)
'''

'''
8.Count word occurrences in a sentence.

Write a Python program to count the occurrences of each word in a given sentence.
Click me to see the sample solution
'''
'''
str=input("Enter string: ")
dict={}
words=str.split()
for word in words:
    if word in dict.keys():
        dict[word]+=1
    else:
        dict[word]=1
print(dict)
'''
'''
9. Sort distinct words in comma-separated input.

Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
Click me to see the sample solution
'''
'''
str=input("enter string : ")
l=str.split(",")
l.sort()
print(l)
'''
'''
17. Repeat last 2 chars of a string 4 times.
'''
str="hello"
str=str[:len(str)-2:]+str[-2::]*4
print(str)
print(ord("a"))
print(chr(95))