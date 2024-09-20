import re

def extract_emails(text, exclude_domain):
    # Create a regex pattern that excludes the specified domain
    pattern = r"\b[A-Za-z0-9._%+-]+@(?!{})[A-Za-z0-9.-]+\.[A-Za-z]{{2,}}\b".format(re.escape(exclude_domain))
    
    # Find all matching emails in the text
    emails = re.findall(pattern, text)
    return emails

# Sample text containing email addresses
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Specify the domain to exclude
exclude_domain = "exclude.com"

# Call the function and print the results
valid_emails = extract_emails(text, exclude_domain)
print("Extracted Emails:", valid_emails)
