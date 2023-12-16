import inspect
import re


class FormatChecker:
    """ """

    BLANK = " "  # 半角スペース
    LINE_BREAK = "\n"  # 改行
    DOUBLE_BLANK = "　"  # 全角スペース

    @classmethod
    def check_multiple_blanks(cls, stdin: str) -> str | None:
        if (cls.BLANK + cls.BLANK) in stdin:
            return "空白が2つ連続している箇所があります。"
        return None

    @classmethod
    def check_multiple_line_breaks(cls, stdin: str) -> str | None:
        if (cls.LINE_BREAK + cls.LINE_BREAK) in stdin:
            return "改行が2つ連続している箇所があります。"
        return None

    @classmethod
    def check_blank_before_line_break(cls, stdin: str) -> str | None:
        if (cls.BLANK + cls.LINE_BREAK) in stdin:
            return "行末が空白の箇所があります。"
        return None

    @classmethod
    def check_blank_after_line_break(cls, stdin: str) -> str | None:
        if (cls.LINE_BREAK + cls.BLANK) in stdin:
            return "行頭が空白の箇所があります。"
        return None

    @classmethod
    def check_double_byte_blank(cls, stdin: str) -> str | None:
        if cls.DOUBLE_BLANK in stdin:
            return "全角空白があります。"
        return None

    @classmethod
    def check_startswith(cls, stdin: str) -> str | None:
        if stdin.startswith(cls.BLANK) or stdin.startswith(cls.LINE_BREAK):
            return "先頭行が空白または改行で始まっています。"
        return None

    @classmethod
    def check_endswith(cls, stdin: str) -> str | None:
        if not stdin.endswith(cls.LINE_BREAK):
            return "最後が改行で終わっていません。"
        return None

    @classmethod
    def check(cls, stdin: str) -> list:

        if not stdin:
            stdin = ""

        error_list = []

        for method in inspect.getmembers(cls, inspect.ismethod):
            method_name = method[0]
            if method_name.startswith("check_"):
                result = getattr(cls, method_name)(stdin)
                error_list.append(result)

        return error_list


def adjust_line_feed_code(std: str) -> str:
    """
    std_in, std_outを改行コードをLFに統一する
    """
    # 改行コードの統一
    text = re.sub(r"\r\n|\r|\n", "\n", std)
    return text
