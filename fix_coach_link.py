import os
import re

def fix_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # We want to find the App Settings link block
    # and prepend the Coach Directory link block to it.
    
    coach_block = """      <div class="drawer-link" onclick="runNavTo('fitquest_screen20.html')">
        <span class="drawer-icon">👨‍🏫</span><span>Pro Coach Directory</span>
      </div>
"""
    
    if "Pro Coach Directory" in content:
        return # already has it
        
    # Find the exact App Settings block
    app_settings_block = """      <div class="drawer-link" onclick="runNavTo('fitquest_screen19.html')">
        <span class="drawer-icon">⚙️</span><span>App Settings</span>
      </div>"""
      
    if app_settings_block in content:
        content = content.replace(app_settings_block, coach_block + app_settings_block)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"App Settings block not found exactly in {file_path}")

for i in range(1, 22):
    fn = f"fitquest_screen{i}.html"
    if os.path.exists(fn):
        fix_file(fn)
