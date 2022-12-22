def assignTk(token):
    match token:
        case 'SPL':
            return 'import os\nimport sys'
        case 'AA':
            return 'if '
        case 'AB':
            return 'def '
        case 'AC':
            return 'class'
        case 'AD':
            return 'else '
        case 'AE':
            return 'elif '
        case 'AF':
            return 'import '
        case 'AG':
            return 'as '
        case 'AH':
            return 'for '
        case 'AI':
            return 'in '
        case 'AJ':
            return 'with '
        case 'AK':
            return 'try:'
        case 'AL':
            return 'except:'
        case 'AM':
            return 'case '
        case 'AN':
            return 'return '
        case 'AO':
            return 'match '
        case 'A1':
            return 'print'
        case 'A2':
            return 'input'
        case 'B0':
            return '#'
        case 'B1':
            return ':'
        case 'B2':
            return '"'
        case 'B3':
            return '('
        case 'B4':
            return ')'
        case 'B5':
            return '='
        case 'B6':
            return '=='
        case 'B7':
            return '!='
        case 'B8':
            return '+'
        case 'B9':
            return "'"
        case 'B10':
            return '{'
        case 'B11':
            return '}'
        case 'B12':
            return ','
        case 'B13':
            return '.'
        case 'B14':
            return '+='
        case 'B15':
            return '['
        case 'B16':
            return ']'
        case 'C1':
            return 'True'
        case 'C2':
            return 'False'
        case 'D1':
            return '    '
        case 'D2':
            return ' '
        case 'D3':
            return '\n'
        case false:
            return f'{token}'