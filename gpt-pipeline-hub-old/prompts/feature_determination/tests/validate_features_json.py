import json
from jsonschema import validate, ValidationError

# Schema definition
schema = {
    "type": "object",
    "properties": {
        "features": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "value": {"type": "string"},
                    "unit": {"type": "string"},
                    "source": {
                        "type": "string",
                        "enum": ["title", "part_number", "manufacturer"],
                    },
                },
                "required": ["name", "value", "source"],
                "additionalProperties": false,
            },
            "minItems": 1,
        }
    },
    "required": ["features"],
    "additionalProperties": false,
}


def validate_features(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    try:
        validate(instance=data, schema=schema)
        print("✅ JSON is valid.")
    except ValidationError as e:
        print("❌ Validation failed:")
        print(e.message)
        print("At path:", list(e.path))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python validate_features_json.py <path_to_json_file>")
        exit(1)
    validate_features(sys.argv[1])
