import pyinputplus as pyip
try:
    name = input('請輸入姓名:')
    high = pyip.inputFloat('請輸入身高(120~230)(cm):',min=120,max=230) 
    weight = pyip.inputFloat('請輸入體重(40~170)(kg):',min=40,max=170)
    bmi = weight /( high / 100) ** 2
    print(f'你的名字是{name},體重為{weight},身高為{high},經計算後BMI為{round(bmi,ndigits=1)}')
    if bmi<18.5 :
        print('體重過輕')
    elif bmi>=18.5 and bmi<24:
        print('BMI正常')
    elif bmi>=24 and bmi<27:
        print('過重')
    elif bmi<=27 and bmi<30:
        print('輕度肥胖')
    elif bmi<=30 and bmi<35:
        print('中度肥胖')
    else:
        print('重度肥胖')
except Exception as e:
    print(f'錯誤: {e}')