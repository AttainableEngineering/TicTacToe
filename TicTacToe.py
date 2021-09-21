from CheckTicTacToeSolutions import CheckTicTacToe

def hline():
    '''Prints horizontal line...only used for convenience'''
    print(' --- --- ---')

def ShowGame(display):
    '''
    This function displays the result of tic tac toe game in gameboard form.
    Display input is of form [[,,,],[,,,],[,,,]]    
    '''
    # Show the results from the updated gameboard
    print()
    hline()
    print('|', display[0][0], '|', display[0][1], '|', display[0][2], '|')
    hline()
    print('|', display[1][0], '|', display[1][1], '|', display[1][2], '|')
    hline()
    print('|', display[2][0], '|', display[2][1], '|', display[2][2], '|')
    hline()
    print()

# Function to check bounds vs game board
def CheckBounds(player):
    '''
    function takes a [#,#] list and determines if the number is a valid input for tic tac toe bounds.\n
    player -> input list for player choice.\n
    flag -> error output (0 if no error).
    '''

    # Initialize
    checking = True
    flag = 0

    # Make sure number is not above 3 or below 0
    while checking:
        if player[0] > 3 or player[0] < 0:
            flag = 1
        if player[1] > 3 or player[1] < 0:
            flag = 2
        checking = False
        if flag != 0:
            if flag == 1:
                text = 'first'
            else:
                text = 'second'
            print("Error in the", text, "bounds.")
    return flag # Throws flag corresponding to position of error

def PlayTicTacToe():
    '''
    When called, this function begins playing an interactive game of tic tac toe.
    To use, please enter coordinates of form <row, column> (without <>) and when
    a win is detected, the game will end, say who won, and display the resultant gameboard.
    '''
    ## Initialize Game
    playing = True
    used = []   # Make list to store used values
    game = [[0,0,0],[0,0,0],[0,0,0]]    # Empty gameboard
    
    # Print initializing message
    print("\n--- Tic Tac Toe game by Carlos Ortiz ---\n")
    print("Welcome to Tic Tac Toe!")
    print("The gameboard is represented by 3x3 coordinates, ranging from (1,1) to (3,3).")
    print("When prompted, please enter whichever coordinate you would like to fill.")
    print("All inputs should be of the form <row, column> (without the <>).")
    print("If at any point you would like to exit Tic Tac Toe, type exit at the prompt.")
    print("Enjoy Tic Tac Toe!\n")
    #print("Welcome to tic tac toe. When prompted, please input coordinates as (row,col).")

    # Loop game sequence
    while playing:
        # Initialize asking sequence
        askone = True
        asktwo = True

        # Recieve, clean, and check bounds of input. Returns [#, #]
        while askone:
            pone = input("Player 1, Where would you like to move? ")

            # Break if you type exit
            if pone == 'exit':
                print("\nExiting Tic Tac Toe...\n")
                break

            # Ensure input is int,int or ask for a new input
            try:
                p1 = [int(ii.strip()) for ii in pone.split(',')]
                if len(p1) != 2:
                    print("Incorrect input format. Try again.")
                    continue
            except:
                print("Invalid input Player 1. Please try again.")
                continue
            
            flag_one = CheckBounds(p1)  # Check bounds and throw flags as needed
            if flag_one != 0: continue  # Restart if an erroor flag is thrown. Message is displayed within function ^

            #Check for reused values and if reused, take new input
            if p1 in used:
                print("Player 1, please select a number that has not been used.")
                continue

            #Update used values
            used.append(p1)

            askone = False # Do not continue asking b/c input is valid
        
        if pone == 'exit':
                break

        #Update game board
        game[p1[0]-1][p1[1]-1] = 1


        #Check for a winner of the game
        winner = CheckTicTacToe(game)

        if winner != 0 and winner!= 999:
            print("\nPlayer", winner, "Wins! Congratulations")
            playing = False
            break
        elif winner == 999:
            print("Tie!")
            break

        # If there is no winner, move on to player 2 input and repeat same cycle
        while asktwo:
            ptwo = input("Player 2, Where would you like to move? ")

            if ptwo == 'exit':
                print("\nExiting Tic Tac Toe...\n")
                break

            try:
                p2 = [int(jj.strip()) for jj in ptwo.split(',')]
                if len(p2) != 2:
                    print("Incorrect input format. Try again.")
                    continue
            except:
                print("Invalid input Player 2. Please try again.")
                continue

            flag_two = CheckBounds(p2)
            if flag_two !=0: continue

            if p2 in used:
                print("Player 2, please select a number that has not been used.")
                continue

            used.append(p2)

            asktwo = False

        if ptwo == 'exit':
                break
        
        game[p2[0]-1][p2[1]-1] = 2
        
        winner = CheckTicTacToe(game)

        if winner != 0:
            print("\nPlayer", winner, "Wins! Congratulations")
            playing = False
            break
        # Anything above this and below the ask 1 sequence
        # is essentially repeat code.. Next section displays board and results

        # Take the gameboard list of 0 1 and 2's and convert it to x o and -'s
        # Then add them to a gameboard (empty list)
        dispgame = [''.join([str(item) for item in row]) for row in game]
        display = []
        for strings in dispgame:
            newstr = strings.replace('1','X')
            newstr = newstr.replace('2','O')
            newstr = newstr.replace('0', '-')
            display.append(newstr)

        ShowGame(display)
        
    # Display final resultant gameboard
    dispgame = [''.join([str(item) for item in row]) for row in game]
    display = []
    for strings in dispgame:
        newstr = strings.replace('1','X')
        newstr = newstr.replace('2','O')
        newstr = newstr.replace('0', '-')
        display.append(newstr)
    
    ShowGame(display)
    

if __name__ == '__main__':
    PlayTicTacToe()