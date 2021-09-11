# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Convert the values from string to float
height = float(height)
weight = float(weight)

#Use BMI formula 
BMI = weight/(height ** 2)

#Convert Float of BMI into Integer
print(int(BMI))

