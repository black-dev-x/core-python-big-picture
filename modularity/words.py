from urllib.request import urlopen


def fetch_words():
    lines = urlopen('http://sixty-north.com/c/t.txt')
    words = []
    for line in lines:
        for word in line.decode('utf-8').split():
            words.append(word)
    lines.close()
    return words


def print_items(items):
    for item in items:
        print(item)


if __name__ == '__main__':
    words = fetch_words()
    print_items(words)
