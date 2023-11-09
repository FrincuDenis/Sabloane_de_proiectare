class Dependency:
    def do_something(self):
        print("Doing something")

class MyClass:
    def __init__(self, dependency):
        self.dependency = dependency

    def some_method(self):
        self.dependency.do_something()

# Dependency Injection Container
class Container:
    def __init__(self):
        self.dependency = Dependency()

    def get_my_class(self):
        return MyClass(self.dependency)

# Usage
container = Container()
my_class = container.get_my_class()
my_class.some_method()
