class SubChapter:
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def print_subchapter(self):
        print(f"Subchapter name: {self.name}")
        for element in self.elements:
            element.print()
