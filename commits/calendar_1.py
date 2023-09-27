from pprint import pprint
import calendar

cl = calendar.TextCalendar(firstweekday=0)
pprint(cl.formatyear(theyear=2023))

