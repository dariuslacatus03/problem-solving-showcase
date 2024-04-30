class Solution {
    public int countCharacters(String[] words, String chars) {
        // Time complexity: O(n + m)
        // n - length of characters in words,
        // m - length of chars
        
        HashMap<Character, Integer> freq = new HashMap<>();
        for (int i = 0; i < chars.length(); i++)
        {
            freq.put(chars.charAt(i), freq.getOrDefault(chars.charAt(i), 0) + 1);
        }
        boolean valid;
        int i;
        int totalLength = 0;
        char c;
        HashMap<Character, Integer> currWordFreq = new HashMap<>();
        for (String word : words)
        {
            i = 0;
            valid = true;
            currWordFreq.clear();
            while (i < word.length() && valid == true)
            {
                c = word.charAt(i);
                if (freq.getOrDefault(c, 0) == 0)
                {
                    valid = false;
                }
                else
                {
                    currWordFreq.put(c, currWordFreq.getOrDefault(c, 0) + 1);
                    if (freq.get(c) < currWordFreq.get(c))
                    {
                        valid = false;
                    }
                }
                i++;
            }
            if (valid == true)
            {
                totalLength += word.length();
            }
        }
        return totalLength;
    }
}