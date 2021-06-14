import sys
import csv
from datetime import datetime


def read_log(file_name):
    with open(file_name, 'r', encoding="utf-8-sig") as f:
        c = 0
        dicts = []
        global v_bar, v_w
        for line in f:
            if c == 1:
                v_bar = int(line.strip().split()[0])
            elif c == 2:
                v_w = int(line.strip().split()[0])
            elif c > 2:
                d = process_log_line(line)
                dicts.append(d)
            c += 1
        print(dicts)
    return dicts


def process_log_line(line):
    temp = line.strip().split()
    date = temp[0][:-1]
    #date = datetime.fromisoformat(temp[0][:-1])
    if 'top' in line:
        action = 'top'
    else:
        action = 'scoop'
    vol = int(temp[-2][:-1])
    if 'успех' in line:
        result = 'success'
    else:
        result = 'failure'
    k = [date, action, vol, result]
    d = {'date': date, 'action': action, 'vol': vol, 'result': result}
    return d


def process_data(data, date1, date2):
    print(len(data))
    numb_top_up, errors, v_up, v_not_up, numb_scoop, v_scoop, v_not_scoop, v_end_period = 8*[0]
    v_beg_period = v_w
    for i in range(len(data)):
        period = datetime.fromisoformat(data[i]['date'])
        #print(period)
        if date2 > period > date1:
            if data[i]['action'] == 'top':
                numb_top_up += 1
            elif data[i]['result'] == 'failure':
                errors += 1
            elif data[i]['action'] == 'top' and data[i]['result'] == 'success':
                v_up += data[i]['vol']
            elif data[i]['action'] == 'top' and data[i]['result'] == 'failure':
                v_not_up += data[i]['vol']
            elif data[i]['action'] == 'scoop':
                numb_scoop += 1
            elif data[i]['action'] == 'scoop' and data[i]['result'] == 'success':
                v_scoop += data[i]['vol']
            elif data[i]['action'] == 'scoop' and data[i]['result'] == 'failure':
                v_not_scoop += data[i]['vol']

        if date1 > period and data[i]['result'] == 'success':
            if data[i]['action'] == 'top':
                v_beg_period += data[i]['vol']
            elif data[i]['action'] == 'scoop':
                v_beg_period -= data[i]['vol']

    v_end_period = v_beg_period + v_up - v_scoop
    errors = round(100 * errors / len(data), 2)
    return numb_top_up, errors, v_up, v_not_up, numb_scoop, v_scoop, v_not_scoop, v_beg_period, v_end_period


def main():
    try:
        log_name = sys.argv[1]
        date1 = datetime.strptime(sys.argv[2], "%Y-%m-%dT%H:%M:%S")
        date2 = datetime.strptime(sys.argv[3], "%Y-%m-%dT%H:%M:%S")
        #print(date1,'\n',date2)
    except IndexError:
        print('incorrect arguments')
    else:
        data = read_log(log_name)
        print(process_data(data, date1, date2))


if __name__ == "__main__":
    main()
