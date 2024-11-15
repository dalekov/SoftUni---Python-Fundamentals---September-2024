import re

line = input()

# Regex to match the title
title_regex = r'<title>(.*?)</title>'

# Extract the title
title_match = re.findall(title_regex, line)
title = title_match[0] if title_match else ""  # In case there's no title

# Remove the title tag and its content from the body
body_content = re.sub(r'<title>.*?</title>', '', line)

# Regex to remove all HTML tags
cleaned_text = re.sub(r'<[^>]+>', '', body_content)
content = cleaned_text.replace('\\n', '')

print(f"Title: {title}")
print(f"Content: {content}")
