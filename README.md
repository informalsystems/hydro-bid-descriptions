# hydro-bid-descriptions
This repository contains the descriptions and metadata for proposals on the Hydro liquidity auction platform.

We keep these descriptions off-chain to allow for transparent yet easy to manage updates
during the pilot rounds of Hydro. Allowing updates of the information on-chain is
not trivial, because the intention of the bids should not be able to be changed,
but minor corrections and clarifications should be able to be added while we
are working out templates and processes.

This information is expected to live on-chain in the future.

The bid information is stored in the `bid-description.json` file. This file is:
```
{
    "8": { // The "Proposal ID" as in the on-chain data
      "title": "Wooo!", // The title of the bid. If not provided, the on-chain data will be used.
      "description": "This is **markdown enabled**", // The description of the bid. If not provided, the on-chain data will be used.
      "projectDetails": "This is also **markdown enabled**", // The details of the project.
      "points": 100000, // Information about a potential reward for the bid in off-chain points.
      "pointsDenom": "DROPLET", // The denomination of the points, i.e. droplets, points, etc.
      "pointProgramLink": "www.learnaboutmypoints.com", // A link to a page that explains the point program.
      "committeeComments": "**Good job**!", // A space for the comments that the Hydro DAO has on the bid.
      "appendix": "**Blakjsdflkajsfl** and so on" // A space for extra auxiliary information on the bid.
    }
}
```