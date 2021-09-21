def CheckTicTacToe(game):
    '''
    function returns 0, 1, or 2... 
    0 = tie, 1 = player1 victory, 2 = player2 victory.

    game - variable representing gameboard as a list of 3 lists
     '''

    winner = 0

    row1 = game[0]
    row2 = game[1]
    row3 = game[2]

    # check diagonal
    if row1[0] == row2[1] and row2[1] == row3[2] and row1[0] != 0:
        winner = row1[0]
        #print("Diagonal1")
    elif row1[2] == row2[1] and row2[1] == row3[0] and row1[2] != 0:
        winner = row1[2]
        #print("Diagonal2")

    # check vertical
    for spots in range(0,3):
        if row1[spots] == row2[spots] and row2[spots] == row3[spots] and row1[spots] !=0:
            winner = row1[spots]
            #print("Vertical")
    

    # Check horizontal
    for rows in game:
        if sum(rows) == 3 and 0 not in rows:
            winner = 1
            #print("Horizontal")
        elif sum(rows) == 6:
            winner = 2
            #print("Horizontal")
        

    # Check tie
    if winner == 0:
        tie = 0
        for rows in game:
            if 0 not in rows:
                tie+=1
            if tie == 3:
                #print("CAT")
                winner = 999
    
    return winner

if __name__ == '__main__':
    # Run file test if run as main file
    game = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]
    
    winner_is_2 = [[2, 0, 1],
    [2, 1, 0],
    [2, 1, 1]]### change bottom left to 2

    winner_is_1 = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 1]]
    
    winner_is_also_1 = [[0, 1, 0],
    [2, 1, 0],
    [2, 1, 1]]
    
    no_winner = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 2]]

    also_no_winner  = [[1, 2, 0],
    [2, 1, 0],
    [2, 1, 0]]

    diag2case = [[1, 0, 2],
    [1, 2, 0],
    [2, 1, 0]]

    tiecase = [[1, 2, 1],
    [1, 2, 2],
    [2, 1, 1]]

    test1 = CheckTicTacToe(game)
    test2 = CheckTicTacToe(winner_is_2)
    test3 = CheckTicTacToe(winner_is_1)
    test4 = CheckTicTacToe(winner_is_also_1)
    test5 = CheckTicTacToe(no_winner)
    test6 = CheckTicTacToe(also_no_winner)
    test7 = CheckTicTacToe(diag2case)
    test8 = CheckTicTacToe(tiecase)
    test = [test1, test2, test3, test4, test5, test6, test7, test8]
    expected = [1,2,1,1,0,0,2,999]

    if test == expected:
        print("All cases passed")
    else:
        print("Case failed")
# If you want to troubleshoot, uncomment directions of wins
