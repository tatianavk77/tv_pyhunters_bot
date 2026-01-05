from aiogram.filters.callback_data import CallbackData

class CallbackMenu(CallbackData, prefix="СМ"):
    button: str


class CallbackTalk(CallbackData, prefix="СT"):
    button: str
    celebrity: str


class CallbackQUIZ (CallbackData, prefix="СQ"):
    button: str
    subject: str