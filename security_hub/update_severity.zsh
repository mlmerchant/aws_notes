Certainly! The revised script will take the new severity level as the first argument
#!/bin/zsh

# Check for minimum number of arguments
if [ $# -lt 2 ]; then
    echo "Usage: $0 <new_severity> <finding_id1> [<finding_id2> ...]"
    exit 1
fi

# The first argument is the new severity level
new_severity="$1"

# Process each finding ID
for finding_id in "${@:2}"; do
    echo "Updating severity of finding $finding_id to $new_severity..."
    aws securityhub update-findings --filters '{"Id":[{"Value":"'"$finding_id"'","Comparison":"EQUALS"}]}' --severity '{"Label": "'"$new_severity"'"}'
done

echo "Severity update complete."

#. ./update_severity_code.zsh MEDIUM finding_id1 finding_id2 finding_id3
# This will update the severity of findings with IDs `finding_id1`, `finding_id2`, and `finding_id3` to "MEDIUM".