# ---------- Back References ----------
# A back reference allows you to to reuse the expression that proceeds it

import re

# Match a word boundary, 1 or more characters followed
# by a space if it is then followed by the same
# match that is surrounded by the parentheses

randStr = "The cat cat fell out the window"

finding = re.compile(r"(\b\w+)\s+\1")

matches = re.findall(finding, randStr)
# output: ['cat']
print(matches)

# ---------- Back Reference Substitutions ----------

# Replace the bold tags in the link with no tags
randStr = "<a href='#'><b>The Link</b></a>"
# we want to delete the </b> tag
# ? -> lazy mode
finding = re.compile(r"<b>(.*?)</b>")
# Replace the tags with just the text between them
randStr = re.sub(finding, r"\1", randStr)
# o: <a href='#'>The Link</a>
print(randStr)

# ---------- Another Back Reference Substitution ----------

randStr = "412-555-1212"
# we want (412)555-1212
finding = re.compile(r"([\d]{3})-([\d]{3}-\d{3})")
randStr = re.sub(finding, r"(\1)\2", randStr)
# Output (412)555-1212
print(randStr)

# ---------- PROBLEM ----------
# Receive a string like this

randStr = "https://www.youtube.com http://www.google.com"

# We want
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='https://www.google.com'>www.google.com</a>

# \1 -> represents the contents inside()
# \2 -> represents the second outside ()

finding = re.compile(r"(https?://([\w.]+))")
randStr = re.sub(finding, r"<a herf='\1'>\2</a>", randStr)
print(randStr)

# ---------- Look Ahead ---------- (?=)

randStr = "One two three four"
# Grab all letters and numbers of 1 or more separated
# by a word boundary but don't include it

finding = re.compile(r"\w+(?=\b)")
matches = re.findall(finding, randStr)
# output: ['One', 'two', 'three', 'four']
print(matches)

# ---------- Look Behind ---------- (?<=

# The look behind looks for what is before the text
# to return, but doesn't return it
# It is defined like (?<=expression)

randStr = "1. Bread 2. Apples 3. Lettuce"
# output: ['B', 'A', 'L']
finding = re.compile(r"(?<=\d.\s)\w")

# output ['Bread', 'Apples', 'Lettuce']
finding = re.compile(r"(?<=\d.\s)\w+")

matches = re.findall(finding, randStr)

print(matches)

# ---------- Look Ahead & Behind ----------

randStr = "<h1>I'm Important</h1> <h1>So am I</h1>"
# output: ["I'm Important</h1> <h1>So am I"]
finding = re.compile(r"(?<=<h1>).+(?=</h1>)")
# output: ["I'm Important", 'So am I']
# ? -> lazy!!!!!!!!!!!!!!!!!!!!!!!!!!!
finding = re.compile(r"(?<=<h1>).+?(?=</h1>)")
matches = re.findall(finding, randStr)
print(matches)

# ---------- Negative Look Ahead & Behind ----------
# These are used to look for text that doesn't match
# the pattern

# (?!expression) : Negative Look Ahead
# (?<!expression) : Negative Look Behind

randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
# Grab the total number of grocery items by ignoring the $

regex = re.compile(r"(?<!\$)\d+")

matches = re.findall(regex, randStr)

# output: 3
print(len(matches))

# Convert from a string list to an int list
matches = [int(i) for i in matches]

from functools import reduce

# Sum the items in the list with reduce
print("Total Items {}".format(reduce((lambda x, y: x + y), matches)))


