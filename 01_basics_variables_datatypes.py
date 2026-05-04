# ============================================================
# TOPIC 1: BASICS, VARIABLES & DATA TYPES
# ============================================================
# Python was created by Guido van Rossum in 1991
# Python is interpreted, dynamically typed, and object-oriented
# ============================================================

# --- COMMENTS ---
# This is a single-line comment

"""
This is a multi-line comment (docstring)
Used for documentation
"""

# --- VARIABLES ---
# A variable is a name that refers to a value in memory
# No declaration needed — just assign!

name = "Ismail"        # string
age = 24               # integer
height = 5.9           # float
is_student = True      # boolean
nothing = None         # NoneType

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print("Nothing:", nothing)

# --- VARIABLE NAMING RULES ---
# 1. Must start with letter or underscore
# 2. Can contain letters, digits, underscores
# 3. Case-sensitive (Name != name)
# 4. Cannot use keywords (if, else, for, class, etc.)

my_variable = 10       # valid
_private = 20          # valid
var2 = 30              # valid
# 2var = 40            # INVALID — can't start with digit
# my-var = 50          # INVALID — no hyphens

# --- MULTIPLE ASSIGNMENT ---
a, b, c = 1, 2, 3           # assign different values
x = y = z = 0               # assign same value
print(a, b, c)               # 1 2 3
print(x, y, z)               # 0 0 0

# --- DATA TYPES ---
print("\n--- DATA TYPES ---")

# 1. Integer (int) — whole numbers, no size limit
num_int = 100
big_int = 99999999999999999999
print(type(num_int))         # <class 'int'>

# 2. Float — decimal numbers
num_float = 3.14
scientific = 2.5e3           # 2500.0 (scientific notation)
print(type(num_float))       # <class 'float'>

# 3. Complex — real + imaginary
num_complex = 3 + 4j
print(type(num_complex))     # <class 'complex'>
print(num_complex.real)      # 3.0
print(num_complex.imag)      # 4.0

# 4. String (str) — text
str1 = 'Hello'               # single quotes
str2 = "World"               # double quotes
str3 = """Multi
line string"""               # triple quotes
print(type(str1))            # <class 'str'>

# 5. Boolean (bool) — True or False
flag = True
print(type(flag))            # <class 'bool'>
print(bool(0))               # False
print(bool(1))               # True
print(bool(""))              # False (empty string)
print(bool("hello"))         # True (non-empty string)

# 6. List — ordered, mutable
my_list = [1, 2, 3, "hello", True]
print(type(my_list))         # <class 'list'>

# 7. Tuple — ordered, immutable
my_tuple = (1, 2, 3)
print(type(my_tuple))        # <class 'tuple'>

# 8. Dictionary — key-value pairs
my_dict = {"name": "Ismail", "age": 24}
print(type(my_dict))         # <class 'dict'>

# 9. Set — unordered, unique elements
my_set = {1, 2, 3, 3, 3}
print(my_set)                # {1, 2, 3} — duplicates removed!
print(type(my_set))          # <class 'set'>

# 10. NoneType
val = None
print(type(val))             # <class 'NoneType'>

# --- TYPE CONVERSION (CASTING) ---
print("\n--- TYPE CONVERSION ---")
a = int("5")                 # str to int → 5
b = float(10)                # int to float → 10.0
c = str(100)                 # int to str → "100"
d = int(3.9)                 # float to int → 3 (truncates!)
e = list("hello")            # str to list → ['h', 'e', 'l', 'l', 'o']
f = tuple([1, 2, 3])         # list to tuple → (1, 2, 3)
g = set([1, 1, 2, 3])        # list to set → {1, 2, 3}
h = bool(0)                  # int to bool → False
i = bool(42)                 # int to bool → True

print(f"int('5') = {a}")
print(f"float(10) = {b}")
print(f"str(100) = {c}")
print(f"int(3.9) = {d}")
print(f"list('hello') = {e}")
print(f"tuple([1,2,3]) = {f}")
print(f"set([1,1,2,3]) = {g}")
print(f"bool(0) = {h}, bool(42) = {i}")

# --- TYPE CHECKING ---
print("\n--- TYPE CHECKING ---")
x = 10
print(type(x))               # <class 'int'>
print(isinstance(x, int))    # True
print(isinstance(x, str))    # False
