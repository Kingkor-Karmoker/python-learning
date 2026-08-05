# Code for problem 9.1:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name}")
        print(f"Restaurant's cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

restaurant1 = Restaurant('Abesh', 'Bangla Khabar')

print(f"Restaurant name: {restaurant1.restaurant_name}")
print(f"Cuisine type: {restaurant1.cuisine_type}")
print()
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
