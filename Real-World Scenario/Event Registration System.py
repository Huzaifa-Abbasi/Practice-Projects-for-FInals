'''Design a program to manage registrations for an event. It should 
allow users to register by providing their name, email, and any additional required information. 
The program should track the number of registered participants, allow organizers to view 
registrations, and send confirmation emails to attendees.'''

number = 0
data = {"details":[]}

def register():
    name = input("Enter the Name: ")
    email = input("entre the email: ")
    print(f"Conformation Email sent to {name}")
    data["details"].append({"name":name,"email":email})
    

while True:
    user_input = input("Enter the Do you want to add or quit: ")
    if user_input == "add":
        number += 1
        register()
    elif user_input == "quit":
        break

print(f"attendees are {data} and the total attendees are {number}")