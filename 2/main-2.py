lines = []
score = 0

with open("input.txt") as file:
    for line in file:
        player1 = line.split(" ")[0].strip()
        player2 = line.split(" ")[1].strip()
        if player1 == "A":
            if player2 == "X":
                score = score + 3
            elif player2 == "Y":
                score = score + 3 + 1
            elif player2 == "Z":
                score = score + 6 + 2
        
        if player1 == "B":
            if player2 == "X":
                score = score + 1
            elif player2 == "Y":
                score = score + 3 + 2
            elif player2 == "Z":
                score = score + 6 + 3

        if player1 == "C":
            if player2 == "X":
                score = score + 2
            elif player2 == "Y":
                score = score + 3 + 3
            elif player2 == "Z":
                score = score + 6 + 1


print ("score is: ", score)