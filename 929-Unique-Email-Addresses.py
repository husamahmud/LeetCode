class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsSet = set()

        for email in emails: 
            splitted = email.split('@')
            local = splitted[0].split('+')[0].replace('.','')
            domain = splitted[1]
            emailsSet.add((local, domain))

        return len(emailsSet)