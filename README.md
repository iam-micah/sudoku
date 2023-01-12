# sudoku
Sudoku solver using backtracking. Implemented in C++ and Python

PROGRAM PURPOSE:
---------------
    This program solves sudoku puzzles as constraint satisfaction problems
    (CSP). The object of the puzzle is to place the numbers 1 to 9 in the
    empty cells so that each row, each column and each 3 x 3region contains
    the same number only once. The three constraints used in this solution 
    are no simultaneous duplication in rows, columns, or 3x3 grid boxes

    Note that I implemented the solution in two different languages: 
    python and c++
    You can choose to run whichever language you're comfortable with

HOW TO RUN:
-----------------------
    For the python implementation:
    Type "py newsudoku.py ": this will use the latest version of python 
    installed on your computer to run the code.

    For the c++ implementation: 
    First simply compile with: "g++ -o solution.exe sudoku.cpp"
    This is not a complex program to run, but if you want more control, you can
    use different flags to aid your program
    Run: 
    After compilation is successful, type: "./solution.exe" to run the program

    For both implementations, you be in the file location if you're running 
    from the terminal
