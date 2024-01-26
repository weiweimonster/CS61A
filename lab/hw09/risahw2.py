def print_menu(usr_str):
    print("MENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit")
    print("")
    choice = input("Choose an option:")
    if choice == "c":
        print("Number of non-whitespace characters:", get_num_of_non_WS_characters(usr_str))
    elif choice == "w":
        print('Number of words:', get_num_of_words(usr_str))
    elif choice == "f":
        usr_str, count = fix_capitalization(usr_str)
        print('Number of letters capitalized:', count)
        print('Edited text:', usr_str)
    elif choice == "r":
        print('Edited text:', replace_punctuation(usr_str))
    elif choice == "s":
        print('Edited text:', shorten_space(usr_str))

    print("")
    # Complete print_menu() function

    return choice, usr_str


def get_num_of_non_WS_characters(usr_str):
    count = 0
    for i in usr_str:
        if not i.isspace():
            count += 1
    return count


def get_num_of_words(usr_str):
    return len(usr_str.split())


def fix_capitalization(usr_str):
    count = 0
    prev = ''
    result = ""
    for i in usr_str:
        if prev in '?.!' and i.isalpha():
            i = i.upper()
            prev = i
            count += 1
        elif i != ' ':
            prev = i
        result += i
    return result, count


def replace_punctuation(usr_str, exclamation_count=0, semicolon_count=0):
    result = ''
    for i in usr_str:
        if i == '!':
            i = '.'
            exclamation_count += 1
        elif i == ';':
            i = ','
            semicolon_count += 1
        result += i
    print('Punctuation replaced')
    print('exclamation_count:', exclamation_count)
    print('semicolon_count:', semicolon_count)
    return result


def shorten_space(usr_str):
    result = ''
    prev=''
    for i in usr_str:
        if not (prev==' ' and i==' '):
            result+=i
        prev=i

    return result


if __name__ == '__main__':
    s = input("Enter a sample text:")
    print("")
    print("\nYou entered:", s)
    print("")
    choice = ''
    choice, modified_string = print_menu(s)
    while choice != 'q':
        choice, modified_string = print_menu(modified_string)
