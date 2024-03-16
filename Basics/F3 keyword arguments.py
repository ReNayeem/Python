def my_function2(firstName="Md.", lastName="Nayeem", age=23):
    print("This is my function!!")
    print("My name is", firstName, lastName, "and my age is", age)

# This is my function!!
# My name is None None and my age is 22
my_function2(None, None, 22)

# This is my function!!
# My name is Nayeam Ahmed and my age is 22
my_function2(age=22, lastName="Ahmed", firstName="Nayeam")