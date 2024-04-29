class Solution {
    public void setZeroes(int[][] matrix) {
        //Time complexity: O(n*m)

        int rowsLength = matrix.length;
        int colsLength = matrix[0].length;
        boolean firstRow = false;
        boolean firstColumn = false;
        //Mark rows and columns
        for (int i = 0; i < rowsLength; i++)
            for (int j = 0; j < colsLength; j++)
            {
                if(matrix[i][j] == 0)
                {
                    if (i == 0)
                        firstRow = true;
                    if (j == 0)
                        firstColumn = true;
                    if (i != 0 && j != 0)
                    {
                        matrix[i][0] = 0;
                        matrix[0][j] = 0;
                    }
                }
            }
        
        //Transform rows without first one
        for(int i = 1; i < rowsLength; i++)
        {
            if(matrix[i][0] == 0)
            {
                for(int j = 0; j < colsLength; j++)
                    matrix[i][j] = 0;
            }
        }
        //Transform columns without first one
        for (int j = 1; j < colsLength; j++)
        {
            if (matrix[0][j] == 0)
            {
                for (int i = 0; i < rowsLength; i++)
                    matrix[i][j] = 0;
            }
        }
        //Transform first row or column if necessary
        if (firstRow)
        {
            for(int j = 0; j < colsLength; j++)
                matrix[0][j] = 0;
        }
        if (firstColumn)
        {
            for (int i = 0; i < rowsLength; i++)
                matrix[i][0] = 0;
        }
    }
}