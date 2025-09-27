# import os, sys, datetime, json 

# print(os.getcwd())

# import math_utils

# from math_utils import add

# print(math_utils.add(5, 5))

# print(add(5, 5))

# from math_utils import *

# print(minus(10, 5))

import requests

response = requests.get("https://httpbin.org/get")
print(response.json())

