class Member:

  def __init__(self):

    print("A New Member Has Been Added")

member_one = Member()
member_two = Member()
member_three = Member()

print(member_one.__class__)

my_dictionary = {
  'name': "Osama",
  'age': 36,
  'monthly_salary': 5000,
  'yearly_salary': ''  # Something
}


class Member:
  def __init__(self, first_name, middle_name, last_name):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name

member_one = Member("Osama", "Mohamed", "Elsayed")
member_two = Member("Ahmed", "Ali", "Mahmoud")
member_three = Member("Mona", "Ali", "Mahmoud")

# print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)


class Member:
  def __init__(self, first_name, middle_name, last_name, gender):
    self.fname = first_name
    self.mname = middle_name
    self.lname = last_name
    self.gender = gender

  def full_name(self):
    return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):
    if self.gender == "Male":
      return f"Hello Mr {self.fname}"
    elif self.gender == "Female":
      return f"Hello Miss {self.fname}"
    else:
      return f"Hello {self.fname}"

  def get_all_info(self):
    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"


member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")

# print(dir(member_one))

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_two.fname)
# print(member_three.fname)

# print(member_two.full_name())
# print(member_two.name_with_title())

print(member_one.get_all_info())


class Member:

  not_allowed_names = ["Hell", "Shit", "Baloot"]

  users_num = 0

  def __init__(self, first_name, middle_name, last_name, gender):

    self.fname = first_name

    self.mname = middle_name

    self.lname = last_name

    self.gender = gender

    Member.users_num += 1  # Member.users_num = Member.users_num + 1

  def full_name(self):

    if self.fname in Member.not_allowed_names:

      raise ValueError("Name Not Allowed")

    else:

      return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):

    if self.gender == "Male":

      return f"Hello Mr {self.fname}"

    elif self.gender == "Female":

      return f"Hello Miss {self.fname}"

    else:

      return f"Hello {self.fname}"

  def get_all_info(self):

    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

  def delete_user(self):

    Member.users_num -= 1  # Member.users_num = Member.users_num -1

    return f"User {self.fname} Is Deleted."


print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

print(Member.users_num)

print(member_four.delete_user())

print(Member.users_num)

print(dir(member_one))

print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)

print(member_two.full_name())
print(member_two.name_with_title())

print(member_three.get_all_info())

print(dir(Member))


class Member:

  not_allowed_names = ["Hell", "Shit", "Baloot"]

  users_num = 0

  @classmethod
  def show_users_count(cls):

    print(f"We Have {cls.users_num} Users In Our System.")

  @staticmethod
  def say_hello():

    print("Hello From Static Method")

  def __init__(self, first_name, middle_name, last_name, gender):

    self.fname = first_name

    self.mname = middle_name

    self.lname = last_name

    self.gender = gender

    Member.users_num += 1  # Member.users_num = Member.users_num + 1

  def full_name(self):

    if self.fname in Member.not_allowed_names:

      raise ValueError("Name Not Allowed")

    else:

      return f"{self.fname} {self.mname} {self.lname}"

  def name_with_title(self):

    if self.gender == "Male":

      return f"Hello Mr {self.fname}"

    elif self.gender == "Female":

      return f"Hello Miss {self.fname}"

    else:

      return f"Hello {self.fname}"

  def get_all_info(self):

    return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"

  def delete_user(self):

    Member.users_num -= 1  # Member.users_num = Member.users_num -1

    return f"User {self.fname} Is Deleted."

print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Elsayed", "Male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "Male")
member_three = Member("Mona", "Ali", "Mahmoud", "Female")
member_four = Member("Shit", "Hell", "Metal", "DD")

print(Member.users_num)
print(member_four.delete_user())
print(Member.users_num)

print("#" * 50)

Member.show_users_count()

print("#" * 50)

print(member_one.full_name())
print(Member.full_name(member_one))

Member.say_hello()


class Skill:

  def __init__(self):

    self.skills = ["Html", "Css", "Js"]

  def __str__(self):

    return f"This is My Skills => {self.skills}"

  def __len__(self):

    return len(self.skills)

profile = Skill()
print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))

print(profile.__class__)
my_string = "Osama"
print(type(my_string))
print(my_string.__class__)
print(dir(str))
print(str.upper(my_string))


class Food:  # Base Class

  def __init__(self, name, price):

    self.name = name

    self.price = price

    print(f"{self.name} Is Created From Base Class")

  def eat(self):

    print("Eat Method From Base Class")

class Apple(Food):  # Derived Class

  def __init__(self, name, price, amount):

    # Food.__init__(self, name)  # Create Instance From Base Class

    super().__init__(name, price)

    self.amount = amount

    print(f"{self.name} Is Created From Derived Class And Price Is {self.price} And Amount Is {self.amount}")

  def get_from_tree(self):

      print("Get From Tree From Derived Class")

# food_one = Food("Pizza")
food_two = Apple("Pizza", 150, 500)
food_two.eat()
food_two.get_from_tree()



# ---------------------------------------------------------
# -- Object Oriented Programming => Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:

  def __init__(self):

    print("Base One")

  def func_one(self):

    print("One")

class BaseTwo:

  def __init__(self):

    print("Base Two")

  def func_two(self):

    print("Two")

class Derived(BaseOne, BaseTwo):

  pass

my_var = Derived()

# print(Derived.mro())

print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()

class Base:

  pass

class DerivedOne(Base):

  pass

class DerivedTwo(DerivedOne):

  pass


# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------

n1 = 10
n2 = 20

print(n1 + n2)

s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)

print(len([1, 2, 3, 4, 5, 6]))
print(len("Osama Elzero"))
print(len({"Key_One": 1, "Key_Two": 2}))

class A:

  def do_something(self):

    print("From Class A")

    raise NotImplementedError("Derived Class Must Implement This Method")

class B(A):

  def do_something(self):

    print("From Class B")

class C(A):

  def do_something(self):

    print("From Class C")

my_instance = B()
my_instance.do_something()


# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict Access To The Data Stored in Attirbutes and Methods
# Public
# - Every Attribute and Method That We Used So Far Is Public
# - Attributes and Methods Can Be Modified and Run From Everywhere
# - Inside Our Outside The Class
# Protected
# - Attributes and Methods Can Be Accessed From Within The Class And Sub Classes
# - Attributes and Methods Prefixed With One Underscore _
# Private
# - Attributes and Methods Can Be Accessed From Within The Class Or Object Only
# - Attributes Cannot Be Modified From Outside The Class
# - Attributes and Methods Prefixed With Two Underscores __
# ---------------------------------------------------------
# - Attributes = Variables = Properties
# -------------------------------------

class Member:

  def __init__(self, name):

    self.name = name  # Public

one = Member("Ahmed")
print(one.name)
one.name = "Sayed"
print(one.name)

class Member:

  def __init__(self, name):

    self._name = name  # Protected

one = Member("Ahmed")
print(one._name)
one._name = "Sayed"
print(one._name)

class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

one = Member("Ahmed")
# print(one.__name)
print(one.say_hello())
print(one._Member__name)



# ------------------------------------------------------
# -- Object Oriented Programming => Getters & Setters --
# ------------------------------------------------------

class Member:

  def __init__(self, name):

    self.__name = name  # Private

  def say_hello(self):

    return f"Hello {self.__name}"

  def get_name(self):  # Getter

    return self.__name

  def set_name(self, new_name):

    self.__name = new_name

one = Member("Ahmed")

one._Member__name = "Sayed"
print(one._Member__name)

print(one.get_name())
one.set_name('Abbas')
print(one.get_name())


# --------------------------------------------------------
# -- Object Oriented Programming => @Property Decorator --
# --------------------------------------------------------

class Member:

  def __init__(self, name, age):

    self.name = name

    self.age = age

  def say_hello(self):

    return f"Hello {self.name}"

  @property
  def age_in_days(self):

    return self.age * 365

one = Member("Ahmed", 40)

print(one.name)
print(one.age)
print(one.say_hello())
# print(one.age_in_days())

print(one.age_in_days)


# ----------------------------------------------------------------
# -- Object Oriented Programming => ABCs => Abstract Base Class --
# ----------------------------------------------------------------
# - Class Called Abstract Class If it Has One or More Abstract Methods
# - abc module in Python Provides Infrastructure for Defining Custom Abstract Base Classes.
# - By Adding @absttractmethod Decorator on The Methods
# - ABCMeta Class Is a Metaclass Used For Defining Abstract Base Class
# --------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):

  @abstractmethod
  def has_oop(self):

    pass

  @abstractmethod
  def has_name(self):

    pass

class Python(Programming):

  def has_oop(self):

    return "Yes"

class Pascal(Programming):

  def has_oop(self):

    return "No"

  def has_name(self):

    return "Pascal"

one = Pascal()

print(one.has_oop())
print(one.has_name())