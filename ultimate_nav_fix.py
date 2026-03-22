import os
import re

for fn in os.listdir("."):
    if not fn.endswith(".html"): continue
    
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # 1. Strip out goBack() from <head>
    content = re.sub(r'<script>\s*function goBack\(\) \{[\s\S]*?\}\s*</script>\s*', '', content)

    # 2. Revert any onclick="goBack()" strings to navigateBack()
    content = content.replace('onclick="goBack()"', 'onclick="navigateBack()"')
    
    # 3. Apply targeted fallback URLs 
    if fn == "fitquest_screen2.html":
        content = content.replace('onclick="navigateBack()"', "onclick=\"navigateBack('index.html')\"")
    elif fn in ["fitquest_screen13.html", "fitquest_screen18.html", "fitquest_screen19.html", "fitquest_screen20.html"]:
        content = content.replace('onclick="navigateBack()"', "onclick=\"navigateBack('fitquest_screen2.html')\"")

    # 4. Integrate the smart routing into the native navigateBack animations
    new_timeout = """setTimeout(() => { 
    if (document.referrer.indexOf(window.location.host) !== -1 && window.history.length > 1) {
      window.history.back();
    } else {
      window.location.href = fallbackUrl || 'index.html';
    }
  }, 300);"""
    
    # Update function definition
    if 'function navigateBack() {' in content:
        content = content.replace('function navigateBack() {', 'function navigateBack(fallbackUrl) {')
        
    # Switch out the old timeout
    content = re.sub(r'setTimeout\(\(\) => \{ window\.history\.back\(\); \}, 300\);', new_timeout, content)
    
    if content != original_content:
        with open(fn, "w", encoding="utf-8") as f:
            f.write(content)

print("Ultimate Navigation applied successfully.")
