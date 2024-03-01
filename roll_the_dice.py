import random as ra
def roll():
    return ra.randint(1 ,6)
player =0
while True:
    player = input("enter the players")
    if player.isdigit():
        if 2 <= int(player) <= 4:
            break 
        else:
            print("it must be betwwen(2-4)")
    else:
        print("invalid number")
played =1
score = list()
score1 =0
while int(player) >= played:
    score1 =0
    while True:
        answer = input("Roll the dice  for the player number{0}".format(played)).lower()
        if answer == 'yes':
            res = roll()
            if res == 1:
                print("u lost all the scroce u gain and u lost the game")
                score1 =0
                score.append(score1)
                break
            else:
                score1 += res
                print("u were value was {0} and u r score {1}".format(res,score1))
                
        if answer == 'no':
            score.append(score1)
            break
    played+=1
max_value = max(score)
print(score)
if max == 0:
    print("on one win the game")
else:
    print(score.index(max_value)+1)
