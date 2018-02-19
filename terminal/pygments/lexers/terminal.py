from pygments.lexer import RegexLexer
from pygments.token import *

class TerminalLexer(RegexLexer):
    name      = 'Terminal'
    aliases   = ['terminal']
    filenames = ['*.terminal']

    tokens = {
        'root': [
            (r'\$.*\n', Name.Namespace),
            (r'.*\n', Text),
        ]
    }
