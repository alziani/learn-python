# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("#" * 50)

# Using In and Not In With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Italy"

if myCountry in countriesOne:

  print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

elif myCountry in countriesTwo:

  print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")

else:

  print("You Have No Discount")

  # ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login
name = input("Please Type Your Name ").strip().capitalize()

# If Name is In Admin
if name in admins:

  print(f"Hello {name} Welcome Back")

  option = input("Delete Or Update Your Name ?").strip().capitalize()

  # Update Option
  if option == 'Update' or option == 'U':

    theNewName = input("Your New Name Please ").strip().capitalize()

    admins[admins.index(name)] = theNewName

    print("Name Updated.")

    print(admins)

  # Delete Option
  elif option == 'Delete' or option == 'D':

    admins.remove(name)

    print("Name Deleted")

    print(admins)

  # Wrong Option
  else:

    print("Wrong Option Choosed")

else:

  status = input("Not Admin, Add You Y, N ? ").strip().capitalize()

  if status == "Yes" or status == "Y":

    print("You Have Been Added")

    admins.append(name)

    print(admins)

  else:

    print("You Are Not Added.")