第3周 第7课-泛型递归、树的递归

递归步骤：

​	1-递归终止条件

​	2-处理当前层逻辑

​	3-下探到下一层

​	4-清理当前层
​    

    def recursion(level, param1, param2, ...):	
        #递归终止条件
        if level > MAX_LEVEL:
            process_result
            return
    
        # 处理当前层逻辑
        process(level, data, ..)
    
        # 下探到下一层
        recursion(level + 1, p1, p2, ..)
    
        # 清理当前层状态（if needed）

递归思维要点：

​	1-切勿人肉递归，即抛弃画递归状态树；

​	2-找最近重复子问题；

​	3-数学归纳法的思维。

