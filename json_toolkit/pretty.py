import json
import sys

def pretty_print(data, indent=2, color=False):
    output = json.dumps(data, indent=indent, ensure_ascii=False, sort_keys=True)
    if color:
        import re
        output = re.sub(r'("[^"]+"):', r'\033[36m\1\033[0m:', output)
        output = re.sub(r': ("[^"]+")', r': \033[32m\1\033[0m', output)
    return output

def main():
    import argparse
    p = argparse.ArgumentParser(description="Prettify JSON")
    p.add_argument("file", nargs="?", help="JSON file (stdin if omitted)")
    p.add_argument("-i", "--indent", type=int, default=2)
    p.add_argument("-c", "--color", action="store_true")
    args = p.parse_args()
    src = open(args.file) if args.file else sys.stdin
    print(pretty_print(json.load(src), args.indent, args.color))