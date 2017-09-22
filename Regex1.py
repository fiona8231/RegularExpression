import re

#find "ape"

if re.search("ape", "The ape is here"):
    print("Ape in there")

# find all apex

# output ape ape
allApes = re.findall("ape", "The apes was at the apex")

# output apes apex apess
# . -> represent one character ..-> two like so on
allApes = re.findall("ape.", " The apes was at the apex and it is apesss")

for i in allApes:
    print(i)

# the span, put

theStr =  "The apes was at the apex"

# finditer returns an iterator of matching objects
# You can use span to get the location



for i in re.finditer("ape.", theStr):
    # Span returns a tuple
    locationTuple = i.span()

    print()
    # output (4, 8),  (20, 24)
    print(locationTuple)

# Slice the match out using the tuple values
    print()
    # Output: apes apex
    print(theStr[locationTuple[0]: locationTuple[1]])


animalStr = "Cat rat mat pat cat"

# output ['rat ', 'mat ', 'pat ']
allAnimal = re.findall( "[crmfp]at ", animalStr)
print(allAnimal)

print()
# output: ['Cat', 'mat', 'cat']
someAnimal = re.findall("[c-mC-M]at", animalStr)
print(someAnimal)

# ^ -> represent the character that we dont want

# output: ['mat', 'pat', 'cat']
someAnimal1 = re.findall("[^Cr]at", animalStr)
print(someAnimal1)

# Find & Replacing
# By using compile && sub
owlFood = "rat mat pat cat wot"

# output: rat mat pat cat"
finding = re.compile("[cr]at")
owlFood = finding.sub("owl", owlFood)
print(owlFood)

randStr = "Here is \\stuff"
# Not gonna work
print(re.search("\\stuff", randStr))

# output:  <_sre.SRE_Match object; span=(8, 14), match='\\stuff'>
print(re.search("\\\\stuff", randStr))

# Raw string
# output: print(re.search("\\stuff", randStr))
print(re.search(r"\\stuff", randStr))

# Matching period

randStr1 = "F.B.I. I.R.S. CIA"
# o: Matches:  2
# o: ['F.B.I.', 'I.R.S.']
print(re.findall(".\..\..\.", randStr1))
print("Matches: ", len(re.findall(".\..\..\.", randStr1)))

# Multilines
randStr2 = '''this is a long
string that goes
on for many lines
'''
print(randStr2)

# get rid of the \n replacing by " "
# o: this is a long string that goes on for many lines
finding = re.compile("\n")
randStr2 = finding.sub(" ", randStr2)
print(randStr2)


# ---------- Matching Any Single Number ----------
# \d can be used instead of [0-9]
# \D is the same as [^0-9]

print()
# match 3 numbers only
randStr3 = "123445"
# o: ['123', '445']
match = re.findall("\d{3}", randStr3)
print(match)

# ---------- Matching Any Single Letter or Number ----------
#\w -> represents the numbers and characters
# \w is the same as [a-zA-Z0-9_]
# \W is the same as [^a-zA-Z0-9_]

phoneNum = "324-435-764"

if re.search("\w{3}-\w{3}-\w{3}", phoneNum):
    print("This is the correct format")

# check the range of characters

if re.search("\w{2, 5}", "Unicornnnn"):
    print("the right format")
else:
    print("Invalid name")

# ---------- Matching WhiteSpace ----------
# \s is the same as [\f\n\r\t\v]
# \S is the same as [^\f\n\r\t\v]

# for example \s represents space
if re.search("\w{2, 10}\s\w{1,5}", "Unicorn Cat"):
    print("Valid name")

print()
# ---------- Matching One or More ----------
# + matches 1 or more characters

# Match a followed by 1 or more characters

#o: ['a', 'a', 'a']
finding = re.findall("a+", "a as ape bug")
print(finding)



