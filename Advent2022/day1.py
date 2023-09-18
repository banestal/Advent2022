#Day 1 of AdventCode

#starting variable set to 0 **will change later**
maxCalories = 0

#grabbing puzzle data
try:
    with open('puzzle.txt', 'r') as f:
        input_data = f.read()


    #split each Elves inventory based on blank spaces
    elfInventories = input_data.strip().split("\n\n")

    for inventory in elfInventories:
        totalCalories = sum(int(item) for item in inventory.split("\n"))

        #updating max calories
        if totalCalories > maxCalories:
            maxCalories = totalCalories
        
    print(f"Elf Carrying the most Cals has a total of: {maxCalories} ")

except Exception as e:
    print(f"An error occurred: {e}")
    

