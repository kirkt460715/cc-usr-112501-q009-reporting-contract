"""读取分析项目的合成记录格式。"""
+import json
+from pathlib import Path
+
+REQUIRED_FIELDS = ("record_id", "period", "status")
+
+def read_records(path: str | Path) -> list[dict]:
+    data = json.loads(Path(path).read_text(encoding="utf-8"))
+    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
+        raise ValueError("数据文件必须包含 records 数组")
+    for row in data["records"]:
+        if not isinstance(row, dict) or any(field not in row for field in REQUIRED_FIELDS):
+            raise ValueError("记录字段不完整")
+    return data["records"]
+
