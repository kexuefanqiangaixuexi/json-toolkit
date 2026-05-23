import json
import sys

def validate(file_path):
    try:
        with open(file_path) as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)

def main():
    import argparse
    p = argparse.ArgumentParser(description="Validate JSON file")
    p.add_argument("file", help="JSON file to validate")
    args = p.parse_args()
    ok, err = validate(args.file)
    if ok:
        print(f"✅ {args.file} is valid JSON")
    else:
        print(f"❌ {args.file}: {err}")
        sys.exit(1)