#!/usr/bin/env python3
"""
Script to synchronize vocabulary IDs from vocab files to enums in schema files.
This keeps the schema validation in sync with the vocabulary definitions.
"""

import json
import sys
import logging
from pathlib import Path

# Set up logging
logger = logging.getLogger(__name__)

# Define paths relative to project root
REPO_ROOT = Path(__file__).parent.parent
VOCAB_DIR = REPO_ROOT / "vocab"
SCHEMA_DIR = REPO_ROOT / "schema"

# Files to sync
SCHEMA_FILE = SCHEMA_DIR / "sim_manifest.schema.json"
TAGS_FILE = VOCAB_DIR / "semantic-tags.json"
BOUNDARY_CONDITIONS_FILE = VOCAB_DIR / "boundary-conditions.json"


def load_json_file(file_path):
    """Load and parse a JSON file using Path methods."""
    try:
        return json.loads(Path(file_path).read_text(encoding="utf-8"))
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error("Error loading %s", file_path, exc_info=e)
        sys.exit(1)


def save_json_file(file_path, data):
    """Save data to a JSON file using Path methods."""
    try:
        Path(file_path).write_text(json.dumps(data, indent=2), encoding="utf-8")
        logger.info("Updated  %s", file_path)
    except IOError as e:
        logger.error("Error saving %s", file_path, exc_info=e)
        sys.exit(1)


def extract_ids(vocab_file, id_container):
    """Extract IDs from a vocabulary file."""
    data = load_json_file(vocab_file)
    return [item["id"] for item in data.get(id_container, [])]


def update_schema():
    """Update the schema file with IDs from vocabulary files."""
    # Load schema
    schema = load_json_file(SCHEMA_FILE)

    # Extract IDs from vocabulary files
    tag_ids = extract_ids(TAGS_FILE, "tags")
    boundary_condition_ids = extract_ids(BOUNDARY_CONDITIONS_FILE, "conditions")

    # Get references to the enum arrays in the schema
    mappings_items = schema["properties"]["mappings"]["items"]
    tags_enum = mappings_items["properties"]["tags"]["items"]["enum"]
    boundary_conditions_enum = mappings_items["properties"]["boundary_conditions"]["items"]["enum"]

    # Update enums
    if set(tags_enum) != set(tag_ids):
        mappings_items["properties"]["tags"]["items"]["enum"] = tag_ids
        logger.info("Updated tags enum with: %s", tag_ids)
    else:
        logger.info("Tags enum is already in sync")

    if set(boundary_conditions_enum) != set(boundary_condition_ids):
        mappings_items["properties"]["boundary_conditions"]["items"]["enum"] = boundary_condition_ids
        logger.info("Updated boundary conditions enum with %s", boundary_condition_ids)
    else:
        logger.info("Boundary conditions enum is already in sync")

    # Save updated schema
    save_json_file(SCHEMA_FILE, schema)


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger.info("Syncing vocabulary IDs to schema enums...")
    update_schema()
    logger.info("Sync complete!")
