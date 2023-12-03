# print(2**14)

load_avg = 0
ready_threads = 100

for i in range(100):
    load_avg = (59/60)*load_avg + (1/60)*ready_threads
    print(f'load_avg: {load_avg} | ready_threads 대비 %: {load_avg/ready_threads*100}')

print('----------------------------')
print('----------------------------')

# for i in range(100):
#     ready_threads += 2
#     load_avg = (59/60)*load_avg + (1/60)*ready_threads
#     print(f'load_avg: {load_avg} | ready_threads 대비 %: {load_avg/ready_threads*100}')    
