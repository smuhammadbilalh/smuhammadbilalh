#!/usr/bin/env python3
"""Generate the Aceternity-style SVG assets for the GitHub profile README.
Palette: bg #000/#0a0a0a · border #262626 · text #fafafa / #a3a3a3 / #737373 · spotlight hsla(210,100%,85%,.08)"""
import os, html
OUT = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUT, exist_ok=True)
FONT = "Inter,'Segoe UI',-apple-system,BlinkMacSystemFont,Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','Fira Code','Cascadia Code',Consolas,monospace"
E = html.escape

def grid(w, h, step=40, op=0.035):
    return f'<pattern id="grid" width="{step}" height="{step}" patternUnits="userSpaceOnUse"><path d="M {step} 0 L 0 0 0 {step}" fill="none" stroke="#fff" stroke-opacity="{op}" stroke-width="1"/></pattern>'

def pill(x, y, text, w=None, fs=12, fill="#d4d4d4", stroke="#262626", bg="#0a0a0a"):
    w = w or int(len(text) * fs * 0.62 + 24)
    return (f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="13" fill="{bg}" stroke="{stroke}"/>'
            f'<text x="{x + w/2}" y="{y + 17}" text-anchor="middle" font-family="{FONT}" font-size="{fs}" font-weight="500" fill="{fill}">{E(text)}</text>'), w

# ---------------------------------------------------------------- hero
def hero():
    W, H = 1200, 400
    chips = ["Kotlin Multiplatform", "Jetpack Compose", ".NET MAUI", "WinUI 3", "PHP", "Firebase"]
    cx, parts = 80, []
    for c in chips:
        s, w = pill(cx, 300, c, fs=13); parts.append(s); cx += w + 10
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Muhammad Bilal — Core Lead App Developer">
<defs>
  {grid(W,H)}
  <linearGradient id="tg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fafafa"/><stop offset="100%" stop-color="#a3a3a3"/></linearGradient>
  <linearGradient id="line" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="30%" stop-color="#60a5fa" stop-opacity=".9"/><stop offset="70%" stop-color="#a78bfa" stop-opacity=".9"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <radialGradient id="spot1" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="hsl(210,100%,85%)" stop-opacity=".10"/><stop offset="50%" stop-color="hsl(210,100%,55%)" stop-opacity=".03"/><stop offset="100%" stop-color="hsl(210,100%,45%)" stop-opacity="0"/></radialGradient>
  <radialGradient id="spot2" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="hsl(210,100%,85%)" stop-opacity=".06"/><stop offset="100%" stop-color="hsl(210,100%,45%)" stop-opacity="0"/></radialGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity="1"/></linearGradient>
  <clipPath id="r"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>
<g clip-path="url(#r)">
  <rect width="{W}" height="{H}" fill="#000"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <rect x="0" y="{H-160}" width="{W}" height="160" fill="url(#fade)"/>
  <g transform="rotate(-32 300 0)">
    <ellipse cx="300" cy="-80" rx="280" ry="700" fill="url(#spot1)">
      <animate attributeName="cx" values="300;380;300" dur="9s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <g transform="rotate(-22 520 0)">
    <ellipse cx="520" cy="-120" rx="140" ry="620" fill="url(#spot2)">
      <animate attributeName="cx" values="520;470;520" dur="11s" repeatCount="indefinite"/>
    </ellipse>
  </g>
  <ellipse cx="1060" cy="420" rx="420" ry="220" fill="url(#spot2)"/>

  <!-- status pill -->
  <rect x="80" y="86" width="226" height="28" rx="14" fill="#0a0a0a" stroke="#262626"/>
  <circle cx="98" cy="100" r="4" fill="#22c55e"><animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/></circle>
  <text x="110" y="104.5" font-family="{FONT}" font-size="12.5" font-weight="500" fill="#a3a3a3" letter-spacing=".3">Core Lead App Developer · Open to work</text>

  <text x="78" y="196" font-family="{FONT}" font-size="76" font-weight="800" letter-spacing="-3" fill="url(#tg)">Muhammad Bilal</text>
  <text x="81" y="240" font-family="{FONT}" font-size="21" font-weight="400" fill="#a3a3a3" letter-spacing="-.2">I build university-scale mobile apps, offline-first desktop tools and the PHP backends behind them.</text>
  <text x="81" y="268" font-family="{MONO}" font-size="13.5" fill="#737373">Gujrat, Pakistan  ·  MyUOG &amp; MyUOR official apps  ·  Kotlin Multiplatform  ·  .NET</text>
  {''.join(parts)}
  <rect x="0" y="{H-2}" width="{W}" height="2" fill="url(#line)"/>
</g></svg>'''

# ---------------------------------------------------------------- bento card
def card(name, title, lines, tags, mark, accent, cta="View repository", stat=None, W=600, H=250):
    tx, parts = 28, []
    for t in tags:
        s, w = pill(tx, H-56, t, fs=11.5); parts.append(s); tx += w + 8
    desc = "".join(f'<text x="28" y="{118 + i*22}" font-family="{FONT}" font-size="14.5" fill="#a3a3a3">{E(l)}</text>' for i, l in enumerate(lines))
    stat_svg = f'<text x="{W-28}" y="48" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="#737373">{E(stat)}</text>' if stat else ""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{E(title)}">
<defs>
  {grid(W,H,32,0.03)}
  <radialGradient id="g" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{accent}" stop-opacity=".22"/><stop offset="100%" stop-color="{accent}" stop-opacity="0"/></radialGradient>
  <linearGradient id="mk" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{accent}" stop-opacity=".9"/><stop offset="100%" stop-color="{accent}" stop-opacity=".45"/></linearGradient>
  <linearGradient id="tg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fafafa"/><stop offset="100%" stop-color="#d4d4d4"/></linearGradient>
  <clipPath id="r"><rect width="{W}" height="{H}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#r)">
  <rect width="{W}" height="{H}" fill="#0a0a0a"/>
  <rect width="{W}" height="{H}" fill="url(#grid)"/>
  <ellipse cx="{W-60}" cy="-20" rx="300" ry="170" fill="url(#g)"/>
  <rect x="28" y="28" width="40" height="40" rx="11" fill="#171717" stroke="#262626"/>
  <text x="48" y="55" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="800" fill="url(#mk)">{E(mark)}</text>
  {stat_svg}
  <text x="28" y="94" font-family="{FONT}" font-size="23" font-weight="700" letter-spacing="-.6" fill="url(#tg)">{E(title)}</text>
  {desc}
  {''.join(parts)}
  <text x="{W-28}" y="{H-37}" text-anchor="end" font-family="{FONT}" font-size="12.5" font-weight="500" fill="#737373">{E(cta)} →</text>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="#262626"/>
</svg>'''
    open(os.path.join(OUT, f"card-{name}.svg"), "w").write(svg)

# ---------------------------------------------------------------- section label
def label(name, text, W=1200, H=44):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{E(text)}">
<defs><linearGradient id="l" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#262626"/><stop offset="100%" stop-color="#262626" stop-opacity="0"/></linearGradient></defs>
<rect width="{W}" height="{H}" fill="#000"/>
<text x="0" y="29" font-family="{FONT}" font-size="22" font-weight="700" letter-spacing="-.6" fill="#fafafa">{E(text)}</text>
<rect x="0" y="{H-1}" width="{W}" height="1" fill="url(#l)"/>
</svg>'''
    open(os.path.join(OUT, f"label-{name}.svg"), "w").write(svg)

def footer():
    W, H = 1200, 90
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="footer">
<defs><linearGradient id="line" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="30%" stop-color="#60a5fa" stop-opacity=".8"/><stop offset="70%" stop-color="#a78bfa" stop-opacity=".8"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="s" cx="50%" cy="0%" r="60%"><stop offset="0%" stop-color="hsl(210,100%,85%)" stop-opacity=".08"/><stop offset="100%" stop-color="#000" stop-opacity="0"/></radialGradient>
<clipPath id="r"><rect width="{W}" height="{H}" rx="20"/></clipPath></defs>
<g clip-path="url(#r)"><rect width="{W}" height="{H}" fill="#000"/><rect width="{W}" height="{H}" fill="url(#s)"/>
<rect x="0" y="0" width="{W}" height="1.5" fill="url(#line)"/>
<text x="600" y="52" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="500" fill="#737373" letter-spacing=".4">Designed &amp; built by Muhammad Bilal  ·  Thanks for stopping by</text></g></svg>'''

if __name__ == "__main__":
    open(os.path.join(OUT, "banner.svg"), "w").write(hero())
    open(os.path.join(OUT, "footer.svg"), "w").write(footer())
    card("myuog", "MyUOG — Official University of Gujrat App",
         ["Official campus app for students, faculty and applicants: results, attendance,", "fees, live bus tracking, admissions and push notifications."],
         ["Kotlin Multiplatform", "Jetpack Compose", "PHP", "Firebase"], "UG", "#60a5fa", "Google Play", "Core Lead App Developer  ·  10K+ installs")
    card("myuor", "MyUOR — Official University of Rasul App",
         ["Offline-first university app: results, attendance, challans, digital ID,", "GPA tools, admissions and a faculty portal — built for weak networks."],
         ["Kotlin Multiplatform", "Jetpack Compose", "PHP", "Firebase"], "UR", "#a78bfa", "Google Play", "Core Lead App Developer  ·  1K+ installs")
    card("snaperase", "SnapErase",
         ["Windows background remover running the U²-Net model locally", "with ONNX Runtime. No internet, no uploads, no limits."],
         ["WinUI 3", "ONNX Runtime", "C#"], "SE", "#34d399", stat="★ 3  ·  Windows")
    card("quickqr", "QuickQr",
         ["Generate, share and scan QR codes on Android, iOS, macOS", "and Windows from a single .NET MAUI codebase."],
         [".NET MAUI", "ZXing", "SkiaSharp"], "QR", "#f472b6", stat="★ 1  ·  Cross-platform")
    card("recordflow", "RecordFlow",
         ["Dependable screen recorder with live timer, smart save", "locations and clean permission handling."],
         [".NET MAUI", "Android", "MVVM"], "RF", "#fb923c", stat="Cross-platform")
    card("snakegame", "SnakeGame",
         ["Classic snake with three modes, difficulty levels, bonus food,", "sound and persistent high scores — drawn with MAUI Graphics."],
         [".NET MAUI", "MAUI Graphics", "C#"], "SG", "#22d3ee", stat="Game")
    card("cpos", "CPOS — Point of Sale",
         ["Enterprise-grade POS for Windows desktop: billing, inventory,", "customers and reporting. In active development."],
         ["WinUI 3", "Windows App SDK", "C#"], "PS", "#facc15", stat="In development")
    card("ghss", "GHSS Sarai Alamgir — School Website",
         ["Official school site: news, academics, faculty and gallery, managed", "through Decap CMS and auto-deployed to GitHub Pages."],
         ["HTML / CSS / JS", "Decap CMS", "GitHub Pages"], "GS", "#60a5fa", "ghss-sarai.edu.pk", stat="Live")
    print("written:", sorted(os.listdir(OUT)))
