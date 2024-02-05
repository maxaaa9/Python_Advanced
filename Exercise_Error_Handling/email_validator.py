from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


DOMAIN_LIST = ("com", "bg", "net", "org")
pattern = r"\w+"
minimum_symbols = 4

command = input()
while command != "End":

    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    if len(command.split("@")[0]) <= minimum_symbols:
        raise NameTooShortError("Name must be more than 4 characters")

    if command.count("@") != 1:
        raise MoreThanOneAtSymbol

    if command.split(".")[-1] not in DOMAIN_LIST:
        DOMAIN_LIST = ', '.join(DOMAIN_LIST)
        raise InvalidDomainError(f"Domain must be one of the following: {DOMAIN_LIST}")

    if findall(pattern, command.split("@")[0])[0] != command.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")

    print("Email is valid")

    command = input()
