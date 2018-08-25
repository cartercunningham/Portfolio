import statistics as stats
lst=[2,5,6]
print(stats.mean(lst))
lst2=[8,9,10]
for numbers in lst2:
    lst.append(numbers)
print (lst)
print(lst[3])