#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

#define computer 0
#define player 1
#define side 3
#define Cmove 'X'
#define Pmove 'O' 

/*Lets first make a board for tic tac toe
 *after the board, we initialise the board
 */

void showBoard(char board[][side])
{

    printf("\n\n\tWelcome to Tic-Tac-Toe - By Wahid");
    printf("\n\tYou are playing as O");

    printf("\t\t\t %c | %c | %c \n", board[0][0], board[0][1], board[0][2]);
    printf("\t\t\t-----------\n");
    printf("\t\t\t %c | %c | %c \n", board[1][0], board[1][1], board[1][2]);
    printf("\t\t\t-----------\n");
    printf("\t\t\t %c | %c | %c \n\n", board[2][0], board[2][1], board[2][2]);

}  
void showInstructions()
{
    printf("Choose a value from 1-9 to mark on the board");

    printf("\t\t\n 1 | 2 | 3 \n");
    printf("\t\t\n ----------\n");
    printf("\t\t\n 4 | 5 | 6 \n");
    printf("\t\t\n ----------\n");
    printf("\t\t\n 7 | 8 | 9 \n\n");

}
void initialise(char board[][side])
{
    for (int i=0; i<side; i++)
    {
        for(int j=0; j<side; j++)
        board[i][j] = ' ';
    }
}

//declare conditional statement to choose winner 
void getWinner(int choice)
{
    if(choice == computer)
        printf("Computer has Won!");
    else
        printf("Player has won!");
}

//check winning conditions
bool row(char board[][side])
{
    for(int i=0; i<side; i++)
    {
        if(board[i][0] == board[i][1] && 
           board[i][1] == board[i][2] &&
           board[i][0]  != ' ')
        return (true);
    }
    return (false);
}
bool column(char board[][side])
{
    for(int i=0; i<side; i++)
    {
        if(board[0][i] == board[1][i] &&
           board[1][i] == board[2][i] &&
           board[0][i] != ' ')
           return (true);  
    }
    return (false);
}
bool diagonal(char board[][side])
{
    for (int i = 0; i < side; i++)
    {
        if (board[0][0] == board[1][1] &&
            board[1][1] == board[2][2] &&
            board[0][0] != ' ')
           return (true);

        if (board[0][2] == board[1][1] &&
            board[1][1] == board[2][0] &&
            board[0][2] != ' ')
           return (true);
    }
    return (false);
}

bool gameOver(char board[][side])
{
    return(row(board) || column(board) || diagonal(board));
}

//algorithm
