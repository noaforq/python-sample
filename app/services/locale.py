from fastapi import Header

from app.choices.params.locale import Locale


def get_locale(locale: Locale = Header(Locale.JA)) -> Locale:
    return locale
