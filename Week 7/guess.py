import random


def main():
    target = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            s = input("請猜一個 1 到 100 的整數: ")
            guess = int(s)
        except ValueError:
            print("請輸入有效的整數。")
            continue

        attempts += 1

        if guess > target:
            print("太大")
        elif guess < target:
            print("太小")
        else:
            print(f"恭喜你！猜中啦！總共猜了 {attempts} 次。")
            break


if __name__ == "__main__":
    main()
