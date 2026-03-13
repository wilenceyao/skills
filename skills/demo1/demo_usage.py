#!/usr/bin/env python3
"""
demo1技能使用演示
"""

import os
import sys

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import create_algorithm_demo, list_available_algorithms

def demonstrate_skill():
    """演示技能功能"""
    print("="*60)
    print("demo1技能演示 - 创建Python算法示例")
    print("="*60)
    
    # 1. 列出可用算法
    print("\n1. 列出所有可用算法:")
    list_available_algorithms()
    
    # 2. 创建快速排序示例
    print("\n2. 创建快速排序算法示例:")
    quick_sort_file = create_algorithm_demo("sorting", "quick_sort", "demo_quick_sort.py")
    print(f"   已创建: {quick_sort_file}")
    
    # 3. 创建二分查找示例
    print("\n3. 创建二分查找算法示例:")
    binary_search_file = create_algorithm_demo("searching", "binary_search", "demo_binary_search.py")
    print(f"   已创建: {binary_search_file}")
    
    # 4. 创建斐波那契示例
    print("\n4. 创建斐波那契数列示例:")
    fibonacci_file = create_algorithm_demo("dp", "fibonacci", "demo_fibonacci.py")
    print(f"   已创建: {fibonacci_file}")
    
    # 5. 显示文件信息
    print("\n5. 生成的文件信息:")
    files = ["demo_quick_sort.py", "demo_binary_search.py", "demo_fibonacci.py"]
    
    for file in files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            with open(file, 'r', encoding='utf-8') as f:
                lines = len(f.readlines())
            print(f"   {file}: {lines} 行, {size} 字节")
        else:
            print(f"   {file}: 文件不存在")
    
    print("\n" + "="*60)
    print("演示完成！")
    print("="*60)
    
    # 清理生成的文件
    print("\n清理演示文件...")
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"   已删除: {file}")
    
    print("\n演示结束。")

if __name__ == "__main__":
    demonstrate_skill()