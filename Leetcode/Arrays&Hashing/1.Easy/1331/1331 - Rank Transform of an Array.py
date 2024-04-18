class Solution {
    public int[] arrayRankTransform(int[] arr) {
        // Time complexity: O(n + n*logn)
        
        HashMap<Integer, Integer> ranks = new HashMap<>();
        
        int[] copyArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            copyArr[i] = arr[i];
        }

        Arrays.sort(copyArr);

        int i = 1;
        for (int num : copyArr)
        {
            if (!ranks.containsKey(num))
            {
                ranks.put(num, i);
                i++;
            }
        }

        for (i = 0; i < arr.length; i++)
        {
            arr[i] = ranks.get(arr[i]);
        }
        return arr;
    }
}