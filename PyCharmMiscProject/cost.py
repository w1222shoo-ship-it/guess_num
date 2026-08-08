# cost = int(input("請輸入金額:"))
# if cost >= 2000:
#     cost = cost * 0.9
#     print("滿2000優惠後為",int(cost))
# else:
#     print("未達優惠，原價為",int(cost))

# h = float(input('請輸入您的身高(單位:cm): '))
# print('您的身高為',h,'公分')
# w = float(input('請輸入您的體重(單位:kg): '))
# print('您的體重為',w,'公斤')
# h = h/100
# bmi = w/(h*h)
# message = '正常體重'
# if bmi < 18.5:
#     message = '過輕'
# if 24 <= bmi < 27:
#     message = '過重'
# if bmi >= 27:
#     message = '肥胖'
#
# print('您的BMI為',round(bmi,2),'屬於',message)

score_c = int(input("請輸入您的中文成績:"))
score_m = int(input("請輸入您的數學成績:"))
score_e = int(input("請輸入您的英文成績:"))

#數學加權2
score_m = score_m*2
#英文加權2
score_e = score_e*2
#加權總分
total = score_c + score_m + score_e
#加權平均
wa = total/5
print("加權總分:",total)
print("加權平均:",wa)

if wa >= 90:
    print("您的評分為A")
elif wa >= 80:
    print("您的評分為B")
elif wa >= 70:
    print("您的評分為C")
elif wa >= 60:
    print("您的評分為D")
else:
    print("您的評分為E")


