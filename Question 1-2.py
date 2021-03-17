r"""
Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
    для получения информации вида:
    (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
    например:
    raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
           "Debian APT-HTTP/1.3 (0.9.7.9)"'
    parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
"""
import re

# ЧИТАЕМ СОДЕРЖИМОЕ ЛОГ-ФАЙЛА
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    log_str = f.read()

# ПАРСИМ
# Линк на регулярку https://regex101.com/r/gDdBLg/1
RE_PARSE = (r'^(\b.*\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+).*$|^$')                         # регулярка для парсинга
parse_lst = list(re.findall(RE_PARSE, log_str, re.MULTILINE))

# ВЫВОДИМ РЕЗУЛЬТАТ
print(*parse_lst, sep='\n')

# ПРОВЕРКА НА НЕЗАХВАЧЕННЫЕ СТРОКИ
log_lst = log_str.split('\n')
print(f'log_str lines:  {len(log_lst)}\n'   # количество строк в файле
      f'RE_PARSE lines: {len(parse_lst)}')  # количество элементов в результате парсинга

# ВЫВОДИМ СТРОКИ, КОТОРЫЕ НЕ УДАЛОСЬ РАСПАРСИТЬ ЕСЛИ ОНИ ЕСТЬ
for line in log_str.split('\n'):
    parse_str = re.findall(RE_PARSE, line)
    if not parse_str:
        print(f'Строка которую не удалось распарсить: ({line})')
