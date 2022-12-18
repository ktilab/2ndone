from urllib import request as rq


def validate_email(email):
    if rq.urlopen(f'https://api.2ip.me/email.txt?email={email}').read() == 'true':
        return True
    else:
        return False


def validate_login(login):
    if 6 <= len(login) <= 30:

        upper = False
        lower = False
        digits = False
        symbols = False

        if login[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            for i in login:
                if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    upper = True
                if i in 'abcdefghijklmnopqrstuvwxyz':
                    lower = True
                if i in '0123456789':
                    digits = True
                if i in '_':
                    symbols = True
        if upper and lower and digits and symbols:
            return True
        else:
            return False
    else:
        return False


def validate_password(password):
    upper = False
    lower = False
    digits = False
    symbols = False
    if 8 <= len(password) <= 30:
        for i in password:
            if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                upper = True
            if i in 'abcdefghijklmnopqrstuvwxyz':
                lower = True
            if i in '0123456789':
                digits = True
            if i in '_-+*.!%$#@&*^|\/~[]{}':
                symbols = True
        if upper and lower and digits and symbols:
            return True
        else:
            return False
    else:
        return False

