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

def is_free (location_index):
    if board[location_index] != player1char and board[location_index] != player2char:
        return True
    else:
        return False

def look_for_win (my_piece):
    #Checks to see if there any places that would give a win
    #Remember indexes into lists start at 0, not 1.
    counter = 0
    won = False

    #Try each free position in turn
    while counter < 9 and not won:
        if is_free(counter):
            old_char = board[counter]
            board[counter] = my_piece

            #use the check_line function to see whether the free space completes a line
            if not check_line(my_piece):
                #if it doesn't put the number back
                board[counter] = old_char
            else:
                won = True

        counter = counter + 1

    if not won:
        counter = 0

#    print ('look_for_win = ' + str(counter - 1))
    return counter - 1

def look_to_block (mypiece, their_piece):
    #checks to see whether they could complete a row and blocks
    #use look_for_win function with the other players piece, then swap if a place is found
    block_pos = look_for_win (their_piece)

    if block_pos > -1:
        board[block_pos] = mypiece

#    print ('look_to_block = ' + str(block_pos))
    return block_pos


def power_corner (mypiece):
    #looks to see if there is a corner that gives the potential for a line
    #Assuming that 3 in a row has already been checked for

    go_pos = -1

    #Check each corner in turn
    #remember, indexes start at 0 not 1
    if is_free(0):
        for counter in (1,2,3,4,6,8):
            if board[counter] == mypiece:
                go_pos = 0
            
    if go_pos == -1 and is_free(2):
        for counter in (0, 1, 4, 5, 6, 8):
            if board[counter] == mypiece:
                go_pos = 2
    

    if go_pos == -1 and is_free(6):
        for counter in (0, 2, 4, 3, 7, 8):
            if board[counter] == mypiece:
                go_pos = 6

    if go_pos == -1 and is_free(8):
        for counter in (0, 2, 4, 5, 6, 7):
            if board[counter] == mypiece:
                go_pos = 8

    if go_pos > -1:
        board[go_pos] = mypiece

#    print ('power_corner = ' + str(go_pos))
    return go_pos

def opp_opponent (mypiece, their_piece):
    go_pos = -1

    if is_free(4):
        if board[0] == their_piece and is_free(8):
            go_pos = 4

        if board[2] == their_piece and is_free(6):
            go_pos = 4

        if board[6] == their_piece and is_free(2):
            go_pos = 4

        if board[8] == their_piece and is_free(0):
            go_pos = 4

    if go_pos > -1:
        board[go_pos] = mypiece

#    print ('opp_opponent = ' + str(go_pos))
    return go_pos

def any_free_square (mypiece):
    #This will return the last free space it finds in the list,
    #e.g. if the centre (4) is still available that will alway be returned
    #after that a free corner. Finally a side
    go_pos = -1
    for counter in (1, 3, 5, 7, 0, 2, 6, 8, 4):
        if is_free(counter):
            go_pos = counter

    if go_pos > -1:
        board[go_pos] = mypiece

#    print ('any_free_square = ' + str(go_pos))
    return go_pos

def machine_go (mypiece, their_piece):

    go_pos = look_for_win(mypiece)

    if go_pos == -1:
        go_pos = look_to_block (mypiece, their_piece)

    if go_pos == -1:
        go_pos = power_corner (mypiece)

#    if go_pos == -1:
#        go_pos = opp_opponent (mypiece, their_piece)

    if go_pos == -1:
        go_pos = any_free_square (mypiece)

    if go_pos > -1:
        print ('Computer plays ' + str(go_pos + 1))

                
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

#Stop when a player has won or there aren't any more spaces
while not (check_line(player1char) or  check_line(player2char) or (board.count(player1char) + board.count(player2char) == 9)):
           show_board()
           gopos = 0
           
           validpic = False
           while not validpic:
                   #Assume they will enter a number between 1 and 9
                   #It will get reset to False if they don't
                   validpic = True;

                   #Validate the user input
                   nextgo = input('Choose your square: ')
                   try:
                           gopos = int(nextgo) - 1
                   except ValueError:
                           print ('Must be a number')
                           validpic = False

                   if gopos < 0 or gopos > 8:
                        print ('Choose between 1 and 9')
                        validpic = False   
                   if not is_free(gopos):
                        print ('space already taken')
                        validpic = False                        

           board[gopos] = player1char
           
           if check_line (player1char):
                   print('')
                   show_board()
                   print ('You win!')
           else:
               machine_go(player2char, player1char)
               if check_line (player2char):
                       print('')
                       show_board()
                       print ('Computer wins!')


if not (check_line(player1char) or check_line(player2char)):
        print ('It was a draw')
        
