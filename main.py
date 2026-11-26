import os

ENTRY = "Sorry I jammed on page 47 of 48. You staple my insides, feed me damp paper, then act shocked when I choke."


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 120):
        raise ValueError(f"entry length {len(text)} is outside the 1-120 gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
