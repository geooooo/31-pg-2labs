import backout as bo



bo.set_rules([
    {"source": ["G", "H"], "result": ["C"]},
    {"source": ["I", "K"], "result": ["D"]},
    {"source": ["L", "M"], "result": ["E"]},
    {"source": ["N"],      "result": ["F"]},
    {"source": ["O"],      "result": ["F"]},
    {"source": ["C"],      "result": ["A"]},
    {"source": ["D"],      "result": ["A"]},
    {"source": ["E"],      "result": ["B"]},
    {"source": ["F"],      "result": ["B"]},
    {"source": ["A"],      "result": [bo.GOAL]},
    {"source": ["B"],      "result": [bo.GOAL]},
])

bo.init_memory([bo.GOAL, "L", "M", "N"])

bo.build()

bo.out()
