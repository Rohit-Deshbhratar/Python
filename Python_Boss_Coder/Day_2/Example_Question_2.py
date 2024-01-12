# Concatenate two strings and print the result.

string1 = "Rohit"
string2 = "Deshbhratar"

# Using "+" operator
print(string1 +" "+ string2)

# Using join() method
print(" ".join([string1, string2]))

# Using "%" operator 
print("%s %s" % (string1, string2))

# Using .format()
print("{} {}".format(string1, string2))

# Using ","
print(string1, string2)

# Using "f-string"
print(f"{string1} {string2}")