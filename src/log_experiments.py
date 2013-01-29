import logging
FORMAT = '<root log>%(asctime)s %(levelname)s: %(message)s'
DATEFMT = '%Y-%m-%d %I:%M:%S %p'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt=DATEFMT)
logging.info("hello world")
print "word"