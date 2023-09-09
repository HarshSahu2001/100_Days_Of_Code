def move_right():
    turn_left()
    turn_left()
    turn_left()
    
def Jump():
    turn_left()
    move()
    move_right()
    move()
    move_right()
    move()
    turn_left()
    
while at_goal() != True:
    if wall_in_front() == True:
        Jump()
    else:
        move()