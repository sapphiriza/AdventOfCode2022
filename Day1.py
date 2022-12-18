if __name__ == "__main__":
    currentCalories = 0
    caloriesList = []
    file = open("input\calories.txt")
    for line in file.readlines():
        if line := line.strip():
            currentCalories += int(line)
        else:
            caloriesList += [currentCalories]
            currentCalories = 0
    if currentCalories > 0:
        caloriesList += [currentCalories]
    
    # Haha thx python ex dee
    caloriesList.sort(reverse=True)
    sum = sum(caloriesList[:3])
    print("The best three elves are carrying a total of " + str(sum) + " calories...")
    print("One elf is carrying a whopping " + str(caloriesList[-1]) + " calories!")
