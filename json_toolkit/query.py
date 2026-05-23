import json

def query_path(data, path):
    parts = path.replace("[", ".").replace("]", "").split(".")
    current = data
    for part in parts:
        if not part:
            continue
        if part.isdigit():
            current = current[int(part)]
        else:
            current = current[part]
    return current

def main():
    import argparse, sys
    p = argparse.ArgumentParser(description="Query JSON by path")
    p.add_argument("file", help="JSON file")
    p.add_argument("path", help="Dot-separated path (e.g. users[0].name)")
    args = p.parse_args()
    with open(args.file) as f:
        result = query_path(json.load(f), args.path)
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()