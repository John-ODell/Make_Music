#!/usr/bin/env python3
"""Retired legacy exporter; refuses to regenerate mixed/stale-origin files."""
raise SystemExit(
    'Legacy export_review.py is retired. Use fresh Konnect MCP checks/exports '
    'and prepare_pcbway_review.py as documented in manufacturing/README.md. '
    'The old output origin and BOM substitutions must not be reused.'
)
