# 8-14. Cars

# Function that builds a dictionary about a car
def make_car(manufacturer, model, **car_info):
    
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    
    return car_info


# Call the function
car = make_car("subaru", "outback", color="blue", tow_package=True)

# Print the dictionary
print(car)
{'color': 'blue', 'tow_package': True, 'manufacturer': 'subaru', 'model': 'outback'}
