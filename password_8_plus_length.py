import password


def password_check(pw):
    has_upper, has_lower, has_digit = False, False, False
    for ch in pw:
        if 'A' <= ch <= 'Z':
            has_upper = True
        elif 'a' <= ch <= 'z':
            has_lower = True
        elif '0' <= ch <= '9':
            has_digit = True

    return len(pw) >= 8 and has_digit and has_lower and has_upper


def main():
    paw = password.generator_password()
    while not password_check(paw):
        paw = password.generator_password()
    print(paw)


if __name__ == '__main__':
    main()