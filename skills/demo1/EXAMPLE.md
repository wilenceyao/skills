# demo1 使用示例

## 基本用法

### 1. 创建快速排序示例
```bash
python main.py --type sorting --algorithm quick_sort --output quick_sort_demo.py
```

### 2. 创建二分查找示例
```bash
python main.py --type searching --algorithm binary_search --output binary_search_demo.py
```

### 3. 创建斐波那契数列示例
```bash
python main.py --type dp --algorithm fibonacci --output fibonacci_demo.py
```

### 4. 列出所有可用算法
```bash
python main.py --list
```

## 在技能系统中使用

当用户说："创建一个快速排序的Python算法示例"

技能会自动：
1. 识别用户需要快速排序算法
2. 生成包含完整实现的Python文件
3. 包含测试用例和复杂度分析
4. 输出可执行的Python代码

## 生成的代码示例

### 快速排序示例输出
```python
"""
QUICK_SORT - 快速排序算法
类别: 排序算法
描述: 快速排序是一种分治算法，平均时间复杂度为O(n log n)

此文件由 demo1 技能自动生成。
"""

def quick_sort(arr):
    """快速排序算法"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# ... 更多代码 ...

if __name__ == "__main__":
    # 测试数据
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_data)
    
    # 测试快速排序
    sorted_data = quick_sort(test_data.copy())
    print("快速排序结果:", sorted_data)
    
    # 复杂度分析
    print("\n复杂度分析:")
    print("- 时间复杂度: O(n log n) 平均情况, O(n²) 最坏情况")
    print("- 空间复杂度: O(log n) 递归栈空间")
    print("- 稳定性: 不稳定排序")
```

## 测试技能

运行测试用例：
```bash
cd demo1
python -m pytest test/test_demo1.py -v
```

或直接运行：
```bash
python test/test_demo1.py
```

## 扩展技能

要添加新的算法模板，编辑 `main.py` 中的 `ALGORITHM_TEMPLATES` 字典：

```python
ALGORITHM_TEMPLATES = {
    "new_category": {
        "name": "新类别",
        "templates": {
            "new_algorithm": {
                "title": "新算法标题",
                "description": "算法描述",
                "code": """def new_algorithm():
    # 算法实现
    pass""",
                "complexity": {
                    "time": "O(...)",
                    "space": "O(...)"
                }
            }
        }
    }
}
```