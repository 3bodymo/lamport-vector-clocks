ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
P1 = {}
P2 = {}
P3 = {}
senders = []
receivers = []

def nextForP1(key, prevTimestamp):
    arr = P1[key]
    if(arr[0] > prevTimestamp[0]):
        P1[key] = [arr[0], arr[1], arr[2]]
    else:
        P1[key] = [prevTimestamp[0], arr[1], arr[2]]
    arr = P1[key]
    if(arr[1] > prevTimestamp[1]):
        P1[key] = [arr[0], arr[1], arr[2]]
    else:
        P1[key] = [arr[0], prevTimestamp[1], arr[2]]
    arr = P1[key]
    if(arr[2] > prevTimestamp[2]):
        P1[key] = [arr[0], arr[1], arr[2]]
    else:
        P1[key] = [arr[0], arr[1], prevTimestamp[2]]

def nextForP2(key, prevTimestamp):
    arr = P2[key]
    if(arr[0] > prevTimestamp[0]):
        P2[key] = [arr[0], arr[1], arr[2]]
    else:
        P2[key] = [prevTimestamp[0], arr[1], arr[2]]
    arr = P2[key]
    if(arr[1] > prevTimestamp[1]):
        P2[key] = [arr[0], arr[1], arr[2]]
    else:
        P2[key] = [arr[0], prevTimestamp[1], arr[2]]
    arr = P2[key]
    if(arr[2] > prevTimestamp[2]):
        P2[key] = [arr[0], arr[1], arr[2]]
    else:
        P2[key] = [arr[0], arr[1], prevTimestamp[2]]

def nextForP3(key, prevTimestamp):
    arr = P3[key]
    if(arr[0] > prevTimestamp[0]):
        P3[key] = [arr[0], arr[1], arr[2]]
    else:
        P3[key] = [prevTimestamp[0], arr[1], arr[2]]
    arr = P3[key]
    if(arr[1] > prevTimestamp[1]):
        P3[key] = [arr[0], arr[1], arr[2]]
    else:
        P3[key] = [arr[0], prevTimestamp[1], arr[2]]
    arr = P3[key]
    if(arr[2] > prevTimestamp[2]):
        P3[key] = [arr[0], arr[1], arr[2]]
    else:
        P3[key] = [arr[0], arr[1], prevTimestamp[2]]

def isLetterBigger(letter, currentLetter):
    letterLocation = 0
    currentLetterLocation = 0
    for i in range(len(ALPHABET)):
        if(ALPHABET[i] == letter):
            letterLocation = i
        if(ALPHABET[i] == currentLetter):
            currentLetterLocation = i
    if(letterLocation > currentLetterLocation):
        return True
    if(letterLocation < currentLetterLocation):
        return False

def isLetterEqual(letter, currentLetter):
    letterLocation = 0
    currentLetterLocation = 0
    for i in range(len(ALPHABET)):
        if(ALPHABET[i] == letter):
            letterLocation = i
        if(ALPHABET[i] == currentLetter):
            currentLetterLocation = i
    if(letterLocation == currentLetterLocation):
        return True
    if(letterLocation != currentLetterLocation):
        return False

def maxVector(a,b):
    c = []
    for i in range(3):
        if(a[i] > b[i]):
            c.append(a[i])
        else:
            c.append(b[i])
    return c

def eventLocation(letter):
    for l in P1:
        if(l == letter):
            # "P1" represent location of event
            # "P1[l]" represent timestamp of event
            # "l" represent letter of event
            return "P1", P1[l], l
    for l in P2:
        if(l == letter):
            return "P2", P2[l], l
    for l in P3:
        if(l == letter):
            return "P3", P3[l], l

def updateNextForP1(prevTimestamp, location):
    for key in P1:
        bl = isLetterBigger(key, location)
        if(bl):
            nextForP1(key, prevTimestamp)

def updateNextForP2(prevTimestamp, location):
    for key in P2:
        bl = isLetterBigger(key, location)
        if(bl):
           nextForP2(key, prevTimestamp)

def updateNextForP3(prevTimestamp, location):
    for key in P3:
        bl = isLetterBigger(key, location)
        if(bl):
            nextForP3(key, prevTimestamp)

def main():
    _x = 0
    numOfLetters = int(input("Write the number of letters for P1: "))
    for x in range(numOfLetters):
        P1[ALPHABET[_x]] = [x+1, 0, 0]
        _x = _x + 1

    numOfLetters = int(input("Write the number of letters for P2: "))
    for x in range(numOfLetters):
        P2[ALPHABET[_x]] = [0, x+1, 0]
        _x = _x + 1

    numOfLetters = int(input("Write the number of letters for P3: "))
    for x in range(numOfLetters):
        P3[ALPHABET[_x]] = [0, 0, x+1]
        _x = _x + 1

    numOfMessages = int(input("Write number of messages: "))
    for i in range(numOfMessages):
        senders.append(input(f"Write letter of sender {i+1}: "))
        receivers.append(input(f"Write letter of receiver {i+1}: "))

    for key in P1:
        for i in range(len(senders)):
            if(key == senders[i]):
                location, timestamp, l = eventLocation(receivers[i])
                max = maxVector(P1[key], timestamp)
                if(location == "P2"):
                    P2[l] = max
                    updateNextForP2(max, l)
                elif(location == "P3"):
                    P3[l] = max
                    updateNextForP3(max, l)
    
    for key in P2:
        for i in range(len(senders)):
            if(key == senders[i]):
                location, timestamp, l = eventLocation(receivers[i])
                max = maxVector(P2[key], timestamp)
                if(location == "P1"):
                    P1[l] = max
                    updateNextForP1(max, l)
                elif(location == "P3"):
                    P3[l] = max
                    updateNextForP3(max, l)

    for key in P3:
        for i in range(len(senders)):
            if(key == senders[i]):
                location, timestamp, l = eventLocation(receivers[i])
                max = maxVector(P3[key], timestamp)
                if(location == "P1"):
                    P1[l] = max
                    updateNextForP1(max, l)
                elif(location == "P2"):
                    P2[l] = max
                    updateNextForP2(max, l)

    for key in P2:
        for i in range(len(senders)):
            if(key == senders[i]):
                location, timestamp, l = eventLocation(receivers[i])
                locationOfSender, timestampOfSender, lOfSender = eventLocation(senders[i])
                if(location == "P1"):
                    for key in P1:
                        bl = isLetterBigger(key, l)
                        if(bl or isLetterEqual(key, l)):
                            nextForP1(key, timestampOfSender)
                            for i in range(len(senders)):
                                if(key == senders[i]):
                                    location, timestamp, l = eventLocation(receivers[i])
                                    locationOfSender, timestampOfSender, lOfSender = eventLocation(senders[i])
                                    if(location == "P2"):
                                        for key in P2:
                                            bl = isLetterBigger(key, l)
                                            if(bl or isLetterEqual(key, l)):
                                                nextForP2(key, timestampOfSender)
                                    if(location == "P3"):
                                        for key in P3:
                                            bl = isLetterBigger(key, l)
                                            if(bl or isLetterEqual(key, l)):
                                                nextForP3(key, timestampOfSender)
                elif(location == "P3"):
                    for key in P3:
                        bl = isLetterBigger(key, l)
                        if(bl or isLetterEqual(key, l)):
                            nextForP3(key, timestampOfSender)
                            for i in range(len(senders)):
                                if(key == senders[i]):
                                    location, timestamp, l = eventLocation(receivers[i])
                                    locationOfSender, timestampOfSender, lOfSender = eventLocation(senders[i])
                                    if(location == "P1"):
                                        for key in P1:
                                            bl = isLetterBigger(key, l)
                                            if(bl or isLetterEqual(key, l)):
                                                nextForP1(key, timestampOfSender)
                                    if(location == "P2"):
                                        for key in P2:
                                            bl = isLetterBigger(key, l)
                                            if(bl or isLetterEqual(key, l)):
                                                nextForP2(key, timestampOfSender)

    for key in P3:
        for i in range(len(senders)):
            if(key == senders[i]):
                location, timestamp, l = eventLocation(receivers[i])
                locationOfSender, timestampOfSender, lOfSender = eventLocation(senders[i])
                if(location == "P1"):
                    for key in P1:
                        bl = isLetterBigger(key, l)
                        if(bl or isLetterEqual(key, l)):
                            nextForP1(key, timestampOfSender)
                            for i in range(len(senders)):
                                if(key == senders[i]):
                                    location, timestamp, l = eventLocation(receivers[i])
                                    locationOfSender, timestampOfSender, lOfSender = eventLocation(senders[i])
                                    if(location == "P2"):
                                        for key in P2:
                                            bl = isLetterBigger(key, l)
                                            if(bl or isLetterEqual(key, l)):
                                                nextForP2(key, timestampOfSender)
                                    if(location == "P3"):
                                        for key in P3:
                                            bl = isLetterBigger(key, l)
                                            if(bl or isLetterEqual(key, l)):
                                                nextForP3(key, timestampOfSender)
                elif(location == "P2"):
                    for key in P2:
                        bl = isLetterBigger(key, l)
                        if(bl or isLetterEqual(key, l)):
                            nextForP2(key, timestampOfSender)
                            for i in range(len(senders)):
                                if(key == senders[i]):
                                    location, timestamp, l = eventLocation(receivers[i])
                                    locationOfSender, timestampOfSender, lOfSender = eventLocation(senders[i])
                                    if(location == "P1"):
                                        for key in P1:
                                            bl = isLetterBigger(key, l)
                                            if(bl or isLetterEqual(key, l)):
                                                nextForP1(key, timestampOfSender)
                                    if(location == "P3"):
                                        for key in P3:
                                            bl = isLetterBigger(key, l)
                                            if(bl or isLetterEqual(key, l)):
                                                nextForP3(key, timestampOfSender)

    print(P1)
    print(P2)
    print(P3)


if __name__ == "__main__":
    main()