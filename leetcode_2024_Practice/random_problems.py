''' 929. Unique email addresses '''

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def numUniqueEmails(emails):
    updated_emails = set()
    for email in emails:
        name, domain = email.split('@')
        name = name.split('+')[0].replace('.', '')
        
        new_email = name + '@' + domain
        updated_emails.add(new_email)

    return len(updated_emails)

print(numUniqueEmails(emails))

   
    

            
   
        