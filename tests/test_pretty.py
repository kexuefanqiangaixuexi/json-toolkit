import json
from json_toolkit.pretty import pretty_print

def test_pretty_basic():
    data = {"b": 2, "a": 1}
    result = pretty_print(data)
    parsed = json.loads(result)
    assert list(parsed.keys()) == ["a", "b"]

def test_pretty_indent():
    data = {"x": [1, 2, 3]}
    result = pretty_print(data, indent=4)
    assert "    " in result