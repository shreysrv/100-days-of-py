print('''
                         _____
                     _-~~     ~~-_//
                   /~             ~\
                  |              _  |_
                 |         _--~~~ )~~ )___
                \|        /   ___   _-~   ~-_
                \          _-~   ~-_         \
                |         /         \         |
                |        |           |     (O  |
                 |      |             |        |
                 |      |   O)        |       |
                 /|      |           |       /
                 / \ _--_ \         /-_   _-~)
                   /~    \ ~-_   _-~   ~~~__/
                  |   |\  ~-_ ~~~ _-~~---~  \
                  |   | |    ~--~~  / \      ~-_
                   |   \ |                      ~-_
                    \   ~-|                        ~~--__ _-~~-,
                     ~-_   |                             /     |
                        ~~--|                                 /
                          |  |                               /
                          |   |              _            _-~
                          |  /~~--_   __---~~          _-~
                          |  \                   __--~~
                          |  |~~--__     ___---~~
                          |  |      ~~~~~
                          |  |

1''')
print("Welcome to treasure Island with ducks")
print("Your mission is to save the ducks")
crossroad = input("You\'re at a cross road, do you want to go left or right?")
if crossroad.lower() == "left":
    river = input("You are at the river. Do you want to wait for boat or swim?")
    if river.lower() == "wait":
        print("Congrats you have reached the Island")
        door = input("We have three doors - red, blue and yellow, which one you want to choose?")
        if door.lower() == "yellow":
            print("Congrats!!! you found the ducks")
        elif door.lower() == "red":
            print("Burned by fire, GAME OVER")
        elif door.lower() == "blue":
            print("Eaten by Beast!! GAME OVER")
        else:
            print("GAME OVER!!")
    elif river.lower() == "swim":
        print("Eaten by trouts, GAME OVER")
    else:
        print("GAME OVER!!")
else:
    print("you fell into pit, GAME OVER")
