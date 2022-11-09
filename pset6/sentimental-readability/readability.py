import string


def main():

    text = input("What is the text\n")
    print_grade(text)


def print_grade(text):
    # Number of letters of the text
    letters = count_letters(text)
    # Number of words of the text
    words = count_words(text)
    # Number of senteces of the text
    sentences = count_senteces(text)

    # the average number of letters per 100 words in the text
    L = (letters / words) * 100
    # the average number of sentences per 100 words in the text.
    S = (sentences / words) * 100

    # Coleman-Liau index equation (aka Grade)
    grade = round(((0.0588 * L) - (0.296 * S) - 15.8))

    if grade < 1:
        print("Before Grade 1")
    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def count_letters(text):

    # Puts Both upper lowercase and upper case in a string called Alphabet
    alphabet = string.ascii_letters
    countLetters = 0

    # loop goes throught the text
    for i in text:
        if i in alphabet:
            countLetters += 1

    return countLetters


def count_words(text):
    countWords = len(text.split())

    return countWords


def count_senteces(text):

    punctuation = ".?!"
    count_senteces = 0

    for i in text:

        if i in punctuation:
            count_senteces += 1
    return count_senteces


main()