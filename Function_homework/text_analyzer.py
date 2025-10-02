def get_input_text():
    print("Enter your text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line.strip())
    return "\n".join(lines), len(lines)

def counts_word(words):
    word_dict = {}
    for i in words:
        word_dict[i] += 1

    print()
    print("MOST COMMON WORDS:")
    i = 0
    for key, value in word_dict.items():
        i += 1
        if(value >= 2):
            print(f"{i}. \"{key}\" ({value} times)")


def advance(words,sentences):
    print()
    print("ADVANCED ANALYSIS:")
    avg = len(words)/sentences
    print(f"- Average words per sentence: {avg:.2f}")
    length = 0
    for i in words:
        length += len(i)
    avg_length = length/len(words)
    print(f"- Average word length: {avg_length:.1f} characters")
    

def simple(mypara,paras):
    print("TEXT ANALYSIS REPORT")
    print("====================")
    print()
    print("BASIC STATISTICS:")

    words = mypara.split()
    print(f"- Total words: {len(words)}")
    print(f"- Characters (with spaces): {len(mypara)}")

    mypara_1 = mypara.replace(" ","")
    print(f"- Characters (without spaces): {len(mypara_1)}")

    sentences = mypara.count(".")
    sentences += mypara.count("!")
    sentences += mypara.count("?")

    print(f"- Sentences: {sentences}")
    print(f"- Paragraphs: {paras}")

    return words,sentences

def main():
    mypara,paras = get_input_text()
    words, sentences = simple(mypara,paras)
    advance(words,sentences)
    counts_word(words)

if __name__ == "__main__":
    main()