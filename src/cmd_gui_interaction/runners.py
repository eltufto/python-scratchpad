import logging
    
def interactive(cmd, expected_response, user_prompt):
    logging.info("Some logging stuff")
    response = user_prompt.response("Did you see this question?")
    if response:
        logging.info("Excellent!")
    else:
        logging.error("What the heck did you answer then?")