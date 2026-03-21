import os
import re

def update_feed_link(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Generic regex to swap whatever screen was there with 17 for The Arena Feed entry
    # Content example: 
    # <div class="drawer-link" onclick="runNavTo('fitquest_screen15.html')">
    #   <span class="drawer-icon">📰</span><span>The Arena Feed</span>
    # </div>
    
    pattern = r'(onclick="runNavTo\(\'fitquest_screen)(\d+)(\.html\'\)">\s*<span class="drawer-icon">📰</span><span>The Arena Feed</span>)'
    # We want to change the d+ to 17
    
    new_content = re.sub(pattern, lambda m: f'onclick="runNavTo(\'fitquest_screen17.html\')">{m.group(3)}', content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated Arena Feed link in {file_path}")
    else:
        # Fallback for manual button/link text matches
        new_content = re.sub(r'\'fitquest_screen\d+\.html\'(?=.*The Arena Feed)', "'fitquest_screen17.html'", content)
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated Arena Feed link (fallback) in {file_path}")

try:
    for i in range(1, 16):
        fn = f"fitquest_screen{i}.html"
        if os.path.exists(fn):
            update_feed_link(fn)
    # Also update screen 16 if it exists (which it does)
    if os.path.exists("fitquest_screen16.html"):
        update_feed_link("fitquest_screen16.html")
        
    print("Link synchronization for Arena Feed complete")
except Exception as e:
    print("Error:", e)
