# x256 [![Tests](https://github.com/magarcia/python-x256/actions/workflows/test.yml/badge.svg)](https://github.com/magarcia/python-x256/actions/workflows/test.yml) [![Code Analysis](https://github.com/magarcia/python-x256/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/magarcia/python-x256/actions/workflows/codeql-analysis.yml) [![PyPI version](https://badge.fury.io/py/x256.svg)](https://pypi.org/project/x256/)

_This is a python version from [node-x256](https://github.com/substack/node-x256)_

Return the nearest
[xterm 256 color code](http://www.frexx.de/xterm-256-notes/)
for rgb inputs.

# Example

You can just print the index:

```python
from x256 import x256
ix = x256.from_rgb(220, 40, 150)
print ix # 162
```

or you can use raw ansi escape codes:

```python
from x256 import x256
ix = x256.from_rgb(220, 40, 150)
print '\x1b[38;5;' + str(ix) + 'mBEEEEEP'
```

output:

![x256 raw beep](./screenshots/x256_raw_beep.png)

# Methods

## x256.from_rgb(red, green, blue)

Return the nearest xterm 256 color code for the 24-bit `[red, green, blue]`
values.

`red`, `green`, and `blue` should each be integers from 0 through 255,
inclusive.

## x256.from_hex(hex)

Return the nearest xterm 256 color code for the hexadecimal color
values.

`hex` should be string without 0x.

## x256.to_rgb(ix)

Return 24-bit `[red, green, blue]` values from xterm 256 color code.

`ix` should be integer.

## x256.to_hex(ix)

Return hexadecimal color from xterm 256 color code.

`ix` should be integer.

# Install

```shell
python -m pip install x256
```

# License

Copyright (c) 2012 Martin Garcia (newluxfero@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
