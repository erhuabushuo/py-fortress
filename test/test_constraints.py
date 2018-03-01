'''
Created on Feb 24, 2018

@author: smckinn
'''
import unittest
from util.date import Date
from util.day import Day
from util.lockdate import LockDate
from util.time import Time
from util.timeout import TimeOut
from util.current_date_time import CurrentDateTime
from model.constraint import Constraint
from test.utils import print_ln, print_constraint

cons1 = [
    Constraint(
        name='foo1',
        timeout='0',
        begin_time='0100',
        end_time='2400',
        begin_date='20170101',
        end_date='20171231',
        begin_lock_date='20170101',
        end_lock_date='20171231',
        day_mask='1234567',
        ),
    Constraint(
        name='foo2',
        timeout='0',
        begin_time='0100',
        end_time='2400',
        begin_date='20170101',
        end_date='20171231',
        begin_lock_date='20180101',
        end_lock_date='20181231',
        day_mask='1234567',
        ),
    Constraint(
        name='foo3',
        timeout='0',
        begin_time='0100',
        end_time='2400',
        begin_date='20170101',
        end_date='20181231',
        begin_lock_date='20170101',
        end_lock_date='20171231',
        day_mask='1234567',
        ),
    ]

class BasicTestSuite(unittest.TestCase):
    """Test Constraints."""
                
class TestConstraints(unittest.TestCase):
    
        
    def test_time(self):
        """
        Test time-based constraints
        """
        print('test time-based constraints')
        now = CurrentDateTime()
        validators = []
        validators.append(Date(None))
        validators.append(Day(None))
        validators.append(LockDate(None))
        validators.append(Time(None))
        validators.append(TimeOut(None))
        for constraint in cons1:
            for validator in validators:
                result = validator.validate(constraint, now)
                print_constraint( constraint, "Validate" + str(validator) )
                print_ln( 'result=' + str(result), 1 )
    

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestConstraints('test_time'))
    return suite  


if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())


if __name__ == "__main__":
    unittest.main()