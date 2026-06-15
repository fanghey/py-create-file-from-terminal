import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv

    d_index = args.index("-d") if "-d" in args else None
    f_index = args.index("-f") if "-f" in args else None

    if d_index is not None:
        if f_index is not None and f_index > d_index:
            dir_parts = args[d_index + 1:f_index]
        else:
            dir_parts = args[d_index + 1:]
    else:
        dir_parts = []

    directory = os.path.join(*dir_parts) if dir_parts else ""

    if directory:
        os.makedirs(directory, exist_ok=True)

    if f_index is not None and f_index + 1 < len(args):
        filename = args[f_index + 1]
    else:
        filename = "file.txt"

    full_path = os.path.join(directory, filename) if directory else filename

    lines = []

    while True:
        text = input("Enter content line: ")

        if text == "stop":
            break

        lines.append(text)
        
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_lines = [f"{i + 1} {line}" for i, line in enumerate(lines)]

    content = timestamp + "\n" + "\n".join(formatted_lines) + "\n"

    with open(full_path, "a", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    main()
