import msvcrt
import time

done = False
currtime = 0
log = []
while not done:
    c = msvcrt.getch()
    if c == b'\x1b':
        print("END LOGGING")
        break
    if len(log) == 0: 
        currtime = time.time()
        new_time = currtime
    else:
        new_time = time.time()
    log.append((c,new_time-currtime))
    currtime = new_time

print("LOG")
# print(*log, sep = '\n')

data = {}
for i in range(1,len(log)):
    if (log[i-1][0],log[i][0]) not in data:
        data[(log[i-1][0],log[i][0])] = [log[i][1]]
    else:
        data[(log[i-1][0],log[i][0])].append(log[i][1])
# print(data)

model = {}
for k,v in data.items():
    model[k] = (min(v),max(v))
print(model)