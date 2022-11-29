import datetime
import time

import allure

now = datetime.datetime.now()


class work_with_time:

    def str_time(self):
        begin_date = self.get_now_date_for_api_g2(timedelta_days=3)
        a = datetime.datetime.strptime(begin_date, "%Y-%m-%dT%H:%M:%SZ")
        bedin_unix = a.timestamp()
        return bedin_unix

    # Возвращяет строку "08.09.2017 10:59"
    def get_time_now(self):
        return now.strftime("%d.%m.%Y %H:%M")

    # Возвращяет строку "080920171059"
    def get_time_now_2(self):
        return now.strftime("%d%m%Y%H%M")

    # Возвращяет строку "2017.08.09 10:59:59"
    def get_date_time_Y_m_d_H_M_S(self):
        return time.strftime("%Y.%m.%d %H:%M:%S")

    # Возвращяет (текущую дату + timedelta_days) ввиде строки "08.09.2017"
    def date_increased_x_days(self, timedelta_days):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        return datetime2.strftime("%d.%m.%Y")

    # Возвращяет (текущую дату + timedelta_days) ввиде строки "08.09.2017"
    def date_add_x_dayTime(self, date, timedelta_days, timedelta_hours):
        datetime2 = date + datetime.timedelta(days=timedelta_days, hours=timedelta_hours)
        return datetime2

    # Возвращает текущую дату
    def get_date_now(self):
        return now.strftime("%d.%m.%Y")

    # Входная строка должна быть вида "08.09.2017 10:00:00"
    def convert_string_to_date(self, string):
        return datetime.datetime.strptime(string, "%d.%m.%Y %H:%M:%S")

    # Входная строка должна быть вида "1959.02.02 00:00:00"
    def convet_string_to_date_2(self, string):
        return datetime.datetime.strptime(string, "%Y.%m.%d %H:%M:%S")

    # Входная дата должна быть вида "2022.09.05 13:32:20"
    # Выходная дата будет в виде "2022-09-05T13:32:20Z"
    def tickets_date(self, string):
        date = datetime.datetime.strptime(string, "%Y.%m.%d %H:%M:%S")
        return date.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Выходная дата будет в виде "2022-09-05T13:32:20Z"
    def tickets_date_minus_2_sec(self, string):
        date = datetime.datetime.strptime(string, "%Y-%m-%dT%H:%M:%SZ") - datetime.timedelta(seconds=2)
        return date.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Выходная дата будет в виде "08.09.2017 10:00:00"
    def convert_date_to_string(self, date):
        return datetime.datetime.strftime(date, "%d.%m.%Y %H:%M:%S")

    # Возвращяет дату "2015-07-25 00:00:00.000"
    def get_date_time_for_sql(self):
        date_text = time.strftime("%Y-%m-%d %H:%M:%S")
        date_text = date_text + '.000'
        return date_text

    # Возвращяет дату "2015-07-25 00:00:00.000"
    def get_date_time_for_sql_increased_x_days(self, timedelta_days):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        temp = datetime2.strftime("%Y-%m-%d %H:%M:%S")
        temp = temp + '.000'
        return temp

    # Возвращяет (текущую дату + timedelta_days) ввиде строки "2018-10-23T11:15:55+03:00"
    def get_date_increased_x_days_json(self, timedelta_days):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        return datetime2.strftime("%Y-%m-%dT%H:%M:%S+03:00")

    def convert_date(self, date):
        new_date = datetime.datetime.strptime(date, '%d.%m.%Y')
        return new_date.strftime("%Y-%m-%dT%H:%M:%S+03:00")

    def convert_date_time(self, date):
        new_date = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M')
        return new_date.strftime("%Y-%m-%dT%H:%M:%S+03:00")

    def convert_date_time_second(self, date):
        new_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        new_date = new_date + datetime.timedelta(hours=3)
        return new_date.strftime("%Y-%m-%dT%H:%M:%S+03:00")

    # Возвращает текущую дату и время ввиде строки 20191001175409
    def get_date_time_Users_API(self):
        return time.strftime("%Y%m%d%H%M%S")

    # Возвращает текущую дату в виде строки 20191001
    def get_date_Users_API(self):
            return time.strftime("%Y%m%d")

    def timestamp_now(self):
        return datetime.datetime.now().timestamp()

    # Возвращает текущую дату ввиде строки '2020-02-18T13:10:01Z'
    def get_date_time_for_api_g2(self, timedelta_days=0):
        datetime2 = now + datetime.timedelta(days=timedelta_days)
        return datetime2.strftime("%Y-%m-%dT%H:%M:%SZ")

    @allure.step('Добавление часа(ов) к текущей дате (Возвращает текущую дату ввиде строки "2020-02-18T13:10:01Z")')
    def get_date_time_for_api_g2_hours(self, timedelta_hours=0):
        datetime2 = now + datetime.timedelta(hours=timedelta_hours)
        return datetime2.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Берёт текущую дату и время, обрезает до даты, переводит в вид строки '2020-02-18T00:00:00Z'
    def get_now_date_for_api_g2(self, timedelta_days=0, timedelta_hours=0, timedelta_minutes=0):
        datetime2 = now + datetime.timedelta(days=timedelta_days, hours=timedelta_hours, minutes=timedelta_minutes)
        return datetime2.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Добавляет к дате формата '2020-02-18T00:00:00Z' - # секунд
    def add_seconds_to_date_for_api_g2(self, date_in, timedelta_seconds=0):
        # Переводим в формат доступный для мат. действий.
        date_time = datetime.datetime.strptime(date_in, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
        time_1 = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")

        result = time_1 + datetime.timedelta(seconds=timedelta_seconds)

        return str(result)

    # передаётся в виде 25.02.2020
    # возвращается в виде 2020-02-25T13:10:01Z
    def convert_date_to_2020_02_18T13_10_01Z(self, date):
        new_date = datetime.datetime.strptime(date, '%d.%m.%Y')
        return new_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Возвращяет (текущую дату + timedelta_days) ввиде строки "08092017_1059"
    def date_time_for_task_calendar(self, timedelta_days=0, timedelta_hours=0, timedelta_minutes=0):
        datetime2 = now + datetime.timedelta(days=timedelta_days, hours=timedelta_hours, minutes=timedelta_minutes)
        return datetime2.strftime("%d%m%Y_%H%M")

    # перевод в unixtime
    def convert_to_unixtime(self, date, form="%Y-%m-%dT%H:%M:%SZ"):
        # перевод строки во время
        str_to_time = datetime.datetime.strptime(date, form)
        unix_time = str_to_time.timestamp()
        return unix_time

    # Возвращяет строку "20170809105959"
    def get_time_now_3(self):
        return time.strftime("%Y%m%d%H%M%S")

    # 0:12:56
    def convert_seconds_in_hms(self, tests_time):
        seconds = float(tests_time) % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return "%d:%02d:%02d" % (hour, minutes, seconds)

    # подаём дату в формате 2023-04-20T17:44:29Z
    # возвращается строка в виде unix_time
    def return_delta_date(self, date_in):
        date = datetime.datetime.strptime(str(date_in), '%Y-%m-%dT%H:%M:%SZ')
        unix_time = date.timestamp()
        return unix_time

    # возвращается строка в виде unix_time
    def get_timestamp_unix_time(self):
        return now.timestamp()

    # Добавить/Убрать # мин. к дате. Начальный формат даты %Y-%m-%dT%H:%M:%SZ или %Y-%m-%d %H:%M:%S (В convert_format указывать: '%Y-%m-%d %H:%M:%S' или '%Y-%m-%dT%H:%M:%S+03:00' или другой похожий формат)
    def update_time_in_date_in(self, date_in, amount_minutes, convert_format):
        date = datetime.datetime.strptime(str(date_in), convert_format)
        return date + datetime.timedelta(minutes=amount_minutes)

    # Преобразовать в обычный datetime из формата '%Y-%m-%d %H:%M:%S' (В convert_format указывать: '%Y-%m-%d %H:%M:%S' или '%Y-%m-%dT%H:%M:%S+03:00' или другой похожий формат)
    def convert_to_correct_datetime_from_format_in(self, date_in, convert_format):
        return datetime.datetime.strptime(str(date_in), convert_format)

    # Преобразовать в обычный datetime формата '%Y-%m-%d %H:%M:%S' или '%Y-%m-%dT%H:%M:%S+03:00' из формата String (В convert_format указывать: '%Y-%m-%d %H:%M:%S' или '%Y-%m-%dT%H:%M:%S+03:00' или другой похожий формат)
    def convert_to_correct_datetime_from_string(self, date_in, convert_format):
        return datetime.datetime.strptime(date_in, convert_format)

    @allure.step('Преобразовать из формата "%Y-%m-%dT%H:%M:%SZ" в формат "%Y-%m-%d %H:%M:%S" для сравнений')
    def convert_json_datetime_into_default_datetime(self, date_in):
        x = datetime.datetime.strptime(date_in, '%Y-%m-%dT%H:%M:%SZ')
        return x.strftime('%Y-%m-%d %H:%M:%S')

    @allure.step('Определить кол-во секунд между двумя датами (Формат дат на вход "%Y-%m-%dT%H:%M:%SZ")')
    def determinate_time_interval_between_dates(self, begin_date, end_date):

        # Подготавливаем переменные времени для опр. временного промежутка

        # Переводим формат даты '%Y-%m-%dT%H:%M:%SZ' в формат '%Y-%m-%d %H:%M:%S'
        time = datetime.datetime.strptime(begin_date, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
        # Переводим переменную time из типа String в тип datetime (Формат '%Y-%m-%d %H:%M:%S') для возможности производить операции
        time_1 = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        # Переводим формат даты '%Y-%m-%dT%H:%M:%SZ' в формат '%Y-%m-%d %H:%M:%S'
        time = datetime.datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
        # Переводим переменную time из типа String в тип datetime (Формат '%Y-%m-%d %H:%M:%S') для возможности производить операции
        time_2 = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")

        # Определяем временной промежуток между датами
        time_interval = time_2 - time_1

        # Определяем кол-во секунд в временном промежутке
        total_minutes = abs(time_interval.total_seconds())

        return total_minutes
