from random import randint



def choose_number():
    random_number = randint(1, 10)
    for _ in range(3):
        number = input('Nhap so can tim tu 1-10: ')
        if not number.isdigit() or not 1 <= int(number) <= 10:
            print('Gia tri can nhap la mot so tu nhien trong khoang 1-10')
        else:
            number = int(number)
            if number == random_number:
                print(f'Chuc mung ban, ban da doan dung gia tri can tim: {random_number}')
                break
            print(f'{number} {"lon" if number > random_number else "nho"} hon gia tri can tim')
    print("Het")
    play_option()

def play_option():
    while True:
        choice = input("Ban co muon choi nua? (1: Co, 0: Khong): ")
        if choice in ('0', '1'):
            break
        print("Ban phai chon 1 hoac 0")
    if choice == '1':
        choose_number()
    else:
        exit()

choose_number()