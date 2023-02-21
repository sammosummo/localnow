import datetime

tz: datetime.tzinfo = datetime.datetime.utcnow().astimezone().tzinfo
default_datetime: datetime.datetime = datetime.datetime.fromtimestamp(0, tz=tz)


def now() -> datetime:
    """Wrapper for datetime.now() injected with local timezone."""
    return datetime.datetime.now(tz=tz)
