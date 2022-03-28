lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(lst)




def check_1(num_of_elements1,lst):
    for i in range(len(lst)):
        if lst[i] == '-':
            num_of_elements1 += 1
        else:
            True
        if num_of_elements1 == int(len(lst)):
            print("Winner is player number 1\nCONGRATULATIONS")
            exit()
        else:
            True
def check_2(num_of_elements2, lst):
    for i in range(len(lst)):
        if lst[i] == '-':
            num_of_elements2 += 1
        else:
            True
        if num_of_elements2 == int(len(lst)):
            print("Winner is player number 2\nCONGRATULATIONS")
            exit()
        else:
            True

def choice(lst):
    print("Hello, Welcome to kyles game ")
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num_of_elements1 = 0
    num_of_elements2 = 0
    while True:

        num_choices1 = int(input("Player1: one num or two ? "))
        if num_choices1 != 2 and num_choices1 != 1:
            print("invalid num")
            continue


        if num_choices1 == 1:
           p1_turn = int(input("Enter num to remove: "))
           lst.remove(p1_turn)
           lst.insert(p1_turn-1, "-")
           print(lst)

        elif num_choices1 == 2:
            p1_turn1 = int(input("Player1: Enter 1st number to remove: "))
            p1_turn2 = int(input("Player1: Enter 2nd number to remove: "))
            if p1_turn2 == p1_turn1 + 1:
                lst.remove(p1_turn1)
                lst.remove(p1_turn2)
                lst.insert(p1_turn1-1, '-')
                lst.insert(p1_turn2-1, '-')
                print(lst)
            else:
                print("Enter two adjacent nums")
                continue

        check_1(num_of_elements1, lst)

        num_choices2 = int(input("Player2: One num or Two ? "))
        if num_choices2 != 2 and num_choices2 != 1:
            print("invalid num")
            continue

        if num_choices2 == 1:
            p2_turn = int(input("Enter num to remove: "))
            lst.remove(p2_turn)
            lst.insert(p2_turn-1, '-')
            print(lst)

        elif num_choices2 == 2:
            p2_turn1 = int(input("Enter 1st number to remove: "))
            p2_turn2 = int(input("Enter 2nd number to remove: "))
            if p2_turn2 == p2_turn1 + 1:
                lst.remove(p2_turn1)
                lst.remove(p2_turn2)
                lst.insert(p2_turn1-1, '-')
                lst.insert(p2_turn2-1, '-')
                print(lst)
            else:
                print("choose two adjacent numbers")
                continue

        check_2(num_of_elements2, lst)

choice(lst)

