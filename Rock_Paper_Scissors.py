import random
my_list = ['rock', 'paper', 'scissors', 'EXIT']
def Validation():
    user_choice = input('Rock Paper Scissors!\n')
    while user_choice not in my_list:
        print("Error! Input can only be 'rock' or 'paper' or 'scissors'")
        user_choice = input('Rock Paper Scissors!\n')
        
    return user_choice
        
        
    

def main():
    score = 0
    print('Welcome to the game: Rock Paper Scissors')
    print('In each round of the game you will enter your answer, rock, paper or scissors and if you win then you will gain a point.')
    print('You can also exit the game by entering EXIT')

    
    
    while True:
        computer_choice = random.choice(my_list[0:3])
        user_choice = Validation()
        if user_choice == 'EXIT':
            print(score)
            return score
        
        elif user_choice == computer_choice:
            print('DRAW')
            score += 1
            
        elif (user_choice == my_list[0]) and (computer_choice == my_list[2]):
            print('WIN')
            score += 2
            
        elif (user_choice == my_list[1]) and (computer_choice == my_list[0]):
            print('WIN')
            score += 2
        
        elif (user_choice == my_list[2]) and (computer_choice == my_list[1]):
            print('WIN')
            score += 2
            
        else:
            print('LOSE')
            

if __name__ == '__main__':
    main()