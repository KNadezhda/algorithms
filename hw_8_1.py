"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def descendent(self):
        return self.left, self.right


def draw_a_tree(node, code=""):
    if type(node) is str:
        return {
            node: code
        }

    l, r = node.descendent()

    result = {}
    # 0 - налево, 1 - направо
    result.update(draw_a_tree(l, code + "0"))
    result.update(draw_a_tree(r, code + "1"))

    return result


original_string = "to be or not to be"

freak = {}
for char in original_string:
    if char not in freak:
        freak[char] = 0

    freak[char] += 1

tree = freak.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Node(char1, char2), count1 + count2)
    )

frequency_table = draw_a_tree(tree[0][0])

codes = []
for char in original_string:
    codes.append(frequency_table[char])


print("Исходная строка: " + original_string)
print("Закодированная строка: %s" % " ".join(codes))

# Закодированная строка: 101 01 11 100 001 11 01 0001 11 0000 01 101 11 101 01 11 100 001
