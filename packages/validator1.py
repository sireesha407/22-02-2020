import re
def phonevalidator1(no):
    pattern='^[6-9][0-9]{9}$|[0][6-9][0-9]{9}$|[+][9][1][6-9][0-9]{9}$'
    if(re.match(pattern,str(no))):
        return True
    return False

def emailValidator(mail):
    pattern='[a-z0-9][a-z0-9._]{5,20}[@][a-z0-9._]{4,8}[.][a-z]{2,4}'
    if re .match(pattern,mail):
        return True
    else:
        return False
