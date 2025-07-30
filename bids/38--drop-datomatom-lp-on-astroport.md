---
title: 'Drop: dATOM/ATOM LP on Astroport'
projectLogoUrl: /images/logo-drop.png
projectUrl: 'https://www.drop.money/ '
requestAmount: [[71000, "ATOM"]]
minMaxTargetPolApr: [1, 1.23]
points:
- 10000000
- DROPLETS
pointProgramUrl: https://droplets.drop.money
projectName: Drop
---

# About the Project

Drop is a liquid staking protocol for Interchain assets and a member of the Lido Alliance. Built on Neutron, Drop's smart contract architecture uses the IBC protocol and Neutron's ICTX and ICQ modules to provide liquid staking services and scale with minimal overhead and risk. Drop's architecture consists of CosmWasm contracts controlling the flow of assets between multiple blockchains using IBC, ICTX, and ICQ. Upon receipt of supported assets, the protocol mints liquid staking receipt tokens (called dAssets) using the Token Factory standard.

# Bid Description

## Use case

We aim to maintain DEX LPing on Astroport on the ATOM/dATOM pairs, a total of 71K of ATOM comes from Hydro in the LP from the previous rounds' winnings.

The deployment breakdowns as:

- Maintaining Astroport dATOM/ATOM LP with 71k ATOM.
- The rest of the liquidity won in this round can be used for other Drop bids if needed

## Duration, Tribute, Yield & Target

The PoL target is 71,000 ATOM. The deployment duration will be 3 months.

ATOM -> dATOM conversion does not incur any cost. The current pool APR is 1.23%; we expect this to fluctuate around 1% for the next month.

The tribute will be paid in Droplets (point system), which will be converted into DROP tokens upon the TGE. In total, 100 Million DROP tokens will be distributed to the Droplets owners in proportion to their share of the overall Droplet amount. While it is impossible to predict the future value of Droplets accurately, here is useful information that may be relevant to Hydro voters:

|  % of the total token supply allocated to points  | 10 to 20% of the total DROP supply will be distributed to Droplets holders |
| :-----------------------------------------------: | :------------------------------------------------------------------------: |
| % of points provided to Hydro voters for this bid | 0.0007% (20M\* points out of a total points supply of 39.92B\*\* Droplets) |

\*- This is the initial size of the tribute

\*\*- The amount of Droplets is changing daily; the figures provided are accurate as of the bid submission date.

For additional information on Droplets distribution, you can check out the [Unofficial Droplets Dashboards](https://dropletsdash.xyz/) built by the Drop community. The dashboards provide the number of addresses receiving Droplets and the total daily emission.

## Risk Mitigation

LPing will be subject to cap the bid at 25% of the current circulating supply of the dATOM LST.

## Security

The Drop code is open-source and is available [here](https://github.com/hadronlabs-org/drop-contracts). The current on-chain code is audited by OAK security and can be found [here](https://github.com/oak-security/audit-reports/tree/main/Drop). The documentation for the Drop protocol can be found [here](https://docs.drop.money/). Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee may monitor the Astroport position via Astroport UI in [this pool](https://app.astroport.fi/pools/neutron1yem82r0wf837lfkwvcu2zxlyds5qrzwkz8alvmg0apyrjthk64gqeq2e98)

## Deployment

Astroport ATOM/dATOM pool:

`neutron1yem82r0wf837lfkwvcu2zxlyds5qrzwkz8alvmg0apyrjthk64gqeq2e98`

Queries for deployment venue can be found [here](https://hackmd.io/@fuVAsWArQUK74edzCTXdYA/BJ8QPfGYye)

# Committee Review

For this deployment, the newly created framework for LSTs is applicable. The requested amount will proceed under the condition that Hydro's share does not exceed 25% of the total LSTs circulating for dATOM. If this threshold is reached, the committee will periodically review the allocation, making adjustments by adding or removing liquidity as needed to maintain the target balance.
