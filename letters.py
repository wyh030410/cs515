def format_ordinal(num):
    """Convert a number to its ordinal form """
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return f"{num}{suffix}"


def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    try:
        while True:
            try:
                user_input = input("Enter a letter: ")
            except EOFError:
                print("Goodbye.")
                break

            if user_input.lower() == 'stop':
                print("Goodbye.")
                break

            if len(user_input) != 1:
                print("Please enter a single letter.")
                continue

            letter = user_input.lower()

            try:
                position = alphabet.index(letter) + 1
                ordinal = format_ordinal(position)
                print(f"'{letter}' is the {ordinal} letter of the alphabet.")
            except ValueError:
                print("Please enter a letter from the English alphabet.")

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
