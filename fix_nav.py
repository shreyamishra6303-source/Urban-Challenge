import os
import re

head_script = """
<script>
function goBack() {
  if (window.history.length > 1) {
    window.history.back();
  } else {
    window.location.href = 'index.html'; // Fallback to home if no history
  }
}
</script>
"""

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # 1. Inject script into <head>
    if "function goBack()" not in content:
        content = content.replace("</head>", head_script + "</head>")
        changed = True

    # 2. Replace navigateBack() with goBack()
    if 'onclick="navigateBack()"' in content:
        content = content.replace('onclick="navigateBack()"', 'onclick="goBack()"')
        changed = True
        
    # Also replace any stray hrefs on the back button
    # Using regex to find <div class="back-btn" href="..."> and <a class="back-btn" href="...">
    # and swap href with onclick="goBack()"
    content_new = re.sub(r'href="fitquest_screen[^"]*\.html"[^>]*class=".*back-btn.*"', r'onclick="goBack()" class="back-btn"', content)
    if content_new != content:
        content = content_new
        changed = True
    
    # Another pattern just in case: <a href="fitquest..." class="back-btn">
    content_new = re.sub(r'<a([^>]+)href="[^"]*"([^>]*)class="([^"]*)back-btn([^"]*)"', r'<a\1onclick="goBack()"\2class="\3back-btn\4"', content)
    if content_new != content:
        content = content_new
        changed = True

    # 3. Ensure .back-btn has cursor: pointer;
    if ".back-btn {" in content and "cursor: pointer;" not in content:
        content = content.replace(".back-btn {", ".back-btn { cursor: pointer;")
        changed = True

    # 4. Check absolute File Path Links (C:/Users/...)
    if "C:/Users/" in content or "c:/Users/" in content:
        content = re.sub(r'[cC]:/Users/[^"]*/([^"/]+\.html)', r'\1', content)
        changed = True
        
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

for fn in os.listdir("."):
    if fn.endswith(".html"):
        process_file(fn)

print("All navigation fixes applied.")
