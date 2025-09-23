import random
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

# Base War Game Simulation
def create_deck():
    """Create a standard 52-card deck (values 2-14)."""
    return [rank for rank in range(2, 15) for _ in range(4)]

def play_war(max_rounds=100000, war_down=3, track_transfers=False):
    """
    Simulate one game of War.
    Returns: winner (1 or 2), rounds played, initial average of P1 cards, transfer stats (if enabled).
    """
    deck = create_deck()
    random.shuffle(deck)

    p1 = deque(deck[:26])
    p2 = deque(deck[26:])

    init_avg_p1 = np.mean(deck[:26])

    # Problem 4 tracking
    transfers = {"2": 0, "9": 0, "14": 0} if track_transfers else None

    round_count = 0
    while p1 and p2 and round_count < max_rounds:
        round_count += 1
        c1, c2 = p1.popleft(), p2.popleft()
        pile = [c1, c2]

        if track_transfers:
            for card in [c1, c2]:
                if str(card) in transfers:
                    transfers[str(card)] += 1

        # Handle wars
        while c1 == c2:
            if len(p1) < war_down + 1:
                return 2, round_count, init_avg_p1, transfers
            if len(p2) < war_down + 1:
                return 1, round_count, init_avg_p1, transfers
            pile.extend([p1.popleft() for _ in range(war_down)])
            pile.extend([p2.popleft() for _ in range(war_down)])
            c1, c2 = p1.popleft(), p2.popleft()
            pile.extend([c1, c2])

            if track_transfers:
                for card in [c1, c2]:
                    if str(card) in transfers:
                        transfers[str(card)] += 1

        if c1 > c2:
            p1.extend(pile)
        else:
            p2.extend(pile)

    if not p1:
        return 2, round_count, init_avg_p1, transfers
    elif not p2:
        return 1, round_count, init_avg_p1, transfers
    else:
        return 0, round_count, init_avg_p1, transfers  # draw

# Problem 1 & 2
def problem1_and_2(num_games=1000):
    V_all = []
    V_win = []
    for _ in range(num_games):
        winner, _, init_avg, _ = play_war()
        V_all.append(init_avg)
        if winner == 1:
            V_win.append(init_avg)
    print(f"Problem 1: Average V over all games = {np.mean(V_all):.2f}")
    print(f"Problem 2: Average V for Player 1 wins = {np.mean(V_win):.2f}")

# Problem 3
def problem3():
    game_counts = [3, 20, 40, 80, 160, 320, 640, 1280]
    win_percentages = []
    for g in game_counts:
        wins = sum(1 for _ in range(g) if play_war()[0] == 1)
        win_percentages.append(100 * wins / g)

    plt.bar([str(g) for g in game_counts], win_percentages)
    plt.xlabel("Number of Games")
    plt.ylabel("Win % for Player 1")
    plt.title("Problem 3: Player 1 Win Percentage")
    plt.show()

# Problem 4
def problem4(num_games=1000):
    transfer_counts = {"2": 0, "9": 0, "14": 0}
    total_rounds = 0
    for _ in range(num_games):
        winner, rounds, _, transfers = play_war(track_transfers=True)
        total_rounds += rounds
        for k in transfer_counts:
            transfer_counts[k] += transfers[k]

    print("Problem 4: Average transfer rates")
    for card in transfer_counts:
        avg_rate = transfer_counts[card] / total_rounds
        print(f"Card {card}: {avg_rate:.4f} transfers per round")

# Problem 5
def problem5(num_games=10000):
    wins = {1: 0, 2: 0}
    for _ in range(num_games):
        # Each player gets identical decks
        base_deck = create_deck()
        random.shuffle(base_deck)
        deck1, deck2 = base_deck[:26], base_deck[:26]
        p1 = deque(deck1)
        p2 = deque(deck2)
        winner, rounds, _, _ = play_war()
        if winner in wins:
            wins[winner] += 1
    print(f"Problem 5: Player 1 win % = {100 * wins[1] / num_games:.2f}%")

# Problem 6
def problem6(num_games=10000):
    war_down_values = [3, 5, 10]
    for war_down in war_down_values:
        rounds = []
        for _ in range(num_games):
            winner, r, _, _ = play_war(war_down=war_down)
            if winner == 1:
                rounds.append(r)
        print(f"Problem 6 (war_down={war_down}): "
              f"Avg rounds = {np.mean(rounds):.2f}, Std = {np.std(rounds):.2f}")

# Run All Problems
if __name__ == "__main__":
    problem1_and_2()
    problem3()
    problem4()
    problem5()
    problem6()
