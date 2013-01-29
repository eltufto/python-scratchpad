import runsuite
import logging
from user_prompt import CmdLineUserPromptBinary

def main():
    
    FORMAT = '<MY_LOG>%(asctime)s %(levelname)s: %(message)s'
    DATEFMT = '%Y-%m-%d %I:%M:%S %p'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt=DATEFMT)

    runsuite.run(CmdLineUserPromptBinary())

if __name__ == "__main__":
    main()
