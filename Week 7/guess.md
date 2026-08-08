# guess.py - 猜數字遊戲

簡介
---
這個程式是一個簡單的命令列猜數字遊戲：電腦隨機產生 1 到 100 的整數，玩家輸入猜測，程式會回應「太大」、「太小」，猜中時顯示總共猜了幾次。

檔案
---
- 程式檔案：[Week 7/guess.py](Week%207/guess.py)

使用方式
---
在終端執行：

```bash
python "d:\2026python\Week 7\guess.py"
```

程式碼 (完整)
---

```python
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
```

互動範例（擷取）
---
- 輸入 `50` → 顯示 `太大`
- 輸入 `25` → 顯示 `太大`
- 輸入 `12` → 顯示 `太小`
- 輸入 `6`  → 顯示 `太小`

備註
---
- 已包含非整數輸入的驗證，避免程式因 ValueError 終止。
- 若要將遊戲改為限次猜測、或增加提示（例如高低範圍），我可以幫你改寫。
