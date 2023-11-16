# Visitor interface
class Visitor:
    def visit_element(self, elementV):
        pass


# ConcreteVisitorA and ConcreteVisitorB are the classes of visitors
# that define the operations to be performed on the elements.
class ConcreteVisitorStats(Visitor):
    nri = 0
    nrt = 0
    nrp=  0
    def visit_concrete_element_paragraph(self, element_a):
        pass
    def visit_concrete_element_image(self, element_b):
        pass

    def visit_concrete_element_table(self, element_b):
        pass

