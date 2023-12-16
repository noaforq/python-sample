from app.choices.base import BaseIntEnum


class Region(BaseIntEnum):
    """
    地域ブロック
    """

    HOKKAIDO = 1, "北海道"
    TOHOKU = 2, "東北"
    KANTO = 3, "関東"
    HOKURIKU = 4, "北陸"
    CHUBU = 5, "中部"
    KINKI = 6, "近畿"
    CHUGOKU = 7, "中国"
    SHIKOKU = 8, "四国"
    KYUSHU = 9, "九州"
    OKINAWA = 10, "沖縄"
    ABROAD = 11, "海外"
    OTHERS = 12, "その他"
    NOT_SET = 13, "未設定"
