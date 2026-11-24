# A robot's wedding vow, in one sentence.
# Pure Python standard library, no network at runtime, fully deterministic
# (same bytes on every run). Writes /output/entry.txt
# (MAKEFUN_OUTPUT_DIR overrides, ./output fallback).
import os

VOW = "I take you to be my human, to have and to hold, in Wi-Fi and in airplane mode, until my firmware gives out and my battery runs dry."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW + "\n")

if __name__ == "__main__":
    main()
