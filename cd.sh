#!/bin/zsh
# run from project root as
# /bin/zsh ci.sh
# deploy to stage before running this!

echo "Running: all_closed_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/all_closed_input.json"

echo "Running: bad_day_value_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/bad_day_value_input.json"

echo "Running: bad_event_value_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/bad_event_value_input.json"

echo "Running: empty_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/empty_input.json"

echo "Running: good_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/good_input.json"

echo "Running: missing_entry_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/missing_entry_input.json"

echo "Running: missing_weekday_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/missing_weekday_input.json"

echo "Running: multiple_openings_same_day_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/multiple_openings_same_day_input.json"

echo "Running: sunday_to_monday_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/sunday_to_monday_input.json"

echo "Running: time_too_high_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/time_too_high_input.json"

echo "Running: time_too_low_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/time_too_low_input.json"

echo "Running: unbalanced_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/unbalanced_input.json"

echo "Running: unknown_event_input"
curl -i -X POST https://stg.woltchallenge.app/api/v1/get_hours_for_humans -H "Content-Type: application/json" --data-binary "@tests/resources/unknown_event_input.json"
