import random

def game1():
    playerScore = 0
    computerScore = 0
    for i in range(3):
        player = input("请输入石头剪刀布：")
        computer = random.choice(["石头","剪刀",'布'])
        print("电脑出了:",computer)
        if player == computer:
            continue
        elif player == '石头' and computer == '剪刀' or player == '剪刀' and computer == '布' or player == '布' and computer == '石头':
            playerScore += 1
        else:
            computerScore += 1
        print("玩家分数%d,电脑分数%d" % (playerScore,computerScore))

    if playerScore == computerScore:
        print("平局")
    elif playerScore > computerScore:
        print("玩家胜利")
    else:
        print("电脑胜利")


def guessNum():
    num = random.randint(1, 100)
    while True:
        playerNum = int(input("请输入一个整数"))
        if playerNum == num:
            print("猜对了")
            break
        elif playerNum > num:
            print("猜大了")
        else:
            print("猜小了")


def main():
    guessNum()




