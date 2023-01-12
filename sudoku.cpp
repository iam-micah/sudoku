// ===========================================================================
//   Purpose:
//       Solve a sudoku puzzle

//   Notes:
//       1. This program models the puzzle as a CSP
//       2. This program uses backtracking to solve the puzzle
//       3. The constraints we're using in this solution are: 
//          non duplication across rows, columns, and 3x3 grid boxes
// ===========================================================================

// ===========================================================================
//                             Library Includes
// ===========================================================================
# include<bits/stdc++.h>
# include<iostream>
# include<climits>
# include<cmath>
# include<algorithm>
# include<cstring>
# include<iomanip>
# include<vector>
# include<stack>
# include<queue>
# include<map>
# include<unordered_map>
# include<unordered_set>

# define fast ios_base::sync_with_stdio(false),cin.tie(NULL)

# define modValue 1e9 + 7
# define ll long long int

using namespace std;

//  is_valid
//     Purpose: verify our three constraints for any entry
//  Parameters: &board  -> reference to the sudoku board
//              int row -> row to be checked
//              int col -> column to be checked
//              char c  -> entry value 
//     Returns: bool
//
//       Notes: none
bool isValid(vector<vector<char>> &board, int row, int col, char c) {
    for (int i = 0; i < 9; i++) {
        // verify column constraint
        if (board[i][col] == c)
            return false;

        // verify row constraint
        if (board[row][i] == c)
            return false;

        // verify column constraint
        if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c)
            return false;
    }
    return true;
}

//  solve
//     Purpose: solve our sudoku grid
//  Parameters: &board  -> reference to the sudoku board to be solved
//
//     Returns: bool
//
//       Notes: solves the board recursively
bool solve(vector<vector<char>> &board) {
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            if (board[i][j] == '.') {
                for (char c = '1'; c <= '9'; c++) {
                    if (isValid(board, i, j, c)) {
                        board[i][j] = c;

                        if (solve(board))
                            return true;
                        else
                            board[i][j] = '.';
                    }
                }
                // implement backtracking here
                return false;
            }
        }
    }
    return true;
}

//  main
//     Purpose: driver code for sudoku
//  Parameters: none
//     Returns: 0 or 1 if program fails or succeeds
//
//       Notes: none
int main() {

    vector<vector<char>> board = {{'6', '.', '8', '7', '.', '2', '1', '.', '.'},
                                  {'4', '.', '.', '.', '1', '.', '.', '.', '2'},
                                  {'.', '2', '5', '4', '.', '.', '.', '.', '.'},
                                  {'7', '.', '1', '.', '8', '.', '4', '.', '5'},
                                  {'.', '8', '.', '.', '.', '.', '.', '7', '.'},
                                  {'5', '.', '9', '.', '6', '.', '3', '.', '1'},
                                  {'.', '.', '.', '.', '.', '6', '7', '5', '.'},
                                  {'2', '.', '.', '.', '9', '.', '.', '.', '8'},
                                  {'.', '.', '6', '8', '.', '5', '2', '.', '3'}};
    cout<<"Previous Sudoku Board"<<endl;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }

    solve(board);
    // print the board
    cout<<"\nSolved Sudoku Board"<<endl;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }


    return 0;
}






