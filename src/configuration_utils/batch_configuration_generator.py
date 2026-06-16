"""
Sources:

References:

Synopsis:
    批量生成配置文件的工具类。

Notes:

"""

from __future__ import annotations
from loguru import logger

from jinja2 import Template
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class BatchConfigurationGenerator:
    """
    批量生成配置文件的工具类。

    基于 jinja2 语法，需要提前在模板中进行构建。
    """
    # ====主要方法。====
    @staticmethod
    def batch_make_configuration_files(
        template_path: str | Path,
        configs_kwargs: dict,
        paths_to_save: str | Path,
    ) -> None:
        ...

    # ====基础方法。====
    @staticmethod
    def make_configuration_file(
        template_path: str | Path,
        configs_kwargs: dict,
        path_to_save: str | Path,
    ) -> None:
        """
        通过配置的模板文件，生成指定参数后的配置文件。

        Args:
            template_path (Union[str, Path]): 模板文件的路径。不限制模板类型，但需要以jinja2语法提供可变配置。
            configs_kwargs (dict): 需要配置设置的参数。
            path_to_save (Union[str, Path]): 保存的路径。

        Returns:
            None: 保存配置文件至指定路径。
        """
        # 读取模板文件。不限制文件类型。
        with open(template_path, 'r', encoding='utf-8') as template:
            template = Template(template.read())
        # 填入配置。
        configuration = template.render(**configs_kwargs)
        # 保存配置文件。
        with open(path_to_save, 'w', encoding='utf-8') as file:
            file.write(configuration)

