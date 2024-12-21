#!/bin/bash

# Create a report directory with the current date
REPORT_DIR="reports/$(date +%Y-%m-%d_%H-%M-%S)"
mkdir -p "$REPORT_DIR"

# Run tests and save the output to an HTML file in the report directory
pytest --html="$REPORT_DIR/report.html" --run-env dev -v --junitxml="reports/result.xml"

# py.test --browser_name "$browserName" --run-env "$run_env" --html="$WORKSPACE/$REPORT_DIR/report.html" -v --junitxml="result.xml"

echo "Test report saved to $REPORT_DIR/report.html"