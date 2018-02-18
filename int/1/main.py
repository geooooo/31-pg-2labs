from mysort import ProducSort



sequence = "abacd"
rules = {
    "aba": "cd",
    "aa": "bb",
    "cb": "bac",
    "a": "c",
    "b": "ac"
}
a = ProducSort(sequence, rules)
a.sort()
a.print_colored_tree()
