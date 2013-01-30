import runsuite
import logging
from interaction.harness import cmdline_interaction

def main():
    
    FORMAT = '<MY_LOG>%(asctime)s %(levelname)s: %(message)s'
    DATEFMT = '%Y-%m-%d %I:%M:%S %p'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt=DATEFMT)

    runsuite.run(cmdline_interaction)

if __name__ == "__main__":
    main()
