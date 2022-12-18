if __name__ == "__main__":
    fullOverlaps = 0
    anyOverlaps = 0
    for line in open("input/cleanupPairs.txt").readlines():
        orders = line.strip().split(',')
        left = orders[0].split('-')
        right = orders[1].split('-')
        if(int(left[0]) >= int(right[0]) and int(left[1]) <= int(right[1])):
            fullOverlaps += 1
            
        elif(int(left[0]) <= int(right[0]) and int(left[1]) >= int(right[1])):
            fullOverlaps += 1

        if not (int(left[0]) > int(right[1]) or int(left[1]) < int(right[0])):
            anyOverlaps += 1
    print("The number of cleanup pairs with fully overlapping sets is " + str(fullOverlaps))
    print("The number of cleanup pairs with ANY overlapping work is " + str(anyOverlaps))