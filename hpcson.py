# -*- coding: utf-8 -*-
"""HPCSon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eQVTuUaEtECTUWKJL4sJm748xH8x7cjw
"""

import numba
from numba import cuda
cuda.detect()

cuda.select_device(0)

cuda.close()
cuda.gpus

#Device name
cuda.close()
con_ = cuda.get_current_device()
cuda.gpus.current

#Get memory size
cuda.select_device(0)
con_ = cuda.current_context()
con_.get_memory_info()

from numba.cuda.cudadrv import enums
from numba import cuda
import numpy as np
device = cuda.get_current_device()
attribs= [name.replace("CU_DEVICE_ATTRIBUTE_", "") for name in dir(enums) if name.startswith("CU_DEVICE_ATTRIBUTE_")]
print(np.array(attribs))
atrr_s = ['MULTIPROCESSOR_COUNT', 'TOTAL_CONSTANT_MEMORY', 'MAX_SHARED_MEMORY_PER_MULTIPROCESSOR']
for attr in attribs:
  if attr in atrr_s:
    print(attr, '=', getattr(device, attr))

cc_cores_per_SM_dict = {
    (2,0) : 32,
    (2,1) : 48,
    (3,0) : 192,
    (3,5) : 192,
    (3,7) : 192,
    (5,0) : 128,
    (5,2) : 128,
    (6,0) : 64,
    (6,1) : 128,
    (7,0) : 64,
    (7,5) : 64,
    (8,0) : 64,
    (8,6) : 128,
    (8,9) : 128,
    (9,0) : 128
    }

device = cuda.get_current_device()
my_sms = getattr(device, 'MULTIPROCESSOR_COUNT')
my_cc = device.compute_capability
cores_per_sm = cc_cores_per_SM_dict.get(my_cc)
total_cores = cores_per_sm*my_sms
print("GPU compute capability: " , my_cc)
print("GPU total number of SMs: " , my_sms)
print("total cores: " , total_cores)