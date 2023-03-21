''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''



def filter_integers(ints):
    OddList = list(filter(lambda x: x % 2 == 1, ints))
    EvenList = list(filter(lambda x: x % 2 == 0, ints))
    return OddList, EvenList 
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
OddList, EvenList = filter_integers(integers)
print(OddList)
print(EvenList)




#2) find which days of the week have exactly 6 characters.


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def six_char(characters):
    return list(filter(lambda i: len(i) == 6, characters))
six_days = six_char(weekdays)
print(six_days)



#3) remove specific words from a given list 
#Original list:
og_words = ['orange', 'red', 'green', 'blue', 'white', 'black']

#Remove words:
remove_words = ['orange', 'black']

#After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

def remove_words(word):
    return list(filter(lambda x: x in remove_words, list))
day_filter = remove_words(og_words)
print(day_filter)




# '''
# # 4)remove all elements from a given list present in another list
# Original lists:
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2: [2, 4, 6, 8]

# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]
 






#  5)
# find the elements of a given list of strings that contain specific substring using lambda
# Original list:
# ['red', 'black', 'white', 'green', 'orange']
# Substring to search:
# ack
# Elements of the said list that contain specific substring:
# ['black']
# Substring to search:
# abc
# Elements of the said list that contain specific substring:
# []








#  6)
# check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
# (This is like a password verification function, HINT: Python function 'any' may be useful)


# str1 = "Hello8world"
# str1 = "HELLO"
# str1= "hello"












#  7)
# Write a Python program to sort a list of tuples using Lambda.

# # Original list of tuples:
# original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# # Expected Result:
# # [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
# '''
