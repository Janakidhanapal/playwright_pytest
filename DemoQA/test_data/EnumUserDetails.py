from enum import Enum


class UserDetails(str, Enum):
    FIRSTNAME = 'firstname'
    LASTNAME = 'lastname'
    AGE = 'age'
    EMAIL = 'email'
    SALARY = 'salary'
    DEPARTMENT = 'department'
