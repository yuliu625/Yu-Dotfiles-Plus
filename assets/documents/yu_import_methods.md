# Import Methods

## Overview
当一个项目变大，导入包也开始需要规范。

我知道[PEP8](https://peps.python.org/pep-0008/)中关于包导入的规范，并且也知道经典工具例如`isort`、`black`、`ruff`、`flake8`这样的自动化工具。我明白按照如字母顺序在多人成熟项目的好处，以及约定大于配置的方便。

但是，很多我自己项目只有我一个人构建，我更需要的是语义和功能的导入方法。因此我定义了一些我自己管理导入的规范。


## Specification
按照和当前项目的相关程度。
### Prioritization
分为3类，每部分之间用1个空行划分。
- 自构建。排在最前面最能看清当前文件的目的。先相对路径文件，一般为同一包的文件。再绝对路径包。
- 外部包。先第三方包，再标准库包。
- 类型。使用TYPE_CHECKING控制减少开销。仅type-hints相关包。
```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # import some packages
```
### Special Programs
- \_\_init__.py: 仅使用相对路径导入，按照具体功能自定义部分。
- interface.py: 额外一类，在程序文件初始。
```python
from abc import ABC, abstractmethod
```

