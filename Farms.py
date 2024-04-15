import sys
index  =  0
for line in sys.stdin:
    index+=1
    if index == 1:
        continue
    if index == 2:

        close_times = [int(x) for x in line.strip().split(' ')]
        continue
    if index == 3:
        visit_times = [int(x) for x in line.strip().split(' ')]
        continue

    order= [i for i in range(0,len(visit_times))]
    neworder = []
    starting = [int(x) for x in line.strip().split(' ')][0]
    expected = [int(x) for x in line.strip().split(' ')][1]
    actual_times = [time+starting for time in visit_times]
    new_actual_times = actual_times[:]
    new_close_times = close_times[:]
    for i in range(0,len(actual_times)):
        if actual_times[i]>close_times[i]:
            new_close_times.remove(close_times[i])
            new_actual_times.remove(actual_times[i])
            order.remove(i)
    max_farms = len(order)
    for i in range(0,len(new_close_times)):
        for j in range(i,len(new_close_times)):
            if not i == j:
                if new_actual_times[j] < new_close_times[i]:
                    max_farms -=1
    if max_farms<=expected:
        print("YES")
    else:
        print("NO")