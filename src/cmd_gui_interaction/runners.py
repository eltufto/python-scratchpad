def interactive(cmd, user_prompt):
    response = user_prompt.binary_question.response(cmd)
    return response
