class Solution {
    public int longestConsecutive(int[] nums) {
        //Time complexity: O(n logn)
        
        if (nums.length == 0)
            return 0;
        Arrays.sort(nums);
        int maxLen = -1;
        int count = 1;
        int lastNum = nums[0];
        for (int i = 1; i < nums.length; i++)
        {
            if (nums[i] != lastNum + 1 && nums[i] != lastNum)
            {
                if (count > maxLen)
                {
                    maxLen = count;
                }
                count = 1;
            }
            else if (nums[i] != lastNum)
            {
                count++;
            }
            lastNum = nums[i];
        }
        if (count > maxLen)
            maxLen = count;
        return maxLen;
    }
}