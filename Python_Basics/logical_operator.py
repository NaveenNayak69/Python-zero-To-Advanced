#logical Operators
a = True
b = False

# AND
and_result = a and b
print("AND:", and_result)

"""The AND operator returns True only if both operands are True. In this case, since b is False, the result is False."""

#Real world example of AND operator
username_correct = True
password_correct = False

if username_correct and password_correct:
    print("Login successful!")
else:
    print("Invalid credentials.")  # This will print because one condition is False


# OR
or_result = a or b
print("OR:", or_result)

"""The OR operator returns True if at least one of the operands is True. In this case, since a is True, the result is True."""

#Real world example of OR operator
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("You can relax!")  # This will print because one condition is True

   
# NOT
not_result = not a
print("NOT:", not_result)

"""The not operator is a bit different because it only acts on a single condition. 
It simply reverses the boolean value—turning True into False, and False into True.."""

#Real world example of NOT operator
is_raining = False
if not is_raining:
    print("You can go outside!")  # This will print because is_raining is False

