# 学习文档

本仓库用于学习 Python 基础，包含若干可直接运行的示例。

## 项目结构
- `examples/hello.py`：字符串格式化与基础函数
- `examples/math_ops.py`：加法、乘法与阶乘
- `examples/oop_example.py`：类与对象、方法、`__repr__`
- `examples/file_io.py`：文件读写与 `pathlib.Path`

## 快速运行
在仓库根目录执行：
- `python3 examples/hello.py`
- `python3 examples/math_ops.py`
- `python3 examples/oop_example.py`
- `python3 examples/file_io.py`

## Git 推送说明（SSH）
- 已配置 `~/.ssh/config` 通过 `ssh.github.com:443` 连接 GitHub
- 直接使用：`git pull`、`git push`

## 下一步建议
- 为示例添加基础单元测试（`unittest` 或 `pytest`）
- 扩展数据结构示例：列表、字典、集合、推导式
- 增加异常处理与上下文管理（`with`）的示例
