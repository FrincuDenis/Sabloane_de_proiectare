import element as elmm
class subchapters:
    def __init__(self,title):
        self.title=title

    def print(self):
        print(f"Subchapter: {self.title}")
        for elm in elmm.element:
            elm.print()