import random
import numpy as np

#Create the deck and starting hands
def Start():
    deck = list(range(2, 15)) * 4  # 2–14, with 11=J, 12=Q, 13=K, 14=A
    random.shuffle(deck)
    p1 = deck[:26]
    p2 = deck[26:]
    p1count = [26]
    pile1, pile2 = [], []
    return p1, p2, p1count, pile1, pile2


#Handle when a player wins a round
def WinRound(pwin, pilewin, pilelose):
    pwin.extend(pilewin)
    pwin.extend(pilelose)
    pilewin.clear()
    pilelose.clear()


#Handle a tie situation
def Tie(p1, p2, p1count, pile1, pile2):
    if len(p2) > 1:
        N = min(3, len(p2) - 1)
        for i in range(N):
            pile2.append(p2.pop(0))
    if len(p1) > 1:
        N = min(3, len(p1) - 1)
        for i in range(N):
            pile1.append(p1.pop(0))


#Play one round
def Play1(p1, p2, p1count, pile1, pile2):
    pile1.append(p1.pop(0))
    pile2.append(p2.pop(0))

    if pile1[-1] == pile2[-1]:
        if len(p1) == 0:
            WinRound(p2, pile2, pile1)
        if len(p2) == 0:
            WinRound(p1, pile1, pile2)
        Tie(p1, p2, p1count, pile1, pile2)

    elif pile1[-1] > pile2[-1]:
        WinRound(p1, pile1, pile2)

    elif pile1[-1] < pile2[-1]:
        WinRound(p2, pile2, pile1)

    p1count.append(len(p1))

    if len(p1) < 1 or len(p2) < 1:
        return False
    else:
        return True


#Play one game to completion
def RunGame(p1, p2, p1count, pile1, pile2, max_rounds=10000):
    ok = True
    rounds = 0
    while ok and rounds < max_rounds:
        ok = Play1(p1, p2, p1count, pile1, pile2)
        rounds += 1
    if len(p1) > 1:
        return 1, rounds
    else:
        return 2, rounds


#Play many games
def Go(N=1000):
    wins_p1 = 0
    wins_p2 = 0
    wrounds = []

    for i in range(N):
        p1, p2, p1count, pile1, pile2 = Start()
        win, rounds = RunGame(p1, p2, p1count, pile1, pile2)
        
        if win == 1:
            wins_p1 += 1
        else:
            wins_p2 += 1
        
        wrounds.append(rounds)

    wrounds = np.array(wrounds)
    return wins_p1, wins_p2, wrounds


    #Example run
if __name__ == "__main__":
    p1, p2, p1count, pile1, pile2 = Start()
    winner, rounds = RunGame(p1, p2, p1count, pile1, pile2)
    print(f"Winner: Player {winner}, Rounds played: {rounds}")

    #Run multiple games
    wins_p1, wins_p2, rounds_list = Go(100)
    print(f"\nPlayer 1 wins: {wins_p1}")
    print(f"Player 2 wins: {wins_p2}")
    print(f"Total games: {wins_p1 + wins_p2}")
    print(f"Average rounds per game: {np.mean(rounds_list):.2f}")