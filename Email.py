from email_validator import validate_email, EmailNotValidError

try:
    v = validate_email('idra@@gmail.com')
    print('Email is valid')
except EmailNotValidError as e:
    print('Email is not valid')
    print(e)    #show error explanation
