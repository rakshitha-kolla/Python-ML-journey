import re
'''
#^(caret)=used to check whether particular string starts with a particular pattern or not
string="python is high level progamming language python"
x=re.findall("^pyton",string)
print(x)
if x:
    print("yes,starts with python")
else:
    print("no, does not starts with python")'''

#$dollar=checks is string ends with particular charactetr or not
'''
string="python is high level progamming language python"
x=re.findall("python$",string)
print(x)
if x:
    print("yes,ends with python")
else:
    print("no, does not ends with python")'''

#or |=checks either or condition
'''
string="python is high level progamming language python"
x=re.findall("python|language",string)
print(x)
if x:
    print("yes,starts with python")
else:
    print("no, does not starts with python")'''

#.(dot) used to match single char excpet newline char
'''
string="python is high level progamming language python plot play"
x=re.search("a.e",string)
y=re.findall("pl.",string)
print(x)
print(y)
if x:
    print("yes,starts with python")
else:
    print("no, does not starts with python")'''

#(slash) \ escape char
'''
string="python is high level progamming language python"
x=re.search(".",string)
y=re.search("\.",string)
print(x)
print(y)
'''


#star * =zero or more occurances of a string
'''
string="python is high level progamming language python leeeo"
x=re.findall("le*",string)
y=re.findall("l*",string)
print(y)
print(x)
'''

#plus +
'''
string="python is high level progamming language python leeo"
x=re.findall("le+",string)
y=re.findall("l+",string)
print(y)
print(x)
'''
# [] (brackets)
'''
string="python is high level progamming language python"
x=re.findall("[A-Z]",string)
y=re.findall("[a-z]",string)
print(y)
print(x)'''

# {} curly braces=matches exactly specigfied no of occurances
'''
string="python is high level progamming language python meta mmmmmmm mmm "
y=re.findall("m{2}",string)
print(y)
x=re.findall("m{1,5}",string)
print(x)
'''

#() paranthesis=used to group sub patterns
'''
string="python is high level progamming language python"
x=re.findall("(is)",string)
y=re.findall("(high|level)",string)
print(y)
print(x)
'''

# sequence characters

#\A=matches with string begins with the given character
'''
string="python is high level progamming language python"
x=re.findall("\Apython is",string)
y=re.findall("^python is",string)
print(y)
print(x)

output
['python is']
`['python is']
'''
#\b matches if word begins or end with given character
'''
string="python is high level progamming language python"
p=r'\b' + 'python' + r'\b'
x=re.findall(p,string) 
print(x)    #['python', 'python']'''

#d matches any digit [0-9] 
#D matches any non degit chracter
#\s macthes any white space character
#\w matches with alpha numeric character
#\S matches no spave\
'''
string="python is high level progamming language python founded in 1991 feb2"
x=re.findall("\d",string)
y=re.findall("\D",string)
z=re.findall("\s",string)
p=re.findall("\w",string)
c=re.findall("feb2\Z",string)
s=re.findall("\S",string)
#\z matches if the string ends with givrn regexp
print(x)
print(y)
print(z)
print(p)
print(c)
print(s)
'''
'''
output

['1', '9', '9', '1', '2']
['p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'h', 'i', 'g', 'h', ' ', 'l', 'e', 'v', 'e', 'l', ' ', 'p', 'r', 'o', 'g', 'a', 'm', 'm', 'i', 'n', 'g', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 'f', 'o', 'u', 'n', 'd', 'e', 'd', ' ', 'i', 'n', ' ', ' ', 'f', 'e', 'b']
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
['p', 'y', 't', 'h', 'o', 'n', 'i', 's', 'h', 'i', 'g', 'h', 'l', 'e', 'v', 'e', 'l', 'p', 'r', 'o', 'g', 'a', 'm', 'm', 'i', 'n', 'g', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', 'p', 'y', 't', 'h', 'o', 'n', 'f', 'o', 'u', 'n', 'd', 'e', 'd', 'i', 'n', '1', '9', '9', '1', 'f', 'e', 'b', '2']
['feb2']
['p', 'y', 't', 'h', 'o', 'n', 'i', 's', 'h', 'i', 'g', 'h', 'l', 'e', 'v', 'e', 'l', 'p', 'r', 'o', 'g', 'a', 'm', 'm', 'i', 'n', 'g', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', 'p', 'y', 't', 'h', 'o', 'n', 'f', 'o', 'u', 'n', 'd', 'e', 'd', 'i', 'n', '1', '9', '9', '1', 'f', 'e', 'b', '2']
'''

#sets

#[abc]
'''
string="python is high level progamming language python founded in 1991 Feb22"
x=re.findall("[aln]",string)
y=re.findall("[e-h]",string)
z=re.findall("[A-Z]",string)
p=re.findall("[A-z]",string)
q=re.findall("[^a-z]",string)
r=re.findall("[0-9][0-9]",string)
print(x)
print(y)
print(z)
print(p)
print(q)
print(r)'''

string="python is high level progamming language python founded in 1991 Feb22"
x=re.findall("..",string)
print(x)