# Lists and Tuples in Python
#lista : A built-in data typr that stores  set of a valuses .
#It can stores of different data types and is mutable (can be modified after creation).
marks = [85, 90, 78, 92, 88]
print(marks)  # Output: [85, 90, 78, 92, 88]
print(type(marks))  # Output: <class 'list'>
print(marks[0])  # Output: 85
print(marks[1])  # Output: 90
print(len(marks))  # Output: 5


#LISTS METHOD

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adds "orange" to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']    
fruits.sort()  # Sorts the list in alphabetical order
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
fruits.reverse()  # Reverses the order of the list
print(fruits)  # Output: ['orange', 'cherry', 'banana', 'apple']
fruits.insert(1, "grape")  # Inserts "grape" at index 1
print(fruits)  # Output: ['orange', 'grape', 'cherry', 'banana', 'apple']
fruits.sort(reverse=True)  # Sorts the list in reverse alphabetical order
print(fruits)  # Output: ['orange', 'grape', 'cherry', 'banana', 'apple']
fruits.insert(0, "kiwi")  # Inserts "kiwi" at index 0
print(fruits)  # Output: ['kiwi', 'orange', 'grape', 'cherry', 'banana', 'apple']


num = [5, 2, 9, 1, 5, 6]
num.remove(5)  # Removes the first occurrence of 5 from the list
print(num)  # Output: [2, 9, 1, 5, 6]
num.pop(2)  # Removes the element at index 2 (which is 1)
print(num)  # Output: [2, 9, 5, 6]


#Tuples : A built-in data type that stores a collection of values. It is similar to a list but is immutable (cannot be modified after creation).
#Tuples are defined using parentheses () instead of square brackets [].
coordinates = (10, 10, 20)
print(coordinates)  # Output: (10, 10, 20)
print(type(coordinates))  # Output: <class 'tuple'>
print(coordinates[0])  # Output: 10
print(coordinates[1])  # Output: 10
print(coordinates[2])  # Output: 20
print(len(coordinates))  # Output: 3
print(coordinates.count(10))  # Output: 2
print(coordinates.index(20))  # Output: 2


#WAP to ask the user to enter names of their 3 favourite movie names and store
#  them in a list. Then, print the list of favourite movies.
favourite_movies = []
movie1 = input("Enter the name of your first favourite movie: ")
movie2 = input("Enter the name of your second favourite movie: ")
movie3 = input("Enter the name of your third favourite movie: ")
favourite_movies.append(movie1)
favourite_movies.append(movie2)
favourite_movies.append(movie3)
print("Your favourite movies are:", favourite_movies)


#WAP to count the number of students with ths "a" grade in the following tuple 
grades = ("c ", "d", "a", "a", "b" , "b", "a")
print(grades.count("a"))  # Output: 3



grades = ["c ", "d", "a", "a", "b" , "b", "a"]
grades.sort()  # Sorts the list in alphabetical order
print(grades)  # Output: ['a', 'a', 'a', 'b', 'b', 'c ', 'd']


