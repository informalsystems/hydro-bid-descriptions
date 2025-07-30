---
title: Drop Adding Liquidity to Astroport & Osmosis LP
projectLogoUrl: /images/logo-drop.png
projectUrl: https://www.drop.money/
requestAmount: [[500000, "ATOM"]]
minMaxTargetPolApr: [0, 0]
points:
- 10000000
- DROPLETS
pointProgramUrl: https://droplets.drop.money
projectName: Drop
---

# Bid Description

## Use case

Adding DEX LPing on Astroport and Osmosis on the ATOM/dATOM pairs. 50/50 split.

## Performance goals

The committee may monitor the position using [Astroport Pools UI](https://app.astroport.fi/pools/neutron1yem82r0wf837lfkwvcu2zxlyds5qrzwkz8alvmg0apyrjthk64gqeq2e98).

Depending on the size of the POL we manage to get in the Hydro Pilot Rounds, we might deploy a portion of the POL on Osmosis pools.

ATOM -> dATOM conversion does not incur any cost. The current pool APR is 0.83%, and we expect this to fluctuate around 1% for the next month.

## Tribute & Target

The tribute will be paid in Droplets (point system) which will be converted into DROP tokens upon the TGE. In total, 100 Million DROP tokens will be distributed to the Droplets owners, in proportion to their share of the overall Droplet amount. The PoL target is 50,000 ATOM.

## Risk mitigation

LPing will be subject to cap the bid at 33% of total existing deposits.

## Security

The Drop code is open-source and is available [here](https://github.com/hadronlabs-org/drop-contracts). The current on-chain code is audited by OAK security and can be found [here](https://github.com/oak-security/audit-reports/tree/main/Drop). The documentation for the Drop protocol can be found [here](https://docs.drop.money/). Emergency security contact has been provided to the hydro committee.

## Deployment

- Astroport ATOM/dATOM pool

  `neutron1yem82r0wf837lfkwvcu2zxlyds5qrzwkz8alvmg0apyrjthk64gqeq2e98`

# Committee Review

The risk from adding liquidity to the existing Astroport LP ATOM/dATOM is small. The committee will enforce the 33% cap on overall LP shares owned by Hydro.

There are no live dATOM LPs on Osmosis so bootstrapping new liquidity LPs won't be done during the first pilot round.
