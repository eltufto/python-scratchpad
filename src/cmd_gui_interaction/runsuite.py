import runners
import logging
def run(user_prompt):
    response = runners.interactive('Do you see me?',user_prompt)
    if response == True:
        logging.info("Excellent!")
    else:
        logging.error("What the heck did you answer then?")
    