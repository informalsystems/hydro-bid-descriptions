---
title: 'Drop: Astroport & Osmosis LP and Mars pool'
projectLogoUrl: /images/logo-drop.png
projectUrl: https://www.drop.money/
requestAmount: [[50000, "ATOM"]]
minMaxTargetPolApr: [0, 0]
points:
- 10000000
- DROPLETS
pointProgramUrl: https://droplets.drop.money
projectName: Drop
---

# About the Project

Drop is a liquid staking protocol for Interchain assets and a member of the Lido Alliance. Built on Neutron, Drop's smart contract architecture uses the IBC protocol and Neutron's ICTX and ICQ modules to provide liquid staking services and scale with minimal overhead and risk. Drop's architecture consists of CosmWasm contracts controlling the flow of assets between multiple blockchains using IBC, ICTX, and ICQ. Upon receipt of supported assets, the protocol mints liquid staking receipt tokens (called dAssets) using the Token Factory standard.

# Bid Description

## Use Case

Adding DEX LPing on Astroport and Osmosis on the ATOM/dATOM pairs, adding ATOM to Mars protocol borrowing pool.

The Osmosis deployment is a part of a bootstrapping strategy and will be limited to 10K ATOM.

The rest of the Hydro liquidity will be split between Mars protocol and Astroport.

## Duration, Tribute, Yield & Target

The tribute will be paid in Droplets (point system), which will be converted into DROP tokens upon the TGE.

In total, 100 million DROP tokens will be distributed to the Droplets owners in proportion to their share of the overall Droplet amount.

The PoL target is 50,000 ATOM.

The deployment duration will be 3 months.

ATOM → dATOM conversion does not incur any cost.

The current pool APR is 0.83%; we expect this to fluctuate around 1% for the next month.

## Risk Mitigation and Security

LPing will be subject to a cap of 33% of total existing deposits.

The Drop code is open-source and is available [here](https://github.com/hadronlabs-org/drop-contracts).

The current on-chain code is audited by OAK Security and can be found [here](https://github.com/oak-security/audit-reports/tree/main/Drop).

The documentation for the Drop protocol can be found [here](https://docs.drop.money/).

Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee may monitor the position via Astroport UI in [this pool].

## Deployment

**Astroport ATOM/dATOM pool**

Neutron1yem82r0wf837lfkwvcu2zxlyds5qrzwkz8alvmg0apyrjthk64gqeq2e98

# Committee Review

The risk from adding liquidity to the existing Astroport LP ATOM/dATOM is small.

The committee will enforce the 33% cap on overall LP shares owned by Hydro.

There are no live dATOM LPs on Osmosis, so bootstrapping new liquidity LPs won't be done during the first pilot round.

Regarding lending deposits into Mars, Hydro requires an LTV ratio of 50-60% for deposited ATOMs, which translates to a maximum leverage of 2.5x for undercollateralized loans.

This safety restriction will be gradually reduced over time.

Additionally, lending facilities are subject to a 50% Hydro share deposit cap, whereas LP positions are capped at 33%.
