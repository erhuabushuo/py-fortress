'''
Created on Mar 2, 2018

@author: smckinn
'''

from model import Session, User, Permission, Constraint
from util.validator import Validator
from util.date import Date
from util.day import Day
from util.lockdate import LockDate
from util.time import Time
from util.timeout import TimeOut
from util.current_date_time import CurrentDateTime
from ldap import permdao, userdao, LdapException, NotFound, NotUnique
from impl.security_exception import SecurityException
from util.logger import logger

validators = []
validators.append(Date())
validators.append(Day())
validators.append(LockDate())
validators.append(Time())
# TODO addme:
#validators.append(TimeOut())

def create_session (user, is_trusted):
    session = Session()
    result = True
    if is_trusted is False:
        result = userdao.authenticate(user)
        session.is_authenticated = True
    if result:
        entity = userdao.read(user)
    result = validate_constraint(entity.constraint)
    if result is False:
        raise SecurityException
    for role_constraint in entity.role_constraints:
        result = validate_constraint(role_constraint)
        if result is False:
            logger.debug('deactivate user-role: ' + entity.uid + '.' + role_constraint.name)
            entity.roles.remove(role_constraint.name)
            entity.role_constraints.remove(role_constraint)
    session.user = entity    
    return session

def validate_constraint(constraint):
    result = True
    for validator in validators:
        result = validator.validate(constraint, CurrentDateTime())
        if result is False:
            logger.debug(validator.__class__.__name__ + ' validation failed:' + constraint.name )
            break
    return result


def check_access (session, permission):
    result = False
    # TODO validate constraints here:
    
    entity = permdao.read(permission)
    
    # TODO check perm here:
    # for ever user-role in activation list... do
    
    return result


def is_user_in_role (session, role):
    result = False
    # TODO validate constraints here:
    
    # TODO check role here:
    # for ever user-role in activation list... do
    
    return result
