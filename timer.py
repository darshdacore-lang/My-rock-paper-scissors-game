from random import Random, random

def get_timer():
    return random.randint(1, 10)
"i uh"
import time

start_time = time.time()

import select
import sys

def get_timed_choice(timeout=5):
    print(f"You have {timeout} seconds to make a choice.")
    print("Enter your choice (rock, paper, scissors): ", end='', flush=True)
    
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        choice = sys.stdin.readline().strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return None
    else:
        print("\nTime's up! No choice made.")
        return None


