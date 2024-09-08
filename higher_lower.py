logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import random
from replit import clear
import game_data

def format_data(account):
    """Format the account data into printable format"""
    acc_name=account["name"]
    acc_desc=account["description"]
    acc_country=account["country"]
    return f"{acc_name}, a {acc_desc}, from {acc_country}"
    
def check_answer(guess,a_followers,b_followers):
    """Use if statement to check if user is correct"""
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"
        
print(logo)
score=0
acc2=random.choice(game_data.data)
game_should_continue=True

while game_should_continue:
    
    acc1=acc2
    acc2=random.choice(game_data.data)
    
    while acc1==acc2:
        acc2=random.choice(game_data.data)
    if acc1==acc2:
        acc2=random.choice(game_data.data)
    print(f"Compare A: {format_data(acc1)} ")
    print(vs)
    print(f"Against B: {format_data(acc2)} ")
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count=acc1["follower_count"]
    b_follower_count=acc2["follower_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    clear()
    print(logo)
    if is_correct:
        score+=1
        print(f"You're right. Current score={score}")
    else:
        game_should_continue=False
        print(f"Sorry! that's wrong. Final score={score}")
    

    
    


