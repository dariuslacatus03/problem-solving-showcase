class Solution {
    public String destCity(List<List<String>> paths) {
        // Time complexity: O(n)
        
        HashMap<String, String> hashPaths = new HashMap<>();
        for (List<String> path : paths)
        {
            hashPaths.put(path.get(0), path.get(1));
        }
        for (List<String> path : paths)
        {
            if (hashPaths.containsKey(path.get(1)) == false)
                return path.get(1);
        }
        return "";
    }
}