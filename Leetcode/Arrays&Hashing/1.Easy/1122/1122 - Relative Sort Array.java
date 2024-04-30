class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        // Time complexity: O(n*m)
        // n - length of arr1
        // m - length of arr2
        int curr_pos = 0;
        int aux;
        for (int arr2_num : arr2)
        {
            for (int arr1_it = 0; arr1_it < arr1.length; arr1_it++)
            {
                if (arr1[arr1_it] == arr2_num)
                {
                    aux = arr1[curr_pos];
                    arr1[curr_pos] = arr1[arr1_it];
                    arr1[arr1_it] = aux;
                    curr_pos++;
                }
            }
        }
        if (curr_pos < arr1.length)
        {
            int sorted = 0;
            while (sorted == 0)
            {
                sorted = 1;
                for (int i = curr_pos; i < arr1.length - 1; i++)
                {
                    if (arr1[i] > arr1[i + 1])
                    {
                        aux = arr1[i];
                        arr1[i] = arr1[i + 1];
                        arr1[i + 1] = aux;
                        sorted = 0;
                    }
                }
            }
        }
        return arr1;
    }
}