FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir pyyaml jsonschema

# Copy schema and validation script
COPY schema/cad_manifest.schema.json /app/schema/cad_manifest.schema.json
COPY validate.sh /app/validate.sh

# Make script executable
RUN chmod +x /app/validate.sh

# Set entrypoint to run validation script
ENTRYPOINT ["/app/validate.sh"]

# Default command expects manifest path as argument
CMD ["echo", "Usage: docker run --rm -v /path/to/manifest.yaml:/app/manifest.yaml image-name manifest.yaml"]
