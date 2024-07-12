import random
from game_data import data
from art import logo
from art import vs



a = data[random.randint(0,len(data)-1)]
score = 0
def game():
    global a
    global score
    b = data[random.randint(0,len(data)-1)]
    while a == b:
        b = data[random.randint(0,len(data)-1)]

    print(logo)    
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    if a["follower_count"] > b["follower_count"]:
        answer = "A"
    elif a["follower_count"] < b["follower_count"]:
        answer = "B"

    if answer == guess:
        score= score +1
        a=b
        print(f"You're right! Current score: {score}")
        game()
    else:
        print(f"Sorry, that's wrong. Final score: {score}") 
        return   


game()