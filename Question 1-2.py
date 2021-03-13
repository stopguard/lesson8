r"""
Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
    для получения информации вида:
    (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
    например:
    raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
           "Debian APT-HTTP/1.3 (0.9.7.9)"'
    parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
"""
