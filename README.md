# hydro-bid-descriptions

This repository contains the descriptions and metadata for proposals on the Hydro liquidity auction platform.

We keep these descriptions off-chain to allow for transparent yet easy to manage updates
during the pilot rounds of Hydro. Allowing updates of the information on-chain is
not trivial, because the intention of the bids should not be able to be changed,
but minor corrections and clarifications should be able to be added while we
are working out templates and processes.

This information is expected to live on-chain in the future.

## File Structure

Each file follows the naming convention: `${bidId}--${kebabCase(title)}.md`

## Front Matter

Each file contains YAML front matter with the following properties:

- `title`: The bid title
- `projectLogoUrl`: URL to the project logo
- `projectUrl`: URL to the project website
- `requestAmount`: Array containing the amount and token type
- `minMaxTargetPolApr`: Array containing minimum and maximum APR targets
- `points`: (optional) Array containing points amount and type
- `pointProgramUrl`: (optional) URL to the points program

## Content Sections

The markdown content is organized into the following sections (when available):

1. **About the Project**: Project background and description
2. **Bid Description**: Detailed description of the bid proposal
3. **Committee Review**: Comments and review from the committee

## Example

```markdown
---
title: 'Example Bid Title'
projectLogoUrl: '/images/logo-example.png'
projectUrl: 'https://example.com/'
requestAmount: [[10000, 'ATOM']]
minMaxTargetPolApr: [5, 10]
---

# About the Project

Project description...

# Bid Description

Bid details...

# Committee Review

Committee comments...
```
