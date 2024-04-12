class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        #Time complexity: O(n)
        # n - number of characters in emails

        res = {}
        for email in emails:
            aux = ""
            skip = 0
            found = 0
            for char in email:
                if char == "." and found == 0:
                    continue
                elif char == "+" and found == 0:
                    skip = 1
                elif char == "@":
                    aux += char
                    found = 1
                    skip = 0
                elif skip == 1:
                    continue
                else:
                    aux += char
            print(aux)
            res[aux] = 1

        print(res)
        return len(res)
            