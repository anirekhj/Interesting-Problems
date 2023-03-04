import random

i = 0
prize_history = []

choice = input('Do you wanna switch doors [y|n]?\n')

while i < 10000:
    # prizes
    my_list = ['goat','goat','car']
    # put prizes behind doors
    random.shuffle(my_list)
    # contestant picks a door without opening
    contestant_original_choice = random.randint(0, 2)
    contestant_original_prize = my_list[contestant_original_choice]
    del my_list[contestant_original_choice]
    # host opens opens a door that wasn't the contestant_choice but has a goat behind it
    host_reveal = my_list.index('goat')
    del my_list[host_reveal]
    # contestant switches their choice
    contestant_new_prize = my_list[0]
    
    # theory testing
    if(choice=="y"):
        prize_history.append(contestant_new_prize)
    else:
        prize_history.append(contestant_original_prize)
    i+=1

if(choice=="y"):
    print("Contestant switches door")
else:
    print("Contestant DOES NOT switch door")

print("Ws: ",prize_history.count('car'))
print("Ls: ",prize_history.count('goat'))
print("Win Probability: ", prize_history.count('car')*100/len(prize_history), "%")
