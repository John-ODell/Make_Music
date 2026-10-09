#!/usr/bin/env python3
"""Record exact saved CAD/library inputs before a fresh Konnect export stage."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from prepare_pcbway_review import design_hashes

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('output', type=Path)
args = parser.parse_args()
with args.output.open('x') as stream:
    json.dump({'captured_utc': datetime.now(timezone.utc).isoformat(),
        'design_sha256': design_hashes()}, stream, indent=2)
    stream.write('\n')
print('Saved native-source checkpoint; do not mutate CAD until exports and packaging finish.')
