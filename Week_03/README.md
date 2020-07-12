第3周 第7课-泛型递归、树的递归

Python递归模板
def recursion(level, param1, param2, ...):
    # 递归终止条件
    if level > MAX_LEVEL:
        process_result
        return
    
    # 处理当前层逻辑
    process(level, data, ..)
    
    # 下探到下一层
    recursion(level + 1, p1, p2, ..)
    
    # 清理当前层状态（if needed）

递归思维要点：

​	1-切勿人肉递归，即抛弃画递归状态树的方式；

​	2-找最近重复子问题；

​	3-数学归纳法的思维。

第3周 第8课-分治、回溯
分治
递归状态树
图片: https://uploader.shimo.im/f/6OS8r1VbO4fb9h86.png

分治Divide&Conquer
图片: https://uploader.shimo.im/f/zkAhNoDaQ7UtWjiy.png

Python分治代码模板
  def divide_conquer(problem, param1, param2, ...):
      # recursion terminator 分到没有子问题可以解决时
      if problem is None:
          print_result
          return
      
      # prepare data 处理当前层逻辑，如何拆分成子问题
      data = prepare_data(problem)
      subproblems = split_problem(problem, data)
      
      # conquer subproblems 下探到下一层，解决子问题
      subresult1 = self.divide_conquer(subproblems[0], p1,...)
      subresult2 = self.divide_conquer(subproblems[1], p1,...)
      subresult3 = self.divide_conquer(subproblems[2], p1,...)
      ...
      
      # process and generate the final result 子问题结果的组合
      result = process_result(subresult1, subresult2, subresult3,...)
      
      # revert the current level states
常见问题：求Pow(x, n)；求众数
回溯
def backtrack(level, paras):
    if exist_condition(level):
        return
    state = keepsate(level)  #保存当前状态
    backtrack(level+1, paras):
    reverseState(level, state) #恢复当前状态
回溯的处理思想有点类似枚举搜索。通过枚举所有的解，找到满足期望的解。为了有规律地枚举所有可能的解，避免遗漏和重复，我们把问题求解的过程分为多个阶段。每个阶段，都会面对一个岔路口，我们先随意选一条路走，当发现这条路走不通的时候（不符合期望的解），就回退到上一个岔路口，另选一种走法继续走。

常见问题：括号生成；子集；电话号码的字母组成；全排列；全排列II；组合

刷题记录
0706周一
22-括号生成：递归法，记录左右括号的个数（两种记录方式：已用的个数和剩余的个数）

0707周二
98-验证二叉搜索树：中序遍历递增的性质；自身定义，利用递归，注意设置比较的low和high值

0709周四
50-Pow(x, n)：分治法，考虑n的奇偶

0710周五
78-子集：迭代法，用Python生成函数，思想为每次将新元素添加到前面的每一个子集结果中去；回溯法，

0711周六
46-全排列：回溯法
77-组合：回溯法

0712周日
236-二叉树的最近公共祖先：递归，考虑根为空、左右子树有一个为根、左右子树递归结果是否为空的情况
