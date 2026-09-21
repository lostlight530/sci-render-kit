# Frontier Research Part C3 — Population-Conditioned Accessibility Evidence

## Question

What can a population-specific accessibility study validate without becoming universal accessibility authority

## Object and sources

- “Towards Enhancing Low Vision Usability of Data Charts on Smartphones”
- DOI: 10.1109/TVCG.2024.3456348
- online publication date: 2024-09-20
- IEEE VIS 2024 paper page / camera-ready paper
- participant study: 26 low-vision participants

## Observations

The work addresses low-vision screen-magnifier users on smartphones

The reported problem is loss of visual context under magnification

The proposed system transforms otherwise non-interactive chart images into personalizable interactive charts that support selective viewing while preserving context

The study reports improved usability relative to comparison conditions for its participant/task setting

## Analysis

This is strong evidence that accessibility is not one global property attached to a figure

The validated surface is conditioned by:

```text
user population
+ assistive technology
+ device/screen
+ chart type/task
+ interaction model
+ personalization state
+ study protocol
```

Therefore:

```text
accessible for tested low-vision smartphone workflow
!= universally accessible
!= blind screen-reader validation
!= WCAG certification
```

## Temporal boundary

The DOI/online publication is dated 2024-09-20

Conference presentation occurred later, so publication date and presentation date are kept separate

## Conclusion

`SUPPORTED_OBSERVATION / POPULATION_BOUNDED`

Accessibility evidence should attach to a communication state and validation population, not to the scientific claim globally
