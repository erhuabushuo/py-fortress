'''
Created on Feb 24, 2018

@author: smckinn
@copyright: 2018 - Symas Corporation
'''

from util.validator import Validator
from util.logger import logger
from util.global_ids import CONSTRAINT_LOCKDATE_ERROR, SUCCESS

class LockDate(Validator):
        
    def validate(self, constraint, now):
        if not constraint.begin_lock_date or constraint.begin_lock_date is None or not constraint.end_lock_date or constraint.end_lock_date is None:
            return SUCCESS                
        elif constraint.begin_lock_date == 'none' or constraint.end_lock_date == 'none':
            return SUCCESS                
        elif constraint.begin_lock_date <= now.date <= constraint.end_lock_date:
            return CONSTRAINT_LOCKDATE_ERROR
        else:
            return SUCCESS        
        
        