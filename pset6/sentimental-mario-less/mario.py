# main method

def main():
    height = get_height()
    draw(height)

# try to get the height
# showing an error if the user gives a invalid input


def get_height():
    while True:
        try:
            n = int(input("What is the height of the pyramid: "))
            if (n > 0 and n <= 8):
                break
        except ValueError:
            print("That's not an integer!")
    return n

# draws the pyramid


def draw(height):
    for i in range(height):
        for k in range(height - i, 1, -1):
            print(" ", end="")
        for j in range(height):
            if i >= j:
                print("#", end="")
        print("")


main()