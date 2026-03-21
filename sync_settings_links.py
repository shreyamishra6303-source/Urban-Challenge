import os
import re

def update_settings_link(directory):
    # Pattern to find the App Settings link in the drawer
    # Look for: <div class="drawer-link" onclick="runNavTo('fitquest_screen17.html')">
    #           <span class="drawer-icon">⚙️</span><span>App Settings</span>
    #         </div>
    
    target_screen = "18"
    
    for filename in os.listdir(directory):
        if filename.startswith("fitquest_screen") and filename.endswith(".html"):
            if filename == f"fitquest_screen{target_screen}.html":
                continue
                
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Use \g<1> to avoid group number ambiguity (e.g. \118 vs \1 + 18)
            pattern = re.compile(
                r"(<div class=\"drawer-link\" onclick=\"runNavTo\('fitquest_screen)\d+(\.html'\)\">\s*<span class=\"drawer-icon\">⚙️</span><span>App Settings</span>)",
                re.MULTILINE
            )
            
            new_content = pattern.sub(rf"\g<1>{target_screen}\2", content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

if __name__ == "__main__":
    update_settings_link(".")
