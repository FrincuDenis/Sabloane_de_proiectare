import author,element,chapters,subchapters,paragraph,image,table
class Book:
    def __init__(self,title):
        self.title=title
        self.author=author
        self.chapters=[]
        self.subchapters=[]

    def add_chapter(self, chapter):
        self.chapters.append(chapter)

    def print(self):
        print(f"Book Title: {self.title}")
        if author:
            self.author.print()
        else:
            print "None"
        for chpt in chapters:
            chpt.print()