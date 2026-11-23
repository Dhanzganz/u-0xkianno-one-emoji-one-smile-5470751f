#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji, the one most likely to make a stranger smile,
to /output/entry.txt and nothing else: no words, no caption, no newline.

The output is verified after writing: the file is read back and must
contain exactly that single emoji, byte for byte.
"""
import os

EMOJI = "\U0001F602"  # 😂 FACE WITH TEARS OF JOY

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")

# /output is a mounted volume in the grader: only create it, never
# delete or recreate it (rmdir on a mount point fails with EBUSY).
os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_FILE, "w", encoding="utf-8", newline="") as f:
    f.write(EMOJI)

# Verify: read the file back and confirm it holds exactly one emoji.
with open(OUT_FILE, "r", encoding="utf-8", newline="") as f:
    written = f.read()
assert written == EMOJI, f"expected exactly {EMOJI!r}, got {written!r}"
print(f"Wrote one emoji to {OUT_FILE}: {EMOJI}")
