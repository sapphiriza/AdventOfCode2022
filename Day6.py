if __name__ == "__main__":
    file = open("input/commPacket.txt")
    #file = open("input/commSamples.txt")
    lines = file.readlines()

    print("Start-of-packet markers:")
    for line in lines:
        line = line.strip()
        if len(line) < 4:
            print("Haha tiny packet!")
            break
        
        isStartFound = False
        for i in range(0, len(line) - 3):
            isPacketStart = True
            substr = line[i:i+4]
            for j in range(0, 4):
                if substr.count(substr[j]) > 1:
                    isPacketStart = False
                    break
            if isPacketStart:
                print(f"First marker after character {i+4}")
                isStartFound = True
                break
        if not isStartFound:
            print("Who built the Radio of Babel?")
    
    print("Start-of-message markers:")
    for line in lines:
        line = line.strip()
        if len(line) < 14:
            print("Haha tiny packet!")
            break
        
        isStartFound = False
        for i in range(0, len(line) - 13):
            isPacketStart = True
            substr = line[i:i+14]
            for j in range(0, 14):
                if substr.count(substr[j]) > 1:
                    isPacketStart = False
                    break
            if isPacketStart:
                print(f"First marker after character {i+14}")
                isStartFound = True
                break
        if not isStartFound:
            print("Who built the Radio of Babel?")
