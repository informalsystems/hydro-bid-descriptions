---
title: 'Drop: dATOM/stATOM LP on Magma'
projectLogoUrl: '/images/logo-drop.png'
projectUrl: 'https://www.drop.money/'
requestAmount: [[30000, 'ATOM']]
minMaxTargetPolApr: [22.8, 25]
points: [15000000, 'DROPLETS']
pointProgramUrl: 'https://droplets.drop.money'
---

# About the Project

Drop is a liquid staking protocol for Interchain assets and a member of the Lido Alliance. Built on Neutron, Drop's smart contract architecture uses the IBC protocol and Neutron's ICTX and ICQ modules to provide liquid staking services and scale with minimal overhead and risk. Drop's architecture consists of CosmWasm contracts controlling the flow of assets between multiple blockchains using IBC, ICTX, and ICQ. Upon receipt of supported assets, the protocol mints liquid staking receipt tokens (called dAssets) using the Token Factory standard.

# Bid Description

## Use case

Strategically, we aim to support [MAGMA vaults](https://app.magma.eco/vaults) with bootstrapping dATOM/stATOM LP on their platform. The manager for the dATOM/stATOM LP will be [RoboMcGobo](https://x.com/RoboMcGobo) from Stride.

## Duration, Tribute, Yield & Target

The PoL target is 30,000 ATOM. The deployment duration will be 3 months. The current pool APR for MAGMA dATOM/stATOM is 22.8%; we expect this to fluctuate around 25% for the next month.

The tribute will be paid in Droplets (point system), which will be converted into DROP tokens upon the TGE. In total, 100 Million DROP tokens will be distributed to the Droplets owners in proportion to their share of the overall Droplet amount. While it is impossible to predict the future value of Droplets accurately, here is useful information that may be relevant to Hydro voters:

|  % of the total token supply allocated to points  |  10 to 20% of the total DROP supply will be distributed to Droplets holders  |
| :-----------------------------------------------: | :--------------------------------------------------------------------------: |
| % of points provided to Hydro voters for this bid | 0.000975% (15M\* points out of a total points supply of 14.92B\*\* Droplets) |

\*- This is the initial size of the tribute. \*\*- The amount of Droplets is changing daily; the figures provided are accurate as of the bid submission date.

For additional information on Droplets distribution, you can check out the [Unofficial Droplets Dashboards](https://dropletsdash.xyz/) built by the Drop community. The dashboards provide the number of addresses receiving Droplets and the total daily emission.

## Risk Mitigation

Bootstrapping LPs will be subjected to a cap of 10K ATOM.

## Security

The Magma code is audited by Oak Security and the audit report can be found [here](https://github.com/oak-security/audit-reports/blob/main/Magma%20Core/2024-12-04%20Audit%20Report%20-%20Magma%20Core%20v1.0.pdf). Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee may monitor the position via Magma UI in [this vault](https://app.magma.eco/vault/osmo1nc572g8xtmw0rece858klqhrsedls7x44wuhj682gpvy6azcw7qsg5gdsc).

Queries for our deployment venues can be found [here](https://hackmd.io/@fuVAsWArQUK74edzCTXdYA/BJ8QPfGYye).

## Deployment

The liquidity should be split and deployed as 15k dATOM and 15k stATOM into the Magma dATOM/stATOM pool:

[https://app.magma.eco/vault/osmo1nc572g8xtmw0rece858klqhrsedls7x44wuhj682gpvy6azcw7qsg5gdsc](https://app.magma.eco/vault/osmo1nc572g8xtmw0rece858klqhrsedls7x44wuhj682gpvy6azcw7qsg5gdsc)

`osmo1nc572g8xtmw0rece858klqhrsedls7x44wuhj682gpvy6azcw7qsg5gdsc`

Example transactions for deployments can be found [here.](https://www.mintscan.io/osmosis/tx/55630cf8bbb00278a77bbbbdeb9bd86d30f5078b2b963dc4a9e5e67a7c25f840)

# Committee Review

Reviewed by PhilRX on 23-April-2025: Assuming this bid is successful, requesting an amount eligible for the bootstrap framework allows Hydro to distribute the full amount.
