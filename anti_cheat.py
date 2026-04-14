# Simple Anti-Cheat System

previous_score = 0

while True:
    score = int(input("Enter player score (0 to stop): "))

    if score == 0:
        print("Game Ended 🎮")
        break

    # Rule 1: Negative score
    if score < 0:
        print("Invalid Score ❌")
        continue

    # Rule 2: Sudden jump detection
    if score - previous_score > 50:
        print("Cheating Detected 🚨 (Score increased too fast)")
    
    # Rule 3: Unrealistic high score
    elif score > 1000:
        print("Cheating Detected 🚨 (Unrealistic score)")
    
    else:
        print("Score Accepted ✅")

    previous_score = score