import random 
item_list=["rock","paper","scissor"]

user_choice = input("enter your move (Rock,Paper,Scissor)")
computer_choice = random.choice(item_list)

print(f"User choice ={user_choice}")
print (f"Computer choice ={computer_choice}")

if user_choice==computer_choice :
    print(" MATCH TIE ")

elif user_choice=="rock" :
    if computer_choice=="paper":
        print(" COMPUTER WINS ....!")
    else:
        print("USER WINS.....!")

elif user_choice == "paper":
    if computer_choice=="scissor":
        print("computer wins......!")
    else:
        print("user wins.......!")

elif user_choice == "scissor":
    if computer_choice=="paper":
        print("user wins......!")
    else:
        print("computer wins.......!")
else:
    print(" invalid input ")

    
