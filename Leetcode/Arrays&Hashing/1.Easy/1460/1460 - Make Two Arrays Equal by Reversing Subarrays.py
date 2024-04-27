class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        //Time complexity: O(n)

        HashMap<Integer, Integer> targetCount = new HashMap<>();
        for (int i = 0; i < target.length; i++)
        {
            targetCount.put(
                target[i], 
                targetCount.getOrDefault(target[i], 0) + 1
                );
        }
        //HashMap<Integer, Integer> arrCount = new HashMap<>();
        for (int i = 0; i < arr.length; i++)
        {
            if (targetCount.containsKey(arr[i]))
            {
                if (targetCount.get(arr[i]) == 0)
                    return false;
                targetCount.put(
                    arr[i],
                    targetCount.get(arr[i]) - 1
                );
            }
            else
            {
                return false;
            }
        }
        return true;

    }
}