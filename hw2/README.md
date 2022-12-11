## ДЗ 2 ##


### Запуск докер образа ###

1) Докер должен быть установлен и запущен.

2) Для сборки и запуска образа используются следующие команды:

Сборка
```
 docker build -t mtu -f Dockerfile .
```

Запуск
```
 docker run --rm -p 8080:8080 -it mtu
```
Запуск кода
```
python3 main.py имя_хоста
```

Пример вывода для host=ya.ru
```
Checked host format.
ICMP is enabled.
Searching MTU...
MTU = 1500
```
