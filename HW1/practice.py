directory = {'CHEWBACCA': ['Ron', 'LUKE', 'Yoda', 'Dave', 'Pam'], 'Ron': ['CHEWBACCA', 'BERU'],
 'LUKE': ['Yoda'], 'Dave': ['BERU'], 'BERU': ['CHEWBACCA'], 'Alice': [], 'Pam': [], 'Aaragon': [], 'Yoda': [ 'CHEWBACCA', 'BERU']}




class Dog:
    # constructor: called when you create a new Dog
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age      # instance variable

    # method: makes the dog bark
    def bark(self):
        print(f"{self.name} says woof!")

    # method: birthday
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}, you are now {self.age} years old!")

dog1 = Dog(Rex, 3)