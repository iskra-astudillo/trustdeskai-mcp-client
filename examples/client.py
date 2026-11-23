#!/usr/bin/env python3
"""Minimal MCP client for TrustDeskAI: initialize, then tools/list. Standard library only."""
import json, urllib.request
URL = "https://trustdeskai.eliteaiempire.com/mcp"
H = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
def call(body, extra=None):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={**H, **(extra or {})}, method="POST")
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode(), r.headers
body, hd = call({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "example", "version": "1"}}})
print(body[:600])
sid = hd.get("Mcp-Session-Id")
extra = {"Mcp-Session-Id": sid} if sid else None
body, _ = call({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}, extra)
print(body[:2000])
