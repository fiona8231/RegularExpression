import re
# ---------- OR CONDITIONAL ----------
# You can use | to define the matches you'll except

randStr = "1. Dog 2. Cat 3. Turtle 4. Fish"
finding = re.compile(r"\d.\s(Dog|Cat)")
matches = re.findall(finding, randStr)
# output: ['Dog', 'Cat']
print(matches)

# ---------- PROBLEM ----------
# Create a regex that will match for 5 digit zip codes
# Or zip codes with 5 digits a dash and then 4 digits

randStr = "12345 12345-1234 1234 12346-333"

finding = re.compile(r"(\d{5}\s|\d{5}-\d{4})")
matches = re.findall(finding, randStr)
# output: ['12345 ', '12345-1234']
print(matches)

# ---------- GROUP ----------
# We can use group to retrieve parts of regex matches

'''bd = input("Enter your birthday (mm-dd-yyyy) : ")

# By using () to represents the group
finding = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)

print("You are born on ", finding.group())
print("Birth month ", finding.group(1))
print("Birth Day ", finding.group(2))
print("Birth Year ", finding.group(3))'''


# ---------- MATCH OBJECT FUNCTIONS ----------
# There are functions that provide more information on your matches

matches = re.search(r"\d{2}", "The 12 chicken weighed 13 lbs ")
# output:12 only the first number
print(matches.group())

# output: (4, 6)
print(matches.span())

# output: 4
print(matches.start())
# output 6
print(matches.end())

# ---------- NAMED GROUPS ----------
# You can also assign names to matches ?P -> group tag

randStr = "December 21 1974"

# ^ : Beginning of String
finding = r"^(?P<month>\w+)\s(?P<day>\d+)\s(?P<year>\d+)"

matches = re.search(finding, randStr)
print("Month: ", matches.group('month'))
print("Year: ", matches.group('year'))
print("Day: ", matches.group('day'))

# ---------- PROBLEM ----------
# Find all of the following email addresses

randStr = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"

finding = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+")
matches =re.findall(finding, randStr)
print(matches)















