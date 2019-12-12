import random

#bodyParts = list(input("Enter the body parts (separated with a ';' character): ").split(";"))
#players = list(input("Enter the players (separated with a ';' character): ").split(";"))
bodyParts = ["Arm", "Bein", "Fuß"]
players = ["Gustav", "Donald", "Dagobert"]

while True:
    for player in players:
        sourceBodypart = bodyParts[random.randrange(len(bodyParts) - 1)]
        personToTouch = players[random.randrange(len(bodyParts) - 1)]
        targetBodypart = bodyParts[random.randrange(len(bodyParts) - 1)]
        print(f"The next player {player} needs to touch {personToTouch}'s {targetBodypart} with their {sourceBodypart}" )
    if(input("Another round? y/n ") == "n"):
        break