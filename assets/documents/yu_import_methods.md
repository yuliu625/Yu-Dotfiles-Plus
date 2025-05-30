# Import Methods

## Overview
当一个项目变大，导入包也开始需要规范。

我知道[PEP8](https://peps.python.org/pep-0008/)中关于包导入的规范，并且也知道经典工具例如`isort`、`black`、`ruff`、`flake8`这样的自动化工具。我明白按照如字母顺序在多人成熟项目的好处，以及约定大于配置的方便。

只是，对于那些我自己一个人构建的项目，我更需要的是语义和功能的导入方法。因此，我定义了一些我自己管理导入的规范。


## Specification
按照和当前项目的相关程度。
### Prioritization
分为4类，每部分之间用1个空行划分。
- 字符串标注和文件类型。每个文件都有，以实现延迟解析。特殊文件类型会和标注在一起。
- 自构建。排在最前面最能看清当前文件的目的。先相对路径文件，然后绝对路径包。
- 外部包。先第三方包，然后标准库包。
- 类型。使用TYPE_CHECKING控制减少开销。仅type-hints相关包。
```python
"""
这部分可作为Python-Script-Template大规模复用。 
"""

from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # import some packages
```
### Absolute Path & Relative Path
- 整体优先absolute-path，方便重构时相关工具自动修改。
- \_\_init__.py中是相对路径，但是仅添加确定的稳定功能。
- 仅完全确定和稳定在同一文件夹下程序使用相对路径。如果使用相对路径，不超过2级。
### Special Programs
- interface.py: 抽象类。在文件初始说明。
```python
from __future__ import annotations
from abc import ABC, abstractmethod
```
- test.py: 测试工程。在文件初始说明。
```python
from __future__ import annotations
import pytest
```

