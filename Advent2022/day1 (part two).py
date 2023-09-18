import heapq

try:
    with open('puzzle.txt', 'r') as f:
        input_data = f.read()
        
    elfInventories = input_data.strip().split("\n\n")

    topThree = []
    
    for inventory in elfInventories:
        totalCalories = sum(int(item) for item in inventory.split("\n"))
        
        heapq.heappush(topThree, totalCalories)
        if len(topThree) > 3:
            heapq.heappop(topThree)
        
    
    topThree.sort(reverse=True)
    print(f"THe top 3 Elves are carrying {topThree} calories")
    print(f"The sum of their Calories is: {sum(topThree)}")
    
    
except Exception as b:
    print(f"An error occurred: {b}")