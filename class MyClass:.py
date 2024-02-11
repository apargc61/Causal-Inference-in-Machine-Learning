class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the __init__ method of the parent class
        self.breed = breed

    def make_sound(self):
        # Calling the make_sound method of the parent class
        parent_sound = super().make_sound()
        return f"{self.name} barks: Woof! {parent_sound}"

    def fetch(self):
        return f"{self.name} is fetching the ball."

# Creating an instance of the Dog class
my_dog = Dog(name="Buddy", breed="Labrador")

# Accessing methods of the Dog class
print(my_dog.make_sound())  # Calls the overridden method in Dog class
print(my_dog.fetch())       # Calls the method specific to Dog class


raise ValueError






class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def from_class_method(cls, value):
        # The class method can access and modify class-level variables
        cls.class_variable = value
        print(cls.OBJECT_NAME)
        return cls(value)

# Creating an instance using the class method
obj = MyClass.from_class_method("New Value")

# Accessing instance and class variables
print(obj.instance_variable)  # Output: New Value
print(obj.class_variable)      # Output: New Value
