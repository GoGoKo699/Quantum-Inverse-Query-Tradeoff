#!/usr/bin/env python3
"""Run the two finite scientific checks and print their complete JSON results."""

import json
from pathlib import Path
import subprocess
import sys


def main():
    directory = Path(__file__).resolve().parent
    results = {}
    for name in ("check_dicke_probe", "check_poisson_features"):
        completed = subprocess.run(
            [sys.executable, str(directory / f"{name}.py")],
            check=True,
            capture_output=True,
            text=True,
        )
        results[name] = json.loads(completed.stdout)
    print(json.dumps({"status": "passed", "checks": results},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
