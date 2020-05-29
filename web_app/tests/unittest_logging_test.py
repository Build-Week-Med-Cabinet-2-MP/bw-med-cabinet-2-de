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


# import unittest
# import logging
# import sys


# class MyTest(unittest.TestCase):
#     def runTest(self):
#         log = logging.getLogger("TestLog")
#         log.debug("debug message")
#         self.assertEqual(1, 1)

# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# unittest.TextTestRunner().run(MyTest())


if __name__ == '__main__':
    log_file = 'log_file.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)