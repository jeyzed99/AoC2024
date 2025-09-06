input = open("Day4Input.txt", "r")
wordsearch =[]

#Making a wordsearch matrix
data = input.readline()
while data:
    realdata = list(data)
    realdata.pop()
    wordsearch.append(realdata)
    data = input.readline()

def masSearch(matrix):
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] == 'M'):
                
                #M's on right
                if (j > 1 and i < len(matrix)-2):
                    if (matrix[i+2][j] == 'M'):
                        if (matrix[i+1][j-1] == 'A'):
                            if (matrix[i+2][j-2] == 'S' and matrix[i][j-2]=='S'):
                                count += 1

                #M's on top
                if (j < len(matrix[i])-2 and i < len(matrix)-2):
                    if (matrix[i][j+2] == 'M'):
                        if (matrix[i+1][j+1] == 'A'):
                            if (matrix[i+2][j+2] == 'S' and matrix[i+2][j]=='S'):
                                count += 1

                #M's on left
                if (j < len(matrix[i])-2 and i > 1):
                    if (matrix[i-2][j] == 'M'):
                        if (matrix[i-1][j+1] == 'A'):
                            if (matrix[i-2][j+2] == 'S' and matrix[i][j+2]=='S'):
                                count += 1

                #M's on bottom
                if (j > 1 and i > 1):
                    if (matrix[i][j-2] == 'M'):
                        if (matrix[i-1][j-1] == 'A'):
                            if (matrix[i-2][j-2] == 'S' and matrix[i-2][j]=='S'):
                                count += 1
        print(count)

masSearch(wordsearch)