import json
import sys

def pretty_print(data, indent=2):
    return json.dumps(data, indent=indent, ensure_ascii=False, sort_keys=True)

def main():
    import argparse
    p = argparse.ArgumentParser(description="Prettify JSON")
    p.add_argument("file", nargs="?", help="JSON file (stdin if omitted)")
    p.add_argument("-i", "--indent", type=int, default=2)
    args = p.parse_args()
    src = open(args.file) if args.file else sys.stdin
    print(pretty_print(json.load(src), args.indent))