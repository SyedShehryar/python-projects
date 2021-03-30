import random

def play():
    user = input ( "what's your choice ? (r) for rock , (p) for paper , (s) for scissor :" )
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f"it is a tie , computer also chose {computer}"

    if is_win(user , computer):
        return f"You won , computer chose {computer}"

    return f"You lost , computer chose {computer}"

def is_win(player, opponent):
    
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True 

print(play())