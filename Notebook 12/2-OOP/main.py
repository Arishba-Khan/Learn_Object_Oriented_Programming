class Car:      #This is a class definition for a Car.
    def __init__(self, model, color):       # constructor
        #This is the constructor method that initializes the attributes of the class.
        self.model = model          # attribute
        self.color = color          # attribute
        #This method initializes the attributes of the class with the values passed as arguments.
    def full_desc(self):                # method / function
       #This method returns the full description of the car.
        return f"{self.model} {self.color}"

my_car =Car("Rolce Royce", "Black")  # object
#This creates an instance of the Car class with the model "Rolce Royce" and color "Black".
print(my_car.full_desc())       # This prints the full description of the car.

# Accessing attributes
print(my_car.model)
print(my_car.color)


