import random

def get_sum(number):
    return number//10+number%10


def luhn(card_number):                # return 0 if card number is valide
    even_numbers = card_number[::2]
    odd_numbers = list(card_number[1::2])
    sum_odd_numbers = 0
    k = 0
    digits_sum = 0

    for i in odd_numbers:
        sum_odd_numbers += int(i)
    for i in even_numbers:
        k = int(i)*2
        digits_sum += get_sum(k)
    return (digits_sum+sum_odd_numbers)%10 


def get_new_number():
    result = '4'
    for i in range(2, 16):
        random.seed()
        result += str(random.randint(0, 9))
        if i%4 == 0:
            result += ' '
            
    for i in range(0, 9):
        if luhn((result+str(i)).replace(' ', '')) == 0:
            result += str(i)
            return result
    return get_new_number()

        
def check_card_number(number):
    if len(number) == 0:
        print("Incorrect card number!")
        return
    card_number = number.replace(' ', '')
    if len(card_number) != 16 or not card_number.isdigit():
        print("Incorrect card number!")
        return
    if luhn(card_number) == 0:
        print("Correct card number!")
    else:
        print("Incorrect card number!")


def main():
    card = input("Put you card number to check: ")
    check_card_number(card)
    valide_card = get_new_number()
    print(valide_card)


if __name__ == '__main__':
    main()
    input()
