# 分析单词搜索 II题目用Trie树方式实现的时间复杂度 

# 第7周 第13课 | 字典树和并查集 

## 字典树Trie 

### 三点基本性质 


* 结点本身不存任何完整单词 
* 从根结点到某一结点，路径上经过的所有字符连接起来，为这一结点对应的字符串 
* 每个结点的子结点所代表的字符都不相同 
### 核心思想— **空间换时间** 

利用字符串的公共前缀来降低查询时间的开销，可以返回所有候选字符串/候选单词 

### 结点的内部实现 

![图片](https://uploader.shimo.im/f/WTq7Da4UcUIbL1yz.png!thumbnail)

结点也能存储额外的信息，如记录某个字符串/单词出现的频次 

### 字典树的实现代码模板 

```python
class Trie(object): 
   
	def __init__(self):  
		self.root = {}  
		self.end_of_word = "#"  
  
	def insert(self, word):  
		node = self.root  
		for char in word:  
			node = node.setdefault(char, {})  
		node[self.end_of_word] = self.end_of_word  
  
	def search(self, word):  
		node = self.root  
		for char in word:  
			if char not in node:  
				return False  
			node = node[char]  
		return self.end_of_word in node  
  
	def startsWith(self, prefix):  
		node = self.root  
		for char in prefix:  
			if char not in node:  
				return False  
			node = node[char]  
		return True 
```
## 并查集 

查找、合并 

```python
def init(p):  
	# for i = 0 .. n: p[i] = i;  
	p = [i for i in range(n)]  
  
def union(self, p, i, j):  
	p1 = self.parent(p, i)  
	p2 = self.parent(p, j)  
	p[p1] = p2  
  
def parent(self, p, i):  
	root = i  
	while p[root] != root:  
		root = p[root]  
	while p[i] != i: # 路径压缩 ? 
		x = i; i = p[i]; p[x] = root  
	return root 
```
# 第7周 第14课 | 高级搜索 

## 剪枝 

## 双向BFS 

## 启发式搜索（A*） 


# 第7周 第15课 | AVL和红黑树 

## 

