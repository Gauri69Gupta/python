print("Question--1")
import numpy as np
import math
np_arr=np.random.random((10,1))
print(np_arr)
gauri=np.mean(list(np_arr))
print(gauri)
print("\n")
print("QUESTION--2")
import numpy as np
np_arr=np.random.random((20,1))
print(np_arr)
gauri=np.var(list(np_arr))
print(gauri)
riya=np.std(list(np_arr))
print(riya)
print("\n")
print("QUESTION--3")
import numpy as np
np_arr1=np.random.random((10,20))
print(np_arr1)
np_arr2=np.random.random((20,25))
print(np_arr2)
gauri=np.matmul(np_arr1,np_arr2)
riya=np.shape((10,25))
print(riya)
print("\n")
print("QUESTION--4")
import numpy as np
import math
a=np.random.randint(10,size=(10,1))
def f(x):
    return(1/1+math.exp(-x))
arr=np.array(list(map(f,a)))
print(arr)
            

print("\n")

