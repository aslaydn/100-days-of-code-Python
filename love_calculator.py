print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

new_name1 = name1.lower()
new_name2 = name2.lower()

total_true = new_name1.count("t") + new_name2.count("t") + new_name1.count("r") + new_name2.count("r") + new_name1.count("u") + new_name2.count("u") + new_name1.count("e") +new_name2.count("e")

total_love = new_name1.count("l") + new_name2.count("l") + new_name1.count("o") + new_name2.count("o") + new_name1.count("v") + new_name2.count("v") + new_name1.count("e") +new_name2.count("e")

totalLove = str(total_love)
totalTrue = str(total_true)
score = (totalTrue) + (totalLove)
loveScore=int(score)

if loveScore<10 or 90<loveScore:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif 40<loveScore<50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")        