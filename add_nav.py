import os

css_to_add = """
    /* ─── GLOBAL NAV DRAWER ─── */
    .menu-trigger {
      position: absolute; top: 55px; right: 20px; z-index: 900;
      width: 40px; height: 40px; border-radius: 12px;
      display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 5px;
      background: rgba(0,245,212,0.1); border: 1px solid rgba(0,245,212,0.3);
      box-shadow: 0 0 15px rgba(0,245,212,0.2); cursor: pointer; transition: all 0.2s;
    }
    .menu-trigger:hover { background: rgba(0,245,212,0.2); box-shadow: 0 0 20px rgba(0,245,212,0.4); }
    .menu-trig-line { width: 22px; height: 2px; background: #00f5d4; border-radius: 2px; box-shadow: 0 0 5px #00f5d4; }
    
    .nav-drawer {
      position: absolute; top: 0; right: -100%; width: 280px; height: 100%;
      background: rgba(6, 9, 19, 0.95); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
      border-left: 1.5px solid rgba(0,245,212,0.3); z-index: 1000;
      display: flex; flex-direction: column; padding: 24px 20px;
      transition: right 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
      box-shadow: -10px 0 30px rgba(0,0,0,0.8);
    }
    .nav-drawer.open { right: 0; }
    
    .drawer-overlay {
      position: absolute; inset: 0; background: rgba(0,0,0,0.6); z-index: 950;
      opacity: 0; pointer-events: none; transition: opacity 0.3s;
    }
    .drawer-overlay.open { opacity: 1; pointer-events: auto; }
    
    .drawer-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 30px; }
    .drawer-user { display: flex; align-items: center; gap: 12px; }
    .drawer-ava { width: 44px; height: 44px; border-radius: 50%; border: 2px solid #39ff14; box-shadow: 0 0 10px rgba(57,255,20,0.3); overflow: hidden; }
    .drawer-ava img { width: 100%; height: 100%; object-fit: cover; }
    .drawer-uinfo { display: flex; flex-direction: column; }
    .drawer-uname { font-size: 16px; font-weight: 800; color: #fff; }
    .drawer-ulvl { font-size: 12px; font-weight: 700; color: #39ff14; letter-spacing: 0.05em; text-transform: uppercase; }
    
    .drawer-close {
      width: 32px; height: 32px; border-radius: 8px; background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1); color: #fff; font-size: 18px;
      display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.2s;
    }
    .drawer-close:hover { background: rgba(255,59,48,0.2); border-color: #ff3b30; color: #ff3b30; }
    
    .drawer-nav { display: flex; flex-direction: column; gap: 16px; flex: 1; margin-top: 10px; }
    .drawer-link {
      display: flex; align-items: center; gap: 14px; padding: 14px 16px;
      border-radius: 12px; background: rgba(0,245,212,0.05); border: 1px solid transparent;
      text-decoration: none; color: #fff; font-size: 14px; font-weight: 600; cursor: pointer;
      transition: all 0.2s;
    }
    .drawer-link:hover {
      background: rgba(0,245,212,0.15); border-color: rgba(0,245,212,0.4);
      transform: translateX(-5px); box-shadow: 0 4px 15px rgba(0,245,212,0.1);
    }
    .drawer-icon { font-size: 18px; filter: drop-shadow(0 0 5px rgba(255,255,255,0.3)); }
"""

html_to_add = """
  <!-- GLOBAL NAV DRAWER -->
  <div class="menu-trigger" onclick="toggleNavDrawer()">
    <div class="menu-trig-line"></div>
    <div class="menu-trig-line"></div>
    <div class="menu-trig-line"></div>
  </div>
  
  <div class="drawer-overlay" id="drawerOverlay" onclick="toggleNavDrawer()"></div>
  <div class="nav-drawer" id="navDrawer">
    <div class="drawer-header">
      <div class="drawer-user">
        <div class="drawer-ava"><img src="https://i.pravatar.cc/100?img=11" alt="Me"></div>
        <div class="drawer-uinfo">
          <span class="drawer-uname">My Profile</span>
          <span class="drawer-ulvl">Hero Level 1</span>
        </div>
      </div>
      <div class="drawer-close" onclick="toggleNavDrawer()">✕</div>
    </div>
    <div class="drawer-nav">
      <div class="drawer-link" onclick="runNavTo('fitquest_screen14.html')">
        <span class="drawer-icon">🛡️</span><span>My Hero Profile</span>
      </div>
      <div class="drawer-link" onclick="runNavTo('fitquest_screen15.html')">
        <span class="drawer-icon">⚡</span><span>Squad Compatibility</span>
      </div>
      <div class="drawer-link" onclick="runNavTo('fitquest_screen13.html')">
        <span class="drawer-icon">🏛️</span><span>Hall of Heroes</span>
      </div>
      <div class="drawer-link" onclick="runNavTo('fitquest_screen16.html')">
        <span class="drawer-icon">📰</span><span>The Arena Feed</span>
      </div>
      <div class="drawer-link" onclick="runNavTo('fitquest_screen17.html')">
        <span class="drawer-icon">⚙️</span><span>App Settings</span>
      </div>
    </div>
  </div>
"""

js_to_add = """
function toggleNavDrawer() {
  const drawer = document.getElementById('navDrawer');
  const overlay = document.getElementById('drawerOverlay');
  if(drawer && overlay) {
    drawer.classList.toggle('open');
    overlay.classList.toggle('open');
  }
}
function runNavTo(url) {
  if(typeof navTo === 'function') { navTo(url); }
  else { window.location.href = url; }
}
"""

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "GLOBAL NAV DRAWER" in content:
        print(f"Skipping {file_path} (already modified)")
        return

    # Insert CSS
    if "</style>" in content:
        content = content.replace("</style>", css_to_add + "\n  </style>")

    # Insert HTML
    if "<script>" in content:
        if "</div>\n\n<script>" in content:
            content = content.replace("</div>\n\n<script>", html_to_add + "\n</div>\n\n<script>")
        elif "</div>\n<script>" in content:
            content = content.replace("</div>\n<script>", html_to_add + "\n</div>\n<script>")
        elif "</div>\n  <script>" in content:
            content = content.replace("</div>\n  <script>", html_to_add + "\n</div>\n  <script>")
        else:
            # Fallback for weird formatting
            parts = content.split("<script>")
            last_div_idx = parts[0].rfind("</div>")
            if last_div_idx != -1:
                parts[0] = parts[0][:last_div_idx] + html_to_add + "\n</div>\n"
                content = "<script>".join(parts)

        # Insert JS
        content = content.replace("<script>", "<script>\n" + js_to_add)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Patched {file_path}")

try:
    for i in range(1, 13):
        fn = f"fitquest_screen{i}.html"
        if os.path.exists(fn):
            process_file(fn)
    print("Done executing Python Script")
except Exception as e:
    print("Error:", e)
