def triangle(n):
    """
    递归函数，返回包含n行三角形字符串的列表
    每一行都有适当的空格和星号
    """
    if n == 0:
        # 基础情况：0行返回空列表
        return []
    else:
        # 递归情况：先构建前n-1行的三角形
        smaller_triangle = triangle(n - 1)

        # 然后添加第n行（最底下的一行）
        # 第n行有0个前导空格，n个星号用空格分隔
        bottom_row = " ".join(["*"] * n)

        return smaller_triangle + [bottom_row]


def show_triangle(n):
    """
    打印一个漂亮的三角形
    参数 n: 三角形的行数
    """
    if n == 0:
        # 如果n为0，不打印任何内容
        return

    # 获取三角形的所有行
    rows = triangle(n)

    # 需要给每一行添加正确的前导空格
    # 第i行（从1开始）需要(n-i)个前导空格
    formatted_rows = []
    for i, row in enumerate(rows):
        spaces = " " * (n - i - 1)
        formatted_rows.append(spaces + row)

    # 用换行符连接所有行并打印
    print("\n".join(formatted_rows))


show_triangle(5)  # 打印一个5行的三角形