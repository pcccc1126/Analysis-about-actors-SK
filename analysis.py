# -*- coding: UTF-8 -*-
import numpy
import operator
import matplotlib.pyplot as plt
import matplotlib as mpl
import pylab as pl

def all_np(arr):
    arr = numpy.array(arr)
    key = numpy.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

file = open('korea.txt', 'r', encoding='utf8')
next(file)
next(file)
name = next(file).strip().split('，')
for i in range(49):
    next(file)
    next(file)
    next(file)
    name += next(file).strip().split('，')

result = sorted(all_np(name).items(), key = operator.itemgetter(1))
name_list = []
num_list = []
for i in range(len(result)):
    if result[len(result)-i-1][1] < 2: break;
    name_list.append(result[len(result)-i-1][0])
    num_list.append(result[len(result)-i-1][1])

plt.rcParams['savefig.dpi'] = 700
plt.rcParams['figure.dpi'] = 700
plt.xticks(fontsize = 8)
pl.xticks(rotation = 40)
pl.xticks(color = '#483d8b')
pl.yticks(color = '#483d8b')
plt.bar(range(len(num_list)), num_list, color = '#483d8b', tick_label = name_list)
plt.savefig("korea.jpg", dpi = 700)
plt.show()