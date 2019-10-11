#-*-coding: UTF-8 -*-

from multiprocessing import Process
import os

def run_proc(child_process):
    print('Run child process %s %s' % (child_process, os.getpid()))

print('Parent process %s' % os.getpid())
p = Process(target=run_proc, args=('test',))
p.start()
p.join()
print('Child process end')

from multiprocessing import Pool
import time, random

def long_time_task(name):
    print('Run task %s %s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s run %0.2f seconds' % (name, (end-start)))

if __name__ =='__main__':
    print('Parent process %s' % os.getpid())
    #p = Process(target=long_time_task, args=('child',))
    p = Pool(3)

    print('Waiting for all subprocesses done...')
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))

    p.close()
    p.join()
    print('Child process end')