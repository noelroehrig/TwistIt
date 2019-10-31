import random

bodyParts = list(input("Enter the body parts (separated with a ';' character): ").split(";"))
players = list(input("Enter the players (separated with a ';' character): ").split(";"))

sourceBodypart = bodyParts[random.randrange(len(bodyParts) - 1)]
personToTouch = players[random.randrange(len(bodyParts) - 1)]
targetBodypart = bodyParts[random.randrange(len(bodyParts) - 1)]

print(f"The next player in line needs to touch {personToTouch}'s {targetBodypart} with their {sourceBodypart}" )