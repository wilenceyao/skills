# demo1 - Python算法示例创建技能

## 概述

`demo1` 是一个用于创建Python算法示例的技能。当用户需要学习或演示算法实现时，此技能可以快速生成包含完整实现、测试用例和复杂度分析的Python代码。

## 功能特性

- **多种算法类型**：支持排序、搜索、动态规划等常见算法
- **完整实现**：包含算法核心函数、辅助函数和测试用例
- **复杂度分析**：每个算法都包含时间和空间复杂度分析
- **易用性**：简单的命令行接口，清晰的输出格式
- **可扩展**：易于添加新的算法模板

## 支持的算法

### 排序算法
- `quick_sort` - 快速排序算法
- `merge_sort` - 归并排序算法

### 搜索算法
- `binary_search` - 二分查找算法

### 动态规划
- `fibonacci` - 斐波那契数列

## 安装和使用

### 基本使用
```bash
# 列出所有可用算法
python main.py --list

# 创建快速排序示例
python main.py --type sorting --algorithm quick_sort --output quick_sort_demo.py

# 创建二分查找示例
python main.py --type searching --algorithm binary_search --output binary_search_demo.py

# 创建斐波那契数列示例
python main.py --type dp --algorithm fibonacci --output fibonacci_demo.py
```

### 在技能系统中使用
当用户说以下短语时触发此技能：
- "创建python算法示例"
- "python算法演示"
- "算法示例代码"
- "python算法实现"
- "演示算法"
- "算法demo"

## 文件结构
```
demo1/
├── SKILL.md          # 技能描述文档
├── main.py           # 主程序
├── test/             # 测试目录
│   └── test_demo1.py # 单元测试
├── EXAMPLE.md        # 使用示例
├── README.md         # 本文档
├── requirements.txt  # 依赖文件
└── demo_usage.py     # 演示脚本
```

## 测试
运行测试用例：
```bash
python test/test_demo1.py
```

或使用pytest：
```bash
python -m pytest test/test_demo1.py -v
```

## 扩展技能

要添加新的算法，编辑 `main.py` 中的 `ALGORITHM_TEMPLATES` 字典：

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

## 示例输出

生成的算法示例包含：
1. 算法实现代码
2. 测试用例
3. 复杂度分析
4. 使用说明

示例文件内容：
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

# ... 更多代码和测试用例 ...
```

## 许可证

此技能遵循MIT许可证。