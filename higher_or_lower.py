from random import randrange

def get_random_number():
     rand_number = input("Give me a number between 1 and 10: ")
     return int(rand_number)

def get_random_number2():
     rand_number2 = randrange(1, 11)
     return rand_number2

def do_randos_match(rnum1, rnum2):
     if (rnum1 == rnum2):
          guess = "That is correct"
     elif (rnum1 < rnum2):
          guess = "Your guess was too low"
     else:
          guess = "Your guess was too high"
     return guess


player_number = get_random_number()
game_number = get_random_number2()
result = do_randos_match(player_number, game_number)

print(f"Random number generated: {game_number}")
print(f"Your guess was: {player_number}")
print(result)
