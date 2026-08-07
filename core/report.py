class Report:

    def __init__(self):

        self.lines = []

    def add(self, text):

        self.lines.append(text)

    def print(self):

        for line in self.lines:

            print(line)