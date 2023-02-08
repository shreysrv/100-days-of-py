def turn_right():
    turn_left()
    turn_left()
    turn_left()


def climb_up():
    turn_left()
    move()
    turn_right()


while not at_goal():
    height = 0
    while wall_in_front():
        height += 1
        climb_up()
    move()
    if height > 0:
        turn_right()
        while height > 0:
            height -= 1
            move()
        turn_left()
