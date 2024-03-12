import sys

#list comprehension is [new_expression for item in iterable if condition]

#lambda function receives one argument, word and applies function, which is used as a condition

def generate_list_of_matching_length_words(s: str, length: int) -> list:
    return [word for word in s.split() if (lambda word: len(word) > length)(word)]

def main():
    try:
        assert len(sys.argv) == 3, "AssertionError: the arguments are bad"

        single_str = sys.argv[1]
        length = sys.argv[2]

        length = int(length)  # Convert to int

        words_list = generate_list_of_matching_length_words(single_str, length)
        print(words_list)

    except AssertionError as error:
        print(error)

if __name__ == "__main__":
    main()