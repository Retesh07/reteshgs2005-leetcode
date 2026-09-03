
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for ch in expression:
            if ch == 't':
                stack.append(True)
            elif ch == 'f':
                stack.append(False)
            elif ch in '&|!(':
                stack.append(ch)
            elif ch == ',':
                continue
            elif ch == ')':
                values = []

                while stack[-1] != '(':
                    values.append(stack.pop())

                stack.pop()
                op = stack.pop()

                if op == '&':
                    result = True
                    for i in values:
                        if i==False:
                            result=False
                            break
                elif op == '|':
                    result = False
                    for i in values:
                        if i==True:
                            result=True
                            break
                else:
                    result = not values[0]

                stack.append(result)

        return stack[0]

