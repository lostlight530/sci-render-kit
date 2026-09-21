# Stage B Month Reconstruction — 2024-06

## Evidence anchor

- Vega-Lite 5.19.0 released 2024-06-14

## Story

June makes a subtle scientific-communication problem explicit: invalid data have representation policy

Null and NaN values can be filtered, shown, encoded, or otherwise handled according to mark/scale policy

This means a final figure can differ materially without the source dataset changing

    invalid-data handling
    != data validity
    hidden/null-filtered value
    != nonexistent observation

The month therefore closes Stage B by connecting renderer policy back to evidence interpretation

## Boundary

No claim is made that one invalid-data policy is universally correct
