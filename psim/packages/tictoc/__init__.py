# see https://stackoverflow.com/questions/5849800/what-is-the-python-equivalent-of-matlabs-tic-and-toc-functions

import time


tics = []

def tic():
    tics.append(time.process_time())

def toc():
    if len(tics) == 0:
        return None
    else:
        return time.process_time() - tics.pop()
