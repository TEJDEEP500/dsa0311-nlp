import re

text = "Email me at example@gmail.com or admin@yahoo.com"

pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

# Search
match = re.search(pattern, text)

# Find all
matches = re.findall(pattern, text)

print("Search Result:", match.group() if match else "No match")
print("All Matches:", matches)























