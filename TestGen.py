import random, os

base = os.path.dirname(__file__) # đường dẫn hiện t
number = int(input("Nhập số lượng cần random: ")) # number = 1000000
Min = float(input("Nhập số bé nhất: "))           # Min = -1000000
Max = float(input("Nhập số lớn nhất: "))          # Max = 1000000

# test1: mảng tăng dần số nguyên
arr = [random.randint(int(Min), int(Max)) for _ in range(number)]
arr.sort()
f = open(os.path.join(base, "test", "test1.txt"), "w")
for x in arr:
    f.write(str(x) + " ")
f.close()

# test2: mảng giảm dần số thực
arr = [random.uniform(Min, Max) for _ in range(number)]
arr.sort(reverse=True)
f = open(os.path.join(base, "test", "test2.txt"), "w")
for x in arr:
    f.write(str(x) + " ")
f.close()

# test3 → test10
for i in range(3, 11):
    f = open(os.path.join(base, "test", f"test{i}.txt"), "w")

    if i % 2 == 1:
        arr = [random.randint(int(Min), int(Max)) for _ in range(number)]
    else:
        arr = [random.uniform(Min, Max) for _ in range(number)]

    for x in arr:
        f.write(str(x) + " ")

    f.close()
