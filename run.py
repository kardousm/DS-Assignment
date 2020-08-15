import re


def create_list():
    temp = 1
    intervals = []
    f = open('1.in', 'r')
    f1 = f.readlines()
    for line in f1:
        if temp == 1:
            temp += 1
            pass
        else:
            x = re.sub('\s+', ",", line.strip())
            int_interval = convert_str_to_int(x)
            intervals.append(int_interval)
    return intervals

def convert_str_to_int(s):
    x = s.split(',')
    x[0] = int(x[0])
    x[1] = int(x[1])
    return x


def combine(time_intervals):
    temporary_list = time_intervals.copy()
    temporary_list.sort(key=lambda x: x[0])
    y = 1
    while y < len(temporary_list):
        if temporary_list[y][0] <= temporary_list[y - 1][1]:
            temporary_list[y - 1][1] = max(temporary_list[y - 1][1], temporary_list[y][1])
            temporary_list.pop(y)
        else:
            y += 1
    return temporary_list

def compute(final_intervals):
    val = 0
    for item in final_intervals:
        val += item[1] - item[0]
    return val


def run():
    untouched_list = create_list()
    max_coverage = 0
    max_time_interval = None
    for i in range(len(untouched_list)):
        temp = untouched_list[i]
        touched_list = [x[:] for x in untouched_list]
        touched_list.pop(i)
        new_interval = combine(touched_list)
        coverage = compute(new_interval)
        print('{}% Completed'.format((i / len(untouched_list)) * 100))
        if coverage > max_coverage:
            max_coverage = coverage
            max_time_interval = untouched_list[i]


    #max_time_interval gives you the time interval of the life guard who has minimum impact on pool coverage

    f = open('1.out', 'w+')
    f.write(str(max_coverage))

    return max_coverage


if __name__ == "__main__":
    run()
