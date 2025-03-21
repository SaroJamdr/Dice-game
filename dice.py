import random

def roll_dice():
    return random.randint(1, 6)
def main():
    score1 = 0
    score2 = 0
    player_turn = 0

    while(score1 < 50 or score2 < 50):
        turn_score =0
        six_count = 0
        print(f"\n Player {player_turn+1}'s turn")

        while True:
            roll = roll_dice()
            print(f"Player {player_turn+1} rolled: {roll}")
            if roll == 6:
                six_count += 1
                if(six_count == 3):
                    print(f"Player {player_turn+1} got three 6s in a row!")
                    turn_score =0
                    break
                else:
                    print("Rolled a 6, roll again!")
                    turn_score +=roll
                    continue
            else:
                turn_score += roll
                six_count = 0
            break
        if(player_turn == 0):
            score1 += turn_score
            print(f"player1's score: {score1}")
        else:
            score2 += turn_score
            print(f"player2's score: {score2}")

        player_turn = 1- player_turn

    if(score1>=50):
        print("Player1 wins")
    else:
        print("Player2 wins")

main()