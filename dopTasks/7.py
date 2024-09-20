def max_boots(K, n, repair_times):
    repair_times.sort()
    count = 0
    time_worked = 0

    for time in repair_times:
        if time_worked + time <= K:
            count += 1
            time_worked += time
        else:
            break

    return count

with open("input7.txt", "r") as file:
    K, n = map(int, file.readline().split())
    repair_times = list(map(int, file.readline().split()))

result = max_boots(K, n, repair_times)

with open("output7.txt", "w") as file:
    file.write(str(result))
