"""
Exercise — printtime context manager

We had this:
>>> t = time.time()
>>> ans = do_calculations()
>>> t2 = time.time()
>>> print('calculations took {} s'.format(t2-t))
calculations took 3.4 s

Implement this:
>>> with printtime_cm():
...     time.sleep(3)
calculations took 3.40001 s
"""

import time
import contextlib

@contextlib.contextmanager
def printtime_cm():
    t = time.time()
    yield
    t2 = time.time()
    print('execution took', t2 - t, 's')
