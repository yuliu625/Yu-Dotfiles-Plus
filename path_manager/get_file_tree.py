"""
文件树管理工具。

为简化文件树的管理，我遵循: 约定大于配置。

操作方法:
    - 全局配置。在项目根定义这个文件，所有路径相关均统一使用这个文件方法。
    - 指定_BASE_DIR。
    - 定义需要字段。使用pydantic定义所有的路径，类型全部是Path。
    - 定义文件树。在get_file_tree中写入所有的路径计算方法，基于pathlib实现。

使用:
    - 约定。所有文件都默认使用get_file_tree方法获取路径。
    - 项目迁移。仅修改_BASE_DIR。
"""

from pathlib import Path
from pydantic import BaseModel, Field


__BASE_DIR = r""


class FileTree(BaseModel):
    """声明所有需要的路径。"""
    base_dir: Path = Field(description="最基础的路径，其他路径都由这个路径生成。")


def get_file_tree(
    base_dir: str = __BASE_DIR,
) -> FileTree:
    """
    全局的获取文件树的方法。

    Args:
        base_dir: 最根本的路径，其他路径都为其子路径。

    Returns:
        具体的所有子路径，都是Path对象。
    """
    base_dir = Path(base_dir)
    # 这里写生成FileTree的方法
    file_tree = FileTree(
        base_dir=base_dir,
    )
    return file_tree

