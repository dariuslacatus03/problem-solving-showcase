class Solution {
    public boolean isValidSudoku(char[][] board) {
        //Time complexity: O(1)
        Set seen = new HashSet();
        char number;
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                number = board[i][j];
                if (number != '.')
                {
                    if (
                        seen.add(number + " in row " + i) == false ||
                        seen.add(number + " in column " + j) == false ||
                        seen.add(number + " in block " + i/3 + j/3) == false
                    )
                    {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}