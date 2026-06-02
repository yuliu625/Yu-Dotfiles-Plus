"""
Sources:

References:

Synopsis:
    路径非法字符处理映射方法。

Notes:

"""

from __future__ import annotations
from loguru import logger

import re

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class SafeFileNameProcessor:
    """
    安全文件名处理器。

    以固定的规则对文件名进行编解码。
    可能会在解码时出现问题。
    """

    def __init__(
        self,
        custom_map: dict = None
    ):
        """
        为了灵活自定义，这个工具类需要实例化。

        Args:
            custom_map (dict): 增加或替换的映射规则。
        """
        # 默认的字符映射表(非法字符 -> 替代字符串)
        self.encode_map = {
            '/': '__fs__',
            '\\': '__bs__',
            ':': '__cln__',
            '*': '__ast__',
            '?': '__q__',
            '<': '__lt__',
            '>': '__gt__',
            '"': '__dq__',
            '|': '__pipe__',
        }
        if custom_map:
            self.encode_map.update(custom_map)
        # 解码表(替代字符串 -> 原始字符)
        self.decode_map = {v: k for k, v in self.encode_map.items()}

        illegal_chars = map(re.escape, self.encode_map.keys())
        replacements = map(re.escape, self.decode_map.keys())
        self._encode_pattern = re.compile('|'.join(illegal_chars))
        self._decode_pattern = re.compile('|'.join(replacements))

    def encode(
        self,
        file_name: str
    ) -> str:
        return self._encode_pattern.sub(lambda m: self.encode_map[m.group()], file_name)

    def decode(
        self,
        encoded_name: str
    ) -> str:
        return self._decode_pattern.sub(lambda m: self.decode_map[m.group()], encoded_name)

