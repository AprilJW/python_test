import os
import django

# 参考wsgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salary.settings')
django.setup()

from employee.models import Employee, Salary, Department, Title

mgr = Employee.objects



# 字段查询表达式（Field Lookup）
# 字段查询可以作为filter() exclude() get()的参数，相当于where语句

# 比较运算符的用法
# iexact, icontains, istartswith, iendswith,表示匹配时忽略大小写
# 精确匹配出一条数据
# print(mgr.filter(emp_no__exact=10001))


# 用的不多，emp_no字段中只要包含5，就都选出来，相当于like%5%
# print(mgr.filter(emp_no__contains='5'))
# print(mgr.filter(emp_np__startswith='5'))
# print(mgr.filter(emp_no_endswith='5'))

# 选出不是null的数据
# print(mgr.filter(emp_no__isnull=False))
# print(mgr.filter(emp_no__isnotnull=False))

# 查询范围
# print(mgr.filter(emp_no__in=[10001, 10005]))
# print(mgr.filter(emp_no__gt=10005))
# print(mgr.filter(emp_no__gte=10005))
# print(mgr.filter(emp_no__lt=10005))
# print(mgr.filter(emp_no__lte=10005))
# from datetime import date
# print(mgr.filter(hire_date__gt=date(1991, 1, 1)))

# 选出指定时间或者日期字段的year，month, day, week_day, hour, minute, second
# print(mgr.filter(hire_date__month=1))


# Q对象实现与或非条件
from django.db.models import Q
# 与
# print(mgr.filter(pk__gt=10003).filter(pk__lt=10006))
# print(mgr.filter(pk__gt=10003, pk__lt=10006))
# print(mgr.filter(Q(pk__gt=10003) & Q(pk__gt=10006)))

# 或
# print(mgr.filter(Q(pk=10003) | Q(pk__exact=10006)))
# print(mgr.filter(pk__in=[10003, 10006]))

# 非
# print(mgr.filter(~Q(pk=10001)))


# 聚合、分组
from django.db.models import Q, Avg, Sum, Max, Min, Count

# print(mgr.filter(pk__gt=10005).count())  # 返回单值 15
# print(mgr.filter(pk__gt=10005).aggregate())  # 只是查询了一次，返回空字典
# print(mgr.filter(pk__gt=10005).aggregate(Count('pk')))
# print(mgr.filter(pk__gt=10005).aggregate(Avg('pk')))
# print(mgr.filter(pk__gt=10005).aggregate(Max('pk')))
# print(mgr.filter(pk__gt=10005).aggregate(Min('pk')))
# print(mgr.filter(pk__gt=10005).aggregate(Sum('pk')))

# # 返回的字典 {'pk__min': 10001, 'pk__max': 10020}
# print(mgr.aggregate(Min('pk'), Max('pk')))
#
# # 起别名 {'min': 10001, 'max': 10020}
# print(mgr.aggregate(min=Min('pk'), max=Max('pk')))


# s = mgr.filter(pk__gt=10005).values().aggregate(Count('pk'))
# print(s)  # 用不用values，s都是一个字典{'pk__count': 15}


# # 分组聚合返回查询集
# # s = mgr.filter(pk__gt=10005).annotate()  # 不加参数默认使用主键分组，非空，返回大于10005的查询集QuerySet
# s = mgr.filter(pk__gt=10005).annotate(Count('pk'))
# for x in s:
#     print(x)
#     print(x.__dict__)  # 分组聚合后，字典里面多了一个'pk__count': 1属性


# 分组聚合返回查询集，增加values方法
# filter返回结果是QuerySet中存放的对象
# 加上values，则是返回QuerySet中存放的字典
#


# s = mgr.filter(pk__gt=10005).values().annotate(Count('pk'))
# for i in s:
#     print(i)  # 分组聚合后，字典里面多了一个'pk__count': 1属性



# # 给values中加参数练习，
# # 只取出性别字段
# s = mgr.filter(pk__gt=10005).values('gender')
# s = mgr.filter(pk__gt=10005).values('gender').annotate()  #默认使用主键进行分组
# # 根据gender分组，根据gender聚合
# s = mgr.filter(pk__gt=10005).values('gender').annotate(c=Count('gender')).order_by('-c')
# print(s)  # <QuerySet [{'gender': 1, 'c': 8}, {'gender': 2, 'c': 7}]>

# Django 只支持单一主键
sala_mgr = Salary.objects
# print(sala_mgr.filter(emp_no_id__lt=10002).values())
# print(*Salary.__dict__.items(), sep='\n')
# print('~~~~~~~')
# print(*Employee.__dict__.items(), sep='\n')

# 查询10004员工所有工资
# print(mgr.filter(pk=10004).salary_set)  # 结果集没有salary_set属性，实例才有这个属性
# print(mgr.get(pk=10004))  # 一个
# print(mgr.get(pk=10004).salary_set.all())
# print(mgr.get(pk=10004).salaries.all())
# print(mgr.get(pk=10004).salaries.values('emp_no', 'salary', 'from_date'))  # 投影

# print(type(mgr.get(pk=10004).salaries))  # mgr
# 10004 号员工，工资大于55000的记录
# print(mgr.get(pk=10004).salaries.filter(salary__gt=55000).all())

# 方法2
# salmgr = Salary.objects
# slist = list(salmgr.filter(emp_no=10004))
# print('slist:', slist)
# if slist:
#     first = slist[0]
#     emp = first.emp_no
#     for s in slist:
#         print(emp.pk, emp.name, s.emp_no_id, s.salary)


salmgr = Salary.objects
# slist = list(salmgr.filter(emp_no=10004))
#
# if slist:
#     for s in slist:
#         print(s.emp_no.pk, s.emp_no.name, s.emp_no_id, s.salary)

# 发了工资的员工
# print(sala_mgr.values('emp_no').distinct())
# 工资大于55000的所有员工姓名,2种写法

# print(mgr.filter(emp_no__in=sala_mgr.filter(salary__gt=55000).values('emp_no').distinct()))
# print(mgr.filter(emp_no__in=[d.get('emp_no') for d in sala_mgr.filter(salary__gt=55000).values('emp_no').distinct()]))


# # 查询10010号员工所在部门编号及员工信息
empmgr = Employee.objects
# deptmgr = Department.objects
#
# emp = empmgr.filter(pk=10010).get()  # < Employee: 10010 Duangkaew Piveteau>
# # print(emp)
# depts = emp.dept_emp_set.all()
# # print(*Employee.__dict__.items(), sep='\n')
# # for x in depts:
#     # print(type(x), x)
#     # e = x.emp_no
#     # print(type(e), e)
#     # d = x.dept_no
#     # print(type(d), d)
#     # print()

tilmgr = Title.objects
# print(tilmgr.all())

sql = """select t.id, t.emp_no, t.title from titles t join employees e on t.emp_no=e.emp_no;
"""
# print(type(tilmgr.raw(sql)))
for x in tilmgr.raw(sql):
    if x.emp_no == 10009:
        print(x.emp_no, x.title)


