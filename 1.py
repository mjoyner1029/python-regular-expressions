import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
exclude_domain = "exclude.com"

# Use f-string to correctly format the regex pattern
pattern = rf'\b[A-Za-z0-9._%+-]+@(?!{re.escape(exclude_domain})\b[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Find all email addresses except those from 'exclude_domain'
emails = re.findall(pattern, text)

print(emails)
