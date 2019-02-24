def remove_dollar_sign(s):
    new_s = s.replace("$", "")
    return new_s
s = "10000$"
print(remove_dollar_sign(s))