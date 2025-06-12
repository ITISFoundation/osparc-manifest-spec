#!/bin/bash
# Simple script to validate a CAD manifest against a schema
# This is now a wrapper for the new script in the scripts directory

# Forward arguments to the new script
./scripts/validate-uvx.sh "$@"
