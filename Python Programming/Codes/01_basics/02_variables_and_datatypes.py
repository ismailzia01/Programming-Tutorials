"""
Topic: Variables & Data Types
Section: 01 - Basics
Difficulty: Beginner
Author: Messi Zia

Description:
    Everything about Python variables — how to create them, naming rules,
    and a deep dive into every built-in data type with examples.

Prerequisites:
    - 01_goal_assist.py

Key Concepts:
    - Variable creation and assignment
    - Naming conventions (snake_case, PEP 8)
    - All built-in data types
    - Mutable vs Immutable types
    - Memory model (id, references)
"""

# ============================================================
# VARIABLES — Names That Point to Values
# ============================================================

# In Python, variables are just NAMES that REFER to objects in memory.
# No declaration needed — just assign!

player_name = "Messi"       # str
jersey_number = 10          # int
player_rating = 93.5        # float
is_captain = True           # bool
red_card = None             # NoneType

print("Player:", player_name)
print("Jersey:", jersey_number)
print("Rating:", player_rating)
print("Captain:", is_captain)
print("Red Card:", red_card)


# ============================================================
# VARIABLE NAMING RULES
# ============================================================

# 1. Must start with a letter (a-z, A-Z) or underscore (_)
# 2. Can contain letters, digits (0-9), and underscores
# 3. Case-sensitive (Name ≠ name ≠ NAME)
# 4. Cannot use Python keywords (if, else, for, class, def, etc.)

my_variable = 10        # ✅ Valid — snake_case (recommended)
_private = 20            # ✅ Valid — convention for "internal use"
var2 = 30                # ✅ Valid — digits allowed (not at start)
myVariable = 40          # ✅ Valid — camelCase (not Pythonic, but works)
# 2var = 50              # ❌ Invalid — cannot start with digit
# my-var = 60            # ❌ Invalid — hyphens not allowed
# class = 70             # ❌ Invalid — 'class' is a keyword

# --- PEP 8 NAMING CONVENTIONS ---
# Variables & functions: snake_case       → player_name, calculate_points
# Constants:             UPPER_SNAKE_CASE → MAX_SQUAD_SIZE, PITCH_LENGTH
# Classes:               PascalCase       → FootballPlayer, MatchResult
# Private:               _leading_underscore → _internal_method
# "Really" private:      __double_leading  → __secret (name mangling)
# Dunder/Magic:          __double_both__   → __init__, __str__

MAX_SQUAD_SIZE = 25      # Constant (convention — Python doesn't enforce it)


# ============================================================
# MULTIPLE ASSIGNMENT
# ============================================================

goals, assists, rating = 15, 20, 93       # Assign different values
home = away = drawn = 0                   # Assign same value to multiple
print(f"goals={goals}, assists={assists}, rating={rating}")
print(f"home={home}, away={away}, drawn={drawn}")

# Swap values — Pythonic way!
home_score, away_score = 3, 1
home_score, away_score = away_score, home_score
print(f"After swap: home={home_score}, away={away_score}")   # home=1, away=3


# ============================================================
# DATA TYPES — Complete Guide
# ============================================================
print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)

# --- 1. INTEGER (int) ---
# Whole numbers, NO size limit in Python!
num_int = 100
big_int = 99999999999999999999999999999
negative = -42
print(f"\nint: {num_int}, type: {type(num_int)}")
print(f"Big int: {big_int}")

# Integer representations
binary = 0b1010          # Binary → 10
octal = 0o17             # Octal → 15
hexadecimal = 0xFF       # Hex → 255
print(f"Binary 0b1010 = {binary}, Octal 0o17 = {octal}, Hex 0xFF = {hexadecimal}")

# Underscores for readability (Python 3.6+)
population = 1_400_000_000
print(f"Population: {population}")

# --- 2. FLOAT (float) ---
num_float = 3.14
scientific = 2.5e3           # 2500.0
infinity = float('inf')
not_a_number = float('nan')
print(f"\nfloat: {num_float}, type: {type(num_float)}")
print(f"Scientific: {scientific}, Infinity: {infinity}")

# ⚠️ FLOATING POINT PRECISION WARNING
print(f"0.1 + 0.2 = {0.1 + 0.2}")              # 0.30000000000000004 (NOT 0.3!)
print(f"0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}") # False!
print(f"Fix: round(0.1 + 0.2, 1) = {round(0.1 + 0.2, 1)}")

from decimal import Decimal
print(f"Decimal fix: {Decimal('0.1') + Decimal('0.2')}")  # 0.3 exact

# --- 3. COMPLEX (complex) ---
num_complex = 3 + 4j
print(f"\ncomplex: {num_complex}, type: {type(num_complex)}")
print(f"Real: {num_complex.real}, Imaginary: {num_complex.imag}")
print(f"Conjugate: {num_complex.conjugate()}")

# --- 4. STRING (str) ---
str1 = 'Single quotes'
str2 = "Double quotes"
str3 = """Triple quotes\ncan span multiple lines"""
str4 = r"Raw string: \n is literal"
print(f"\nstr: '{str1}', type: {type(str1)}")

# --- 5. BOOLEAN (bool) ---
flag = True
print(f"\nbool: {flag}, type: {type(flag)}")
print(f"True + True = {True + True}")     # 2 (True is 1)
print(f"True * 10 = {True * 10}")          # 10

# Falsy values:
print("\n--- Falsy Values ---")
falsy_values = [False, 0, 0.0, 0j, "", [], (), {}, set(), None]
for val in falsy_values:
    print(f"  bool({val!r:12}) = {bool(val)}")

# Everything else is Truthy!
print(f"bool('goal') = {bool('goal')}")   # True
print(f"bool(42) = {bool(42)}")             # True

# --- 6. LIST (list) ---
squad = ["Messi", "Haaland", "Mbappe", 10, True, [4, 5]]
print(f"\nlist: {squad}, type: {type(squad)}")

# --- 7. TUPLE (tuple) ---
match_score = (3, 1, "Barcelona")
single_tuple = (5,)      # Comma needed for single element!
print(f"tuple: {match_score}, type: {type(match_score)}")

# --- 8. DICTIONARY (dict) ---
player = {"name": "Messi", "goals": 15}
print(f"dict: {player}, type: {type(player)}")

# --- 9. SET (set) ---
my_set = {1, 2, 3, 3, 3}
print(f"set: {my_set}, type: {type(my_set)}")   # {1, 2, 3}

# --- 10. FROZENSET (frozenset) ---
my_frozenset = frozenset([1, 2, 3])
print(f"frozenset: {my_frozenset}, type: {type(my_frozenset)}")

# --- 11. BYTES & BYTEARRAY ---
my_bytes = b"goal"
my_bytearray = bytearray(b"goal")
my_bytearray[0] = 72     # Change 'h' to 'H'
print(f"\nbytes: {my_bytes}")
print(f"bytearray: {my_bytearray}")

# --- 12. NONETYPE ---
val = None
print(f"\nNone: {val}, type: {type(val)}")
print(f"Always use 'is': val is None → {val is None}")


# ============================================================
# MUTABLE vs IMMUTABLE
# ============================================================
print("\n" + "=" * 50)
print("MUTABLE vs IMMUTABLE")
print("=" * 50)

# IMMUTABLE: int, float, complex, str, tuple, frozenset, bytes, bool, None
# MUTABLE:   list, dict, set, bytearray

# Immutable — creates new object on "change"
club = "Barcelona"
old_club = club
club = "Inter Miami"
print(f"club: {club}, old_club: {old_club}")  # old_club still "Barcelona"

# Mutable — changes affect all references!
lineup1 = ["Messi", "Neymar", "Suarez"]
lineup2 = lineup1              # Both point to SAME object
lineup1.append("Busquets")
print(f"lineup1: {lineup1}")   # ['Messi', 'Neymar', 'Suarez', 'Busquets']
print(f"lineup2: {lineup2}")   # ALSO changed!

# Fix: Make a copy
lineup3 = ["Messi", "Neymar", "Suarez"]
lineup4 = lineup3.copy()       # Independent copy
lineup3.append("Busquets")
print(f"lineup3: {lineup3}, lineup4: {lineup4}")  # lineup4 unchanged


# ============================================================
# MEMORY MODEL — id() and References
# ============================================================
print("\n" + "=" * 50)
print("MEMORY MODEL")
print("=" * 50)

a = 42
b = 42
print(f"id(a) = {id(a)}, id(b) = {id(b)}")
print(f"a is b: {a is b}")     # True! Python caches small ints (-5 to 256)

s1 = "goal"
s2 = "goal"
print(f"s1 is s2: {s1 is s2}") # True (string interning)


# ============================================================
# PRACTICE EXERCISES
# ============================================================

# Exercise 1: Create variables for player name, club, jersey, rating.
#             Print them with f-strings.
# Exercise 2: Show mutable vs immutable with a squad list and a player name string.
# Exercise 3: What is the type of: 10, 93.5, "Messi", True, None, ["GK"], (3,1)?
# Exercise 4: Show that 0, "", [], (), {}, None, set() are all falsy.
# Exercise 5: Why does 0.1 + 0.2 != 0.3? How to fix it?
