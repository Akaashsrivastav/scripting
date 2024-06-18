'''import re

example = "Here we are trying to learn about regular expression"
pattern = r"are"

search = re.search(pattern, example)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")'''



'''import re

text = "Here we are trying to learn about regular expression"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")'''



'''import re

text = "Here we are trying to learn about regular expression"
pattern = r"trying"

replacement = "learning"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)'''



import re

text = "India,WI,USA,Canada,Japan"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)
