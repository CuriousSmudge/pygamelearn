def main2 () :
    scores = open('recordHighScores.txt')
    
    line = scores.readline().strip()

    while line != '' :
        fields = line.split(',')
        print (f'Player {fields[0]} got a score of : {fields[1]}')
        line = scores.readline().strip()    
main2()