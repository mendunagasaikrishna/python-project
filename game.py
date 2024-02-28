answer = input("do u want to play a game:").lower()
lla = ['goat','wolf','cabbage']
llb = list()
rules ={
    'wolf' : 'goat',
    'goat' : 'cabbage',
    'cabbage' : 'goat'
}
if answer == 'yes':
    print("A farmer wants to cross a river and take with him a wolf, a goat and a cabbage. He has a boat, but it can only fit himself plus either the wolf, the goat or the cabbage. If the wolf and the goat are alone on one shore, the wolf will eat the goat. If the goat and the cabbage are alone on the shore, the goat will eat the cabbage. How can the farmer bring the wolf, the goat and the cabbage across the river without anything being eaten?")
    while True:
        print("who are standing on A side")
        print(lla)
        print("who are standing on B side")
        print(llb)
        if int(input("how many want to go form A side to B side ")) == 2:
            if len(lla) == 1:
                print("there is only one")
                continue
            s1 = input("enter the who want to cross form Aside to B side:").lower()
            s2 = input("enter the who want to cross form Aside to B side:").lower()
            if len(llb) == 1:
                llb.append(s1)
                llb.append(s2)
                print("the final list at side b:")
                print(llb)
                print("u won the game:")
                break

            lla.remove(s1)
            lla.remove(s2)
            llb.append(s1)
            llb.append(s2)
            answer = input("do u want to take any one back (type yes are no):").lower()
            if answer == 'yes':
                re =input("enter whom want to take back:").lower()
                if len(llb) == 2 or len(llb) == 1:
                    llb.remove(re)
                    lla.append(re)

            else:
                if len(lla) == 1:
                    if rules[s1] == s2 or rules[s2] == s1 :
                        print("it is a worng step u lost the game:")
                        break
                if len(lla) == 0:
                    print("the final list at side b:")
                    print(llb)
                    print("u won the game")
                    break
                
        else:
            s1 = input("enter the who want to cross frist from a side to b side:")
            lla.remove(s1)
            if len(lla) == 2:
                if rules[lla[0]] == lla[1] or rules[lla[1]] == lla[0] :
                    print("it is a worng step u lost the game:")
                    break
            if len(llb) == 2:
                llb.append(s1)
                print("the final list at side b:")
                print(llb)
                print("u won the game")
                break
            if len(llb) == 1:
                answer = input("do u want to take any one back (type yes are no):").lower()
                if answer == 'yes':
                    re =input("enter whom want to take back").lower()
                    llb.remove(re)
                    lla.append(re)
                else:
                    if rules[llb[0]] == s1:
                        print("it is a worng step u lost the game:")
                        break
                    else:
                        llb.append(s1)
                        print("the final list at side b:")
                        print(llb)
                        print("u won the game")
                        break 
            if len(llb) == 0:
                llb.append(s1)
            
            
else:
    print("Ok Bye")
    quit()
