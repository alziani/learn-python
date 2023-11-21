# ----------------------
# -- Strings Methods
# ----------------------

# split()  rsplit()

a = "I Love Python and JavaScript and MySQL"
print(a.split())

b = "I-Love-Python-and-JavaScript-and-MySQL"
print(b.split("-"))
 
c = "I-Love-Python-and-JavaScript-and-MySQL"
print(c.split("-", 3)) 

d = "I-Love-Python-and-JavaScript-and-MySQL"
print(d.rsplit("-", 3))

# center()

e = "Ziani"
print(e.center(9)) #spaces
print(e.center(9, "#")) #spaces


# count()
f = "I love Python and JavaScript"
print(f.count("p"))
print(f.count("p", 2, 7))

# swapecase()

g = "I love Python"
h = "i lOVE pYTHon"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "Hello World"
print(i.startswith("a"))

# endswith()

i = "Hello World"
print(i.endswith("ld"))

j = "Hello World and I love JavaScript"
print(i.endswith("t", 7 , 31))


# index( Substring, Start , End )

# k = "I Love Python"
# print(k.index("v"))
# print(k.index("v", 0, 10))
# print(k.index("v",8,10))

# find( Substring, Start , End )

l = "I Love Python"
print(l.find("v"))
print(l.find("v", 0, 10))
print(l.find("v",8,10))

# rjust(Wisth, Fill Char)   # ljust(Wisth, Fill Char)

m = "I Love Python"
print(m.rjust(20,"v"))

m = "I Love Python"
print(m.ljust(20,"v"))


# Splitlines()
n = """ First Line
Second Line 
Third Line """

print(n.splitlines())


# Expandtabs()

o = "Hel1o\tWorld\tI\tLove\tPython"
print(o)
print(o.expandtabs(10))


# functions return Boolean values

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())


a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join(Iterable)

myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))






