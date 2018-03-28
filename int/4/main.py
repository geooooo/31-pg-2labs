import backout as bo



bo.set_rules([
    {"source": ["G", "H"], "result": ["C"]}, #1
    {"source": ["I", "K"], "result": ["D"]}, #2
    {"source": ["L", "M"], "result": ["E"]}, #3
    {"source": ["N"],      "result": ["F"]}, #4
    {"source": ["O"],      "result": ["F"]}, #5
    {"source": ["C"],      "result": ["A"]}, #6
    {"source": ["D"],      "result": ["A"]}, #7
    {"source": ["E"],      "result": ["B"]}, #8
    {"source": ["F"],      "result": ["B"]}, #9
    {"source": ["A"],      "result": [bo.GOAL]}, #10
    {"source": ["B"],      "result": [bo.GOAL]}, #11
])

bo.init_memory([bo.GOAL, "L", "M", "N"])

bo.build()

bo.out_to_html("result.html")
