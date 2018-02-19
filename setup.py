from setuptools import setup, find_packages

lexers = [
    'terminal   = terminal.pygments.lexers:TerminalLexer',
]

setup(
    name = "terminal-pygments",
    version = "0.1.dev1",
    packages = find_packages(),
    install_requires = ['Pygments>=2'],
    entry_points = {
        'pygments.lexers' : lexers,
    },
)
