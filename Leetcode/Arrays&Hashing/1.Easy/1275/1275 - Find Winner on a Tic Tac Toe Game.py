public class Solution {
    public String tictactoe(int[][] moves) {
        // Time complexity: O(1)

        char[][] board = new char[3][3];
        
        for (int i = 0; i < moves.length; i++) {
            int row = moves[i][0];
            int col = moves[i][1];
            char player = (i % 2 == 0) ? 'A' : 'B';
            board[row][col] = player;
        }
        
        if (checkWinningCondition(board, 'A')) return "A";
        if (checkWinningCondition(board, 'B')) return "B";
        
        if (moves.length < 9) return "Pending";
        return "Draw";
    }
    
    private boolean checkWinningCondition(char[][] board, char player) {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == player && board[i][1] == player && board[i][2] == player) {
                return true;
            }
        }
        
        for (int j = 0; j < 3; j++) {
            if (board[0][j] == player && board[1][j] == player && board[2][j] == player) {
                return true;
            }
        }
        
        if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
            (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {
            return true;
        }
        
        return false;
    }
}