from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime



def now_utcnow():
    print('Запуск функции now_utcnow()')
    print(f'Текущая дата и время: {datetime.now()}')
    print(f'Текущая дата и время UTC: {datetime.utcnow()}\n')

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    now_utcnow()