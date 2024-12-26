# # ЗАДАЧА 1

# import logging

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# debug_info_handler = logging.FileHandler('debug_info.log')
# debug_info_handler.setLevel(logging.DEBUG)
# debug_info_handler.setFormatter(formatter)
# logger.addHandler(debug_info_handler)

# warnings_errors_handler = logging.FileHandler('warnings_errors.log')
# warnings_errors_handler.setLevel(logging.WARNING)
# warnings_errors_handler.setFormatter(formatter)
# logger.addHandler(warnings_errors_handler)

# logger.debug('Это сообщение уровня DEBUG.')
# logger.info('Это сообщение уровня INFO.')
# logger.warning('Это сообщение уровня WARNING.')
# logger.error('Это сообщение уровня ERROR.')
# logger.critical('Это сообщение уровня CRITICAL.')


# # ЗАДАЧА 2

# from datetime import datetime

# def display_current_datetime():
#     now = datetime.now()

#     formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

#     day_of_week = now.strftime('%A')
#     week_number = now.isocalendar()[1]

#     print(f'Current date and time: {formatted_date}')
#     print(f'Day of the week: {day_of_week}')
#     print(f'Week number: {week_number}')

# if __name__ == '__main__':
#     display_current_datetime()


# # ЗАДАЧА 3

# from datetime import datetime, timedelta

# def fuuture_date(days_from_now):
    
#     today = datetime.now()

#     future_date = today + timedelta(days=days_from_now)

#     formatted_future_date = future_date.strftime('%Y-%m-%d')

#     return formatted_future_date

# if __name__ == '__main__':
#     days = 30
#     print(f'Date {days} days from now: {fuuture_date(days)}')



# # ЗАДАЧА 4

# import argparse

# def main():
#     parser = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями')
#     parser.add_argument('number', type=int, help='Число для вывода')
#     parser.add_argument('text', type=str, help='Строка для вывода')

#     parser.add_argument('--verbose', action='store_true',
# help='Вывод дополнительно информации')
#     parser.add_argument('--repeat', type=int, default=1,
# help='Количество повторений строки')
    
#     args = parser.parse_args()

#     if args.verbose:
#         print(f'Полученные аргументы: number={args.number}, text"{args.texs}", repeat={args.repeat}')

#         print(f'Число: {args.number}, Строка: {args.text * args.repeat}')

# if __name__ == '__main__':
#     main()



# ЗАДАЧА 5

import os 
import logging
from collections import namedtuple
from argparse import ArgumentParser

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def collect_info(directory_path):
    if not os.path.isdir(directory_path):
        raise ValueError(f"Указанный путь {directory_path} не является директорией")
    
parent_directory =os.path.basename(os.path.abspath(directory_path))

for entry in os.listdir(directory_path):
    enrty_path = os.path.join(directory_path, entry)

    if os.path.isdir(enrty_path):
        file_info = FileInfo(name=entry, extension=None, is_directory=True, parent_directory=parent_directory)

    else:
        name, exception = os.path.splitext(entry)
        file_info = FileInfo(name=name, extension=exception.lstrip('.'), is_directory=False, parent_directory=parent_directory)

        logging.info(f'{file_info.name} | {file_info.extension if file_info.extension else "N/A"} | {"Directory" if file_info.is_directory else "False"} | {file_info.parent_directory}')

def main():
    parser = ArgumentParser(description="Сбор информации о содержимом директории и запись в лог")
    parser.add_argument('directory', type=str, help="Путь до директории для анализа")

    args = parser.parse_args()
    parent_directory = args.directory

    try:
        collect_info(directory_path)
        print(f'Информация о содержимом директории "{directory_path}" успешно записана в файл "directory_contents.log".')
    
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()