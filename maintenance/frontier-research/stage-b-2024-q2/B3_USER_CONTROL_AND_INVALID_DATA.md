# Frontier Research Part B3 — User Control and Invalid-Data Representation

## Identity

- Stage: B / 2024-Q2
- Coverage: SEARCH_BOUNDED
- Status: COMPLETE

## Research question

What happens to scientific communication evidence when users can change information density/order and rendering systems can explicitly choose how invalid data are represented

## Objects and sources

- O6 Customization is Key
- O2 Vega-Lite 5.19
- S6 https://vis.mit.edu/pubs/customization/
- S2 https://github.com/vega/vega-lite/blob/main/CHANGELOG.md

## Customization observation

Customization is Key identifies four design goals for screen-reader-accessible visualizations:

- presence: what content is included
- verbosity: how concisely it is presented
- ordering: how content is sequenced
- duration: how long customization remains active

The authors instantiate these goals with configurable content tokens and report a study with 13 blind/low-vision participants

The study reports benefits for identifying/remembering information while also noting added complexity, especially for users less familiar with similar tools

## Vega-Lite observation

Vega-Lite 5.19.0 added more options and examples for how marks and scales represent invalid data such as nulls and NaNs

That makes invalid-data presentation a declared rendering policy rather than an invisible implementation detail

## Analysis

Scientific communication is no longer captured by:

    data -> one fixed figure

A more realistic state includes:

    data/model
    + representation policy
    + invalid-data policy
    + ordering/verbosity/presence
    + interaction/query state
    + user-selected modality

Different communication states may be legitimate for different tasks without becoming semantically interchangeable

## Counterevidence

Customization can add cognitive/configuration burden

Showing invalid data explicitly does not validate or repair the underlying data

A user preference does not become scientific authority

## Conclusion

SUPPORTED_OBSERVATION

Q2 makes representation policy and user-control state first-class communication provenance
