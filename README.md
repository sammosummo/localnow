# localnow

## Description

This small Python package is a drop-in replacement for `datetime.datetime.now` that returns the current time in the 
local timezone.

## Usage

Suppose you want the current date and time. You could do this:

```python
import datetime

x = datetime.datetime.now()
```

By default, `x` will be in UTC. `datetime.datetime.now` takes an optional `tz` argument that you can use to specify a
different timezone. However, if you want to use your *local* timezone, wherever that may be, you need an extra step:

```python
import datetime

tz = datetime.datetime.utcnow().astimezone().tzinfo
x = datetime.datetime.now(tz=tz)
```

Personally, I find the `tz = ...` line to be a bit of a distraction and difficult to remember, so I made this package.
It provides a drop-in replacement for `datetime.datetime.now` that is essentially does the same as the code above but
with a little less code:

```python
from localnow import now

x = now()
```

That's it.

## Installation

You can install this package from PyPI:

```bash
pip install localnow
```

## License

MIT

