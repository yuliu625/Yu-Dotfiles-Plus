# Python可变对象安全性

## Overview
我对于 Python 在机制方面有3点不喜欢，1是隐式推理，2是没有块级生命周期控制，3是可变对象。该文件对于可变对象的规范性进行约束，以完全避免所有因可变对象造成的不安感。

## str
Python中的str其实是immutable objects，之所以有相关的顾虑主要来源于C++中字符和字符串是不同的数据类型，以及Python中特殊的内存只读优化。

在Python中，相同的字符串会共用字符串指针。这一自动优化会造成字符串复制时候的不安。

但是，仔细想一下，其实完全没有必要担心。因为只有完全相同的字符串才会造成引用绑定。而当字符发生修改，因为字符串完全不可变，这只会造成新建字符串，原本的字符串并不会受到影响。

字符串的修改是一种错觉，除了完全的仅赋值操作(很少见)，所有的操作都实际上等同于新建字符串。Python字符串的驻留机制是一条没有必要去了解的特性，Python中的字符串一直都是安全的。


## list & dict
Python中的list和dict是重头戏。从静态类型编程语言如C++和Java转换时，Python原生实现原本STL中的功能真的非常舒适。然而当项目构建变大，使用list和dict只会造成极大的不安。

### Mutable Default Arguments
这种情况其实是最容易避免的。当定义函数时，提供的默认参数会绑定到`__defaults__`上。如果该参数不被指定而函数却又被重复调用，函数就有类似闭包(但不是)的记忆特性。
但恰好我很不喜欢defaults，我不喜欢默认指定行为导致的状态被隐式指定，包括连ide有时也不会提醒。
我的工程规范有更强的约束，我的防御性编程约定不能转入`None`而最多传入空容器。即使为了兼容性的代码被设定为`None`，函数首要的操作就是立即转化为空容器。因此这个问题也从一开始被避免。

### pydantic
pydantic中的dataclass的定义是所有困惑的开始。在pydantic中，field如果有default，那么对于list和dict，需要通过`default_factory`进行构造。很多时候定义dataclass，无法避免的需要设置一些default，这个问题就必须面对了。

但是，pydantic中的强制设定实际上并不是当前这个问题。当定义schema的时候，所有的field是以类属性进行定义的，这只是一个声明，这里的default是元数据。数据对象的构建会去复制元数据，此时可变对象就是极其糟糕的。

因此，pydantic的设计是对**类属性定义**打了一个补丁，基础的Python并不会糟糕的在这里像字符串一样执行内存优化。可变对象如果共享内存，结果是灾难性的逻辑错误。


## Solutions
区别**直接赋值**、**浅拷贝**、**深拷贝**。

### typing::Sequence & typing::Mapping
宽进严出。在输入的声明中承诺不会修改原始数据对象，初始阶段执行深拷贝，再进行处理。但返回类型依然精确标记数据类型。

### Defensive Copying
> 默认不信任，入库拷贝，出库保护。
```python
import copy

data_ = copy.deepcopy(data)
```

对于list和dict，完全避免由另一个相同类型的对象赋值。

Python原生，以及存在可变对象的工具，约定开始操作前执行深拷贝，完全避免各种副作用。

### Never In-place Mutation
命令式 -> 函数式
- 列表添加: l.append(x) -> new_l = l + [x]
- 字典合并: d.update(d2) -> new_d = {**d, **d2}
- 列表过滤: for...if...l.remove() -> new_l = [x for x in l if condition]
- 字典删除: del d['key'] -> "new_d = {k: v for k, v in d.items() if k != 'key'}"


### pyrsistent
该工具目前不是社区事实标准，暂时观望。
```python
from pyrsistent import v, m
```

