import json, tempfile, os
from json_toolkit.validate import validate

def test_valid():
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    json.dump({"ok": True}, f); f.close()
    ok, err = validate(f.name)
    assert ok
    os.unlink(f.name)

def test_invalid():
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    f.write("{invalid"); f.close()
    ok, err = validate(f.name)
    assert not ok
    os.unlink(f.name)