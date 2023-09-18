def calculateScore(opponent, outcome):
    #returns the score for the shape i must choose and the outcome i must achieve
    if outcome == "X":  
        if opponent == "A":  
            return 3  
        if opponent == "B":  
            return 1  
        if opponent == "C":  
            return 2  
    elif outcome == "Y":  
        if opponent == "A":  
            return 4  
        if opponent == "B":  
            return 5  
        if opponent == "C":  
            return 6  
    elif outcome == "Z":  
        if opponent == "A":  
            return 8  
        if opponent == "B":  
            return 9  
        if opponent == "C":  
            return 7  

# main logic
total_score = 0

try:
    with open('strategyguide.txt', 'r') as file:
        for line in file.readlines():
            opponent, outcome = line.strip().split()
            total_score += calculateScore(opponent, outcome)
except Exception as e:
    print(f"An error occurred: {e}")

print(f"My total score is: {total_score}")
