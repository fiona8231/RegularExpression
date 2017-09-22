import re

randStr = "cat cats"

#o: ['cats']
finding = re.compile("[cat]+s")
matches = re.findall(finding, randStr)

print(matches)

# o: ['cat', 'cats']
# ? -> represents 0 or 1 of whatever precedes it.
finding = re.compile("[cat]+s?")
matches = re.findall(finding, randStr)
print(matches)

# ---------- Matching Zero or More ----------
# * matches zero or more of what proceeds it

randStr = "doctor doctors doctor's doctorsss"

# Match doctor doctors or doctor's
finding = re.findall("[doctor]+['s]*", randStr)
# o: ['doctor', 'doctors', "doctor's", 'doctorsss']
print(finding)

# ---------- Greedy & Lazy Matching ----------

randStr = "<name>Life On Mars</name><name>Freaks and Geeks</name>"

# Greedy -> Grab the largest possible
finding = re.compile("<name>.*</name>")

# o: ['<name>Life On Mars</name><name>Freaks and Geeks</name>'], which is not good enough

matches = re.findall(finding, randStr)
print(matches)

# Lazy -> Grab the smallest possible
# We want to grab the smallest match we use *?, +?, or
# {n,}? instead

# output: ['<name>Life On Mars</name>', '<name>Freaks and Geeks</name>']
finding = re.compile("<name>.*?</name>")
matches = re.findall(finding, randStr)
print(matches)

# If we want to get rid of the <name>
finding = re.compile("<name>(.*?)</name>")
matches = re.findall(finding, randStr)
# ['Life On Mars', 'Freaks and Geeks']
print(matches)

# ---------- Word Boundaries ----------
# We use word boundaries to define where our matches start
# and end

# \b matches the start or end of a word

# If we want ape it will match ape and the beginning of apex

randStr = "ape at the apex sssape ape"

finding = re.compile(r"\bape\b")
matches = re.findall(finding, randStr)
#o: 2
print(len(matches))


print()
# ---------- String Boundaries ----------
# ^ : Matches the beginning of a string if outside of a [ ]
# $ : Matches the end of a string

# Grab everything from the start of the string, except for @

randStr = "Match everything up to @"
finding = re.compile(r"^.*[^@]")
matches = re.findall(finding, randStr)
# output: ['Match everything up to ']
print(matches)

# matching the end fo the string
randStr = "@ Get this string"

finding = re.compile(r"[^@\s].*$")
# o: ['Get this string']
matches = re.findall(finding, randStr)
print(matches)


print()
# Grab the 1st word of each line using the the multiline
# code which allows for the targeting of each line after
# a line break with ^
randStr = '''Ape is big
Turtle is slow
Cheetah is fast'''

# ^ -> Matches the beginning of a string if outside of a [ ]
finding =re.compile(r"(?m)^.*?\s")
# o: ['Ape ', 'Turtle ', 'Cheetah ']
matches = re.findall(finding, randStr)
print(matches)

# ---------- Subexpressions ----------
# surround what you want with ( )

# we looking for 555-1212
randStr = "My number is 412-555-1212"

finding = re.compile(r"412-(.*)")
# output: ['555-1212']
matches = re.findall(finding, randStr)
print(matches)

print()
# ---------- Problem ----------

# Get just the numbers minus the area codes from this string
randStr = "412-555-1212 412-555-1213 412-555-1214"
# output: ['555-1212', '555-1213', '555-1214']
# next 8th characters
finding = re.compile(r"412-(.{8})")
matches = re.findall(finding, randStr)
print(matches)

print()
# ---------- Multiple Subexpressions ----------

# You can have multiple subexpressions as well
# Get both numbers that follow 412 separately
randStr = "My number is 412-555-1212"

finding = re.compile(r"412-(.*)-(.*)")
matches = re.findall(finding, randStr)

# output 555
print(matches[0][0])
# output: 1212
print(matches[0][1])
