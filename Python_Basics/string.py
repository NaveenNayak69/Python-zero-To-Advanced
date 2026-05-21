#indexing : Indexing allows us to access individual characters in a string or individual elements in a list using their position. The index starts at 0 for the first character or element.
name = "Alice"
print(name[0])  # Output: A
print(name[1])  # Output: l
print(name[2])  # Output: i
print(name[3])  # Output: c
print(name[4])  # Output: e

tasks = ["Buy groceries", "Clean the house", "Pay bills", "Call mom"]
print(tasks[0])  # Output: Buy groceries
print(tasks[1])  # Output: Clean the house
print(tasks[2])  # Output: Pay bills
print(tasks[3])  # Output: Call mom

print(len(name))  # Output: 5
print(len(tasks))  # Output: 4

#slicing : Slicing allows us to extract a portion of a string or list by specifying a range of indices. The syntax for slicing is [start:stop:step], where start is the index to begin slicing, stop is the index to end slicing (exclusive), and step is the interval between indices (optional).
print(name[1:4])  # Output: lice
print(name[:3])   # Output: Ali 
print(name[2:4])  # Output: li
print(name[::2])  # Output: Ace
print(tasks[1:3])  # Output: ['Clean the house', 'Pay bills']
print(tasks[:2])   # Output: ['Buy groceries', 'Clean the house']   
print(tasks[2:])   # Output: ['Pay bills', 'Call mom']
print(tasks[::2])  # Output: ['Buy groceries', 'Pay bills']
print(tasks[ : -1])  # Output: ['Buy groceries', 'Clean the house', 'Pay bills']
