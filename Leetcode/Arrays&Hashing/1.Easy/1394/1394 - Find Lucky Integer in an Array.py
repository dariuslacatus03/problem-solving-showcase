class Solution {
    public int findLucky(int[] arr) {
        // Time complexity: O(n)
        
        HashMap<Integer, Integer> counter = new HashMap<>();
        for (int num : arr)
        {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        int max = -1;
        for (Integer key : counter.keySet())
        {
            if (counter.get(key) == key)
            {
                if (key > max)
                    max = key;
            }
        }

        return max;

    }
}