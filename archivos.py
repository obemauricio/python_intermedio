def read():
    numbers = []
    with open("./archive/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    
    print(numbers)

def write():
    name = ["facundo", "Miguel", "Pepe", "Christian"]
    with open("./archive/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.wirte("\n")


def run():
    read()


if __name__ == '__main__':
    run()