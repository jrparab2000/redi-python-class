def get_input_text():
    print("Enter your text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line.strip())
    return "\n".join(lines)