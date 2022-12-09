lines = []
score = 0

with open("input.txt") as file:
    for line in file:
        player1 = line.split(" ")[0].strip()
        player2 = line.split(" ")[1].strip()
        if player2 == "X":
            score = score + 1
            if player1 == "C":
                score = score + 6
            elif player1 == "A":
                score = score + 3
        if player2 == "Y":
            score = score + 2
            if player1 == "A":
                score = score + 6
            elif player1 == "B":
                score = score + 3
        if player2 == "Z":
            score = score + 3
            if player1 == "B":
                score = score + 6
            elif player1 == "C":
                score = score + 3

print ("score is: ", score)