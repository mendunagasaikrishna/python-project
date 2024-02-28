import random as ra
ll = ['ro','ss','pp']
user_win =0
computer_win =0
while True:
    i = ra.randint(0,2)
    value = input("enter ro/ss/pp or q ").lower()
    print(ll[i])
    if value == 'q':
        if user_win > 0 or computer_win > 0:
            print("user score : {0} computer score : {1}".format(user_win,computer_win)) 
        quit()
    else:
        if value == ll[i]:
            print("same")
        elif ll[i] == 'ro' and value == 'pp':
            print("you won !")
            user_win+=1
        elif ll[i] == 'ss' and value == 'ro':
            print("you won !")
            user_win+=1
        elif ll[i] == 'pp' and value == 'ss':
            print("you won !")
            user_win+=1
        else:
            print("computer won !")
            computer_win+=1
