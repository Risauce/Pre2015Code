

def legal_play(first_value, first_color, second_value, second_color):
    if (first_value == second_value):
        print("Legal Play!")
        return True
    elif(first_color == second_color):
        print("Legal Play!")
        return True
    else:
        print("Doesn't Work!")
        return False
        

legal_play("5", "Red", "5", "Blue")
legal_play("5", "Red", "2", "Red")
legal_play("3", "Yellow", "4", "Blue")
