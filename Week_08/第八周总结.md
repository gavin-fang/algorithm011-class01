## 初级排序算法代码 

```python
def insert_sort(lists): 
    # 插入排序 
    count = len(lists) 
    for i in range(1, count): 
        key = lists[i] 
        j = i - 1 
        while j >= 0: 
            if lists[j] > key: 
                lists[j + 1] = lists[j] 
                lists[j] = key 
            j -= 1 
    return lists 
     
def select_sort(lists): 
    # 选择排序 
    count = len(lists) 
    for i in range(0, count): 
        min = i 
        for j in range(i + 1, count): 
            if lists[min] > lists[j]: 
                min = j 
        lists[min], lists[i] = lists[i], lists[min] 
    return lists 
     
def bubble_sort(lists): 
    # 冒泡排序 
    count = len(lists) 
    for i in range(0, count): 
        for j in range(i + 1, count): 
            if lists[i] > lists[j]: 
                lists[i], lists[j] = lists[j], lists[i] 
    return lists 
```
## 第8周 第16课 | 位运算 

## 第8周 第17课 | 布隆过滤器和LRU缓存 

## 第8周 第18课 | 排序算法 

![图片](https://uploader.shimo.im/f/mzBk3wf3YihNtwFw.png!thumbnail)

