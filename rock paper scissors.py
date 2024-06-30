


import random
computer_score = 0
your_score = 0
options = ["Rock", "Paper", "Scissors"]
play_again ='y'
while play_again == 'y':
   user_choice = input("Choose Rock, Paper, or Scissors: ")
   computer_choice = random.choice(options)
   print("You chose: ", user_choice)
   print("Computer chose: ", computer_choice)
   
   if user_choice == computer_choice:
      print("It's a tie")
   elif user_choice == "Rock" and computer_choice == "Scissors":
      print("You win!")
      print("your_score = 1")
      print("computer_score = 0")
   elif user_choice == "Paper" and computer_choice == "Rock":
      print("You win!")
      print("your_score = 1")
      print("computer-score = 0")
   elif user_choice == "Scissors" and computer_choice == "Paper":
      print("You win!")
      print("your_score = 1")
      print("computer_score = 0")
   else:
      print("Computer wins!")
      print("your_score = 0")
      print("computer_score = 1")

   play_again =input("Do you want to play again?(y/n): ")
   
print("THANKS FOR PLAYING")
    
