public int numEquivDominoPairs(int[][] dominoes) {
        //Time complexity: O(n)
        Map<Integer, Integer> count = new HashMap<>();
        int res = 0;
        
        for (int[] d : dominoes) {
            int key = Math.min(d[0], d[1]) * 10 + Math.max(d[0], d[1]);
            count.put(key, count.getOrDefault(key, 0) + 1);
        }

        //Number of pairs of n dominoes <=> number of edges in connected graph with n nodes
        for (int value : count.values()) {
            res += value * (value - 1) / 2;
        }
        return res;
    }