
def main():
    money = int(input("Are you sure you can buy a bag of potato? How many dollars do you have? "))
    if money <= 49:
        print("You don't have enough money to buy a bag of potato!")
        exit(49)
    print("You have", money, "dollars!")
    product = 50
    money = money - product
    print("You bought an extra-large bag of potato and now have " + str(money) + " dollars!")
    argent = 550


if __name__ == '__main__':
    main()