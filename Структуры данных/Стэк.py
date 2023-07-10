# push, pop, top; O(1)

def stack1():
    stack = []
    stack.append(2)
    stack.append(7)
    print(stack[-1])
    stack.pop()
    stack.append(3)
    stack.append(4)
    print(stack[-1])
    stack.pop()
    print(stack[-1])
    stack.pop()


def is_open(s: str) -> bool:
    return s == '{' or s == '(' or s == '['


def is_pair(open: str, close: str) -> bool:
    return open == '{' and close == '}' or open == '(' and close == ')' or open == '[' and close == ']'


def for_stack2(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        if is_open(s[i]):
            stack.append(s[i])
        else:
            if stack and is_pair(stack[-1], s[i]):
                stack.pop()
            else:
                return False
    if not stack:
        return True


def stack2():
    string1 = '()({[]}())' #true
    string2 = '{}' #true
    string3 = '}{' #false
    string4 = '' #true
    string5 = '(()' #false
    string6 = '())' #false
    string7 = '[(])' #false
    print(for_stack2(string1))
    print(for_stack2(string2))
    print(for_stack2(string3))
    print(for_stack2(string4))
    print(for_stack2(string5))
    print(for_stack2(string6))
    print(for_stack2(string7))

stack2()