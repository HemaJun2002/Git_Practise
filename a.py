class MyClass:
    def __init__(self):
        self.__private_var = "I am Private"

    def show_private(self):
        return self.__private_var

obj = MyClass()
# Accessing private variable using name mangling
print(obj._MyClass__private_var)  # ✓ Access using name mangling