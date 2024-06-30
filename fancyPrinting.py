

# Define a function to print superscripts
def to_superscript(num):
    superscripts = {
        '0': '\u2070',
        '1': '\u00B9',
        '2': '\u00B2',
        '3': '\u00B3',
        '4': '\u2074',
        '5': '\u2075',
        '6': '\u2076',
        '7': '\u2077',
        '8': '\u2078',
        '9': '\u2079',
        '-': '\u207B'
    }
    return ''.join(superscripts.get(digit, '') for digit in str(num))

# Define a function to print subscripts
def to_subscript(num):
    subscripts = {
        '0': '\u2080',
        '1': '\u2081',
        '2': '\u2082',
        '3': '\u2083',
        '4': '\u2084',
        '5': '\u2085',
        '6': '\u2086',
        '7': '\u2087',
        '8': '\u2088',
        '9': '\u2089',
        '-': '\u208B'
    }
    return ''.join(subscripts.get(digit, '') for digit in str(num))

lambda_unicode = '\u03BB'
fancy_x_unicode = '\U0001D4CD'
