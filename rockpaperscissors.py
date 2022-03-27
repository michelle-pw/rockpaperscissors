import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"

# complete the program here

def rps(player1,player2):

    if player1 == player2:
      print('it\'s a tie!')

    elif player1 == 'rock':
      if player2 == 'scissors':
        print("player1 won!")
      else:
          print("player2 won!")

    elif player1 == 'paper':
      if player2 == 'scissors':
        print("player2 won!")
      else:
          print("player1 won!")

    elif player1 == 'scissors':
      if player2 == 'paper':
        print("player1 won!")
      else:
          print("player2 won!")

player1 = choose_rps()
player2 = choose_rps()

play = True
while play:

  print(f"Player 1 chose {player1}")
  print(f"Player 2 chose {player2}")
  rps(player1,player2)
  print("\n------\n")
  play = random.choice([True,False])

print("Thank you for playing!")
