"""
Topic: Type Conversion & Casting
Section: 01 - Basics
Difficulty: Beginner
Author: Messi Zia

Description:
    Implicit and explicit type conversions, type checking with
    type() and isinstance(), and edge cases to watch out for.

Prerequisites:
    - 02_variables_and_datatypes.py
"""

# ============================================================
# TYPE CONVERSION (CASTING)
# ============================================================

# --- IMPLICIT CONVERSION (Python does it automatically) ---
print("--- IMPLICIT CONVERSION ---")

# int + float → float (Python promotes int to float)
result = 10 + 3.5
print(f"10 + 3.5 = {result}, type: {type(result)}")   # 13.5, float

# int + bool → int (True=1, False=0)
result = 10 + True
print(f"10 + True = {result}, type: {type(result)}")   # 11, int

# bool + float → float
result = True + 2.5
print(f"True + 2.5 = {result}")    # 3.5

# ⚠️ Python does NOT auto-convert str + int
# print("Goals: " + 25)  # ❌ TypeError!
print("Goals: " + str(25))  # ✅ Explicit conversion needed


# --- EXPLICIT CONVERSION (You do it manually) ---
print("\n--- EXPLICIT CONVERSION ---")

# int() — convert to integer
print(f"int('42')    = {int('42')}")          # 42
print(f"int(3.99)    = {int(3.99)}")          # 3 (truncates, NOT rounds!)
print(f"int(True)    = {int(True)}")          # 1
print(f"int(False)   = {int(False)}")         # 0
print(f"int('0b1010', 2) = {int('1010', 2)}")  # 10 (binary to int)
print(f"int('FF', 16)    = {int('FF', 16)}")   # 255 (hex to int)
# int("goal")  # ❌ ValueError!
# int("")       # ❌ ValueError!

# float() — convert to float
print(f"\nfloat('3.14') = {float('3.14')}")   # 3.14
print(f"float(42)     = {float(42)}")          # 42.0
print(f"float('inf')  = {float('inf')}")       # inf
print(f"float(True)   = {float(True)}")        # 1.0

# str() — convert to string
print(f"\nstr(42)    = '{str(42)}'")           # '42'
print(f"str(3.14)  = '{str(3.14)}'")           # '3.14'
print(f"str(True)  = '{str(True)}'")           # 'True'
print(f"str(None)  = '{str(None)}'")           # 'None'
print(f"str([1,2]) = '{str([1, 2])}'")         # '[1, 2]'

# bool() — convert to boolean
print(f"\nbool(1)     = {bool(1)}")            # True
print(f"bool(0)     = {bool(0)}")              # False
print(f"bool('')    = {bool('')}")             # False (empty string)
print(f"bool('hi')  = {bool('hi')}")           # True
print(f"bool([])    = {bool([])}")             # False (empty list)
print(f"bool([0])   = {bool([0])}")            # True (non-empty list!)
print(f"bool(None)  = {bool(None)}")           # False

# list(), tuple(), set() conversions
print(f"\nlist('goal')     = {list('goal')}")       # ['h','e','l','l','o']
print(f"tuple([1,2,3])   = {tuple([1, 2, 3])}")      # (1, 2, 3)
print(f"set([1,1,2,3])   = {set([1, 1, 2, 3])}")     # {1, 2, 3}
print(f"list(range(5))   = {list(range(5))}")         # [0, 1, 2, 3, 4]
print(f"list((1,2,3))    = {list((1, 2, 3))}")        # [1, 2, 3]

# dict() conversions
stats_pairs = [("goals", 15), ("assists", 20), ("rating", 93)]
print(f"dict(pairs) = {dict(stats_pairs)}")               # {'goals': 15, 'assists': 20, 'rating': 93}

# chr() and ord() — character ↔ ASCII/Unicode
print(f"\nchr(65)  = '{chr(65)}'")             # 'A'
print(f"chr(97)  = '{chr(97)}'")               # 'a'
print(f"ord('A') = {ord('A')}")                # 65
print(f"ord('a') = {ord('a')}")                # 97


# ============================================================
# TYPE CHECKING
# ============================================================
print("\n" + "=" * 50)
print("TYPE CHECKING")
print("=" * 50)

jersey = 10
print(f"type(10)        = {type(jersey)}")              # <class 'int'>
print(f"type(10) == int = {type(jersey) == int}")       # True

# isinstance() — preferred! Also works with inheritance
print(f"isinstance(42, int)       = {isinstance(42, int)}")         # True
print(f"isinstance(42, (int, float)) = {isinstance(42, (int, float))}")  # True (check multiple)
print(f"isinstance(True, int)     = {isinstance(True, int)}")       # True! (bool is subclass of int)
print(f"isinstance(True, bool)    = {isinstance(True, bool)}")      # True

# type() vs isinstance():
# type()       — checks EXACT type only
# isinstance() — checks type AND parent types (inheritance)


# ============================================================
# COMMON CONVERSION PITFALLS
# ============================================================
print("\n--- COMMON PITFALLS ---")

# 1. int() truncates, doesn't round
print(f"int(3.9) = {int(3.9)}")    # 3 (NOT 4!)
print(f"round(3.9) = {round(3.9)}") # 4 (use round for rounding)

# 2. int() on invalid strings
try:
    int("3.14")    # ❌ ValueError! Can't convert float string to int directly
except ValueError as e:
    print(f"int('3.14') → Error: {e}")

# Fix: convert to float first, then int
print(f"int(float('3.14')) = {int(float('3.14'))}")   # 3

# 3. Be careful with bool()
print(f"\nbool('False') = {bool('False')}")  # True! (non-empty string)
print(f"bool('0')     = {bool('0')}")        # True! (non-empty string)
print(f"bool('')      = {bool('')}")          # False (empty string)


# ============================================================
# PRACTICE EXERCISES
# ============================================================

# Exercise 1: Convert user input (string) to int for jersey numbers. Handle errors.
# Exercise 2: Convert a list of string goal counts ["3","1","4"] to integers.
# Exercise 3: Convert a player's match rating from string "8.5" to float.
# Exercise 4: What does int("0xFF", 16) return? What about int("0o17", 8)?
# Exercise 5: Why does bool("False") return True? How would you fix it?
