'''Movie Recommendation System:
1.Design a program that asks the user for their favorite movie genre (e.g., comedy, action, 
drama).
2.Based on the user's input, recommend a few movies from that genre 
using a list of predefined movie titles and genres.'''

comedy = ["3 Idiots","Pk","Johnny English"]
action = ["John Wick","300", "Troy"]
drama = ["Shutter Island","Shawshank Redemption","wanted" ]

user_input = input("Enter the Genre: Comedy, Action, drama :) ")
if user_input == "comedy":
    print(comedy)
elif user_input == "action":
    print(action)
elif user_input == "drama":
    print(drama)
else:
    print("Invalid Genre")