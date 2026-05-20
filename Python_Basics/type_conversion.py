#Type Conversion in Python
# Implicit Type Conversion
x = 10
y = 5.5
result = x + y  # x is implicitly converted to float
print("Result of implicit type conversion:", result)

# Explicit Type Conversion
a = 10
b = 5.5
# Convert a to float
a_float = float(a)
print("Explicitly converted a to float:", a_float)
# Convert b to int
b_int = int(b)
print("Explicitly converted b to int:", b_int)

x = 10.5
y = str(x)  # Convert float to string
print(type(y))  # Output: <class 'str'>

x = "100"
y = int(x)  # Convert string to integer
print("Explicitly converted x to integer:", y)  
print(type(y))  # Output: <class 'int'>
