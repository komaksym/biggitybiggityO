# Time:  O(n * l)

class Solution(object):
    def numUniqueEmails(self, emails):
        
        def convert(email):
            name, domain = email.split('@')
            name = name[:name.index('+')]
            return "".join(["".join(name.split(".")), '@', domain])

        lookup = set()
        for email in emails:
            lookup.add(convert(email))
        return len(lookup)
  
