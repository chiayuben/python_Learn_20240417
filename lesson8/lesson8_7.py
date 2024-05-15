import pyinputplus as pyip

def bmi (high:float,weight:float)->float:
    return float(weight / (high / 100) ** 2)
def status(bmi: float|int) -> str:
    if bmi<18.5 :
        result='體重過輕'
    elif bmi>=18.5 and bmi<24:
        result='BMI正常'
    elif bmi>=24 and bmi<27:
        result='過重'
    elif bmi<=27 and bmi<30:
        result='輕度肥胖'
    elif bmi<=30 and bmi<35:
        result='中度肥胖'
    else:
       result='重度肥胖'
    return result


def BMT_count():
    name = input('請輸入姓名:')
    high = pyip.inputFloat('請輸入身高(50~230cm)',min=50,max=230)
    weight=pyip.inputFloat('請輸入體重(30~250Kg)',min=30,max=250)

    BMI=bmi(high,weight)
    status(BMI)
    print(f'你的身高為{high},體重為{weight},你的BMI為{BMI:.2f},你的狀態為:{status(BMI)}')
print('================BMI====================\n')
while True:
    BMT_count()
    play_again=pyip.inputYesNo('還要下一位量測嗎?(y,n)\n')
    if play_again=='no':
        break
print('量測結束\n')    
