# July 2025 Reconstruction — Runtime Target Identity

## Monthly event
Matplotlib 3.10.5 was released on 2025-07-31 with packaging/runtime-target changes including Python 3.14 wheels, free-threaded variants, and Windows ARM wheels.

## Historical interpretation
July makes a familiar "library version" less sufficient as a provenance label.

```text
Matplotlib version
+ Python ABI
+ free-threaded/non-free-threaded state
+ OS/architecture
+ wheel artifact
```

These coordinates identify candidate execution environments more precisely than a version string alone.

## Month boundary
No 3.10.5 wheel, Python 3.14 runtime, free-threaded runtime, or Windows ARM render was executed locally. Distribution availability is not render verification.
