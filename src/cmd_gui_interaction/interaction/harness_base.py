from modes_base import QuestionBase

class HarnessBase(object):
    _binary_question = QuestionBase()
    @property
    def binary_question(self): 
        return self._binary_question
    @binary_question.setter
    def binary_question(self, val):
        self._binary_question = val
