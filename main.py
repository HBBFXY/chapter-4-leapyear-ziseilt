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
            year_input = input("请输入年份: ")
            
            # 检查是否为空输入
            if year_input.strip() == "":
                print("输入错误")
                continue
            
            # 转换为整数（可能抛出ValueError）
            year = int(year_input)
            
            # 判断是否为闰年（包括0和负数）
            if is_leap_year(year):
                print(f"{year}年是闰年")
            else:
                print(f"{year}年不是闰年")
                
        except ValueError:
            # 处理非数字输入（包括浮点数）
            print("输入错误")
        except Exception as e:
            # 处理其他意外错误
            print(f"输入错误")

# 运行程序
if __name__ == "__main__":
    main()
