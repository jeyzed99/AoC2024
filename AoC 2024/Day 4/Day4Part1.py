input = open("Day4Input.txt", "r")
wordsearch =[]

#Making a wordsearch matrix
data = input.readline()
while data:
    realdata = list(data)
    realdata.pop()
    wordsearch.append(realdata)
    data = input.readline()

#Searching for 'xmas' in the matrix
def xmasSearcher(matrix):
    count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 'X'):
                spelling = ['X']
                #looking to the right of letter matrix[i][j]
                if (j < len(matrix[i])-3):
                    if (matrix[i][j+1] == 'M'):
                        spelling.append(matrix[i][j+1])
                        if (matrix[i][j+2] == 'A'):
                            spelling.append(matrix[i][j+2])
                            if (matrix[i][j+3] == 'S'):
                                spelling.append(matrix[i][j+3])
                                if (spelling == ['X','M','A','S']):
                                    count += 1
                                    print(count)
                                
                            else:
                               count += 0
                        else:
                            count += 0
                    else:
                        count += 0

                else:
                    count += 0
                
                #looking to the top-right of letter matrix[i][j]
                if (i>2 and j < len(matrix[i])-3):
                    if (matrix[i-1][j+1] == 'M'):
                        if (matrix[i-2][j+2] == 'A'):
                            if (matrix[i-3][j+3] == 'S'):
                                count += 1
                                print(count)
                            else:
                               count += 0
                        else:
                            count += 0
                    else:
                        count += 0

                else:
                    count += 0
                
                #looking above letter matrix[i][j]
                if (i>2):
                    if (matrix[i-1][j] == 'M'):
                        if (matrix[i-2][j] == 'A'):
                            if (matrix[i-3][j] == 'S'):
                                count += 1
                                print(count)
                            else:
                               count += 0
                        else:
                            count += 0
                    else:
                        count += 0

                else:
                    count += 0
                
                #looking to the top-left of letter matrix[i][j]
                if (i>2 and j>2):
                    if (matrix[i-1][j-1] == 'M'):
                        if (matrix[i-2][j-2] == 'A'):
                            if (matrix[i-3][j-3] == 'S'):
                                count += 1
                                print(count)
                            else:
                               count += 0
                        else:
                            count += 0
                    else:
                        count += 0

                else:
                    count += 0
                
                #looking to the left of letter matrix[i][j]
                if (j>2):
                    if (matrix[i][j-1] == 'M'):
                        if (matrix[i][j-2] == 'A'):
                            if (matrix[i][j-3] == 'S'):
                                count += 1
                                print(count)
                            else:
                               count += 0
                        else:
                            count += 0
                    else:
                        count += 0

                else:
                    count += 0

                #looking to the bottom-left of letter matrix[i][j]
                if (i < len(matrix)-3 and j>2):
                    if (matrix[i+1][j-1] == 'M'):
                        if (matrix[i+2][j-2] == 'A'):
                            if (matrix[i+3][j-3] == 'S'):
                                count += 1
                                print(count)
                            else:
                               count += 0
                        else:
                            count += 0
                    else:
                        count += 0

                else:
                    count += 0
                
                #looking below letter matrix[i][j]
                if (i < len(matrix)-3):
                    if (matrix[i+1][j] == 'M'):
                        if (matrix[i+2][j] == 'A'):
                            if (matrix[i+3][j] == 'S'):
                                count += 1
                                print(count)
                            else:
                               count += 0
                        else:
                            count += 0
                    else:
                        count += 0

                else:
                    count += 0
                
                #looking to the bottom-right of letter matrix[i][j]
                if (i < len(matrix)-3 and j < len(matrix[i])-3):
                    if (matrix[i+1][j+1] == 'M'):
                        if (matrix[i+2][j+2] == 'A'):
                            if (matrix[i+3][j+3] == 'S'):
                                count += 1
                                print(count)
                            else:
                               count += 0
                        else:
                            count += 0
                    else:
                        count += 0

                else:
                    count += 0
            
    print(count)

xmasSearcher(wordsearch)

