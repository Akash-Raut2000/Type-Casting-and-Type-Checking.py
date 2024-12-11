# Type Casting
# Converting between different data types
num_str = "123"            # String
num_int = int(num_str)     # Convert to integer
num_float = float(num_str) # Convert to float
num_bool = bool(num_str)   # Convert to boolean (non-empty string is True)

print("String to Integer:", num_int, "Type:", type(num_int))
print("String to Float:", num_float, "Type:", type(num_float))
print("String to Boolean:", num_bool, "Type:", type(num_bool))

# Casting float to integer
float_num = 45.67
int_num = int(float_num)   # Convert to integer (truncates decimal)
print("Float to Integer:", int_num, "Type:", type(int_num))

# Type Checking
# Using type() function
name = "Alice"
age = 25
is_student = True

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of is_student:", type(is_student))

# Checking types with isinstance()
print("Is 'age' an integer?", isinstance(age, int))
print("Is 'name' a string?", isinstance(name, str))
print("Is 'is_student' a boolean?", isinstance(is_student, bool))
