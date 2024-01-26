laptop = { "brand": "dell", "model": "alienware", "year": 2010 }

# Print the brand value of the dictionary 
print(laptop["brand"])

# Add new information (key: value)by using a boolean data type as value and home as key: 
#This laptop is at home now, so "home": True
laptop["home"] = True
print(laptop)

# Modify the value of the key year to 2019
laptop["year"] = 2019
print(laptop)