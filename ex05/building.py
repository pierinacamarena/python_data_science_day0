import sys
import string


def count_uppercase_letters(s: str) -> int:
    """
    Return the number of uppercase letters in a given string.
    """
    # sum of every time an upper case char is encountered
    return sum(1 for char in s if char.isupper())


def count_lowercase_letters(s: str) -> int:
    """
    Return the number of lowercase letters in a given string.
    """
    # sum of every time a lowercase char is encountered
    return sum(1 for char in s if char.islower())


def count_digits(s: str) -> int:
    """
    Return the number of digits in a given string.
    """
    # sum of every time a digit is encountered
    return sum(1 for char in s if char.isdigit())


def count_punctuation_marks(s: str) -> int:
    """
    Return the number of punctuation marks in a given string.
    """
    # getting all punctuation marks
    punctuation_marks = string.punctuation

    # sum of every time a punctuation is encountered
    return sum(1 for char in s if char in punctuation_marks)


def count_spaces(s: str) -> int:
    """
    Return the number of spaces in a given string.
    """
    # count all spaces
    return s.count(' ')


def string_analysis(single_str: str) -> None:
    """
    Perform a comprehensive analysis of characters in the input string,
    including the count of uppercase letters, lowercase letters,
    punctuation marks, spaces, and digits.

    Args:
        single_str (str): The string to analyze.
    """
    str_len = len(single_str)
    print(f"The text contains {str_len} characters:")

    upper_case = count_uppercase_letters(single_str)
    print(f"{upper_case} upper letters")

    lower_case = count_lowercase_letters(single_str)
    print(f"{lower_case} lower letters")

    punctuation_marks = count_punctuation_marks(single_str)
    print(f"{punctuation_marks} punctuation marks")

    spaces = count_spaces(single_str)
    print(f"{spaces} spaces")

    digits = count_digits(single_str)
    print(f"{digits} digits")


def main():
    try:
        if len(sys.argv) < 2:
            # prompting user when no argument is given
            text_to_count = input("What is the text to count? ")
        else:
            # Asserting only one extra argument is given
            assert len(sys.argv) == 2, \
                "AssertionError: more than one argument is provided"

            # Retrieving argument
            text_to_count = sys.argv[1]

        string_analysis(text_to_count)

    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
