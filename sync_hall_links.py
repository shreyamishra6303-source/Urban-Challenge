import os

def update_hall_link(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to find: Hall of Heroes link
    # We previous had varieties pointing to 13, 14, or 16 (in my test screen 15).
    # Logic: Search for the drawer link with "Hall of Heroes" and update its runNavTo or onclick to fitquest_screen16.html
    
    # Target search string fragment: 
    # <div class="drawer-link" onclick="runNavTo('fitquest_screenXX.html')">
    #   <span class="drawer-icon">🏛️</span><span>Hall of Heroes</span>
    # </div>
    
    import re
    
    # Generic regex to swap whatever screen was there with 16 for the Hall of Heroes entry
    pattern = r'(onclick="runNavTo\(\'fitquest_screen)(\d+)(\.html\'\)">\s*<span class="drawer-icon">🏛️</span><span>Hall of Heroes</span>)'
    replacement = r'\1 16\3'
    
    # Clean up spaces potentially added by regex group
    new_content = re.sub(pattern, lambda m: f'onclick="runNavTo(\'fitquest_screen16.html\')">{m.group(3)}', content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated Hall of Heroes link in {file_path}")
    else:
        # Try a second pattern just in case of different formatting
        # Maybe it's not runNavTo but navTo or something else
        pattern2 = r'(\'fitquest_screen)(\d+)(\.html\')(\s*>.*Hall of Heroes)'
        if "Hall of Heroes" in content:
            new_content = re.sub(r'\'fitquest_screen\d+\.html\'(?=.*Hall of Heroes)', "'fitquest_screen16.html'", content)
            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated Hall of Heroes link (fallback) in {file_path}")

try:
    for i in range(1, 16):
        fn = f"fitquest_screen{i}.html"
        if os.path.exists(fn):
            update_hall_link(fn)
    print("Link synchronization complete")
except Exception as e:
    print("Error:", e)
