#! /usr/bin/env python
"""
Simple script to parse a schedule.yaml and output JSON
"""

import sys
import yaml
import json


def _process_schedule(schedule):
    for sid, spec in schedule.items():
        yield {"id": sid, **spec}


if __name__ == "__main__":
    fname = sys.argv[1]
    with open(fname, "r") as f:
        schedule = yaml.safe_load(f)
    
    new_schedule = {
        "version": 1,
        "minor_version": 1,
        "key": "schedule",
        "data": {
            "items": list(_process_schedule(schedule)),
        },
    }

    print(json.dumps(new_schedule, indent=2, sort_keys=False))
