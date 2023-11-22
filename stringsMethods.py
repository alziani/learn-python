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


name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString)


name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: {}".format("Osama"))
print("My Name is: {}".format(name))
print("My Name is: {} My Age: {}".format(name, age))
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# Format in Version 3.6+

myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")


print (5**2)
print (10//3)
print (10/3)







