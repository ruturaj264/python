# a = list('_'*3)

# b = set(a)
# if '_' in b:
#     print('y')

# a = '5243'
# a.is
# a = a.replace(a[1:], ''.join(sorted(a[1:])))
            
# # print(a)
# import itertools
# from itertools import permutations

# list_1 = ["a", "b", "c","d"]
# list_2 = [1,4,9]
# list_3 = ['!', '#', '$', '%', '^']
 
# perm1 = list(itertools.permutations(list_1, 3))
# perm2 = itertools.permutations(list_2, 3)
# perm3 = itertools.permutations(list_3, 3)


# print(perm1)

# import re

# str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
#   ## re.sub(pat, replacement, str) -- returns new string with all replacements,
#   ## \1 is group(1), \2 group(2) in the replacement
# print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1 \2', str))
#   ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher

# regex_alternating_repetitive_digit_pair = r'''(\d)(?=\d\1)'''
# P = '137370'
# x = re.findall(regex_alternating_repetitive_digit_pair, P) 
# print(x)

# a = float(1.2)
# print(round(a, 2))

# formatted = "{:.3f}".format(9.99) 
# print(formatted)

# print(list(range(0, 8, 4)))

# for i in range(3):
#     a += (str(i) + '\n')

# print(a)

# print(int(0.5))
# print('{0:x}'.format(n)) 

# a = '123.0'
# print(list(a))

   
# from datetime import datetime 
    
# time1 = datetime(2216, 6, 16, 8, 18, 21) 
# time2 = datetime(1991, 9, 13, 21, 59, 15) 

# time1 = datetime.strptime("5:16:20:50", "%D:%H:%M:%S") 
# print('Start time is :', time1.time()) 
  
# time2 = datetime.strptime("5:11:56:18", "%D:%H:%M:%S") 
# print('End time is :', time2.time()) 
  
# difference = time1 - time2  
# minutes = difference.total_seconds()
# # a = -1
# # b = -2
# print(minutes)

# import re
# hexa = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','#','A','B','C','D','E','F']

# n = int(input())
# allPossColours = []
# possColInLine = []
# pattern = '#\w{6}|#\w{3}'
# # pattern2 = ''
# # pattern = '#\w{6}|#\w{3}'

# for i in range(n):
    
#     line = input()
#     if ':' not in line:
#         continue

#     possColInLine = re.findall(pattern, line)
#     if possColInLine:
#         for col in possColInLine:
#             if col != '':
#                 allPossColours.append(col)
        
# # print(allPossColours)

# for colour in allPossColours:
    
#     valid = True
#     for letter in colour:
#         if letter not in hexa:
#             valid = False
#             break
            
#     if valid:
#         print(colour)
# import re

# total_matches = []
# line = 'x&& &&& && && x || | ||\|| x'

# while True:
#         match = re.findall('\s{1}&&\s{1}',  line)
#         if match:
#             line = re.sub('\s{1}&&\s{1}', ' and ',  line)
#         else:
#             break



# print(line) 

# from translate import Translator

# sentence = Translator(from_lang='ar', to_lang='en') 

# input_lang = 'كانشان تونبي'

# output_lang = sentence.translate(input_lang)

# print(output_lang)/

# import sys

# # print(sys.executable)

# a = 1.2
# b = int(a)

# def reduceNumbers(a, b):

#     fact1 = []
#     fact2 = []

#     while a != 1:

#         for i in range(2, a+1):
#             if a % i == 0:
#                 fact1.append(i)
#                 a = int(a / i)
#                 break

#     while b != 1:

#         for i in range(2, b+1):
#             if b % i == 0:
#                 fact2.append(i)
#                 b = int(b / i)
#                 break

#     tempFact1 = fact1.copy()            
#     tempFact2 = fact2.copy()        

#     for number in fact1:
#         if number in tempFact2:
#             tempFact1.remove(number)
#             tempFact2.remove(number)

#     if len(tempFact1) == 0:
#         a = 1
#     else:
#         temp = 1
#         for number in tempFact1:
#             temp = temp * number
#         a = temp

#     if len(tempFact2) == 0:
#         b = 1
#     else:
#         temp = 1
#         for number in tempFact2:
#             temp = temp * number
#         b = temp

#     return a, b

# print(list(reduceNumbers(25,75)))

import re

# def test(*args):
#     print(list(args), type(args), args[1])

# test(1,2,3,1,2)

# a = 'abd 1242maksm23r qwerk 989jk1'

# b = re.findall(r'[\d\s]+', a)
# print(type(re))
# print(b)

# import SquareFreeNumbers as sq

# a = sq.getDivisors(50)

from itertools import permutations

# a = '((()))'
# perm = list(permutations(a))
# perm = [list(x) for x in perm]
# perm = [''.join(x) for x in perm]
# perm = list(set(perm))

# x = lambda a : a + 10
# print(x(5))                 # 15

# x = lambda a, b : a * b
# print(x(5, 6))              # 30

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))           # 13


# a = int(input(" enter charater "))


# if a>=65 and a<=90:
#     print("opposite=",a+32)
# elif a>=97 and a<=122:
#     print("opposite=",a-32)
# else:
#   print("invalid input")



# string = 'this is python'

# words = string.split()
# new_words = []

# for word in words:
    
#     l = len(word)
#     temp = ''
#     for letter in word:
        
#         i = word.index(letter)

#         if i == 0 or i == l-1:
#             temp += letter.upper()
#         else:
#             temp += letter

#     new_words.append(temp)

# print(' '.join(new_words))
            

# string = 'this is python'
# # 'siht si nohtyp'

# array = string.split()
# temp_array = []

# for word in array:
#  temp_array.append(word[::-1])

# #['siht', 'si', 'nohtyp']

# string = ' '.join(temp_array)

# print(string)
 


# class num_array:
 
#     def __init__(self, *args):

#         self.items = []
#         for item in args:
#             self.items.append(item)

#     def get_even(self):

#         even = []
#         for item in self.items:
#             if item % 2 == 0:
#                 even.append(item)

#         return even
 
#     def get_odd(self):

#         odd = []
#         for item in self.items:
#             if item % 2 != 0:
#                 odd.append(item)

#         return odd
    
#     def __str__(self):
#         string = '['
#         string += ', '.join(list(map(str, self.items)))
#         string += ']'
        
#         return string

#     def __len__(self):
#         return len(self.items)
    
# my_array = num_array(1,2,3,4)

# print(my_array)
# print(my_array.items)
# print(my_array.get_even())
# print(my_array.get_odd())
# print(len(my_array))



# ['a', 'b', 'c', 1, 2, 3]

a = [4,5,6]
print(a.pop(2))





    
        