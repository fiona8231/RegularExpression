# ---------- Problem ----------
# Create a Regex that matches email addresses from a list
# 1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
# 2. An @ symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

import re
emailList = "db@aol.com m@.com @apple.com db@.com eat@email.com"
# . -> period
# Do not put spact between {1, 20} like this!!!!!
finding = re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", emailList)
# o: 2
print("Matches Number :", len(finding))

# ---------- PROBLEM ----------
# Create a regex that will grab each of the lines in this
# string, print out the number of matches and each line

print()

longStr = '''Just some words
and some more\r
and more
'''
# o: 'Just some words\n', 'and some more\r\n', 'and more\n']
finding = re.compile(r"[\w\s]+?\n")
matches = re.findall(finding, longStr)
print(matches)

# output:  Just some words
# and some more
# and more
for i in matches:
    print(i)


