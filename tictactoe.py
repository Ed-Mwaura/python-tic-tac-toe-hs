print("Enter cells: ")

inp = list(input())
sub_list1 = inp[0:3]
sub_list2 = inp[3:6]
sub_list3 = inp[6:9]

print("---------")

print("| " + sub_list1[0] + " " + sub_list1[1] + " " + sub_list1[2] + " |")
print("| " + sub_list2[0] + " " + sub_list2[1] + " " + sub_list2[2] + " |")
print("| " + sub_list3[0] + " " + sub_list3[1] + " " + sub_list3[2] + " |")

print("---------")

possible_win_states = [
    # vertical
    sub_list1[0] == sub_list2[0] == sub_list3[0],  # placement == 0
    sub_list1[1] == sub_list2[1] == sub_list3[1],  # placement == 1
    sub_list1[2] == sub_list2[2] == sub_list3[2],  # placement == 2

    # horizontal
    sub_list1[0] == sub_list1[1] == sub_list1[2],  # placement == 3
    sub_list2[0] == sub_list2[1] == sub_list2[2],  # placement == 4
    sub_list3[0] == sub_list3[1] == sub_list3[2],  # placement == 5

    # diagonal
    sub_list1[0] == sub_list2[1] == sub_list3[2],  # placement == 6
    sub_list1[2] == sub_list2[1] == sub_list3[0]  # placement == 7
]

xes = inp.count('X')
oes = inp.count('O')

if abs(xes - oes) > 1:
    print("Impossible")
else:
    count = 0
    for i in range(len(possible_win_states)):
        if possible_win_states[i]:
            count += 1

    if count > 1:
        print("Impossible")
    elif count == 0:
        if "_" in inp:
            print("Game not finished")
        else:
            print("Draw")
    elif count == 1:
        for i in range(len(possible_win_states)):
            if possible_win_states[i] is True:
                placement = i
                print()
                if placement == 0:
                    print(sub_list1[0] + ' wins')
                if placement == 1:
                    print(sub_list1[1] + ' wins')
                if placement == 2:
                    print(sub_list1[2] + ' wins')
                if placement == 3:
                    print(sub_list1[0] + ' wins')
                if placement == 4:
                    print(sub_list2[0] + ' wins')
                if placement == 5:
                    print(sub_list3[0] + ' wins')
                if placement == 6:
                    print(sub_list1[0] + ' wins')
                if placement == 7:
                    print(sub_list1[2] + ' wins')

