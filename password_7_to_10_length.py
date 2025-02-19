from random import randint

min_length = 7
max_length = 10
min_ASCII = 33
max_ASCII = 126


def generator_password():
    length = randint(min_length, max_length)
    password = ''
    for _ in range(length):
        symbol = chr(randint(min_ASCII, max_ASCII))
        password += str(symbol)
    return password


def main():
    print(f'Your password is {generator_password()} \N{fire}')


if __name__ == '__main__':
    main()
