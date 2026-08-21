"""Generate complete iOS AppIcon set from the 1024px source icon."""
import json, os
from PIL import Image

SRC = r"C:/Users/hunin/projects/gramlingo/ios/App/App/Assets.xcassets/AppIcon.appiconset/AppIcon-512@2x.png"
OUT = r"C:/Users/hunin/projects/gramlingo/ios/App/App/Assets.xcassets/AppIcon.appiconset"

img = Image.open(SRC).convert("RGBA")

# (size_pt, scale, idiom) -> pixel size
entries = [
    # iPhone
    ("20x20", "2x", "iphone", 40), ("20x20", "3x", "iphone", 60),
    ("29x29", "2x", "iphone", 58), ("29x29", "3x", "iphone", 87),
    ("40x40", "2x", "iphone", 80), ("40x40", "3x", "iphone", 120),
    ("60x60", "2x", "iphone", 120), ("60x60", "3x", "iphone", 180),
    # iPad
    ("20x20", "1x", "ipad", 20), ("20x20", "2x", "ipad", 40),
    ("29x29", "1x", "ipad", 29), ("29x29", "2x", "ipad", 58),
    ("40x40", "1x", "ipad", 40), ("40x40", "2x", "ipad", 80),
    ("76x76", "1x", "ipad", 76), ("76x76", "2x", "ipad", 152),
    ("83.5x83.5", "2x", "ipad", 167),
]

images = []
for size_pt, scale, idiom, px in entries:
    name = f"icon-{px}.png"
    img.resize((px, px), Image.LANCZOS).save(os.path.join(OUT, name))
    images.append({"filename": name, "idiom": idiom, "scale": scale, "size": size_pt})

# Marketing 1024 (keep existing file name)
images.append({"filename": "AppIcon-512@2x.png", "idiom": "ios-marketing", "scale": "1x", "size": "1024x1024"})

with open(os.path.join(OUT, "Contents.json"), "w") as f:
    json.dump({"images": images, "info": {"author": "xcode", "version": 1}}, f, indent=2)

print(f"Generated {len(images)} icons into {OUT}")
