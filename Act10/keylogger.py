import msvcrt
import time

def logger(name):
    print("LOGGING..."+name)
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

    data = {}
    for i in range(1,len(log)):
        if (log[i-1][0],log[i][0]) not in data:
            data[(log[i-1][0],log[i][0])] = [log[i][1]]
        else:
            data[(log[i-1][0],log[i][0])].append(log[i][1])

    model = {}
    for k,v in data.items():
        # model[k] = (min(v),max(v))
        model[k] = sum(v)/len(v)

    return model

def knn(data,test, sens, percent):
    dif = []
    count = 0
    for k in test.keys():
        if k in data:
            dif.append((k,abs(data[k]-test[k])))
    for d in dif:
        if d[1] <= sens: count += 1
    
    treshold = int(len(test) * percent)
    print(len(test), treshold, count)
    if count >= treshold:
        print("Similar to fingerprint")
    else:
        print("Different from fingerprint")

fingerprint = logger('fingerprint')
testcase = logger('testcase')
knn(fingerprint, testcase, 0.05, 0.6) #sens, acc 