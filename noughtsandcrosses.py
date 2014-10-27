#Noughts and crosses
board = ['1','2','3','4','5','6','7','8','9']
player1char = 'X'
player2char = 'O'

def show_board ():
    """Loops through the board list to display the players' positions"""
    counter = 1
    linecounter = 1
    line = ''
    
    for item in board:
        line = line + item
        #Add the vertical line unless at the last place
        if counter < 3:
            line = line + '|'

        #When a row is completed print it and the horizontal divider line
        if counter == 3:
                print (line)
                if linecounter < 3: 
                        print ('-----')
                counter = 0
                linecounter = linecounter + 1
                line = ''

        counter = counter + 1
                
def check_line (playerchar):
        """Checks whether the specified player has won"""
        #A bit brute force & ignorance

        #horizontals
        if board[0] == playerchar and board[1] == playerchar and board[2] == playerchar:
                return True

        if board[3] == playerchar and board[4] == playerchar and board[5] == playerchar:
                return True

        if board[6] == playerchar and board[7] == playerchar and board[8] == playerchar:
                return True

        #Diagonals
        if board[0] == playerchar and board[4] == playerchar and board[8] == playerchar:
                return True

        if board[2] == playerchar and board[4] == playerchar and board[6] == playerchar:
                return True

        #verticals
        if board[0] == playerchar and board[3] == playerchar and board[6] == playerchar:
                return True

        if board[1] == playerchar and board[4] == playerchar and board[7] == playerchar:
                return True

        if board[2] == playerchar and board[5] == playerchar and board[8] == playerchar:
                return True
        
        return False


#Main loop
nextplayer = player1char

#Stop when a player has won or there aren't any more spaces
while not (check_line(player1char) or  check_line(player2char) or (board.count(player1char) + board.count(player2char) == 9)):
           show_board()
           gopos = 0
           
           validpic = False
           while not validpic:
                   #Assume they will enter a number between 1 and 9
                   #It will get reset to False if they don't
                   validpic = True;

                   nextgo = input('player ' + nextplayer + ' place: ')

                   #Validate the user input
                   try:
                           gopos = int(nextgo) - 1
                   except ValueError:
                           print ('Must be a number')
                           validpic = False

                   if gopos < 0 or gopos > 8:
                        print ('Choose between 1 and 9')
                        validpic = False
                        
                   if (board[gopos] == player1char or board[gopos] == player2char):
                        print ('space already taken')
                        validpic = False                        

           board[gopos] = nextplayer
           
           if check_line (nextplayer):
                   print('')
                   show_board()
                   print ('')
                   print ('Player ' + nextplayer + ' wins!')

           if nextplayer == player1char:
                   nextplayer = player2char
           else:
                   nextplayer = player1char
           

if not (check_line(player1char) or check_line(player2char)):
        print ('It was a draw')
        
