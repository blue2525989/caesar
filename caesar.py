import string


def alphabet_position(char):
    bet = string.ascii_letters
    pos = bet.find(char)
    if pos > 25:
        new_pos = pos - 26
        return new_pos
    else:
        return pos


def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def encrypt(word, n):
    res = ''
    for letter in word:
        if letter != ' ':
            res += rotate_letter(letter, n)
        elif letter == ' ':
            res += ' '
    return res


def main():
    choice = ''
    while choice != 'q':
        choice = input("Please enter a sentence to encrypt\nq to quit\n")
        if choice == 'q':
            break
        else:
            time = input("Please enter the number of times to rotate characters\n")
            time = int(time)
            print(encrypt(choice, time))

if __name__ == '__main__':
    main()
