# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight/(height ** 2))

if BMI < 18.5:
  string = "are underweight."
elif BMI < 25:
  string = "have a normal weight."
elif BMI < 30:
  string = "are slightly overweight."
elif BMI < 35:
  string = "are obese."
else:
  string = "are clinically obese."

print(f"Your BMI is {BMI}, you {string}")