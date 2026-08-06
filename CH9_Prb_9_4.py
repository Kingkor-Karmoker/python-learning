# code for problem 9.4:
# code of 9.1:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 #new

    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name}")
        print(f"Restaurant's cuisine type is {self.cuisine_type}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

restaurant = Restaurant("Le meridian", "Buffet")
print(f"Restaurant has served {restaurant.number_served} people")
print()
restaurant.number_served = 5
print(f"Restaurant has served {restaurant.number_served} people")
print()

restaurant.set_number_served(99)
print(f"Restaurant has served {restaurant.number_served} people")
print()

restaurant.increment_number_served(11)
print(f"Restaurant has served {restaurant.number_served} people")
