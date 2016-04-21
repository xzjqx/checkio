import datetime

def getWeek(day):
    if day == 1:
        return 'Monday'
    elif day == 2:
        return 'Tuesday'
    elif day == 3:
        return 'Wednesday'
    elif day == 4:
        return 'Thursday'
    elif day == 5:
        return 'Friday'
    elif day == 6:
        return 'Saturday'
    else:
        return 'Sunday'

def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    days = []
    first = datetime.date(year,1,1)
    end = datetime.date(year,12,31)
    f = first.isoweekday()
    e = end.isoweekday()
    if f == e:
        days.append(getWeek(f))
    else:
        if f > e:
            tmp = f
            f = e
            e = tmp
        days.append(getWeek(f))
        days.append(getWeek(e))

    return days

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
