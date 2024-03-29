
import datetime


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def validate(timeList):
    # timeList = ['0:00:00', '0:00:15', '9:30:56']
    totalSecs = 0
    for tm in timeList:
        timeParts = [int(s) for s in tm.split(':')]
        totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
    totalSecs, sec = divmod(totalSecs, 60)
    hr, min = divmod(totalSecs, 60)
    return "%d:%02d:%02d" % (hr, min, sec)


format = '%H:%M:%S'
n = int(input())
diff_list = [[] for i in range(n)]
for i in range(n):
    m = int(input())
    for j in range(m):
        start,end = map(str, input().split(" "))
        if start.startswith('24:'):
            start = start.replace('24:00', '0:00')
        if end.startswith('24:'):
            end = end.replace('24:00', '0:00')
        startDateTime = datetime.datetime.strptime(start, format)
        endDateTime = datetime.datetime.strptime(end, format)
        # start1 = startDateTime.strftime(format)
        # end1 = endDateTime.strftime(format)
        diff = endDateTime -startDateTime
        diff = convert(diff.total_seconds())
        diff_list[i].append(diff)

for timedata_list in diff_list:
    result = validate(timedata_list)
    print(result)
