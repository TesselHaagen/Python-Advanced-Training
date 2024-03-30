import re

with open('emails.txt', 'r') as f:
    text = f.readline() #readlines()
    
email_adressen = re.findall(r"\S+@\S+\.(?:com|net|nl)\b", text)

print(email_adressen)