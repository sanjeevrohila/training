import threading
import time
import logging

__author__ = "Sanjeev Rohila"
__license__ = ""
__maintainer__ = "Sanjeev Rohila"
__email__ = "justsanjeev@gmail.com"

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s', )


def foo():
    logging.info('Starting of thread : %s' % threading.currentThread().name)
    time.sleep(2)
    logging.info('Finishing of thread : %s' % threading.currentThread().name)


def bar():
    logging.info('Starting of thread :%s' % threading.currentThread().name)
    logging.info('Finishing of thread :%s' % threading.currentThread().name)


thread1 = threading.Thread(target=foo, name='Thread-1')
thread2 = threading.Thread(target=bar, name='Thread-2')

thread1.start()
thread2.start()
