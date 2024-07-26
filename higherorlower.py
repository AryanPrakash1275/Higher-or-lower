from art import logo, vs
from game_data import data
import random
import os

print(logo)

score = 0
second_option = random.choice(data)
should_continue = True

def clear_console():
  if os.name == 'nt':
      os.system('cls')
  else:
      os.system('clear')

while should_continue:
  def format(option):
    option_name = option["name"]
    option_description = option["description"]
    option_country  = option["country"]
    return f"{option_name} is a {option_description} and originates from {option_country}."
  
  def ans_check(user_answer, first_follower_count, second_follower_count):
    if first_follower_count>second_follower_count:
      return user_answer == 'a'
    else:
      return user_answer == 'b'
  
  first_option = second_option
  second_option = random.choice(data)
  if first_option == second_option:
       second_option = random.choice(data)
  
  print(f"\n Compare A: {format(first_option)}")
  print(vs)
  print(f" with B: {format(second_option)}")
  
  user_answer = input("\nType 'A' or 'B' which you think has a higher follower count.").lower()
  
  first_follower_count = first_option["follower_count"]
  second_follower_count = second_option["follower_count"]
  
  correct = ans_check(user_answer, first_follower_count, second_follower_count)
  clear_console()
  print(logo)
  if correct:
    score += 1
    print(f"You are right! You are at {score}.")
  else:
    should_continue = False
    print(f"Wrong! Final score: {score}.")