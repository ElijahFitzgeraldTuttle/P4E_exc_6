hours = int(input('input hours:'))
rate = int(input('input rate:'))

def computepay(hours, rate):
    if hours <= 40:
        print('hourly pay', (hours * rate))
    if hours > 40:
        overtime = hours - 40
        weekly_pay = (overtime * (rate * 1.5)) + (40 * rate)
        print(weekly_pay)

computepay(hours, rate)