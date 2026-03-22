import os
import re
import glob

# Step 1: Rename files from N=30 down to 3
for i in range(30, 2, -1):
    old_name = f"fitquest_screen{i}.html"
    new_name = f"fitquest_screen{i+1}.html"
    if os.path.exists(old_name):
        print(f"Renaming {old_name} to {new_name}")
        os.rename(old_name, new_name)

# Step 2: Update contents in all fitquest_screen*.html
files = glob.glob("fitquest_screen*.html")

def replace_link(match):
    num = int(match.group(1))
    if num >= 3:
        return f"fitquest_screen{num+1}.html"
    return match.group(0)

def replace_text(match):
    num = int(match.group(2))
    if num >= 3:
        return f"{match.group(1)}{num+1}{match.group(3)}"
    return match.group(0)

def replace_screen_text(match):
    num = int(match.group(1))
    if num >= 3:
        return f"Screen {num+1} of"
    return match.group(0)

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace fitquest_screenX.html
    new_content = re.sub(r'fitquest_screen(\d+)\.html', replace_link, content)
    
    # Replace "Screen X of"
    new_content = re.sub(r'Screen (\d+) of', replace_screen_text, new_content)
    
    if new_content != content:
        print(f"Updating references in {f}")
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("Done shifting screens and references.")
