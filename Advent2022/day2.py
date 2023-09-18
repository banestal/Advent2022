from aocd import get_data

totalScore = 0

# Dictionary to map scores based on choices
mapScoreChoices = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

# Function to determine the outcome of a single round
def roundOutcome(opponent, myChoice):
    if opponent == "A" and myChoice == "Y":
        return 6
    elif opponent == "B" and myChoice == "Z":
        return 6
    elif opponent == "C" and myChoice == "X":
        return 6
    elif opponent == "A" and myChoice == "Z":
        return 0
    elif opponent == "B" and myChoice == "X":
        return 0
    elif opponent == "C" and myChoice == "Y":
        return 0
    else:
        return 3

try:
    with open('strategyguide.txt', 'r') as c:
        rounds = c.read().strip().split("\n")
        
    print(f"Read {len(rounds)} rounds")
        
    for r in rounds:
        if not r.strip():
            continue
        parts = r.split(" ")
        if len(parts) != 2:
            print(f"Skipping malformed line: '{r}'")
            continue
        
        opponent, myChoice = parts
        outcome = roundOutcome(opponent, myChoice)
        totalScore += mapScoreChoices[myChoice] + outcome
    
    print(f"My total score is: {totalScore}")
    
except Exception as e:
    print(f"An error occurred: {e}")
