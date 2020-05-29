from pdb import set_trace as st
import sys
import unittest
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestCase(unittest.TestCase):
    def testSimpleMsg(self):
        stream_handler.stream = sys.stdout
        print("AA")
        logging.getLogger().info("BB")
        # st()


log_file = 'log_file1.txt'
with open(log_file, "w") as f:
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)

with open(log_file, "r") as f:
    f.read()