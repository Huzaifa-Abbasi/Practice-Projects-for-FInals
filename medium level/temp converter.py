'''Develop a program that allows the user to convert temperatures between Celsius and 
Fahrenheit.
 Provide options for the user to choose the conversion direction (Celsius to Fahrenheit or 
vice versa) and enter the temperature value.'''

def celsius():
    temp_in_f=int(input("enter the temp in fahrenheit: "))
    cel = (temp_in_f - 32) * (5/9)
    return cel

def fahrenheit():
    temp_in_c = int(input("Enter the temp in c: "))
    fah = (temp_in_c * 9/5) + 32
    return fah

while True:
    user_input = input("Enter the Yor cmd: ")

    if user_input == "c":
        celsius()
    elif user_input == "f":
        fahrenheit()
    elif user_input == "q":
        break
    else: print("Invalid option")