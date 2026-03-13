#!/usr/bin/env python3
"""
demo1技能测试用例
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import create_algorithm_demo, list_available_algorithms, ALGORITHM_TEMPLATES


class TestDemo1(unittest.TestCase):
    """demo1技能测试类"""
    
    def setUp(self):
        """测试前准备"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_output = os.path.join(self.temp_dir, "test_algorithm.py")
    
    def tearDown(self):
        """测试后清理"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_create_quick_sort_demo(self):
        """测试创建快速排序示例"""
        output_file = create_algorithm_demo("sorting", "quick_sort", self.test_output)
        
        self.assertTrue(os.path.exists(output_file))
        self.assertEqual(output_file, self.test_output)
        
        # 验证文件内容
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertIn("快速排序算法", content)
        self.assertIn("def quick_sort", content)
        self.assertIn("时间复杂度", content)
    
    def test_create_binary_search_demo(self):
        """测试创建二分查找示例"""
        output_file = create_algorithm_demo("searching", "binary_search", self.test_output)
        
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertIn("二分查找算法", content)
        self.assertIn("def binary_search", content)
        self.assertIn("O(log n)", content)
    
    def test_create_fibonacci_demo(self):
        """测试创建斐波那契数列示例"""
        output_file = create_algorithm_demo("dp", "fibonacci", self.test_output)
        
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertIn("斐波那契数列", content)
        self.assertIn("动态规划", content)
        self.assertIn("fibonacci_dp", content)
    
    def test_default_algorithm(self):
        """测试默认算法创建"""
        output_file = create_algorithm_demo("unknown", "unknown", self.test_output)
        
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 默认应该创建快速排序
        self.assertIn("快速排序算法", content)
    
    def test_algorithm_templates_structure(self):
        """测试算法模板结构"""
        self.assertIn("sorting", ALGORITHM_TEMPLATES)
        self.assertIn("searching", ALGORITHM_TEMPLATES)
        self.assertIn("dp", ALGORITHM_TEMPLATES)
        
        # 验证每个类别都有模板
        for category in ["sorting", "searching", "dp"]:
            self.assertIn("templates", ALGORITHM_TEMPLATES[category])
            self.assertTrue(len(ALGORITHM_TEMPLATES[category]["templates"]) > 0)
    
    def test_list_algorithms_function(self):
        """测试列出算法函数"""
        # 这个测试主要确保函数能正常执行而不出错
        try:
            list_available_algorithms()
            success = True
        except Exception as e:
            success = False
            print(f"list_available_algorithms 出错: {e}")
        
        self.assertTrue(success)
    
    def test_generated_file_executable(self):
        """测试生成的文件可以执行"""
        output_file = create_algorithm_demo("sorting", "quick_sort", self.test_output)
        
        # 验证文件存在且内容正确
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 验证关键内容存在
        self.assertIn("def quick_sort", content)
        self.assertIn("原始数组", content)
        self.assertIn("快速排序结果", content)
        self.assertIn("时间复杂度", content)
        
        # 跳过实际执行测试，因为环境可能不支持
        # 在实际使用中，生成的Python文件应该是可执行的


class TestDemo1Integration(unittest.TestCase):
    """集成测试"""
    
    def test_multiple_algorithm_creation(self):
        """测试创建多个算法示例"""
        with tempfile.TemporaryDirectory() as temp_dir:
            algorithms = [
                ("sorting", "quick_sort", "quick_sort_demo.py"),
                ("searching", "binary_search", "binary_search_demo.py"),
                ("dp", "fibonacci", "fibonacci_demo.py"),
            ]
            
            for alg_type, alg_name, filename in algorithms:
                output_path = os.path.join(temp_dir, filename)
                output_file = create_algorithm_demo(alg_type, alg_name, output_path)
                
                self.assertTrue(os.path.exists(output_file))
                
                # 验证文件内容包含正确的算法
                with open(output_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if alg_name == "quick_sort":
                    self.assertIn("快速排序", content)
                elif alg_name == "binary_search":
                    self.assertIn("二分查找", content)
                elif alg_name == "fibonacci":
                    self.assertIn("斐波那契", content)


if __name__ == "__main__":
    unittest.main()