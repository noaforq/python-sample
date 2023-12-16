from app.services.format_checker import FormatChecker, adjust_line_feed_code


def test_check_multiple_blanks() -> None:
    test_text = adjust_line_feed_code("""aa  aa\r\n""")
    assert FormatChecker.check_multiple_blanks(test_text) == "空白が2つ連続している箇所があります。"


def test_check_multiple_line_breaks() -> None:
    test_text = adjust_line_feed_code("""a\r\n\r\n""")
    assert FormatChecker.check_multiple_line_breaks(test_text) == "改行が2つ連続している箇所があります。"


def test_check_blank_before_line_break() -> None:
    test_text = adjust_line_feed_code("""a \r\n""")
    assert FormatChecker.check_blank_before_line_break(test_text) == "行末が空白の箇所があります。"


def test_check_blank_after_line_break() -> None:
    test_text = adjust_line_feed_code("""a\r\n a""")
    assert FormatChecker.check_blank_after_line_break(test_text) == "行頭が空白の箇所があります。"


def test_check_double_byte_blank() -> None:
    test_text = adjust_line_feed_code("""a　\r\n""")
    assert FormatChecker.check_double_byte_blank(test_text) == "全角空白があります。"


def test_check_startswith_blank() -> None:
    test_text = adjust_line_feed_code(""" a\r\n""")
    assert FormatChecker.check_startswith(test_text) == "先頭行が空白または改行で始まっています。"


def test_check_startswith_line_brake() -> None:
    test_text = adjust_line_feed_code("""\r\na\r\n""")
    assert FormatChecker.check_startswith(test_text) == "先頭行が空白または改行で始まっています。"


def test_check_endswith() -> None:
    test_text = adjust_line_feed_code("""a""")
    assert FormatChecker.check_endswith(test_text) == "最後が改行で終わっていません。"


def test_check_all_error() -> None:
    test_text = adjust_line_feed_code(""" \r\n aa  bbb\r\n\r\n\r\ncc \r\ndd　""")

    error_warning_list = [
        "先頭行が空白または改行で始まっています。",
        "空白が2つ連続している箇所があります。",
        "改行が2つ連続している箇所があります。",
        "行末が空白の箇所があります。",
        "全角空白があります。",
        "行頭が空白の箇所があります。",
        "最後が改行で終わっていません。",
    ]

    error_list = FormatChecker.check(test_text)
    for i in error_list:
        assert i in error_warning_list


def test_check_all_passed() -> None:
    test_text = adjust_line_feed_code("""a\r\nb\r\n""")

    error_list = FormatChecker.check(test_text)
    for result in error_list:
        assert result is None
