user_info = {}

user_name = input("What is the user's name?   ")
print(user_name)
user_info['name'] = user_name

user_age = int(input("What is the user's age?   "))
print(user_age)
user_info['age'] = user_age

user_country_of_birth = input("What is the user's country of birth?   ")
print(user_country_of_birth)
user_info['country'] = user_country_of_birth

user_known_for = input("What is the user known for?   ")
print(user_known_for)
user_info['known'] = user_known_for

print(user_info)