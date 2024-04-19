class Solution {
    public boolean checkIfExist(int[] arr) {
        // Time complexity: O(n)

        HashSet<Integer> nums = new HashSet<>();
        for (int i = 0; i < arr.length; i++)
        {
            if (nums.contains(arr[i] * 2))
                return true;

            if (arr[i] % 2 == 0 && nums.contains(arr[i] / 2))
                return true;
            nums.add(arr[i]);

        }
        return false;
    }
}