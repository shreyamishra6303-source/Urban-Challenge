import os

for fn in os.listdir("."):
    if fn.endswith(".html"):
        with open(fn, "r", encoding="utf-8") as f:
            content = f.read()
            
        if 'onclick="goBack()"' in content:
            new_content = content.replace('onclick="goBack()"', 'onclick="navigateBack()"')
            with open(fn, "w", encoding="utf-8") as f:
                f.write(new_content)
        
print("Reverted!")
