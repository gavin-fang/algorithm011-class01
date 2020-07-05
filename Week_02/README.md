## 一周打卡记录

### 0629周一

349-两个数组的交集：用dict实现哈希，nums1用哈希表存放，再遍历nums2，注意输出结果唯一；内置函数两set取&；排序加双指针，结果用set

350-两个数组的交集II：用dict实现哈希，注意匹配时value减一；排序加双指针，结果list即可189-旋转数组：计次，尾部pop头部insert；三次反转

### 0630周二

242-有效的字母异位词：字典，value一加一减，判0；数组放a-z出现次数

49-字母异位词分组：用字典，key为有相同字符的元组（列表不能做key），返回字典的values；用字典，key为字母计数的元组

### 0701周三

1021-删除最外层的括号：用栈，遇左括号入栈：若入栈后栈的长度大于1，即该左括号不是原语首个左括号，结果加入'('，遇右括号出栈若出栈后栈的长度大于0，即该右括号不是原语末个右括号，结果加入')’；用balance计数原语部分括号是否成对，为0则取除了最外层括号的区间 

412-Fizz Buzz：一多条件；二字符串连接；三散列表（在二的基础上）

### 0702周四

589-N叉树的前序遍历：递归，注意多个孩子结点；栈，前序root直接先放stack

94-二叉树的中序遍历：递归；栈，迭代终止为stack空或者遍历指针为空

### 0704周六

144-二叉树的前序遍历：迭代法，root先入栈，迭代中按右左顺序入栈

145-二叉树的后序遍历：第一种迭代，按前序思想，变化的是在0位置插入，后面迭代按左右顺序入栈

429-N叉树的层序遍历：利用二叉树前序解法，且在迭代中更新stack；五行迭代，注意while any(stack)

## 第2周 第5课 哈希表、映射、集合

### 哈希表（Hash Table）

也叫散列表，是根据键值对（key-value）而直接进行访问的数据结构。它通过把key映射到表中一个位置（整型下标）来访问记录，映射函数叫哈希函数（或散列函数），存放记录的数组叫做哈希表（或散列表）。增删查时间复杂度皆为 O(1)，最差 O(n) （产生哈希冲突最后成了链表了），空间复杂度 O(n)。

哈希碰撞/冲突有多种解决方法，常用拉链式，即增加一个维度，某个位置放的是一个链表。工程中哈希表的长度很大，比较少发生哈希冲突，一般哈希表的查询为O(1)。

哈希表在Python中抽象出来的是dict和set，dict中key不重复，value可以重复，set是不重复元素的集合。

## 第2周 第6课 树、二叉树、二叉搜索树

### 二叉树的三种遍历

![image-20200705222251523](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200705222251523.png)

### 操作

二叉树的前序、中序、后序、层次遍历的非递归

N叉树的前后序遍历、层次遍历的递归、非递归

## 第2周 第6课 堆、二叉堆、图

### 堆和二叉堆

二叉堆只是堆的一种，而且是效率最低的一种，只是实现起来较为简单，其为完全二叉树的形式，可以通过数组来存储。二叉堆的插入删除操作时间复杂度为O(logN)。

### 堆的插入

- 堆大小加1
- 将新元素放在堆的尾部
- 从下至上堆化这个元素（HeapifyUp）

### 堆的删除

- 删除根结点元素
- 将堆的最后一个元素复制到根结点位置，删除最后的元素
- 从上至下堆化这个元素（HeapifyDown）

### 图

链表是特殊化的树，树是特殊化的图

图的表示：邻接矩阵和邻接表

图的DFS和BFS的递归代码

![image-20200705225113862](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200705225113862.png)

![image-20200705225125339](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200705225125339.png)

### 几个链接

- 连通图个数：[ https://leetcode-cn.com/problems/number-of-islands/](https://leetcode-cn.com/problems/number-of-islands/)
- 拓扑排序（Topological Sorting）：[ https://zhuanlan.zhihu.com/p/34871092](https://zhuanlan.zhihu.com/p/34871092)
- 最短路径（Shortest Path）：Dijkstra https://www.bilibili.com/video/av25829980?from=search&seid=13391343514095937158
- 最小生成树（Minimum Spanning Tree）：[ https://www.bilibili.com/video/av84820276?from=search&seid=17476598104352152051](https://www.bilibili.com/video/av84820276?from=search&seid=17476598104352152051)



