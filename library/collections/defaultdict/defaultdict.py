'''
defaultdict是collections模块中的一个类。
defaultdict时，我们可以指定一个默认的值类型，并且当我们访问一个不存在的键时，它会返回这个默认值。

'''
from collections import defaultdict
from icecream import ic

a = defaultdict(int)

ic(a)
ic(a.get(100))
ic(a.get(100,0))
ic(a[100])

b = defaultdict(lambda: 0)

ic(b)
ic(b.get(100))
ic(b[100])
ic(b.get(100,0))
ic(b[100])


# 创建一个defaultdict，指定默认值为lambda返回的空列表
d = defaultdict(lambda: [])

d['a'].append(1)
d['b'].append(2)
d['a'].append(3)

ic(d['a'])  # 输出: [1, 3]
ic(d['b'])  # 输出: [2]
# 当我们访问一个不存在的键时，defaultdict会返回一个空列表。我们可以通过append方法向列表中添加元素。
ic(d['c'])  # 输出: []