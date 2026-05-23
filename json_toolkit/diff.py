import json
from collections import OrderedDict

def flatten(obj, prefix=""):
    items = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            items.extend(flatten(v, f"{prefix}.{k}" if prefix else k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            items.extend(flatten(v, f"{prefix}[{i}]"))
    else:
        items.append((prefix, obj))
    return items

def diff_files(file_a, file_b):
    with open(file_a) as a, open(file_b) as b:
        data_a, data_b = json.load(a), json.load(b)
    flat_a = dict(flatten(data_a))
    flat_b = dict(flatten(data_b))
    diffs = []
    for k in set(flat_a) | set(flat_b):
        if k not in flat_a:
            diffs.append(f"+ {k}: {flat_b[k]}")
        elif k not in flat_b:
            diffs.append(f"- {k}: {flat_a[k]}")
        elif flat_a[k] != flat_b[k]:
            diffs.append(f"~ {k}: {flat_a[k]} -> {flat_b[k]}")
    return "\n".join(diffs)

def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("file_a")
    p.add_argument("file_b")
    args = p.parse_args()
    print(diff_files(args.file_a, args.file_b))