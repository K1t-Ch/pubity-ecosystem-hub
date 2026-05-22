#!/usr/bin/env python3
"""Single download — final Andrew Packer."""
import urllib.request, os

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "avatars")
os.makedirs(OUT, exist_ok=True)

url = "https://instagram.fwbw1-1.fna.fbcdn.net/v/t51.2885-19/461368644_548247414440765_8961384685398904096_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.fwbw1-1.fna.fbcdn.net&_nc_cat=105&_nc_oc=Q6cZ2gE3xLAwttcFXltIRzP1fUeB02WKoawvKuyirPCm6NjdPo8rX4cc2TIoKfmHOaQ-kIg&_nc_ohc=a8XsgzCl-csQ7kNvwGknX__&_nc_gid=iaajfDzT0H4aq1vjqoB9ww&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_Af7o3cjl0ZDxfdnBAQJTO_WtlFOO-yjpMLYfZpzHopsk8w&oe=6A13CCD5&_nc_sid=8b3546"
req = urllib.request.Request(url, headers={
    "Referer": "https://www.instagram.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
})
with urllib.request.urlopen(req, timeout=20) as r:
    data = r.read()
with open(os.path.join(OUT, "andpacker.jpg"), "wb") as f:
    f.write(data)
print(f"OK  andpacker  {len(data)} bytes")
