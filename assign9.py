"""
Hasana Parker
CS51A: Assignment 9
April 4th, 2022
"""

# code for you class goes here
import copy


class NQueenState:
    """
    NQueensState
    """

    def __init__(self, size_side_board):
        """
        Constructor Function
        :param size_side_board: (int) Size of the board
        """
        self.size = size_side_board
        self.num_queens_placed = 0
        self.board = []

        for i in range(size_side_board):
            self.board.append([0] * self.size)

    def print_matrix(self):
        """
        This function works to format the matrix in matrix form, instead of a long list
        :return: (list) reformatted matrix
        """
        matrix = ""

        for row in self.board:
            matrix = matrix + str(row) + "\n"

        return matrix

    def __str__(self):
        """
        This function returns a string with the board size, number of queens placed, and the reformatted matrix
        :return: (str) sentence
        """

        return "Board size: " + str(self.size) + "\n" + \
               "Number of queens placed: " + str(self.num_queens_placed) + "\n" + \
               self.print_matrix()

    def is_valid_move(self, row, col):
        """
        This function is checking if a move is valid, meaning there is no conflict horizontally, vertically, or
        diagonally.
        :param row: (int) row of the matrix
        :param col: (int) col of the matrix
        :return: (bol) if the move is valid or not
        """
        # Checking that haven't already placed the size of the board queens on the board

        if self.num_queens_placed >= self.size:
            return False
        # Checking if there is a queen in that exact space
        elif self.board[row][col] == 1:
            return False

        elif self.is_diagonal_1(row, col):  # if this returns True, return False
            return False

        elif self.is_other_diagonal_1(row, col):
            return False

        # Checking if there is a queen in the row/ horizontally
        for c in range(len(self.board)):  # Iterating through the row
            if self.board[row][c] == 1:
                return False

        # Checking if there is a queen in the column/ horizontally
        for r in range(len(self.board)):
            if self.board[r][col] == 1:
                return False

        return True

    # Function to check if row and column is in bounds
    def in_bounds(self, row, col):  # also do I have to check to see if the row and col is less than zero
        """
        This function is working to check if the row and column are within the bounds of the board.
        :param row: (int) row of the matrix
        :param col: (int) column of the matrix
        :return: (bol) if the row and column are in the bounds
        """
        return 0 <= row < self.size and 0 <= col < self.size

    #  Helper function Checking if there is a queen in the first diagonal

    def is_diagonal_1(self, row, col):
        """
        This function is working to check the first diagonal of the matrix and make sure there is no queen there

        :param row: (int) row of the matrix
        :param col: (int) col of the matrix
        :return: (bol) true if there is a queen and false if there is no queen
        """
        for i in range(1, self.size):
            if self.in_bounds(row - i, col - i) and self.board[row - i][col - i] == 1:
                return True

            elif self.in_bounds(row + i, col + i) and self.board[row + i][col + i] == 1:
                return True

        return False

    # Helper function Checking if there is a queen in the second diagonal, returns true if there is a queen present

    def is_other_diagonal_1(self, row, col):
        """
        This function is working to check the second diagonal of the matrix and make sure there is no queen there

        :param row: (int) row of the matrix
        :param col: (int) column of the matrix
        :return: (bol) true if there is a queen and false if there is no queen
        """
        for i in range(1, self.size):
            if self.in_bounds(row + i, col - i) and self.board[row + i][col - i] == 1:
                return True

            elif self.in_bounds(row - i, col + i) and self.board[row - i][col + i] == 1:
                return True

        return False

    def add_queen(self, row, col):
        """
        This function is working to add a queen to the matrix, change a 0 to a 1
        :param row: (int) row of matrix
        :param col: (int) column of matrix
        :return: (list) a new matrix with a queen added to it
        """

        new_state = copy.deepcopy(self)

        if new_state.in_bounds(row, col):
            new_state.board[row][col] = 1
            new_state.num_queens_placed += 1

        return new_state

    def next_states(self):
        """
        This function is working to create lists of valid state matrices

        :return: (list) of valid states
        """
        valid_states_list = []

        # self.num_queens_placed this will dictate the row we are on currently
        # Need to iterate through the columns on that row and check with of the [row][col] to see if it's a valid move

        for c in range(self.size):
            if self.is_valid_move(self.num_queens_placed, c):
                valid_states_list.append(self.add_queen(self.num_queens_placed, c))

        return valid_states_list

    def is_goal(self):
        """
        This function is working to check if the goal state has been reached, if there are the same number of queens
        placed as the size of the board.
        :return: (bol) true if it is a goal state and false if not
        """

        return self.size == self.num_queens_placed


def dfs(state):
    """Recursive depth first search implementation
    
    Input:
    Takes as input a state.  The state class MUST have the following
    returned True that can be reached from the input state.
    """

    # if the current state is a goal state, then return it in a list
    if state.is_goal():
        return [state]
    else:
        # else, recurse on the possible next states
        result = []

        for s in state.next_states():
            # append all the s
            result += dfs(s)

        return result


# uncomment this code when you're ready to test it out


# start_state = NQueenState(8)
#
# solutions = dfs(start_state)
# print("There were " + str(len(solutions)) + " solutions.\n")
#
# if len(solutions) > 0:
#     print(solutions[0])
