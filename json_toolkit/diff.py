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

def diff_files(file_a, file_b, output_format="diff"):
    with open(file_a) as a, open(file_b) as b:
        data_a, data_b = json.load(a), json.load(b)
    flat_a = dict(flatten(data_a))
    flat_b = dict(flatten(data_b))
    diffs = []
    for k in sorted(set(flat_a) | set(flat_b)):
        if k not in flat_a:
            diffs.append({"path": k, "op": "add", "value": flat_b[k]})
        elif k not in flat_b:
            diffs.append({"path": k, "op": "remove", "old": flat_a[k]})
        elif flat_a[k] != flat_b[k]:
            diffs.append({"path": k, "op": "change", "old": flat_a[k], "new": flat_b[k]})
    if output_format == "json":
        return json.dumps(diffs, indent=2, ensure_ascii=False)
    lines = []
    for d in diffs:
        if d["op"] == "add":
            lines.append(f"+ {d['path']}: {d['value']}")
        elif d["op"] == "remove":
            lines.append(f"- {d['path']}: {d['old']}")
        else:
            lines.append(f"~ {d['path']}: {d['old']} -> {d['new']}")
    return "\n".join(lines)