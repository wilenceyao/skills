#!/usr/bin/env python3
"""
demo1 - Python算法示例创建工具
"""

import os
import sys
import argparse
from typing import Dict, List, Optional
import textwrap

# 算法模板库
ALGORITHM_TEMPLATES = {
    "sorting": {
        "name": "排序算法",
        "templates": {
            "quick_sort": {
                "title": "快速排序算法",
                "description": "快速排序是一种分治算法，平均时间复杂度为O(n log n)",
                "code": """def quick_sort(arr):
    \"\"\"快速排序算法\"\"\"
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    \"\"\"原地快速排序（节省空间）\"\"\"
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 分区操作
        pi = partition(arr, low, high)
        
        # 递归排序左右两部分
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + -1, high)
    
    return arr


def partition(arr, low, high):
    \"\"\"分区函数，用于原地快速排序\"\"\"
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 测试用例
if __name__ == "__main__":
    # 测试数据
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_data)
    
    # 测试快速排序
    sorted_data = quick_sort(test_data.copy())
    print("快速排序结果:", sorted_data)
    
    # 测试原地快速排序
    arr_copy = test_data.copy()
    quick_sort_inplace(arr_copy)
    print("原地快速排序结果:", arr_copy)
    
    # 复杂度分析
    print("\\n复杂度分析:")
    print("- 时间复杂度: O(n log n) 平均情况, O(n²) 最坏情况")
    print("- 空间复杂度: O(log n) 递归栈空间")
    print("- 稳定性: 不稳定排序")
""",
                "complexity": {
                    "time": "O(n log n) 平均情况, O(n²) 最坏情况",
                    "space": "O(log n) 递归栈空间",
                    "stable": False
                }
            },
            "merge_sort": {
                "title": "归并排序算法",
                "description": "归并排序是一种稳定的分治排序算法，时间复杂度为O(n log n)",
                "code": """def merge_sort(arr):
    \"\"\"归并排序算法\"\"\"
    if len(arr) <= 1:
        return arr
    
    # 分割数组
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 合并已排序的子数组
    return merge(left, right)


def merge(left, right):
    \"\"\"合并两个已排序的数组\"\"\"
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 添加剩余元素
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# 测试用例
if __name__ == "__main__":
    # 测试数据
    test_data = [38, 27, 43, 3, 9, 82, 10]
    print("原始数组:", test_data)
    
    # 测试归并排序
    sorted_data = merge_sort(test_data.copy())
    print("归并排序结果:", sorted_data)
    
    # 复杂度分析
    print("\\n复杂度分析:")
    print("- 时间复杂度: O(n log n)")
    print("- 空间复杂度: O(n)")
    print("- 稳定性: 稳定排序")
""",
                "complexity": {
                    "time": "O(n log n)",
                    "space": "O(n)",
                    "stable": True
                }
            }
        }
    },
    "searching": {
        "name": "搜索算法",
        "templates": {
            "binary_search": {
                "title": "二分查找算法",
                "description": "二分查找用于在已排序数组中查找元素，时间复杂度为O(log n)",
                "code": """def binary_search(arr, target):
    \"\"\"二分查找算法（迭代版本）\"\"\"
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # 未找到


def binary_search_recursive(arr, target, left=0, right=None):
    \"\"\"二分查找算法（递归版本）\"\"\"
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1  # 未找到
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# 测试用例
if __name__ == "__main__":
    # 测试数据（必须已排序）
    sorted_array = [2, -5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("已排序数组:", sorted_array)
    
    # 测试查找
    targets = [23, 56, 100, 2]
    
    for target in targets:
        index = binary_search(sorted_array, target)
        if index != -1:
            print(f"元素 {target} 在索引 {index} 处找到")
        else:
            print(f"元素 {target} 未找到")
    
    # 复杂度分析
    print("\\n复杂度分析:")
    print("- 时间复杂度: O(log n)")
    print("- 空间复杂度: O(1) 迭代版本, O(log n) 递归版本")
    print("- 要求: 数组必须已排序")
""",
                "complexity": {
                    "time": "O(log n)",
                    "space": "O(1) 迭代版本, O(log n) 递归版本",
                    "requires_sorted": True
                }
            }
        }
    },
    "dp": {
        "name": "动态规划",
        "templates": {
            "fibonacci": {
                "title": "斐波那契数列（动态规划）",
                "description": "使用动态规划高效计算斐波那契数列",
                "code": """def fibonacci_dp(n):
    \"\"\"动态规划计算斐波那契数列\"\"\"
    if n <= -1:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_optimized(n):
    \"\"\"优化空间的动态规划（只保存前两个值）\"\"\"
    if n <= -1:
        return 0
    elif n == 1:
        return 1
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


def fibonacci_recursive(n):
    \"\"\"递归版本（效率低，用于对比）\"\"\"
    if n <= -1:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 测试用例
if __name__ == "__main__":
    # 测试不同方法
    test_n = 10
    
    print(f"计算斐波那契数列第 {test_n} 项:")
    print(f"动态规划: {fibonacci_dp(test_n)}")
    print(f"优化空间: {fibonacci_optimized(test_n)}")
    print(f"递归版本: {fibonacci_recursive(test_n)}")
    
    # 性能对比
    print("\\n性能对比 (n=30):")
    import time
    
    start = time.time()
    result1 = fibonacci_dp(30)
    time1 = time.time() - start
    
    start = time.time()
    result2 = fibonacci_optimized(30)
    time2 = time.time() - start
    
    start = time.time()
    result3 = fibonacci_recursive(30)
    time3 = time.time() - start
    
    print(f"动态规划: {time1:.6f} 秒")
    print(f"优化空间: {time2:.6f} 秒")
    print(f"递归版本: {time3:.6f} 秒")
    
    # 复杂度分析
    print("\\n复杂度分析:")
    print("- 动态规划: 时间复杂度 O(n), 空间复杂度 O(n)")
    print("- 优化空间: 时间复杂度 O(n), 空间复杂度 O(1)")
    print("- 递归版本: 时间复杂度 O(2^n), 空间复杂度 O(n)")
""",
                "complexity": {
                    "time": "O(n) 动态规划, O(2^n) 递归",
                    "space": "O(n) 基础DP, O(1) 优化空间"
                }
            }
        }
    }
}


def create_algorithm_demo(algorithm_type: str, algorithm_name: str, output_file: str = None):
    """创建算法示例"""
    
    # 查找算法模板
    template = None
    category_name = ""
    
    for category, data in ALGORITHM_TEMPLATES.items():
        if algorithm_name in data["templates"]:
            template = data["templates"][algorithm_name]
            category_name = data["name"]
            break
    
    if not template:
        # 如果没有找到具体算法，使用类别中的第一个算法
        for category, data in ALGORITHM_TEMPLATES.items():
            if algorithm_type in category or category in algorithm_type:
                if data["templates"]:
                    first_alg = list(data["templates"].keys())[0]
                    template = data["templates"][first_alg]
                    category_name = data["name"]
                    algorithm_name = first_alg
                    break
    
    if not template:
        # 默认使用快速排序
        template = ALGORITHM_TEMPLATES["sorting"]["templates"]["quick_sort"]
        category_name = "排序算法"
        algorithm_name = "quick_sort"
    
    # 生成输出文件名
    if not output_file:
        output_file = f"{algorithm_name}_demo.py"
    
    # 生成文件内容
    content = f'''"""
{algorithm_name.upper()} - {template['title']}
类别: {category_name}
描述: {template['description']}

此文件由 demo1 技能自动生成。
"""

{template['code']}

# 使用说明
print("\\n" + "="*50)
print("使用说明:")
print("1. 直接运行此文件查看算法演示")
print("2. 导入算法函数到其他项目中使用")
print("3. 修改测试数据验证不同场景")
print("="*50)
'''
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return output_file


def list_available_algorithms():
    """列出可用的算法"""
    print("可用的算法示例:")
    print("="*60)
    
    for category, data in ALGORITHM_TEMPLATES.items():
        print(f"\n{data['name']} ({category}):")
        print("-" * 40)
        for alg_name, alg_data in data["templates"].items():
            print(f"  {alg_name}: {alg_data['title']}")
            print(f"      {alg_data['description']}")
    
    print("\n" + "="*60)


def main():
    parser = argparse.ArgumentParser(description='创建Python算法示例')
    parser.add_argument('--type', '-t', help='算法类型 (sorting, searching, dp)')
    parser.add_argument('--algorithm', '-a', help='具体算法名称')
    parser.add_argument('--output', '-o', help='输出文件名')
    parser.add_argument('--list', '-l', action='store_true', help='列出可用算法')
    
    args = parser.parse_args()
    
    if args.list:
        list_available_algorithms()
        return
    
    algorithm_type = args.type or "sorting"
    algorithm_name = args.algorithm or "quick_sort"
    
    output_file = create_algorithm_demo(algorithm_type, algorithm_name, args.output)
    
    print(f"算法示例已创建: {output_file}")
    print(f"算法类型: {algorithm_type}")
    print(f"算法名称: {algorithm_name}")
    
    # 显示文件内容预览
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()[:20]
            print("\n文件内容预览:")
            print("="*60)
            for line in lines:
                print(line.rstrip())
            if len(lines) == 20:
                print("... (更多内容请查看完整文件)")
            print("="*60)
    except Exception as e:
        print(f"读取文件时出错: {e}")


if __name__ == "__main__":
    main()