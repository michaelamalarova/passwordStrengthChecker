import getpass, re


# prompt (string): The message shown to the user when asking for input
# here the prompt=Password: is default text
# getpass for inputting password
# getuser outputs users username
def get_secure_input(prompt='Password: '):
    return getpass.getpass(prompt)


def has_repetitive_chars(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def has_sequential_chars(s):
    for i in range(len(s) - 2):
        if ord(s[i]) == ord(s[i + 1]) - 1 == ord(s[i + 2]) - 2:
            return True
    return False


# password rules:
# length - at least 12 char
# characters - one uppercase, one lowercase, one numbers, one symbol
# predictable patterns - dont use 2 repetitive  char, dont use 3 sequential char / numbers,
# no personal information - dont include username in pass, that we can check with the getuser()
# test data:
# high - Av7/mic gha.
# medium - Av7/mmc gha., Av7/mic abc., Av7/michaha., Avv7/michabc
# low - Av7/mic, av7/micg, AV7/MICG, Av./micg, Av70micg
# non. - Av7/m
def check_password_strength(password):

    high_criteria = {
        "length": len(password) >= 12,
        "uppercase": re.search(r'[A-Z]', password),
        "lowercase": re.search(r'[a-z]', password),
        "digit": re.search(r'[1-9]', password),
        "symbol": re.search(r'[^A-Za-z0-9]', password),
        "repetitive": not has_repetitive_chars(password),
        "sequential": not has_sequential_chars(password),
        "personalInfo": getpass.getuser() not in password
    }
    medium_criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password),
        "lowercase": re.search(r'[a-z]', password),
        "digit": re.search(r'[1-9]', password),
        "symbol": re.search(r'[^A-Za-z0-9]', password),
    }
    low_criteria = {
        "length": len(password) >= 6,
    }

    if all(high_criteria.values()):
        return f"High"
    elif all(medium_criteria.values()):
        non_compliant_high_criteria = []

        for criterion, is_valid in high_criteria.items():
            if not is_valid:
                non_compliant_high_criteria.append(criterion)
        return f"Medium, \nnon compliant criteria for high strength: {non_compliant_high_criteria}"
    elif all(low_criteria.values()):
        non_compliant_medium_criteria = []
        for criterion, is_valid in medium_criteria.items():
            if not is_valid:
                non_compliant_medium_criteria.append(criterion)
        return f"Low, \nnon compliant criteria for medium strength: {non_compliant_medium_criteria}"
    else:
        non_compliant_low_criteria = []
        for criterion, is_valid in low_criteria.items():
            if not is_valid:
                non_compliant_low_criteria.append(criterion)
        return f"noncompliant, \nnon compliant criteria for low strength: {non_compliant_low_criteria}"


def main():
    print('*** PASSWORD CHECKER ***')
    password_for_check = get_secure_input(prompt=f"Hi {getpass.getuser()}!\nEnter password you wants to check: ")
    password_strength = check_password_strength(password_for_check)
    print(f'Your password strength is {password_strength}')


if __name__ == "__main__":
    main()
