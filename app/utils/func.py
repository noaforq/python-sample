from datetime import timedelta


def get_h_m_s(sec: int) -> tuple[str, str, str] | tuple[int, int, int]:
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    h, m, s = str(int(h)), str(int(m)), str(int(s))  # type: ignore
    if len(h) == 1:  # type: ignore
        h = "0" + h  # type: ignore
    if len(m) == 1:  # type: ignore
        m = "0" + m  # type: ignore
    if len(s) == 1:  # type: ignore
        s = "0" + s  # type: ignore
    return h, m, s


def sec_to_time(millisec: int) -> str:
    if not millisec:
        return "-"

    h, m, s = get_h_m_s(millisec)
    if h == "00":
        pass_time = "{}:{}".format(m, s)
    else:
        pass_time = "{}:{}:{}".format(h, m, s)
    return pass_time


def format_timedelta(td: timedelta) -> str:
    """
    timedeltaから"d日h時間m分s秒"の文字列に変換
    ２４時間以内なら日単位は非表示
    """
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days == 0:
        # 日単位が0の場合は非表示
        result = f"{hours}時間{minutes}分{seconds}秒"
    else:
        result = f"{days}日{hours}時間{minutes}分{seconds}秒"

    return result
