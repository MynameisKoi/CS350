class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

class Polynomial:
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead

    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree

    def __getitem__(self, degree):
        assert self.degree() >= 0, \
            "Operation not permitted on an empty polynomial."

        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree:
            curNode = curNode.next

        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.coefficient

    def evaluate(self, scalar):
        assert self.degree() >= 0, \
            "Only non-empty polynomials can be evaluated."

        result = 0.0

        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next

        return result

    def __add__(self, rhsPoly):
        """
        Creates and returns a new Polynomial that is the result of adding this polynomial and
        the rhsPoly.This operation is not defined if either polynomial is empty.
        """
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
            "Addition only allowed on non-empty polynomials."

        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = rhsPoly._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                coefficient = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                coefficient = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree  # or degree = nodeB.degree
                coefficient = nodeA.coefficient + nodeB.coefficient
                nodeA = nodeA.next
                nodeB = nodeB.next

            newPoly._appendTerm(degree, coefficient)

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newPoly

    def _termMultiply(self, termNode):
        newPoly = Polynomial()

        curr = self._polyHead
        while curr is not None:
            newDegree = curr.degree + termNode.degree
            newCoefficient = curr.coefficient * termNode.coefficient

            newPoly._appendTerm(newDegree, newCoefficient)

            curr = curr.next

        return newPoly

    def _appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm

            self._polyTail = newTerm

    def printPoly(self):
        curNode = self._polyHead
        while curNode is not None:
            if curNode.next is not None:
                # string format based on the dictionary.
                print("%(coefficient)sx^%(degree)s + " % {"coefficient": curNode.coefficient, "degree": curNode.degree}, end="")
            else:
                print("%(coefficient)sx^%(degree)s" % {"coefficient": curNode.coefficient,
                                                       "degree": curNode.degree})
            curNode = curNode.next

# multiply 2 poly together
def conv_LL(l,m):
    assert l.degree() >= 0 and m.degree() >= 0,\
            "Multiplication only allowed on non-empty polynomials."
    node = l._polyHead
    newPoly = m._termMultiply(node)

    node = node.next
    while node is not None:
        tempPoly = m._termMultiply(node)
        newPoly += tempPoly
        node = node.next
    return newPoly

leftPoly = Polynomial(5, 4)
leftPoly += Polynomial(3, 3)
leftPoly += Polynomial(2, 2)
leftPoly += Polynomial(0, 1)

rightPoly = Polynomial(4, 8)
rightPoly += Polynomial(3, 7)
rightPoly += Polynomial(1, 6)
rightPoly += Polynomial(0, 5)

mulPoly = conv_LL(leftPoly, rightPoly)
x = 2
evalPoly = mulPoly.evaluate(x)

print("The multiplication of the two polynomials is:")
mulPoly.printPoly()

print(f"The evaluation of the mulPoly at x = {x} is:", evalPoly)