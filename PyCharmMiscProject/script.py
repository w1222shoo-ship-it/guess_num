# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


dict_p = {}
dict_b = {}
while True:
    cus_n = input("請輸入客戶名稱:")
    cus_p = input("請輸入客戶電話:")
    dict_p[cus_n.upper()] = cus_p
    cus_b = input("請輸入客戶生日:")
    dict_b[cus_n.upper()] = cus_b
    end = input("是否還要繼續輸入客戶資料(Y/N):")
    if end.upper() == "N":
        break

query_n = input("請輸入欲查詢的客戶名稱:")

print("\n------客戶資訊------")
print("客戶電話:"+dict_p[query_n.upper()])
print("客戶生日:"+dict_b[query_n.upper()])

