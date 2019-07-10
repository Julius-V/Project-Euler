import re


# Combining successful log-ins into one pass-code
def recover_pass_code(data):
    pass_code = data[0]
    for i in range(1, len(data) - 1):
        pass_code = re.sub(data[i][0] + data[i][2], data[i], pass_code)
        if pass_code[0] == data[i][1]:
            pass_code = data[i][0] + pass_code
        if pass_code[len(pass_code) - 1] == data[i][1]:
            pass_code = pass_code + data[i][2]
    return pass_code


# Loading log-ins
log_ins = open('p079_keylog.txt', 'r').read()
# Splitting into a list
log_ins = log_ins.split('\n')
print(recover_pass_code(log_ins))
