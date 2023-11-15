import random

# 0以上10以下の整数
print(random.randint(0, 10))

intArr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(intArr)

# 配列の中の数字をランダムに並び替えてみます
for i in range(len(intArr)):
    j = random.randint(i, len(intArr) - 1)

    # temporary(仮)の意味
    # i番目をtempに保存し、i番目をj番目で更新し、j番目をtempで更新します。two pointer
    temp = intArr[i]
    intArr[i] = intArr[j]
    intArr[j] = temp

# ランダムに入れ替えた後の配列
print(intArr)
