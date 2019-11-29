from django.db import models

# Create your models here.

class Employee(models.Model):
    class Meta:
        db_table = 'employees'
    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField(null=False)
    first_name = models.CharField(null=False, max_length=14)
    last_name = models.CharField(null=False, max_length=16)
    gender = models.SmallIntegerField(null=False)
    hire_date = models.DateField(null=False)

    @property
    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __repr__(self):
        return '< Employee: {} {} {}>'.format(self.emp_no, self.first_name, self.last_name)

    __str__ = __repr__


class Salary(models.Model):
    class Meta:
        db_table = 'salaries'
    id = models.AutoField(primary_key=True)  # 额外增加一个主键
    emp_no = models.ForeignKey('Employee',
                               on_delete=models.CASCADE,
                               null=False,
                               db_column='emp_no',
                               related_name='salaries')

    from_date = models.DateField(null=False)
    salary = models.IntegerField(null=False)
    to_date = models.DateField(null=False)

    def __repr__(self):
        return "<Salary: {} {} {}>".format(
            self.emp_no, self.from_date, self.salary)

    __str__ = __repr__


class Department(models.Model):
    class Meta:
        db_table = 'departments'

    dept_no = models.CharField(null=False, max_length=4)
    dept_name = models.CharField(null=False, max_length=40, unique=True)

    def __repr__(self):
        return "<Department: {} {}>".format(self.dept_no,
                                            self.dept_name)


class Dept_emp(models.Model):
    id = models.AutoField(primary_key=True)
    emp_no = models.ForeignKey('Employee', on_delete=models.CASCADE,
                               db_column='emp_no')
    dept_no = models.ForeignKey(to='Department', on_delete=models.CASCADE,
                                max_length=4,
                                db_column='dept_no',)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=False)

    class Mete:
        db_table = 'dept_emp'

    def __repr__(self):
        return "<DeptEmp: {} {}>".format(self.emp_no, self.dept_no)

    __str__ = __repr__

class Title(models.Model):
    class Meta:
        db_table = 'titles'
    emp_no = models.IntegerField(null=False, max_length=11)
    title = models.CharField(null=False, max_length=50)
    from_date = models.DateField(null=False)
    to_date = models.DateField(null=True, default=None)
    id = models.AutoField(max_length=11, primary_key=True)

    def __repr__(self):
        return "<Title: {} {}>".format(self.emp_no, self.title)

    __str__ = __repr__
