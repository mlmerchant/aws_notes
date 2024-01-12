#!/bin/zsh

# Query for all active compliant records
active_compliants=$(aws securityhub get-findings --filter '{"ComplianceStatus":[{"Value":"PASSED","Comparison":"EQUALS"}], "RecordState":[{"Value":"ACTIVE","Comparison":"EQUALS"}]}' --query 'Findings[].Id')

# Check if there are any active compliant records
if [ -n "$active_compliants" ]; then
    echo "Closing active compliant records..."
    for finding_id in ${(z)active_compliants}; do
        # Update the RecordState of each finding to RESOLVED
        aws securityhub update-findings --filters '{"Id":[{"Value":"'"$finding_id"'","Comparison":"EQUALS"}]}' --record-state "RESOLVED"
    done
    echo "All active compliant records have been marked as resolved."
else
    echo "No active compliant records found."
fi
