import random


def get_sum(number):
    return number // 10 + number % 10


def is_correct(card_number):
    even_numbers = card_number[::2]
    odd_numbers = list(card_number[1::2])
    sum_odd_numbers = 0
    k = 0
    digits_sum = 0

    for i in odd_numbers:
        sum_odd_numbers += int(i)
    for i in even_numbers:
        k = int(i) * 2
        digits_sum += get_sum(k)
    return not ((digits_sum + sum_odd_numbers) % 10)


def generate_card_number():
    result = '4'
    for i in range(2, 16):
        random.seed()
        result += str(random.randint(0, 9))
        if i % 4 == 0:
            result += ' '

    for i in range(0, 9):
        if is_correct((result + str(i)).replace(' ', '')):
            result += str(i)
            return result
    return generate_card_number()


def check_card_number(number):
    if not number:
        print("Incorrect card number!")
        return
    card_number = number.replace(' ', '')
    if len(card_number) != 16 or not card_number.isdigit():
        print("Incorrect card number!")
        return
    if is_correct(card_number):
        print("Correct card number!")
    else:
        print("Incorrect card number!")


def main():
    card = input("Put you card number to check: ")
    check_card_number(card)
    print('Generated card number: %s' % generate_card_number())


if __name__ == '__main__':
    main()
