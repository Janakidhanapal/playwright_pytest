from enum import Enum


class TableHeader(str, Enum):
    FIRSTNAME = 'First Name'
    LASTNAME = 'Last Name'
    AGE = 'Age'
    EMAIL = 'Email'
    SALARY = 'Salary'
    DEPARTMENT = 'Department'
    ACTION = 'Action'
