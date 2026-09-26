# H3 — Altair 6.0.0: Wrapper/Grammar Identity and Rerun Stability

## Source identity
- Object: Altair 6.0.0
- Release date: 2025-11-12
- Primary source: https://github.com/vega/altair/releases

## Frontier observation
Altair 6.0.0 compiles against Vega-Lite 6.1.0, adds Python 3.14 support, describes the library as thread-safe, and states that specifications should remain stable after rerunning.

The important research relation is separation of wrapper and grammar identity:

```text
Altair wrapper version
-> Vega-Lite target version
-> Python runtime
-> generated specification
-> renderer/browser
-> visible artifact
```

Stable generated specifications after rerun are valuable reproducibility evidence, but still do not prove identical downstream renderer/browser output.

## Boundary
- wrapper thread-safety != every embedding integration race-free
- stable spec != identical pixels
- Vega-Lite target != browser engine identity
- release claim != independent reproduction

## Repository interpretation
No Altair 6.0.0 generation/render replay was executed locally.
