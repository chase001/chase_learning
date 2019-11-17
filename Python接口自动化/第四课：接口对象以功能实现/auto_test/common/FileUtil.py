"""
    文件处理模块
"""


class FileUtil(object):
    def __init__(self, file_path, method="r+", encoding="utf-8"):
        self.file_name = file_path  # 文件路径和名称
        self.file_obj = self._open_file(method, encoding)

    def _open_file(self, method, encoding):
        f = open(self.file_name, method, encoding=encoding)
        return f

    def read_for_lines(self):
        """
        逐行读取
        :return:list
        """
        lines = self.file_obj.readlines()
        for line in lines:
            print(line)
        return lines

    def clear(self):
        """
        清空文件内容
        :return:
        """
        self.file_obj.truncate()
