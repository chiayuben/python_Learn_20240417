import random
import pyinputplus as pyip

def play_game()->None:
    min = 1
    max = 100
    count=0
    target = random.randint(min,max)
    print(target)
    print('======猜數字遊戲=========\n')
    while True:
        count+=1
        keyin=pyip.inputInt(f'猜數字的範圍{min}~{max}=')
        print(keyin)
        if keyin==target:
            print (f'賓果!! 猜對了,答案是{random}')
            print(f'你總共猜了{count}')
            break
        elif keyin>target:
            print('在小一點')
            max=keyin-1
        elif keyin < target:
            print('再大一點')
            min=keyin+1
        print(f'你已經猜了{count}次')


while True:
    play_game()
    play_again=pyip.inputYesNo('還要繼續玩嗎?(y,n)')
    if play_again=='no':
        break
print('遊戲結束')