def camel_case(sentence):
    """ Convert sentence to camel case, for example, Display all books"
    is converted to "displayAllBooks" """

    title_case = sentence.title()  # Uppcase first letter of each word
    # Remove spaces between the sentence
    upper_camel_cased = title_case.replace(" ", "")
    # Lowercase first letter, join with rest of string
    # Slices don't repoduce index out of bounds errors.
    # So this still works on empty strings, strings of length 1
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]


def main():
    sentence = input("Please enter a sentence: ")
    output = camel_case(sentence)
    print(output)


if __name__ == "__main__":
    main()
