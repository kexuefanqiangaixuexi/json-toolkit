# json-toolkit

CLI tools for JSON processing.

## Tools

- **json-pretty** — format JSON with optional color
- **json-diff** — compare two JSON files key-by-key
- **json-query** — extract values with path expressions
- **json-validate** — check if a file is valid JSON

## Install

```bash
pip install json-toolkit
```

## Usage

```bash
echo '{"hello":"world"}' | json-pretty
json-diff old.json new.json
json-query data.json users[0].name
json-validate config.json
```