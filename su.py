# # print("hii")
# # print('Hello')

# # 1. From a dictionary, print only the items with an arr = [1, 2, 4, 6, 3, 7, 8, 10]odd value of less than 45. dic={‘sweta’ : 45, ‘Mausam’ : 31, ‘Pratik’ : 312, ‘Pari’ : 400}
 
# dic1 = {'sweta' : 45, 'Mausam' : 31, 'Pratik' : 312, 'Pari' : 400}
# filtered_items = {k: v for k, v in dic1.items() if v<45 and v % 2 !=0}
# print(filtered_items)
 
# # 2. Write a python program to count the frequency of each element in the list
# str1 = 'You must be the change , you wish$ to see in the world.'
# #     O/p = {“You” : 2, “must” :1, “be”:1, “the”:2, “change”:1, “wish”:1, “to”:1, “see”:1, “in”:1, “world”:1}
# new = ''
# for i in str1:
#     if i.isalpha() or i.isspace():
#        new += i
# l = new.split()
# d = {}
# for i in l:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)


# # 3. Find the index of the first occurrence in a string:
# # Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# # Example1: input: haystack = “sadbutsad”, needle = “sad” , output = 0
# haystack = 'sadbutsad'
# needle = 'sad'
# print(haystack.find(needle))
# # 4. Find the missing number : (take input from console)
# #     Input:  output = 5, 9
# arr = [1, 2, 4, 6, 3, 7, 8, 10]
# mn = min(arr)
# mx = max(arr)
# for i in range(mn, mx+1):
#     if i not in arr:
#         print(i)

# # 5. Create an iterator to iterate over Fibonacci sequence up to certain limit
# class Fib:
#     def __init__(self, stop):
#         self.stop = stop
#         self.first = 0
#         self.sec = 1
#         self.limit = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         cur = self.first
#         if self.limit > self.stop:
#             raise StopIteration('Stop')
#         new = self.first + self.sec
#         self.first = self.sec
#         self.sec = new
#         self.limit+=1
#         return cur
# obj = Fib(6)
# for i in obj:
#     print(i)

# 6. Write a regex to validate. Phone number in a specific format (8086567898) and email_id also
# import re
# # patt = re.compile('\\+91-[6-8]{1}[0-9]{9}')
# patt = re.compile('[6-8]{1}\d{9}')
# patt1 = re.compile('[a-z0-9-*._$]+@[a-z]+\\.[a-z]{2,}')
# # obj = patt.fullmatch('+91-6086567898')
# obj = patt.fullmatch('8086567898')
# obj1 = patt1.fullmatch('suchitra8658@gmail.in')
# print(obj1)



# 7. Write a decorator that checks if first argument passed to function is integer or not if its integer sum the elements.
# def dec(func):
#     def wrapper(*args, **kwargs):
#         summ = 0
#         res = func(*args, **kwargs)
#         for i in res:
#             if isinstance(i, int):
#                 summ += i
#             else:
#                 raise TypeError("Not integer")
#         return summ
#     return wrapper
# @dec
# def add_number(*args):
#     return args
# print(add_number(1,3,4,21))

# 8. Create a base class Animal with method eat( ). Implement subclasses her behaviour and carnivore that override eat( ) with different eating behaviour.
# class Animal:
#     def eat():
#         return 'I can eat'
# class Tiger(Animal):
#     def eat():
#         return 'I can eat nonveg only'
# class Cow(Animal):
#     def eat():
#         return 'I can eat veg only'


# 9. Create a generator function
# def square(l,h):
#     while l < h:
#         yield l**2
#         l+=1
# obj = square(2,10)
# print(next(obj))
# 10. Create a class Book with attributes title, author, and pages. 
# Write methods to display book information and check if it’s a bestseller based on the number of pages.
# class Book:
#     def __init__(self, title, author, pages) -> None:
#         self.title = title
#         self.author = author
#         self.pages = pages
#     def display(self, pg):
#         if self.pages > pg:
#             return f'Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nBest seller'
#         return f'Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}'
# book1 = Book('Abc', 'suchi', 200)
# print(book1.display(100))
# book2 = Book('Abcd', 'suchi', 200)
# print(book1.display(300))

# 11. Create file(like text file) perform CRUD operations inside the data of text file using file handling.
# with open('suchi.txt', 'a+') as file:
#     # file.write('Helllloooooooooooooo')
#     # file.write('Hiiiiiiiiiiiiiiii')
#     file.seek(0)
#     data = file.read()
#     print(data)

# 12. Write a program for handling the errors like Zero- division error, value error, index error, type error, and type error with syntax.
#       def error_handling_example( ):
#             try:
#                 # Zerodivisionerror
#                 num1 = int(input(“enter a number to divide:   ”))
#                 result = 10/num1
#                 print(f “Result: {result}”)
#                 #valueError
#                 num2 = int(input(“Enter a valid integer:   ”))
#                 #IndexError
#                 lst = [1, 2, 3]
#                 index = int(input(“Enter an index between 0 and 2:  ”))
#                 print(f “Value at index  {index}:  {lst[index]}”)
#                 #typeerror
#                 string = “Hello”
#                 num3 = int(input(“Enter another number:  ”))
#                 combined = string + num3
#            except ZeroDivisionError:
#                 print(“Error:  division by zero is not allowed.”)
#            except ValueError:
#                 print(“Error: Invalid output. Please enter a valid number.”)
#            except IndexError:
#                 print(“Error: List index out of range.”)
#            except TypeError:
#                 print(“Error:  Unsupported operation between different types.”)
#            except Exception as e:
#                print(f “An unexpected error occurred : {e}”)
#       error_handling_example( )