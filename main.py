import os

LINE = (
    # The pitch: one sentence, 1-220 chars, absurd invention with a clever fix.
    "A self-watering plant pot that, when neglected for a week, hires a lawyer, "
    "sues its owner for emotional abandonment, and wins custody of itself."
)


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    # One sentence, no trailing newline: fully deterministic output.
    main()
