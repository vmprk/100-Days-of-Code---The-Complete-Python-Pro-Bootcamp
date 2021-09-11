#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


#Code starts from here

print("Welcome to the tip calculator.")

#Declare bill to get user input
bill = float(input("What was the total bill? $"))

#Caluclate tip %
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
tip = bill * (tip_percentage/100)

#Get information about bill slipt. 
group = int(input("How many people to split the bill? "))

# final bill caluclation
total = (bill + tip)/group
print(f"Each person should pay: {'%.2f' % total}")


# #If the bill was $150.00, split between 5 people, with 12% tip. 
# #Each person should pay (150.00 / 5) * 1.12 = 33.6
# #Round the result to 2 decimal places.
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)

# #FAQ: How to round to 2 decimal places?
# #https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048

# print(f"Each person should pay: ${final_amount}")