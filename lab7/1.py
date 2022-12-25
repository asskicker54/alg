class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['!', '&', '|', 'False', 'True', '+', '-', '*', '/', '&', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['True', 'False']:
            current_tree.set_root_val(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['!', '&', '|', '+', '-', '*', '/', '&']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return e_tree


def evaluate(parse_tree):
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y,
                 '&': lambda x, y: str(bool(x) & bool(y)),
                 '|': lambda x, y: str(bool(x) | bool(y)),
                 '!': lambda x: str(not bool(x))
                 }

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()
    print(parse_tree.get_root_val())
    if left_c and right_c:
        fn = operators[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    elif left_c and not right_c:
        fn = operators[parse_tree.get_root_val()]
        return fn(evaluate(left_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> None:
    left_c = tree.get_left_child()
    right_c = tree.get_right_child()

    if left_c and right_c:
        print("(", end=" ")
        print_exp(left_c)
        print((tree.get_root_val()), end=" ")
        print_exp(right_c)
        print(")", end=" ")
    elif left_c and not right_c:
        print_exp(left_c)
        print(tree.get_root_val())
    else:
        print(tree.get_root_val(), end=" ")


pt = build_parse_tree("( ( True & False ) | False )")
print(evaluate(pt))
print_exp(pt)
