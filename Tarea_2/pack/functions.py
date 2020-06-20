import re


def check_email(email):
    r = re.match('[A-z0-9]*\x40([A-z0-9]*.){1,2}[A-z]*$', email)
    if r:
        return True
    else:
        return False


def check_phone(num):
    if len(re.findall(r'\d', num)) != 10:
        return False
    r = re.match('[(]?[0-9]*[)]?(\s?[0-9]*)*$', num)
    if r:
        return True
    else:
        r = re.match('[(]?[0-9]*[)]?([-]?[0-9]*)*$', num)
        if r:
            return True
        else:
            return False


def check_curp(curp):
    r = re.match('[A-z]{4}[0-9]{6}[MmHh]{1}[A-z]{2}[A-z]{3}[0-9]{2}$', curp)
    if r:
        return True
    else:
        return False


def check_rfc(rfc):
    r = re.match('[A-z]{4}[0-9]{6}[A-z0-9]{3}$', rfc)
    if r:
        return True
    else:
        return False
