# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# x,y and z represent days, weeks and months left.

x = (90 - int(age)) * 365
y = (90 - int(age)) * 52
z = (90 - int(age)) * 12

print("You have {} days, {} weeks, and {} months left.".format(x,y,z))
# Another way of doing it
print(f"You have {x} days, {y} weeks, and {z} months left.")