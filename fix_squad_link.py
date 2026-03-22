import os

def fix_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    bad_squad = "runNavTo('fitquest_screen16.html')\">\n        <span class=\"drawer-icon\">⚡</span><span>Squad Compatibility</span>"
    good_squad = "runNavTo('fitquest_screen15.html')\">\n        <span class=\"drawer-icon\">⚡</span><span>Squad Compatibility</span>"
    
    if bad_squad in content:
        content = content.replace(bad_squad, good_squad)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")

for i in range(1, 22):
    fn = f"fitquest_screen{i}.html"
    if os.path.exists(fn):
        fix_file(fn)
print("Finished Squad Link Update")
