# n = int(input("請輸入終止值:"))
# sum=0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i + 1
# print(sum)


# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# def bmi(h,w):
#     h = h / 100
#     bmi = w / (h * h)
#     message = '正常體重'
#     if bmi < 18.5:
#         message = '過輕'
#     if 24 <= bmi < 27:
#         message = '過重'
#     if bmi >= 27:
#         message = '肥胖'
#     return "您的BMI為"+str(round(bmi,2)),"，屬於"+message
#
#
# h = float(input('請輸入您的身高(單位:cm): '))
# w = float(input('請輸入您的體重(單位:kg): '))
# print(bmi(h,w))
#
print(' '*4,'*'*1)
print(' '*3,'*'*2)
print(' '*2,'*'*3)
print(' '*1,'*'*4)
print(' '*0,'*'*5)


# def Sum_r(nn):
#     if nn == 1:
#         return 1
#     else:
#         return nn+Sum_r(nn-1)
#
# n = int(input('請輸入終止值:'))
# print(Sum_r(n))