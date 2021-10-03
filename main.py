import random

rock = ''' 
                       888      
                       888      
                       888      
888d888 .d88b.  .d8888b888  888 
888P"  d88""88bd88P"   888 .88P 
888    888  888888     888888K  
888    Y88..88PY88b.   888 "88b 
888     "Y88P"  "Y8888P888  888 
'''
paper = '''
88888b.  8888b. 88888b.  .d88b. 888d888 
888 "88b    "88b888 "88bd8P  Y8b888P"   
888  888.d888888888  88888888888888     
888 d88P888  888888 d88PY8b.    888     
88888P" "Y88888888888P"  "Y8888 888     
888             888                     
888             888                     
888             888               
'''
scissors = '''
                d8b                                        
                Y8P                                        
                                                           
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
'''

game_images = [rock,paper,scissors]
your_choice = int(input("What you want type 0 - for rock, 1 - paper, 2 - scissors\n"))
if your_choice > 2:
    print("Invalid Operator")
else:
    print(game_images[your_choice])
computer_choice = random.randint(0,2)
print("Computer choice is")
print(game_images[computer_choice])


if your_choice == 0 and computer_choice == 1:
    print("You lost")
elif your_choice == 1 and computer_choice == 2:
    print("You lost")
elif your_choice == 2 and computer_choice == 0:
    print("You lost")
elif your_choice == 1 and computer_choice == 0:
    print("You WIN !!!")
elif your_choice == 2 and computer_choice == 1:
    print("You WIN !!!")
elif your_choice == 0 and computer_choice == 2:
    print("You WIN !!!")
elif your_choice == 1 and computer_choice == 1:
    print("It's Toe")
elif your_choice == 2 and computer_choice == 2:
    print("It's Toe")
elif your_choice == 0 and computer_choice == 0:
    print("It's Toe")