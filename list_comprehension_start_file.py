'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

# You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


# The list comprehension starts with a '[' and ']', to help you remember that the
# result is going to be a list.

# There are 3 parts to list comprehension:

# *result*  = [*transform/expression*    *iteration*         *filter*     ]

# The filter part answers the question if the item should be transformed.

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# list2 = []

# for i in list1:
#     if i % 2 == 0:
#         y = i * 100
#         list2.append(y)

# list2 = [i*100 for i in list1 if i % 2 == 0]

# print(list2)

# x = [i for i in range(10)]
# print(x)

# x = [i**2 for i in range(10)]
# print(x)

# list1 = [3, 4, 5]
# list2 = [item*3 for item in list1]
# print(list2)

# listOfWords = ['this', 'is', 'a', 'list', 'of', 'words']
# items = [word for word in listOfWords]
# items = [word[0].upper() for word in listOfWords]
# print(items)

# z = [i**2 for i in range(11) if i % 2 == 1]
# print(z)

# string = "Hello 12345 World"
# v = [int(i) for i in string if i.isdigit()]
# print(v)

# numbers = []
# for i in string:
#     if i.isdigit():
#         numbers.append(int(i))

# a = [i for i in string if i.isalpha()]
# print(a)

# infile = open('test.txt', 'r')
# result = [i.rstrip('\n') for i in infile if "line3" in i]
# print(result)


# def double(x):
#     return x*2


# double_result = [double(x) for x in range(10)]
# print(double_result)

# result = [x+y for x in [10, 20, 30] for y in [20, 40, 60]]
# print(result)

## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers",
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(i) for i in numbers if i > 0]
print(newlist)


# 2 create a list of integers which specify the length of each word in
# a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_ints = [len(i) for i in words if i != 'the' and ' ']
print(words)
print(word_ints)


# Given dictionary is consisted of vehicles and their weights in kilograms.
# Contruct a list of the names of vehicles with weight below 5000 kilograms.
# In the same list comprehension make the key names all upper case.

dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400,
        "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

b = [key.upper() for key in dict if dict[key] < 5000]
print(b)


# Find all the numbers from 1 to 1000 that have a 4 in them
n = [i for i in range(1, 1001) if '4' in str(i)]
print(n)

# count how many times the word 'the' appears in the text file - 'sometext.txt'
count = sum(line.lower().count('the') for line in open('sometext.txt', 'r'))
infile2 = open('sometext.txt', 'r')
print(count)


## Extract the numbers from the following phrase ##
phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each event, with about 3 or 4 that were classifled as serious per event.'
words = phrase.split()
a = [int(i) for i in words if i.isdigit()]
print(a)
