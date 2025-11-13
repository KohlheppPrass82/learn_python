# 列表推导式示例
squares = [x ** 2 for x in range(1, 6)]
print("1~5 的平方:", squares)

# 带条件的推导式
evens = [n for n in range(1, 11) if n % 2 == 0]
print("1~10 的偶数:", evens)

# 嵌套推导式（笛卡尔积）
colors = ['red', 'green']
sizes = ['S', 'M', 'L']
tshirts = [(c, s) for c in colors for s in sizes]
print("T 恤组合:", tshirts)