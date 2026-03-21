import os

def fix_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The lines to fix inside the drawer-nav block
    bad_hero = "runNavTo('fitquest_screen14.html')\">\n        <span class=\"drawer-icon\">🛡️</span><span>My Hero Profile</span>"
    good_hero = "runNavTo('fitquest_screen13.html')\">\n        <span class=\"drawer-icon\">🛡️</span><span>My Hero Profile</span>"

    bad_hall = "runNavTo('fitquest_screen13.html')\">\n        <span class=\"drawer-icon\">🏛️</span><span>Hall of Heroes</span>"
    good_hall = "runNavTo('fitquest_screen14.html')\">\n        <span class=\"drawer-icon\">🏛️</span><span>Hall of Heroes</span>"

    changed = False
    if bad_hero in content:
        content = content.replace(bad_hero, good_hero)
        changed = True
    if bad_hall in content:
        content = content.replace(bad_hall, good_hall)
        changed = True
        
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed navigation routes in {file_path}")

try:
    for i in range(1, 14):
        fn = f"fitquest_screen{i}.html"
        if os.path.exists(fn):
            fix_file(fn)
    print("Done executing link fix script")
except Exception as e:
    print("Error:", e)
