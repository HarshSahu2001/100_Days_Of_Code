def move_right():
    turn_left()
    turn_left()
    turn_left()
    
def Jump():
    move()
    turn_left()
    move()
    move_right()
    move()
    move_right()
    move()
    turn_left()
    
for i in range (0,6):
    Jump()
    