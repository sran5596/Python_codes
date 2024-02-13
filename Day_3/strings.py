#mutable--cannot change the values
#immutable--can change the values
#ex-1
#[[strings are immutable]]
# s="ravi"
# s1='ravi1'
# s3=str("ravi3")
#
# e=""
# e1=''
# e3=str("")

#ex-2
# print(id(s))
# s=s+"good boy"
# print(id(s)) # after updation id changed that mena string is immutable

#ex-3 -- Using the "+" & "*" operator
# s="raveendra"
# s=s+"good job" # concatination
# print(s)

# s="raveendra"
# print(s*3) #multiplication

#slicing operatoers __ symbol=[]

#extract the string and
# get the string and
# reverse the string

# s="pythonone" # index start with 0
# print(s[3:8])
# prints--honon

# s="raveendra"
# print(s[:4]) #provided the end index only
# #print(rave)
# print(s[2:]) #provided the end index only
# #print(veendra)
# print(s[3:7:2]) #provided the start and end and step value also
#print(en)

#pass the reverse val;ues also
# print(s[-7:-4])
# print(len(s))#print(count ion element in s)
# print(s[1:-1])

#ord() and chr()
#it gives the ascill number of alphabet
# print(ord("a")) # a=97(ascill number)
# print(chr(97))

#max() & min() & len()
# s=[1,2,3,4]
# print(max(s))
# print(max("abc"))
# print(min("butre"))
# print(len(s))

#membsership operstor
# In operator always tells the boolean values
# in and not in operator
# s="raveendra good one getting good salary"
# print("one" in s ) # True
# print("does" in s) # False
# print("so" not in s) # True

#string Comparision
# compare the alphabets based on the alpahbetical order
#here used the relational operators(<,>,<=,>=,==,!=)

# print("tim"=="tie")#False
# print("free"!="freedom") # True
# print(("arrow">"aron")) # True
# print("right">="left") #True
# print("teeth"<"tee")#False
# print("Yellow"<= "fellow")# False
# print("abc">"")#True

#Testing functions
#gives the boolean values
# .isalnum()
# .isalpha()
# .issuper()
# .isdgit()
# .isidentifier()
# .islower()
# .isspace()

# [r="fugwiuk"
# print(r[::-1])]# string reverse

# s="raveendra have the good job"
#print(s.isalnum()) # it check the s contain the all numbers
#print(False)

# print(s.isalpha()) # True
# print("welcome".isalpha()) #True
# print("2012".isdigit()) #True
# print("first number".isidentifier()) # it check string contain the keyword or not it check
# #Falsew
# print("try".isidentifier()) # True
# print(s.islower()) #True
# print("WELCOME".isupper()) #True # it check the string contain the uppercase or not it checks
# print(" ".isspace()) # True
# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword("try"))

# searching for substrings
#Gives the boolean values
# .endswith("")
# .startswith("")
# .find("")
# .count("")
# s="raveendra one good person"
# print(s.endswith("son")) # True
# print(s.endswith("tre")) # False
# print(s.startswith("ravee")) # True
# print(s.startswith("hytr"))# False
# print(s.find("endra")) # Give the position in string
# print(s.count("e")) # prints how many times the e is there in string

#Converting functions
# .capitalize() -- converted start word  first letter is upper
# .title() -- converted the first letter is capital
# .lower() -- converted into lower
#.upper() -- converted the upper
#.swapcase() -- chnage the  upper to lower and lower to upper
#replace() -- it changed the specific word mean [ "yeg" , "gen" ]
# s="fuyd yjedg yeg"
# # print(s.capitalize()) #each word first letter is converted into uppercase letter
# # s1=s.capitalize()
# # print(s1)
# print(s.capitalize())
# print(s.title())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.replace("yeg" , "gun"))
# print(s.lower())
# print(s.title())#

# most imp thing -- reverse the string

# s="ujykgvewoflgewfikwuj"
# print(s[::- # one type

# s1="raveendra"
# rev=""
# for i in s1:
#     rev=i+rev
# print("reversed string is:",rev)

# s="raveendra income is yearly twenty crores"
# rev=""
# for i in s:
#     rev=i+rev
# print("reversed the string:",rev)

#formating output
#[ name="raveendra"
# age=25
# salary=200000
# print("name is:{} age is:{} salary is:{}".format(name,age,salary))
# print("name is:%s age is:%d salary is:%g"%(name,age,salary))]
# print("{} {} {}".format("value is :",5,"raveendra"))

# s="wydgioukj"
# # # print(len(s))
# rev=""
# for i in s:
#     rev=i+rev
# print("revsersed values:",rev)
# print(s[::-1])
