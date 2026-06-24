#include <iostream>

using namespace std;

// Display the board
void displayBoard(char board[3][3]) {
    cout << "\n";
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            cout << " " << board[i][j] << " ";
            if(j < 2) cout << "|";
        }
        cout << (i < 2 ? "\n---|---|---\n" : "\n");
    }
    cout << "\n";
}

// Check if a player has won
bool checkWin(char board[3][3], char p) {
    for(int i = 0; i < 3; i++) {
        // Rows and Columns
        if((board[i][0] == p && board[i][1] == p && board[i][2] == p) ||
           (board[0][i] == p && board[1][i] == p && board[2][i] == p)) return true;
    }
    // Diagonals
    return (board[0][0] == p && board[1][1] == p && board[2][2] == p) ||
           (board[0][2] == p && board[1][1] == p && board[2][0] == p);
}

// Check if board is full (Draw)
bool isFull(char board[3][3]) {
    for(int i = 0; i < 3; i++)
        for(int j = 0; j < 3; j++)
            if(board[i][j] == ' ') return false;
    return true;
}

int main() {
    char board[3][3];
    char currentPlayer;
    char playAgain;

    do {
        // Initialize/Reset Board
        for(int i=0; i<3; i++) for(int j=0; j<3; j++) board[i][j] = ' ';
        currentPlayer = 'X';
        bool gameOver = false;

        cout << "--- Tic-Tac-Toe ---" << endl;

        while(!gameOver) {
            displayBoard(board);
            int r, c;
            cout << "Player " << currentPlayer << ", enter row and column (0-2): ";
            cin >> r >> c;

            if(r >= 0 && r < 3 && c >= 0 && c < 3 && board[r][c] == ' ') {
                board[r][c] = currentPlayer;
                
                if(checkWin(board, currentPlayer)) {
                    displayBoard(board);
                    cout << "Player " << currentPlayer << " wins!" << endl;
                    gameOver = true;
                } else if(isFull(board)) {
                    displayBoard(board);
                    cout << "It's a draw!" << endl;
                    gameOver = true;
                } else {
                    currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
                }
            } else {
                cout << "Invalid move! Try again." << endl;
            }
        }
        cout << "Play again? (y/n): ";
        cin >> playAgain;
    } while(playAgain == 'y' || playAgain == 'Y');

    return 0;
}