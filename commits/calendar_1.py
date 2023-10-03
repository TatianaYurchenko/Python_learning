from pprint import pprint
import calendar
import time

cl = calendar.TextCalendar(firstweekday=0)
pprint(cl.formatyear(theyear=2023))

# показывает текущую жату
print(f'текущее время {time.perf_counter()}')
t_start = time.perf_counter()
# здесь код, время/производительность
# которого необходимо замерить
time.sleep(1)
# засекаем время окончания работы скрипта
# или куска кода
all_time = time.perf_counter() - t_start
print(all_time)
