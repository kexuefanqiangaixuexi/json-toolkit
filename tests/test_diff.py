import json, tempfile, os
from json_toolkit.diff import diff_files

def test_diff_add():
    a = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    b = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    json.dump({"a": 1}, a); a.close()
    json.dump({"a": 1, "b": 2}, b); b.close()
    result = diff_files(a.name, b.name)
    assert "+ b" in result
    os.unlink(a.name); os.unlink(b.name)