def move_right():
    turn_left()
    turn_left()
    turn_left()
    
def Jump():
    turn_left()
    while wall_on_right() == True:
        move()
    move_right()
    move()
    move_right()
    while wall_in_front() != True:
        move()
    turn_left()
    
while at_goal() != True:
    if wall_in_front() == True:
        Jump()
    else:
        move()
    
