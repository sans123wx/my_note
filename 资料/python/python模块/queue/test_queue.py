import queue , threading

q = queue.Queue(10)
for i in range(11):
    try:
        q.put_nowait(i)
    except queue.Full:
        print('xxx')
def test(q , b):
    while not q.empty():
        print('i am ' + b)
        print(q.get())
        q.task_done()
thread0 = threading.Thread(target = test , args = (q , 'a'))
thread1 = threading.Thread(target = test , args = (q , 'b'))

thread0.start()
thread1.start()
q.join()
print('xxxx')

