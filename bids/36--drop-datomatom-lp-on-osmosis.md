---
title: 'Drop: dATOM/ATOM LP on Osmosis'
projectLogoUrl: /images/logo-drop.png
projectUrl: 'https://www.drop.money/ '
requestAmount: [[30000, "ATOM"]]
minMaxTargetPolApr: [0.1, 26.9]
points:
- 6000000
- DROPLETS
pointProgramUrl: https://droplets.drop.money
projectName: Drop
---

# About the Project

Drop is a liquid staking protocol for Interchain assets and a member of the Lido Alliance. Built on Neutron, Drop's smart contract architecture uses the IBC protocol and Neutron's ICTX and ICQ modules to provide liquid staking services and scale with minimal overhead and risk. Drop's architecture consists of CosmWasm contracts controlling the flow of assets between multiple blockchains using IBC, ICTX, and ICQ. Upon receipt of supported assets, the protocol mints liquid staking receipt tokens (called dAssets) using the Token Factory standard.

# Bid Description

## Use case

We aim to add more liquidity on Osmosis on the ATOM/dATOM LP pairs, a total of 10K of ATOM comes from Hydro in this LP's from the previous rounds winnings and in order to improve LP's efficiency we would like to deepen the liquidity additionally.

The deployment breakdowns as:

- Adding liquidity to Osmosis dATOM/ATOM LP 30k ATOM.
- The rest of the liquidity won in this round can be used for other Drop bids if needed

## Duration, Tribute, Yield & Target

The PoL target is 30,000 ATOM. The deployment duration will be 3 months.

ATOM -> dATOM conversion does not incur any cost. The current pool APR is 1.23%; we expect this to fluctuate around 0.1% - 26.9% for the next month. Our partner [Margined protocol](https://www.margined.io/) will maintain the liquidity on our behalf.

The tribute will be paid in Droplets (point system), which will be converted into DROP tokens upon the TGE. In total, 100 Million DROP tokens will be distributed to the Droplets owners in proportion to their share of the overall Droplet amount. While it is impossible to predict the future value of Droplets accurately, here is useful information that may be relevant to Hydro voters:

|  % of the total token supply allocated to points  | 10 to 20% of the total DROP supply will be distributed to Droplets holders |
| :-----------------------------------------------: | :------------------------------------------------------------------------: |
| % of points provided to Hydro voters for this bid | 0.0007% (20M\* points out of a total points supply of 39.92B\*\* Droplets) |

\*- This is the initial size of the tribute

\*\*- The amount of Droplets is changing daily; the figures provided are accurate as of the bid submission date.

For additional information on Droplets distribution, you can check out the [Unofficial Droplets Dashboards](https://dropletsdash.xyz/) built by the Drop community. The dashboards provide the number of addresses receiving Droplets and the total daily emission.

## Risk Mitigation

LPing will be subject to cap the bid at 25% of the current circulating supply of the dATOM LST

## Security

The Drop code is open-source and is available [here](https://github.com/hadronlabs-org/drop-contracts). The current on-chain code is audited by OAK security and can be found [here](https://github.com/oak-security/audit-reports/tree/main/Drop). The documentation for the Drop protocol can be found [here](https://docs.drop.money/). Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee may monitor the Osmosis positions via [pool id 2371](https://app.osmosis.zone/pool/2371)

## Deployment

Osmosis ATOM/dATOM pool [2371](https://app.osmosis.zone/pool/2371), queries can be found [here](https://hackmd.io/@fuVAsWArQUK74edzCTXdYA/BJ8QPfGYye).

# Committee Review

For this deployment, the newly created framework for LSTs is applicable. The requested amount will proceed under the condition that Hydro's share does not exceed 25% of the total LSTs circulating for dATOM. If this threshold is reached, the committee will periodically review the allocation, making adjustments by adding or removing liquidity as needed to maintain the target balance.
