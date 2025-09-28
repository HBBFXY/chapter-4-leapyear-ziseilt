# 在此处编写代码
def is_leap_year(year):
    """判断是否为闰年"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    """主函数"""
    print("=== 闰年判断程序 ===")
    
    while True:
        try:
            # 获取用户输入
            year_input = input("请输入年份（输入'quit'退出程序）: ")
            
            # 检查是否退出
            if year_input.lower() == 'quit':
                print("程序已退出，再见！")
                break
            
            # 转换为整数（可能抛出ValueError）
            year = int(year_input)
            
            # 检查年份是否合理（年份应该是正整数）
            if year <= 0:
                print("错误：年份必须是正整数！\n")
                continue
            
            # 判断是否为闰年
            if is_leap_year(year):
                print(f"{year}年是闰年！\n")
            else:
                print(f"{year}年不是闰年。\n")
                
        except ValueError:
            # 处理非数字输入
            print("错误：请输入有效的数字年份！\n")
        except Exception as e:
            # 处理其他意外错误
            print(f"发生未知错误：{e}\n")

# 运行程序
if __name__ == "__main__":
    main()
