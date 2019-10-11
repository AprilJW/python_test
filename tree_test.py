from collections import defaultdict
# a = defaultdict(lambda: 0)
# a['count'] += 1
# print(a)


def modify_dic(dic, new_dic={}, stack=[], count=defaultdict(lambda: 0)):
    if not isinstance(dic, dict):
        #print('222')
        count['count'] += 1
        if count['count'] == 2:
            stack = stack[0:1] + stack[2:]
        if count['count'] == 3:
            stack = stack[-2:]
        if count['count'] == 4:
            stack = stack[-4:]
        new_key = '.'.join(stack)
        new_dic[new_key] = dic
        return new_dic

    for key, value in dic.items():
        stack.append(key)
        modify_dic(value)
    #return new_dic
    #print(new_dic)

dic = {'a':{'b':1, 'c':2}, 'd':{'e':3, 'f':{'g':4}}}
modify_dic(dic)