class Solution(object):
    def numUniqueEmails(self, emails):
        res = set()
        for email in emails:
            name, dome = email.split('@')
            name = name.split('+')[0]
            name = name.replace('.', '')
            res.add(name + '@' + dome)
        return len(res)