## 第6周 第12课 | 动态规划 


* 找最近重复子问题，即分治的过程 
* 定义状态数组（同时提前设置好base case） 
* 状态数组的递推公式 
### DP总结的博文： [http://cppblog.com/menjitianya/archive/2015/10/23/212084.html](http://cppblog.com/menjitianya/archive/2015/10/23/212084.html)

![图片](https://uploader.shimo.im/f/NbUmZ8Ah7mw59mNk.png!thumbnail)

![图片](https://uploader.shimo.im/f/bIxjkoWL5C0VesqH.png!thumbnail)

## 刷题记录 

### 0727周一 


* 1142-最长公共子序列：初始化状态矩阵（m+1，n+1）全为0.，比较i、j位置的字符，更新状态值，注意下标的使用 
### 0729周三 


* 120-三角形最小路径和： 
```python
DP 
a. 重复性（分治）       problem(i, j) = min(sub(i+1, j), sub(i+1, j+1)) + a[i, j] 
b. 定义状态数组 dp[i, j] 
c. 状态方程 dp[i, j] = min(dp[i+1, j], dp[i+1, j+1]) + a[i, j] 
```
### 0730周四 


* 53-最大子序和： 
```python
1. 分治（找重复子问题）  
max_sum(i) = max(max_sum(i - 1), max_sum(i - 1) + a[i]) 
2. 状态数组定义 f[i] 
3. dp方程  f[i] = max(f[i - 1], f[i - 1] + a[i]) 
```

* 152-乘积最大子数组：赋值连续乘积的最大值和最小值及返回结果res，遍历数组，遇负数交换最大最小，更新最大最小值 
* 322-零钱兑换： 
```python
1. subproblem 
2. DP array, f(n) = min(f(n - coin), for coin in [coins]) + 1 
3. DP方程， dp[n] = min(dp[n - k] for k in [coins]) + 1 
```
### 0731周五 


* 198-打家劫舍： 
```python
1. subproblem, a[i], i = 0..n-1, 返回a[n - 1] 
## 加一个维度，a[i][0]:不偷，a[i][1]:偷 
2. 状态数组, dp[i][0或1] 
3. dp方程, dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) 
        dp[i][1] = dp[i - 1][0] + a[i] 
```
### 0801周六 


* 64-最小路径和： 
```python
1. subproblem, min_sum(i, j) = min(min_sum(i - 1, j), min_      sum(i, j - 1)) + a[i, j] 
2. dp array, dp[i][j] 
3. dp equation, dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i, j] 
```
### 0802周日 


* 221-最大正方形： 
```python
1. subproblem 
    sq_size(i, j) = min(sq_size(i-1, j-1), sq_size(i, j-1), sq_size(i-1, j)) + 1 if a[i][j] == 1 
2. dp array, dp[i][j] (状态记录正方形最大边长，最终结果只要将其算平方即可) 
3. dp equation,  
    if a[i][j] == 1, dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 
```
