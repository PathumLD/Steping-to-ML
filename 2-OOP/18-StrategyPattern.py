class TextFormatter:
    def format(self, text):
        raise NotImplementedError

class UpperCaseFormatter(TextFormatter):
    def format(self, text):
        return text.upper()

class LowerCaseFormatter(TextFormatter):
    def format(self, text):
        return text.lower()

def print_text(text, formatter: TextFormatter):
    print(formatter.format(text))
