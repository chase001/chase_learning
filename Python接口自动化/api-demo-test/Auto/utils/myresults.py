# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         myresults
# Description:  
# Author            Dongtian
# Date:         2020-01-05
# -------------------------------------------------------------------------------
import unittest


class MyResult(unittest.TestResult):

    def __init__(self,stream=None, descriptions=None, verbosity=None):
        super().__init__(stream=stream, descriptions=descriptions, verbosity=verbosity)
        self.my_success = []
        self.my_fail = []
        self.my_errors = []
        self.my_skiped = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.my_success.append({'TestService': test, "type": "pass", 'time': getattr(test, "total_time",0)})

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.my_fail.append({'TestService': test, "type": "fail", 'time': getattr(test, "total_time",0),
                             "error": (err, test)})

    def addError(self, test, err):
        super().addError(test, err)
        self.my_errors.append({'TestService': test, "type": "err", 'time': getattr(test, "total_time",0),
                               "error": (err, test)})

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.my_skiped.append({'TestService': test, "type": "skiped", 'time': getattr(test, "total_time",0),
                               "reason": reason})
