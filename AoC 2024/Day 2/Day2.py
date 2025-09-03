import numpy as np

#Safe level counter
safeLines = 0

#Opening input file
input = open("Day2Input.txt","r")
data = input.readline()

#Level checker script, returns true if the level is safe
def levelReader(level):
    increasing = False
    decreasing = False

    #Check if increasing
    if level[0] < level[1]:
        increasing = True

    #Check if decreasing
    if level[0] > level[1]:
        decreasing = True
    
    #Weed out constant levels
    if level[0] == level[1]:
        return False
    
    #Checking increasing rule
    if increasing:
        for i in range(len(level)-1):
            if level[i+1]-level[i] > 3 or level[i+1] - level[i] < 1:
                return False
            
    #Checking decreasing rule
    if decreasing:
        for i in range(len(level)-1):
            if level[i] - level[i+1] > 3 or level[i] - level[i+1] < 1:
                return False


    return True

#Going each level in our data
while data:
    #convert a level from our text file to an array of ints
    level = [int(s) for s in data.split(' ')]
    
    #run a levelReader check
    if levelReader(level):
        safeLines += 1
        print(safeLines)
    else:
        #Retry with new safety measure
        for i in range(len(level)):
            hold = level.pop(i) #taking out an entry in a level
            if levelReader(level): #Checking if the removed entry makes a safe level
                safeLines += 1
                break #Remembering to exit a level that's safe after a removed entry so we don't double count any levels
            level.insert(i,hold)
    data = input.readline() #move to next level in report

input.close()

print(safeLines)