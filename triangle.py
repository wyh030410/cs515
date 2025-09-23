def triangle(n):
    if n == 0:
        return []
    else:
        smaller_triangle = triangle(n - 1)
        bottom_row = " ".join(["*"] * n)
        return smaller_triangle + [bottom_row]


def show_triangle(n):
    if n == 0:
        return
    rows = triangle(n)
    formatted_rows = []
    for i, row in enumerate(rows):
        spaces = " " * (n - i - 1)
        formatted_rows.append(spaces + row)
    print("\n".join(formatted_rows))

