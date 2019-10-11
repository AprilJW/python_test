import pickle
import json
import msgpack

# 目录[TOC]
# 空行，段落
# [name](地址)
# ![图片描述](地址)
# *倾斜，**加粗，转义\*
# 列表有序 1.
# 列表无序* 空格
# 表格 |列 ----行
# 代码块```python```
# 行内代码块`<span>`
# 右键保存成html
# chrome右键保存成pdf
# 分隔-----

# gitbook init
# 新建md
# gitbook build --gitbook=2.6.7

# xmind思维导图
# 选择文件中的向右
# shift + enter换行
# table 新块
# 可以拖
# 双击新建

# 回车复制

# d = {'a': 1, 'b': 127, 'c': 'aaa', 'd': [1, 2, 3], 'e': True, 'f': None, 'g': ('1',)}
# for m in [pickle, json, msgpack]:
#     j = m.dumps(d)
#     print(m.__name__, '/', type(j), '/', j)
#     if m == json:
#         j = j.replace(' ', '')
#     j_new = m.loads(j)
#     print('__________________')
#     print(m.__name__, '/', type(j_new), '/', j_new)


