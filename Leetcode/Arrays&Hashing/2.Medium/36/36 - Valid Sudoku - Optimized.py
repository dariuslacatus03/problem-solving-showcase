class Solution {
    public boolean isValidSudoku(char[][] board) {
        //Time complexity: O(1)
        
        for (int row = 0; row < 9; row++) {
            if (!isValidRow(board, row)) {
                return false;
            }
        }
        
        for (int col = 0; col < 9; col++) {
            if (!isValidColumn(board, col)) {
                return false;
            }
        }
        
        for (int row = 0; row < 9; row += 3) {
            for (int col = 0; col < 9; col += 3) {
                if (!isValidSubBox(board, row, col)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean isValidRow(char[][] board, int row) {
        boolean[] seen = new boolean[9];
        for (int col = 0; col < 9; col++) {
            if (!isValidCell(board[row][col], seen)) {
                return false;
            }
        }
        return true;
    }
    
    private boolean isValidColumn(char[][] board, int col) {
        boolean[] seen = new boolean[9];
        for (int row = 0; row < 9; row++) {
            if (!isValidCell(board[row][col], seen)) {
                return false;
            }
        }
        return true;
    }
    
    private boolean isValidSubBox(char[][] board, int startRow, int startCol) {
        boolean[] seen = new boolean[9];
        for (int row = startRow; row < startRow + 3; row++) {
            for (int col = startCol; col < startCol + 3; col++) {
                if (!isValidCell(board[row][col], seen)) {
                    return false;
                }
            }
        }
        return true;
    }
    
    private boolean isValidCell(char c, boolean[] seen) {
        if (c == '.') {
            return true;
        }
        int num = c - '1';
        if (seen[num]) {
            return false;
        }
        seen[num] = true;
        return true;
    }
}