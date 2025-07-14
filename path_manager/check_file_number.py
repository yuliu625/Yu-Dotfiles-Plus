"""
文件数量检查器。
"""

from __future__ import annotations

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def check_file_number(
    dir_path: str | Path,
) -> int:
    """
    检测一个文件夹下有多少个文件。

    Args:
        dir_path (Union[str, Path]): 需要检测的文件夹路径。可以是字符串或Path对象。

    Returns:
        int: 不区分文件或文件夹类型的数量。
    """
    dir_path = Path(dir_path)
    print(len(list(dir_path.iterdir())))
    return len(list(dir_path.iterdir()))


if __name__ == '__main__':
    dir_path_ = r""
    check_file_number(dir_path_)

