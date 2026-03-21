import os
import re

def cleanup_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The bug introduced: onclick="runNavTo('fitquest_screenXX.html')">.html')">
    # We want to remove the extra .html')"> immediately after the closing bracket and quote
    
    pattern = r"(\.html\'\)\">)\.html\'\)\">"
    new_content = re.sub(pattern, r"\1", content)

    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False

if __name__ == "__main__":
    count = 0
    for fn in os.listdir("."):
        if fn.endswith(".html"):
            if cleanup_file(fn):
                print(f"Fixed menu in {fn}")
                count += 1
    print(f"Cleanup complete. Fixed {count} files.")
