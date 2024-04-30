class Solution {
    public List<Integer> majorityElement(int[] nums) {
        //Time complexity: O(n)

        HashMap<Integer, Integer> freq = new HashMap<>();
        int numsLen = nums.length;
        List<Integer> res = new ArrayList<>();
        for (int num : nums)
        {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
            if (freq.get(num) > numsLen / 3)
            {
                res.add(num);
                freq.put(num, -1);
            } 
        }
        return res;
    }
}