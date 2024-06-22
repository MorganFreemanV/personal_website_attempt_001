class Dog():

    species = 'mammal'

    def __init__(self):
        pass

class Circle():
    pi = 3.14
    def __init__(self, radius=5):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def set_radius(self, new_r):
        self.radius = new_r

""" x = Circle()
x.set_radius(100)
print(x.area()) """

# INHERITANCE

class animal():
    def __init__(self) -> None:
        print('animal created')
    def whoami(self):
        print('animal')
    def eat(self):
        print('eating')

class cat(animal):
    def __init__(self) -> None:
        print('cat created')
    def meow(self):
        print('meow')
    # overriding class animal's eat method
    def eat(self):
        print('cat eating')
# class cat inherits properties from class animal and can call on the methods in class animal
""" x = cat()
x.whoami()
x.eat()
x.meow() """

# SPECIAL METHODS

class book():

    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return 'Title: {}, Author: {}, Pages: {}'.format(self.title, self.author,self.pages)

    def __len__(self):
        return len(self.title)
    
    def __del__(self):
        print('book destroyed')

b = book('Python','jose',200)
print(b)
print(len(b))
del b