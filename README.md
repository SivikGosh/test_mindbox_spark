# test_mindbox_spark

Реализовано с Python версии 3.12

## Установка и запуск

```bash
$ git clone git@github.com:SivikGosh/test_mindbox_spark.git

$ cd test_mindbox_spark/

$ python3.12 -m venv venv

$ source venv/bin/activate

(venv) $ pip3 install -r requirements.txt

(venv) $ python main.py

```

### Ответ

```
+--------------+-------------------+
|       product|           category|
+--------------+-------------------+
|      Наушники|        Электроника|
|      Наушники|               NULL|
|       Ноутбук|        Электроника|
|       Ноутбук|               NULL|
|   Холодильник|        Электроника|
|   Холодильник|    Бытовая техника|
| Фитнес-трекер|Портативная техника|
| Фитнес-трекер|             Фитнес|
|4K экшн-камера|        Электроника|
|4K экшн-камера|        Фототехника|
+--------------+-------------------+
```
