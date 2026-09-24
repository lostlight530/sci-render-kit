# March 2025 Reconstruction — Stage E

March is anchored by Vega-Lite 6.0.0 on 2025-03-28.

The release moves Vega-Lite to ESM-only packaging, updates to Vega 6 and changes defaults such as continuous size while also fixing time-format and tick-step behavior.

The month-level narrative is that declarative visualization identity includes both the spec and the versioned compiler/runtime that interprets it.

~~~text
spec text
+ compiler version
+ runtime version
+ package/module environment
-> communication state
~~~

No local compile/render comparison or browser replay was executed.