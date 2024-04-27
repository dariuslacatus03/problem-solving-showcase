class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        //Time complexity: O(n)
        
        int[] count = new int[1001];
        for (int i = 0; i < target.length; i++){
            count[arr[i]]++;
            count[target[i]]--;
        }

        for (int i = 0; i < 1001; i++){
            if (count[i] != 0){
                return false;
            }
        }

        return true;
    }
}