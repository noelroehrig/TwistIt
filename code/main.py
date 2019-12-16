import random

def GetInput(str):
    inputList = []
    while True:
        inputResult = input((f"Enter a {str} ('n' or empty character to stop input): "))
        if inputResult == 'n' or inputResult == "":
            break
        inputList.append(inputResult)
    return inputList

#bodyParts = list(input("Enter the body parts (separated with a ';' character): ").split(";"))
#players = list(input("Enter the players (separated with a ';' character): ").split(";"))
bodyParts = ["Arm", "Bein", "Fuß"]
players = ["Gustav", "Donald", "Dagobert"]

bodyParts.extend(GetInput("body part"))
players.extend(GetInput("player"))

while True:
    for player in players:
        sourceBodypart = bodyParts[random.randrange(len(bodyParts) - 1)]
        personToTouch = players[random.randrange(len(players) - 1)]
        targetBodypart = bodyParts[random.randrange(len(bodyParts) - 1)]
        print(f"{player} needs to touch {personToTouch}'s {targetBodypart} with their {sourceBodypart}" )
    if(input("Another round? y/n ") == "n"):
        break
