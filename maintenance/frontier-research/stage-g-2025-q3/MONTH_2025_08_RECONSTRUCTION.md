# August 2025 Reconstruction — Export/Browser Engine Identity

## Monthly event
Plotly.py 6.3.0 was released on 2025-08-12, updating its Plotly.js line and exposing `plotly.io.get_chrome()` as part of the image-export/browser workflow.

## Historical interpretation
August pulls another hidden layer into the provenance chain:

```text
Python figure object
-> Plotly.py wrapper
-> Plotly.js renderer
-> browser/Chrome runtime
-> export engine
-> output artifact
```

The browser is no longer safely treated as an invisible implementation detail when it is an explicit dependency of the supported export path.

## Month boundary
No Chrome acquisition, Plotly/Kaleido export, browser render, or artifact comparison was executed locally.
