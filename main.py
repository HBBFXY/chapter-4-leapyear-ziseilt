year_input = input("请输入一个年份: ")

try:
    # 转换为整数
    year = int(year_input)

    # 判断闰年规则
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("是闰年")
    else:
        print("不是闰年")

except ValueError:
    # 处理非数字输入
    print("输入错误: 请输入有效的年份数字")
