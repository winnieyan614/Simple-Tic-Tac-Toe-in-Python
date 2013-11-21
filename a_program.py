#Tic-Tac-Toe Game
def main():
	#display instructions for the game
    instructions ()
	
	#Tic-Tac-Toe grid
    display = [[" ","|"," ","|"," "],["-","+","-","+","-"],[" ","|"," ","|"," "],["-","+","-","+","-"],[" ","|"," ","|"," "]]
    
	#choice to store user preference for X or O and used for rotating turns between users
	choice = input ("Would you like to be X or O? (in quotes)")
	
	#setting up values for rows and columns 
    transRow = {'top':0,
                'middle':2,
                'bottom':4}
    transColumn = {'left':0,
                   'center':2,
                   'right':4}
				   
	#win boolean value
    win = False
	
	#counter
    i = 1
    while ((i<10) and win == False):
        move(display,choice,transRow,transColumn)
        if(choice == display[0][0] and choice == display[0][2] and choice == display[0][4]):
            print "You won!"
            win=True
        elif(choice == display[2][0]and choice == display[2][2] and choice == display[2][4]):
            print "You won!"
            win=True
        elif(choice == display[4][0]and choice == display[4][2]and choice ==  display[4][4]):
            print "You won!"
            win=True
        elif(choice == display[0][2]and choice == display[2][2]and choice ==  display[4][2]):
            print "You won!"
            win=True
        elif(choice == display[0][4]and choice == display[2][4]and choice == display[4][4]):
            print "You won!"
            win=True
        elif(choice == display[0][0]and choice == display[2][2]and choice == display[4][4]):
            print "You won!"
            win=True
        elif(choice == display[0][4]and choice == display[2][2]and choice == display[4][0]):
            print "You won!"
            win=True
        elif(choice == display[0][0]and choice == display[2][0]and choice == display[4][0]):
            print "You won!"
            win=True
        if (i > 8):
            print "It's a TIE!"

        if(choice == 'X'):
            choice = 'O'
            print "Player O's turn" 
        else:
            choice = "X"
            print "Player X's turn"

        originalGrid(display)
        i = i+1

#getting and displaying user's moves
def move(display,choice,transRow,transColumn):
    if (choice == "X" or "O"):
        rowMove= input ("Please select a row (top/middle/bottom) (in quotes)")
        columnMove= input ("Please select a row (left/center/right) (in quotes)")    
    else:
        print ("That is a invalid input, only X or O in double quotes")    
    r = transRow[rowMove]
    c = transColumn[columnMove]
    if (rowMove not in transRow or columnMove not in transColumn):
        print ("That is not a valid input!")
    elif (display[r][c]=="X" or display[r][c]=="O"):
        print ("The spot is already taken")
        display[r][c]=" "
    else:
        display[r][c]=choice
        
def originalGrid(display):
    i=0
    while(i<5):
        j=0
        while(j<5):
            print display[i][j],
            j=j+1
        print
        i=i+1
    
def instructions():
    print ("Wlecome to TIC TAC TOE! :)")
    
