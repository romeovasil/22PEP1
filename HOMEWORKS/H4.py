""" Create a context manager that will time how long it took to execute the context and display a graph with
execution time when the context ends.
Since the same instance can be used in multiple contexts make sure that the graph will show data for each time the
object was used in a context
example
obj = Obj()
with obj as value1:
    ...
with obj as value2:
    ...
Now graph will contain 2 values
"""

from contextlib import contextmanager
import time
import matplotlib.pyplot as plt

exec_time=[]

@contextmanager
def file_opener(file_name,mode):
    fig1, (f1) = plt.subplots(nrows=1, ncols=1)
    global exec_time
    file_open=open(file_name,mode)

    try:
        start_time=time.time()
        yield file_open
    except:
        print("The file cannot be returned")
    finally:
        end_time=time.time()
        exec_time.append(end_time-start_time)
        file_open.close()
        print(exec_time)
        f1.plot([i for i in range(1,len(exec_time)+1)],exec_time)
        plt.show() #it will generate 3 graphs in this case


with file_opener("homeworks_file",'r') as file1:
    print(file1.read()+"\n\n")

with file_opener("homeworks_file",'r') as file2:
    print(file2.read()+"\n\n")

with file_opener("homeworks_file",'r') as file3:
    print(file3.read()+"\n\n")

#plt.show() it will generate only 1 graph but it must be manually place after one/more context ends
