"""
Topic: Operators in Python — Complete Guide
Section: 01 - Basics
Difficulty: Beginner
Author: Ismail Zia 

Description:
    Every operator in Python — arithmetic, comparison, logical, assignment,
    bitwise, membership, identity, and the walrus operator. Includes
    operator precedence table and practical examples.

Prerequisites:
    - 02_variables_and_datatypes.py
"""

# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================
print("=" * 50)
print("1. ARITHMETIC OPERATORS")
print("=" * 50)

home_goals, away_goals = 17, 5
print(f"{home_goals} + {away_goals}  = {home_goals + away_goals}")      # 22  — Addition
print(f"{home_goals} - {away_goals}  = {home_goals - away_goals}")      # 12  — Subtraction
print(f"{home_goals} * {away_goals}  = {home_goals * away_goals}")      # 85  — Multiplication
print(f"{home_goals} / {away_goals}  = {home_goals / away_goals}")      # 3.4 — Division (ALWAYS returns float)
print(f"{home_goals} // {away_goals} = {home_goals // away_goals}")     # 3   — Floor Division (rounds DOWN)
print(f"{home_goals} % {away_goals}  = {home_goals % away_goals}")      # 2   — Modulus (remainder)
print(f"{home_goals} ** {away_goals} = {home_goals ** away_goals}")     # 1419857 — Exponentiation

# Floor division with negatives (rounds toward -∞, NOT toward zero!)
print(f"\n-17 // 5  = {-17 // 5}")  # -4 (NOT -3!)
print(f"17 // -5  = {17 // -5}")    # -4

# divmod() — returns (quotient, remainder) at once
q, r = divmod(17, 5)
print(f"divmod(17, 5) = ({q}, {r})")  # (3, 2)


# ============================================================
# 2. COMPARISON (RELATIONAL) OPERATORS
# ============================================================
print(f"\n{'=' * 50}")
print("2. COMPARISON OPERATORS")
print("=" * 50)

messi_goals, ronaldo_goals = 10, 20
print(f"{messi_goals} == {ronaldo_goals} : {messi_goals == ronaldo_goals}")     # False — Equal
print(f"{messi_goals} != {ronaldo_goals} : {messi_goals != ronaldo_goals}")     # True  — Not equal
print(f"{messi_goals} > {ronaldo_goals}  : {messi_goals > ronaldo_goals}")      # False — Greater than
print(f"{messi_goals} < {ronaldo_goals}  : {messi_goals < ronaldo_goals}")      # True  — Less than
print(f"{messi_goals} >= {ronaldo_goals} : {messi_goals >= ronaldo_goals}")     # False — Greater or equal
print(f"{messi_goals} <= {ronaldo_goals} : {messi_goals <= ronaldo_goals}")     # True  — Less or equal

# Chained comparisons (unique to Python!)
rating = 85
print(f"\n70 < {rating} < 99 : {70 < rating < 99}")      # True (valid rating range)
print(f"1 < 2 < 3 < 4 : {1 < 2 < 3 < 4}")                 # True
print(f"80 <= {rating} <= 95 : {80 <= rating <= 95}")      # True


# ============================================================
# 3. LOGICAL OPERATORS
# ============================================================
print(f"\n{'=' * 50}")
print("3. LOGICAL OPERATORS")
print("=" * 50)

is_captain, is_injured = True, False
print(f"True and False = {is_captain and is_injured}")     # False — both must be True
print(f"True or False  = {is_captain or is_injured}")      # True  — at least one True
print(f"not True       = {not is_captain}")                # False — negation

# Short-circuit evaluation
# 'and' stops at first False, 'or' stops at first True
print(f"\n5 > 3 and 10 > 7 = {5 > 3 and 10 > 7}")  # True
print(f"5 > 3 or 10 < 7  = {5 > 3 or 10 < 7}")     # True (doesn't check 2nd)

# ⚠️ and/or return VALUES, not just True/False!
print(f"\n'Messi' and 'Ronaldo' = {'Messi' and 'Ronaldo'}")  # 'Ronaldo' (last truthy)
print(f"'' and 'Ronaldo'       = {'' and 'Ronaldo'}")        # '' (first falsy)
print(f"'Messi' or 'Ronaldo'   = {'Messi' or 'Ronaldo'}")   # 'Messi' (first truthy)
print(f"'' or 'Ronaldo'        = {'' or 'Ronaldo'}")         # 'Ronaldo' (first truthy)
print(f"0 or '' or 'Substitute' = {0 or '' or 'Substitute'}")  # 'Substitute'

# Common pattern: default values
formation = "" or "4-3-3"
print(f"formation = {formation}")   # '4-3-3'


# ============================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================
print(f"\n{'=' * 50}")
print("4. ASSIGNMENT OPERATORS")
print("=" * 50)

x = 10;  print(f"x = 10   → {x}")
x += 5;  print(f"x += 5   → {x}")      # 15
x -= 3;  print(f"x -= 3   → {x}")      # 12
x *= 2;  print(f"x *= 2   → {x}")      # 24
x /= 4;  print(f"x /= 4   → {x}")      # 6.0
x //= 2; print(f"x //= 2  → {x}")      # 3.0
x %= 2;  print(f"x %= 2   → {x}")      # 1.0
x **= 3; print(f"x **= 3  → {x}")      # 1.0

# Bitwise assignment
y = 5
y &= 3;  print(f"\n5 &= 3   → {y}")    # 1
y |= 6;  print(f"1 |= 6   → {y}")      # 7
y ^= 3;  print(f"7 ^= 3   → {y}")      # 4
y <<= 2; print(f"4 <<= 2  → {y}")      # 16
y >>= 1; print(f"16 >>= 1 → {y}")      # 8


# ============================================================
# 5. BITWISE OPERATORS
# ============================================================
print(f"\n{'=' * 50}")
print("5. BITWISE OPERATORS")
print("=" * 50)

a, b = 5, 3   # 5 = 0b101, 3 = 0b011
print(f"5 in binary: {bin(5)}")      # 0b101
print(f"3 in binary: {bin(3)}")      # 0b011

print(f"\n5 & 3  = {a & b}  ({bin(a & b)})")     # 1   AND  (001)
print(f"5 | 3  = {a | b}  ({bin(a | b)})")       # 7   OR   (111)
print(f"5 ^ 3  = {a ^ b}  ({bin(a ^ b)})")       # 6   XOR  (110)
print(f"~5     = {~a}  ({bin(~a)})")              # -6  NOT  (inverts all bits)
print(f"5 << 1 = {a << 1} ({bin(a << 1)})")       # 10  Left shift  (1010)
print(f"5 >> 1 = {a >> 1}  ({bin(a >> 1)})")      # 2   Right shift (10)

# Practical uses of bitwise:
# Check if number is even/odd: n & 1 == 0 means even
print(f"\n10 & 1 = {10 & 1} (even)" )    # 0 → even
print(f"7 & 1  = {7 & 1} (odd)")         # 1 → odd


# ============================================================
# 6. MEMBERSHIP OPERATORS (in, not in)
# ============================================================
print(f"\n{'=' * 50}")
print("6. MEMBERSHIP OPERATORS")
print("=" * 50)

champions = ["Barcelona", "Real Madrid", "Bayern"]
print(f"'Barcelona' in champions : {'Barcelona' in champions}")       # True
print(f"'Liverpool' in champions : {'Liverpool' in champions}")       # False
print(f"'Liverpool' not in champions : {'Liverpool' not in champions}")  # True

# Works with strings
print(f"'Real' in 'Real Madrid' : {'Real' in 'Real Madrid'}")        # True
print(f"'real' in 'Real Madrid' : {'real' in 'Real Madrid'}")        # False (case sensitive)

# Works with dicts (checks KEYS, not values)
player = {"name": "Messi", "goals": 15}
print(f"'name' in dict  : {'name' in player}")                       # True
print(f"'Messi' in dict : {'Messi' in player}")                      # False (it's a value!)

# Works with sets (very fast! O(1) lookup)
jersey_numbers = {7, 9, 10, 11, 23}
print(f"10 in set : {10 in jersey_numbers}")                          # True


# ============================================================
# 7. IDENTITY OPERATORS (is, is not)
# ============================================================
print(f"\n{'=' * 50}")
print("7. IDENTITY OPERATORS")
print("=" * 50)

a = [1, 2, 3]
b = a              # b points to SAME object as a
c = [1, 2, 3]      # c is a DIFFERENT object with same value

print(f"a == b : {a == b}")            # True  (same values)
print(f"a is b : {a is b}")            # True  (same object in memory!)
print(f"a == c : {a == c}")            # True  (same values)
print(f"a is c : {a is c}")            # False (different objects!)
print(f"a is not c : {a is not c}")    # True

# == checks VALUE equality
# is checks IDENTITY (same object in memory)

# Always use 'is' for None checks:
red_card = None
print(f"\nred_card is None : {red_card is None}")    # ✅ Correct
print(f"red_card == None : {red_card == None}")      # Works but not recommended


# ============================================================
# 8. WALRUS OPERATOR (:=) — Python 3.8+
# ============================================================
print(f"\n{'=' * 50}")
print("8. WALRUS OPERATOR (:=)")
print("=" * 50)

# Assigns a value AND returns it in a single expression
# Useful in while loops, if statements, comprehensions

# Without walrus:
data = input("") if False else "goal"  # Simulated
n = len(data)
if n > 3:
    print(f"Long string: {n} chars")

# With walrus (more concise):
data = "goal assist"
if (n := len(data)) > 3:
    print(f"Long string: {n} chars")      # Long string: 11 chars

# In list comprehensions:
import math
results = [y for x in range(10) if (y := math.sqrt(x)) > 2]
print(f"sqrt > 2: {results}")

# In while loops:
# while (line := input("Enter: ")) != "quit":
#     print(f"You said: {line}")


# ============================================================
# OPERATOR PRECEDENCE (Highest to Lowest)
# ============================================================
print(f"\n{'=' * 50}")
print("OPERATOR PRECEDENCE")
print("=" * 50)

# Highest → Lowest:
#  1. ()                    — Parentheses
#  2. **                    — Exponentiation
#  3. ~, +x, -x            — Unary NOT, plus, minus
#  4. *, /, //, %           — Multiplication, division, modulus
#  5. +, -                  — Addition, subtraction
#  6. <<, >>                — Bitwise shifts
#  7. &                     — Bitwise AND
#  8. ^                     — Bitwise XOR
#  9. |                     — Bitwise OR
# 10. ==, !=, <, >, <=, >= — Comparisons
# 11. not                   — Logical NOT
# 12. and                   — Logical AND
# 13. or                    — Logical OR
# 14. :=                    — Walrus operator

# Examples:
print(f"2 + 3 * 4     = {2 + 3 * 4}")        # 14 (not 20!)
print(f"(2 + 3) * 4   = {(2 + 3) * 4}")      # 20
print(f"2 ** 3 ** 2   = {2 ** 3 ** 2}")       # 512 (right-to-left: 2^(3^2) = 2^9)
print(f"True or False and False = {True or False and False}")  # True ('and' before 'or')


# ============================================================
# PRACTICE EXERCISES
# ============================================================

# Exercise 1: What is -7 // 2? What is -7 % 2? Explain why.
# Exercise 2: Use chained comparison to check if a player's rating is between 1 and 99.
# Exercise 3: Use bitwise operators to check if a jersey number is even or odd.
# Exercise 4: What does `"" or "4-3-3"` return? Why?
# Exercise 5: Use the walrus operator to simplify a player rating validation.
