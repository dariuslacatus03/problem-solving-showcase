class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //Time complexity: O(n * m logm)
        //n - number of words
        //m - length of each word
        
        //List<List<String>> res = new ArrayList<>();
        HashMap<String, List<String>> anagrams = new HashMap<>();
        for (String word : strs)
        {
            char[] sortedWordChar = word.toCharArray();
            Arrays.sort(sortedWordChar);
            String sortedWord = new String(sortedWordChar);
            List<String> anagramGroup = anagrams.getOrDefault(sortedWord, new ArrayList<>());
            anagramGroup.add(word);
            anagrams.put(sortedWord, anagramGroup);
        }
        // for (String key : anagrams.keySet())
        // {
        //     List<String> anagramWords = new ArrayList<>();
        //     for (String anagram : anagrams.get(key))
        //     {
        //         anagramWords.add(anagram);
        //     }
        //     res.add(anagramWords);
        // }
        // return res
        return new ArrayList<>(anagrams.values());
    }
}