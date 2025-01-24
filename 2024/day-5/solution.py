import json
import sys

from collections import defaultdict
from itertools import pairwise
from pprint import pprint


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.post: Node | None = None
        self.previous: Node | None = None

    def update_previous(self, node):
        setattr(self, "previous", node)

    def update_post(self, node):
        setattr(self, "post", node)
    
    def __str__(self):
        return f"value: {self.value}\tpre: {self.previous.value}\tpost: {self.post.value}"

    def __repr__(self):
        return f"value: {self.value}\tpre: {self.previous.value}\tpost: {self.post.value}"


PAGE_NODE_MAP: dict[int, Node] = {}


def build_list(rules: list[str]):
    for rule in rules:
        page_pre, page_post = tuple(map(int, rule.split("|")))

        if not PAGE_NODE_MAP.get(page_pre):
            node_pre = Node(page_pre)
            PAGE_NODE_MAP[page_pre] = node_pre
        node_pre = PAGE_NODE_MAP[page_pre]

        if not PAGE_NODE_MAP.get(page_post):
            node_post = Node(page_post)
            PAGE_NODE_MAP[page_post] = node_post
        node_post = PAGE_NODE_MAP[page_post]

        if node_post.previous is None:
            node_post.update_previous(node_pre)
        else:
            if node_post.previous.value > node_pre.value:
                node_post.previous.update_post(node_pre)

        if node_pre.post is None:
            node_pre.update_post(node_post)
        else:
            if node_pre.post.value > node_post.value:
                node_pre.post.update_post(node_post)
            else:
                node_pre.post.update_previous(node_post)

def solve(lines: tuple[str, ...]):
    bool_rules = True
    rules = []
    pages = []
    for line in lines:
        if bool_rules:
            if line.strip():
                rules.append(line)
            else:
                bool_rules = False
        else:
            pages.append(line)

    pred_rule_lookup = defaultdict(dict)
    succ_rule_lookup = defaultdict(dict)
    for rule in rules:
        # print(rule)
        pred, succ = rule.split("|")
        # pprint(f"{pred}, {succ}")
        pred_rule_lookup[pred][succ] = True
        succ_rule_lookup[succ][pred] = True

    for page in pages:
        combos = tuple(pairwise(page.split(",")))
        pprint(f"{page}: {combos}")
    print(json.dumps(pred_rule_lookup, indent=4))
    print(json.dumps(succ_rule_lookup, indent=4))
    build_list(rules)
    pprint(PAGE_NODE_MAP)


def main(input_filename="input.txt"):
    lines = tuple(i.strip() for i in open(input_filename).readlines() if len(i))
    solve(lines)


if __name__ == "__main__":
    input_filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            input_filename = "sample_input.txt"
    main(input_filename)
