# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 02:51:31 2017

@author: qn_li
"""

###Tic Tac Toe Game
def display():
    '''
    display the whole game board
    '''
    global board
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('---------')
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('---------')
    print(board[6]+' | '+board[7]+' | '+board[8])

def win():
    '''
    judge whether the situation on the game board shows the winner
    '''
    global board
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]=='x' or board[i]==board[i+1]==board[i+2]=='o':
            return(True)
    for j in range(0,3):
        if board[j]==board[j+3]==board[j+6]=='x' or board[j]==board[j+1]==board[j+2]=='o':
            return(True)
    if board[0]==board[4]==board[8]=='x' or board[2]==board[4]==board[6]=='x':
        return(True)
    if board[0]==board[4]==board[8]=='o' or board[2]==board[4]==board[6]=='o':
        return(True)
    return(False)

def play():
    global board
    board= [" "]*9
    s=set([])
    while(len(s)<8):
        p1=int(input('Player1:'))
        # if the place is occupied, the player should choose another place
        while(p1 in s):
            print('Choose another place!')
            p1=int(input('Player1:'))
        board[p1]='x'
        display()
        if win():
            return('Player1 Wins!')
        s.add(p1)
        p2=int(input('Player2:'))
        while(p2 in s):
            print('Choose another place!')
            p2=int(input('Player2:'))
        board[p2]='o'
        display()
        if win():
            return('Player2 Wins!')
        s.add(p2)
    return('Tie')

play()