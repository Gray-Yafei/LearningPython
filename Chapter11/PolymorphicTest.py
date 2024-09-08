class Animal(object):

    def speak(self):
        print('Animal is speaking')
class Dog(Animal):
    def speak(self):
        print('I am a dog.')
class Cat(Animal):
    def speak(self):
        print('I am a cat.')


def speak(animal):
    animal.speak()
kitty = Cat()
puppy = Dog()

speak(puppy)
speak(kitty)
