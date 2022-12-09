lines = []
toplist = []
counter = 0
max = 0
with open("input.txt") as file:
    for line in file:
        if line != "\n":
          lineint = int(line)
          counter = counter + lineint
        else:
          if counter > max:
            max = counter
          toplist.append(counter)
          counter = 0 

print ("Most rations: ", max)
print ("Total of top 3 ", sum((sorted(toplist, reverse=True)[0:3])))


