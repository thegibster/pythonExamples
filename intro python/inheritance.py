class Parent():
    def __init__(self,last_name,eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        print("child constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

newKid = Child("bobbyburg","brown",12)
print(newKid.last_name)
