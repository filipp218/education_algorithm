class Stack:

    def __init__(self):
        self.result = []

    def put(self, item):
        self.result.append(item)

    def pop(self):
        return self.result.pop()

    def peek(self):
        # if len(result) == 0:
        #     ex = Exception("Stack is empty")
        #     raise ex
        return self.result[-1]  # IndexError

    def length(self):
        return len(self.result)


def is_balanced(text):
    """
    >>> is_balanced('')
    True
    >>> is_balanced('Sensei says yes!')
    True
    >>> is_balanced('))((')
    False
    >>> is_balanced('(Sensei says yes!)')
    True
    >>> is_balanced('(Sensei says no!')
    False
    >>> is_balanced('(Sensei) (says) (yes!)')
    True
    >>> is_balanced('(Sensei (says) yes!)')
    True
    >>> is_balanced('((Sensei) says) no!)')
    False
    >>> is_balanced('(Sensei (says) (yes!))')
    True
    >>> is_balanced('([]{[]})')
    True

    """
    stack = Stack()
    open_char = {'(', '[', '{'}
    close_char = {')', '}',']'}
    duet = {')': '(','}':'{', ']':'['}
    for char in text:
        if char in open_char:
            stack.put(char)
        elif char in close_char:
            if stack.length() == 0:
                return False
            else:
                if stack.peek() == duet[char]:
                    stack.pop()
                else:
                    return False
    if stack.length() == 0:
        return True
    return False
