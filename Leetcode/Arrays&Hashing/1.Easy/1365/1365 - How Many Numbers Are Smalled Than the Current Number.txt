class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        // Time complexity: O(n)

        int[] copyNums = new int[nums.length];
        for (int i = 0; i < nums.length; i++)
        {
            copyNums[i] = nums[i];
        }
        Arrays.sort(copyNums);
        HashMap<Integer, Integer> counts = new HashMap<>();
        
        int moreThan = 0;
        int i = 0;
        int lastEl = -1;
        while (i < copyNums.length)
        {
            if (copyNums[i] != lastEl)
            {
                counts.put(copyNums[i], i);
                lastEl = copyNums[i];
            }
            i++;
        }
        for (i = 0; i < nums.length; i++)
        {
            nums[i] = counts.get(nums[i]);
        }
        return nums;
    }
}