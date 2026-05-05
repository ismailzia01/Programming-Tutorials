"""
Topic: Goal Assist — Your First Python Program
Section: 01 - Basics
Difficulty: Beginner
Author: Ismail Zia

Description:
    Your very first step into Python! This file covers what Python is,
    how to write your first program, how comments work, and how to use
    the print() function with all its features.

Prerequisites:
    - Python 3.10+ installed on your system
    - A text editor or IDE (VS Code recommended)

Key Concepts:
    - What is Python?
    - The print() function
    - Single-line and multi-line comments
    - Docstrings
"""

# ============================================================
# HELLO WORLD — Your First Python Program
# ============================================================

# --- WHAT IS PYTHON? ---
# Python was created by Guido van Rossum in 1991
# Key characteristics:
#   • Interpreted — runs line by line, no compilation needed
#   • Dynamically typed — no need to declare variable types
#   • Object-oriented — supports classes and objects
#   • High-level — abstracts away hardware details
#   • Readable — syntax is clean and close to English
#   • Versatile — web, AI/ML, automation, data science, and more

# --- YOUR FIRST PROGRAM ---
print("Goal, Assist!")                      # The classic first program! ⚽

# Congratulations! That one line is a complete Python program.
# No boilerplate, no semicolons, no main() function needed.

# Compare with Java:
#   public class Main {
#       public static void main(String[] args) {
#           System.out.println("Goal, Assist!");
#       }
#   }
# Python: 1 line vs Java: 5 lines


# ============================================================
# COMMENTS — Notes for Humans, Ignored by Python
# ============================================================

# --- SINGLE-LINE COMMENTS ---
# This is a comment. Python ignores everything after #
# Use comments to explain WHY, not WHAT

jersey_number = 10  # You can also put comments at the end of a line

# --- MULTI-LINE COMMENTS ---
# Python doesn't have a dedicated multi-line comment syntax.
# Convention: use multiple # signs

# This is a
# multi-line
# comment

# Or use triple-quoted strings (these are actually string literals,
# but when not assigned to a variable, Python ignores them):
"""
This acts like a multi-line comment.
However, technically it's a string literal
that isn't assigned to anything.
"""

'''
You can also use single triple quotes.
Both work the same way.
'''

# --- DOCSTRINGS ---
# Triple-quoted strings placed as the FIRST statement in a
# function, class, or module become documentation (docstrings).

def announce_player(player_name):
    """Announce a football player entering the pitch.

    Args:
        player_name (str): The name of the player.

    Returns:
        str: An announcement message.
    """
    return f"Now entering the pitch: {player_name}!"

# Access the docstring programmatically:
print(announce_player.__doc__)
print(announce_player("Messi"))


# ============================================================
# THE print() FUNCTION — Detailed Guide
# ============================================================

# --- BASIC PRINTING ---
print("Goal scored!")                       # String
print(10)                                  # Integer (jersey number)
print(93.5)                                # Float (player rating)
print(True)                                # Boolean (is_captain)
print(None)                                # NoneType (no red cards)

# --- MULTIPLE ARGUMENTS ---
# print() accepts multiple values, separated by spaces by default
print("Player:", "Messi", "Goals:", 15)    # Player: Messi Goals: 15

# --- THE `sep` PARAMETER ---
# Changes the separator between multiple arguments (default: space)
print("Messi", "Ronaldo", "Mbappe")         # Messi Ronaldo Mbappe
print("Messi", "Ronaldo", "Mbappe", sep="-")  # Messi-Ronaldo-Mbappe
print("M", "C", "F", sep="")                  # MCF
print("Messi", "Ronaldo", "Mbappe", sep=" | ")  # Messi | Ronaldo | Mbappe
print(2026, 5, 4, sep="/")                 # 2026/5/4

# --- THE `end` PARAMETER ---
# Changes what's printed at the end (default: newline \n)
print("Goal", end=" ")
print("Assist")                              # Goal Assist (same line)

print("Loading", end="...")
print("Done!")                              # Loading...Done!

# --- PRINTING ON THE SAME LINE (loop example) ---
for i in range(1, 6):
    print(i, end=" ")                       # 1 2 3 4 5
print()                                     # Move to next line

# --- PRINTING SPECIAL CHARACTERS ---
print("Line 1\nLine 2")                    # \n = newline
print("Column1\tColumn2")                  # \t = tab
print("She said \"Goal\"")                # \" = double quote
print('It\'s Python')                      # \' = single quote
print("Path: C:\\Users\\Messi")           # \\ = backslash

# --- RAW STRINGS ---
# Prefix with r to ignore escape characters
print(r"C:\Users\new_folder\test")         # Prints literally, no escaping

# --- PRINTING EMPTY LINES ---
print()                                     # Just an empty line
print("Before")
print()
print("After")


# ============================================================
# PYTHON PHILOSOPHY — The Zen of Python
# ============================================================

# Run this in your terminal to see Python's guiding principles:
# >>> import this

# Key principles:
# • Beautiful is better than ugly
# • Explicit is better than implicit
# • Simple is better than complex
# • Readability counts
# • There should be one obvious way to do it


# ============================================================
# PRACTICE EXERCISES
# ============================================================

# Exercise 1: Print your favourite player, their club, and jersey number on separate lines
# Exercise 2: Print a pattern using print() and \n:
#             ⚽
#             ⚽⚽
#             ⚽⚽⚽
# Exercise 3: Print "MESSI" with each letter separated by a dot (M.E.S.S.I)
#             Hint: Use sep parameter with unpacking print(*"MESSI", sep=".")
# Exercise 4: Write a function with a proper docstring, then print its docstring

# --- SOLUTIONS ---
# Exercise 3:
print(*"MESSI", sep=".")                    # M.E.S.S.I

# Exercise 4:
def total_goals(league_goals, cup_goals):
    """Calculate total goals from league and cup competitions."""
    return league_goals + cup_goals

print(total_goals.__doc__)                  # Calculate total goals from league and cup competitions.
