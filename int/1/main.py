from mysort import ProducSort



sequence = "caabca"
rules = {
    "ba": "ab",
    "ca": "ac",
    "da": "ad",
    "cb": "bc",
    "db": "bd",
    "dc": "cd",
}
a = ProducSort(sequence, rules)
a.sort()
a.print_colored_tree()
