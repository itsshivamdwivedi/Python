# import random
# win_matrix = []
# choice_list = ["Snake" , "Water" , "Gun"]
# win_matrix = [['D' , 'W' , 'L'],['L' , 'D' , 'W'],['W' , 'L' , 'D']]
# dict_points = {'S' : 0 , 'W' :1 , 'G':2 }

# player_1 = input("Player1 Select your option from (Snake,Water,Gun)?")

# player_2 = random.choice(choice_list)
# print(f"System selected ::  {player_2} ")
# print("Player1  you : " , win_matrix[dict_points[player_1[0]]][dict_points[player_2[0]]])
import random
def check(computer,user):
    if (computer==user):
        return 0
    if(computer==0 and user==1):
        return -1
    if(computer==1 and user==2):
        return -1
    if(computer==2 and user==0):
        return -1
    
    return 1
computer = random.randint(0, 2)
user = int(input("Enter 0 for snake , 1 for water and 2 for Gun"))
score = check(computer,user)
print("you:",user)
print("comp",computer)
if (score==0):
    print("It's a draw")
elif(score==-1):
    print("You lose ")
else:
    print("you won")

