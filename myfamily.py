myfamily = ("mother", "father", "sister", "brother", "sister") 

print(myfamily)

# Checking the type of object myfamily
print(type(myfamily))     

# Accessing tuple items sister by using index numbers 
print(myfamily[2])
print(myfamily[4])

# Checking whether we can add an item me by using the append() method
myfamily.append("me")
print(myfamily)

# Checking whether we can remove the item brother by using the pop() method.   
myfamily.pop("brother")
print(myfamily)