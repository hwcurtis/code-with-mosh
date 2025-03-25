course = "     python programming    "
print(course.upper())  # all letters in upper case
print(course)
print(course.lower())   # sll letters in lower case
print(course.title())  # first two letters capitalized
# removes the white space ...also  r and l gets rid of white space on left and right
print(course.strip())
# index of character or seq of character  "calling the find method" returns the index
print(course.find("Pro"))
print(course.replace("p", "j"))  # replace a letter or word
# existance of charater this the "in" operator "checking the "expression" returns the boulon of true or false
print("pro" in course)
print("swift"not in course)  # does not contain characters or seq of characters
