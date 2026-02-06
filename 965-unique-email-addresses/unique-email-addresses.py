class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        
        for mail in emails:
            name, domain = mail.split('@')
            name = name.split('+')[0].replace('.','')
            uniqueEmails.add(name + '@' + domain)

        return len(uniqueEmails)
        