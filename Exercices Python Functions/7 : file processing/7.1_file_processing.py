"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -
# -
# -
# -

# 1. In:
# My program receives a text file called names.txt.
# The file contains first names and last names.


# 2. Process:
# First, I read the names from the file.
# I remove empty lines.
# I remove extra spaces.
# I correct capital letters.
# I keep "van Rossum" as one last name.
# Finally, I sort the names by last name.


# 3. Out:
# The program creates a new file called 7.1_names_sorted.txt.
# The new file contains 8 clean and sorted names.
# The original file is not changed.


# 4. How I decide which word is the last name:
# The first word is the first name.
# All the other words form the last name.
# For example, in Guido van Rossum,
# "van Rossum" is the last name.
# I sort the names alphabetically by last name.




# Your code below
from pathlib import Path


# Find the folder containing the files
folder = Path(__file__).resolve().parent

# Choose the input and output files
input_file = folder / "names.txt"
output_file = folder / "7.1_names_sorted.txt"


# Read the original file
with open(input_file, "r", encoding="utf-8") as file:
    original_lines = file.readlines()


# Create an empty list for clean names
cleaned_names = []


# Read and clean each name
for line in original_lines:

    # Remove extra spaces
    words = line.split()

    # Ignore empty lines
    if len(words) == 0:
        continue

    # Ignore lines without a last name
    if len(words) < 2:
        continue

    # Correct the first name
    first_name = words[0].capitalize()

    # Correct the last name
    family_words = []

    for word in words[1:]:
        if word.lower() == "van":
            family_words.append("van")
        else:
            family_words.append(word.capitalize())

    last_name = " ".join(family_words)

    # Add the clean name to the list
    cleaned_names.append((last_name, first_name))


# Sort names alphabetically by last name
cleaned_names.sort(
    key=lambda name: name[0].lower()
)


# Save the cleaned names in a new file
with open(output_file, "w", encoding="utf-8") as file:

    for last_name, first_name in cleaned_names:
        file.write(first_name + " " + last_name + "\n")


# Display the results
print("Original lines:", len(original_lines))
print("Cleaned names:", len(cleaned_names))
print("Removed lines:", len(original_lines) - len(cleaned_names))

print(
    "First name in sorted file:",
    cleaned_names[0][1],
    cleaned_names[0][0]
)

print(
    "Last name in sorted file:",
    cleaned_names[-1][1],
    cleaned_names[-1][0]
)

print("Output file:", output_file.name)


# CHECK IT YOURSELF

# The original file contains 10 lines.
# The new file contains 8 names.
# Two empty lines were removed.
# Extra spaces and capital letters were corrected.
# The first sorted name is Margaret Hamilton.
# The last sorted name is Guido van Rossum.
# The original names.txt is not modified.
