'''Design a program that calculates the user's Body Mass Index (BMI) based on their weight 
and height.
Prompt the user to enter their weight (in kilograms) and height (in meters).
Calculate the BMI using the formula: BMI = weight / (height * height).
Display the calculated BMI and interpret it based on the standard BMI categories 
(underweight, normal weight, overweight, obese)'''

body_weight = float(input("Enter the Weight of Body: "))
body_height = float(input("Enter the height of body: "))
bmi = body_weight // ( body_height * body_height)

def calculate_bmi():

    if bmi <= 18.5:
        return  "The Body is underweight "
    elif bmi >=  18.5 and bmi <= 24.9:
        return "The body is normal  "
    elif bmi >=  25 and bmi <= 29.9:
        return "The body is normal  "
    elif bmi >= 30:
        return "The body is normal  "

print(f"the weight is {body_weight} the height is {body_weight} the BMI is {bmi} {calculate_bmi()}")