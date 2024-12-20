#!/bin/bash

# Create a report directory with the current date
REPORT_DIR="reports/$(date +%Y-%m-%d_%H-%M-%S)"
mkdir -p "$REPORT_DIR"

# Run tests and save the output to an HTML file in the report directory
pytest --html="$REPORT_DIR/report.html"

echo "Test report saved to $REPORT_DIR/report.html"