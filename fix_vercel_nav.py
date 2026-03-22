import os
import re

new_script = """
<script>
function goBack() {
  // Check if there is a history to go back to
  if (document.referrer.indexOf(window.location.host) !== -1 && window.history.length > 1) {
    window.history.back();
  } else {
    // Fallback if the user landed directly on the page or history is empty
    window.location.href = 'fitquest_screen2.html'; 
  }
}
</script>
"""

targets = ["fitquest_screen2.html", "fitquest_screen13.html", "fitquest_screen18.html", "fitquest_screen19.html", "fitquest_screen20.html"]

for fn in os.listdir("."):
    if fn.endswith(".html"):
        with open(fn, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 1. Remove old goBack script if exists
        content = re.sub(r'<script>\s*function goBack\(\) \{[\s\S]*?\}\s*</script>', '', content)
        
        # 2. Inject new goBack script right before closing head
        content = content.replace("</head>", new_script + "</head>")
        
        # 3. Add inline styles to back-btn
        # Only inject if it doesn't already have pointer-events auto
        if 'style="cursor: pointer; pointer-events: auto;"' not in content:
            content = re.sub(r'(class="[^"]*back-btn[^"]*")', r'\1 style="cursor: pointer; pointer-events: auto;"', content)
            
        # 4. Remove any stray absolute paths
        content = re.sub(r'[cC]:/Users/[^"]*/([^"/]+\.html)', r'\1', content)
        
        # 5. Fix Screen 2 and specific menu-origin screens
        if fn in targets:
            content = content.replace('onclick="navigateBack()"', 'onclick="goBack()"')
            # Strip any href safely from those buttons specifically just in case
            content = re.sub(r'(class="[^"]*back-btn[^"]*"[^>]*)\s*href="[^"]*"', r'\1', content)
            content = re.sub(r'href="[^"]*"\s*(class="[^"]*back-btn[^"]*")', r'\1', content)
            
        with open(fn, "w", encoding="utf-8") as f:
            f.write(content)
            
print("Vercel navigation smartly patched!")
