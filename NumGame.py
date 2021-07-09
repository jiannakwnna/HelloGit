import random


def redman(minnum, maxnum):
    random.randint(minnum, maxnum)
    # 库函数 random与程序内变量冲突





while (1 == 1):
    print("正在初始化变量...")
    maxnum = 100
    minnum = 0
    random = int(redman(maxnum, minnum))
    bu = 1
    VICTORY = "false"
    while "false" == VICTORY:
        print("变量初始化完毕，游戏正式开始！")
        shuru: int = input("请输入一个数字，范围是%d到%d" % (maxnum, minnum))
        if random == shuru:
            VICTORY = "true"
            print("恭喜您，您赢了！您使用了%d步，游戏正在重新开始" % (bu))
        elif shuru > random and shuru < maxnum:
            print("您的输入大于答案！")
            maxnum = shuru
            bu + 1
        elif (shuru < random and shuru > minnum):
            print("您的输入小于答案！")
            minnum = shuru
            bu + 1
        else:
            print("请输入范围内的数字!")
