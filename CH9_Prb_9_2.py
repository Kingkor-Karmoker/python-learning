# code for problem 9.2:
# code from 9.1:
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant's name is {self.restaurant_name}")
        print(f"Restaurant's cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

# code starts here for 9.2:
restaurant1 = Restaurant('Kacchi Darbar', 'Biryani')
restaurant2 = Restaurant('KFC', 'Fried Chicken')
restaurant3 = Restaurant('Star point', 'Buffet')

restaurant1.describe_restaurant()
print()
restaurant2.describe_restaurant()
print()
restaurant3.describe_restaurant()
print()
