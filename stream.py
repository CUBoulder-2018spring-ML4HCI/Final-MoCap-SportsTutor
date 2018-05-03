import random
import numpy as np
import time
while(True):
    time.sleep(1)
    pipe = open("/tmp/un_pipe", 'w')
    s = ""
    for num in np.random.randn(4):
        s = s + str(num) + ","

    pipe.write(s+'\n')
    pipe.close()
