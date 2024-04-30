class Solution {
    public List<String> commonChars(String[] words) {
        // Time complexity: O(n)
        // n - number of characters in words
        List<String> res = new ArrayList<>();
        int[] min_freq = new int[26];
        Arrays.fill(min_freq, Integer.MAX_VALUE);
        for (String word : words)
        {
            int[] curr_freq = new int[26];
            Arrays.fill(curr_freq, 0);
            //Check frequence of each letter in word
            for(int i = 0; i < word.length(); i++)
            {
                char c = word.charAt(i);
                curr_freq[c-'a']++;
            }
            //Update min_freq
            for(int i = 0; i < 26; i++)
            {
                min_freq[i] = Math.min(min_freq[i], curr_freq[i]);
            }
        }
        //At this point, in min freq we have all the common letters and their
        //frequence of our words.
        //Append the letters in res
        for(int i = 0; i < 26; i++)
        {
            while(min_freq[i] > 0)
            {
                res.add("" + (char)(i+'a'));
                min_freq[i]--;
            }
        }
        return res;
    }
}