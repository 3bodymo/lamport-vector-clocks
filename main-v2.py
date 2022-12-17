ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
processes = {}
vectorOfProcess = []
senders = []
receivers = []

def updateNextForP(process, prevTimestamp, location):
    for letter in processes[process]:
        bl = isLetterBiggerOrEqual(letter, location)
        if(bl):
            for i in range(len(vectorOfProcess)):
                if(processes[process][letter][i] < prevTimestamp[i]):
                    processes[process][letter][i] = prevTimestamp[i]

def isLetterBiggerOrEqual(letter, currentLetter):
    letterLocation = 0
    currentLetterLocation = 0
    for i in range(len(ALPHABET)):
        if(ALPHABET[i] == letter):
            letterLocation = i
        if(ALPHABET[i] == currentLetter):
            currentLetterLocation = i
    if(letterLocation >= currentLetterLocation):
        return True
    if(letterLocation < currentLetterLocation):
        return False

def maxVector(a,b):
    c = []
    for i in range(len(processes)):
        if(a[i] > b[i]):
            c.append(a[i])
        else:
            c.append(b[i])
    return c

def eventLocation(l):
    for p in processes:
        for letter in processes[p]:
            if(letter == l):
                # "p" represent location of event
                # "process[p][letter]" represent timestamp of event
                # "letter" represent letter of event
                return p, processes[p][letter], letter

def arrCopy(arr):
    a = [0] * len(arr)
    for i in range(len(arr)):
        a[i] = arr[i]
    return a
    
def main():
    numOfProcesses = int(input("What is the number of process? "))
    for s in range(numOfProcesses):
        processes[f"P{s+1}"] = {}
        vectorOfProcess.append(0)
    _a = 0
    _x = 0
    for i in range(numOfProcesses):
        numOfLetters = int(input(f"Write the number of letters for P{i+1}: "))
        for x in range(numOfLetters):
            vectorOfProcess[_x] = x+1
            processes[f"P{i+1}"][ALPHABET[_a]] = arrCopy(vectorOfProcess)
            _a = _a + 1
        vectorOfProcess[_x] = 0
        _x = _x + 1

    numOfMessages = int(input("Write number of messages: "))
    for i in range(numOfMessages):
        senders.append(input(f"Write letter of sender #{i+1}: "))
        receivers.append(input(f"Write letter of receiver #{i+1}: "))

    # Here I make the iteration twice, because the second iteration is to update the timestamp after some events got timestamp changed
    for i in range(2):
        for p in processes:
            for letter in processes[p]:
                for i in range(len(senders)):
                    if(letter == senders[i]):
                        locationOfReceiver, timestampOfReceiver, letterOfReceiver = eventLocation(receivers[i])
                        max = maxVector(processes[p][letter], timestampOfReceiver)
                        updateNextForP(locationOfReceiver, max, letterOfReceiver)

    for p in processes:
        print(f"{p}: {processes[p]}")


if __name__ == "__main__":
    main()
