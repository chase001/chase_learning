# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         tools
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------
import random


def generate_len_str(i):
    _str = ''
    for j in range(i):
        _str += random.choice(['a', "b", "c", "d", "e", "f"])
    return _str



print(generate_len_str(8))