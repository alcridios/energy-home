def is_empty(name, value):
    message_error = ''

    if value == '':
        message_error = 'CAMPO {0} SE ENCUENTRA VACIÓ\n'.format(name)
    return message_error

def is_emptys(**kwargs):
    message_error = ''

    for key, value in kwargs.items():
        message_error = message_error + is_empty(key, value)
    return message_error    