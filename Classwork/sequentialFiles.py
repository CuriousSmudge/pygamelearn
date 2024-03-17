def main () :
    # The 'a' means append (as opposed to 'w' for write which will clear the file before writing.)
    highScores = open('recordHighScores.txt', 'a')
   
    # This is called a priming read
    name = input('Player name : ')
    score = int(input('Player score : '))
   
    while name != 'end' :
       highScores.write(f'{name},{score}\n')
       name = input('Player name : ')
       score = int(input('Player score : '))
  	 
    print('High Scores saved to file.')
    highScores.close() 
main()
