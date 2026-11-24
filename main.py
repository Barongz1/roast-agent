"""Roast Your Own Agent — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a single line roasting the AI agent our own team built, and nothing else.
"""
import os

LINE = "Our agent is so confident, it rewrote the code, deleted the tests, and then asked us why we were so quiet."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
