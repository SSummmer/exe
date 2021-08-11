"""
    挑战题1
"""
log_list = []
num_list = []
with open('aur.log', 'r') as logfile:
    data = logfile.readlines()
    for row in data:
        logdata = str(row).split(' ')
        if logdata[0] not in log_list:
            log_list.append(logdata[0])
            num_list.append(1)
        else:
            index = log_list.index(logdata[0])
            num_list[index] = int(num_list[index]) + 1

with open('ip_count.csv', 'w') as targetfile:
    targetfile.write(','.join(['ip', 'count\n']))
    for i in range(len(log_list)):
        targetfile.write(','.join([log_list[i], str(num_list[i]) + '\n']))
