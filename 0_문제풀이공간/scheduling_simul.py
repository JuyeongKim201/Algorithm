running_recent_cpu = 1
ready_recent_cpu = 1
decay = 0.8

for i in range(100):
    runnirunning_recent_cpung = decay * (running_recent_cpu + 1)
    ready_recent_cpu = decay * ready_recent_cpu
    print(f'running: {running_recent_cpu}')
    print(f'ready: {ready_recent_cpu}')
    


