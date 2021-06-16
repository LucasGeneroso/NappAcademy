from contextlib import contextmanager

@contextmanager
def spoiler():
    print('<spoiler>')
    yield
    print('</spoiler>')

with spoiler():
    print('Carminha: tufão, você é corno')