

def main():
    # Get the card number input
    cardNumber = int(input("What is credit card number \n"))
    validades(cardNumber)


def validades(cardNumber):

    length = 1
    sum = 0
    numberEven = 0

    checkCardNumber = cardNumber

    # Loop that only ends if the number of the card is zero
    while checkCardNumber != 0:

        # Check if the location on the number is even
        if (length % 2 == 0):

            numberEven = (checkCardNumber % 10) * 2

            # checks if the result of the equation is smaller than 10 if it's i'll at it to the sum
            if (numberEven >= 0) and (numberEven < 9):

                sum += numberEven

            else:
                # divide the number in the even position in two and add it to the sum+
                sum += (numberEven // 10)
                sum += (numberEven % 10)
        else:
            # if the number is odd adds the position to sum
            sum += checkCardNumber % 10

        checkCardNumber = checkCardNumber // 10
        length += 1

    # checks if the last digit in the sum number is zero, if it's check what creditcard valid or not and what type it's
    if (sum % 10) == 0:
        if ((cardNumber >= 4000000000000 and cardNumber <= 4999999999999) or (cardNumber >= 4000000000000000
                                                                              and cardNumber <= 4999999999999999)):
            print("VISA")

        elif ((cardNumber >= 340000000000000 and cardNumber <= 349999999999999) or (cardNumber >= 370000000000000
                                                                                    and cardNumber <= 379999999999999)):
            print("AMEX")

        elif ((cardNumber >= 5100000000000000 and cardNumber <= 5599999999999999)):
            print("MASTERCARD")

        else:
            print("INVALID")
    else:
        print("INVALID")


main()