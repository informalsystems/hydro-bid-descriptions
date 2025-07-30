---
title: "Drop: dATOM/ATOM LP on Shade"
projectLogoUrl: "/images/logo-drop.png"
projectUrl: "https://www.drop.money/ "
requestAmount: [[10000,"ATOM"]]
minMaxTargetPolApr: [1.5,2.5]
points: [2000000,"DROPLETS"]
pointProgramUrl: "https://droplets.drop.money"
---

# About the Project

Drop is a liquid staking protocol for Interchain assets and a member of the Lido Alliance. Built on Neutron, Drop's smart contract architecture uses the IBC protocol and Neutron's ICTX and ICQ modules to provide liquid staking services and scale with minimal overhead and risk. Drop's architecture consists of CosmWasm contracts controlling the flow of assets between multiple blockchains using IBC, ICTX, and ICQ. Upon receipt of supported assets, the protocol mints liquid staking receipt tokens (called dAssets) using the Token Factory standard.

# Bid Description

## Use case

Drop protocol aims to strategically open up new venues for liquidity deployment by bootstrapping new pools and keep the existing deployments from previous rounds.
We would like to support ShadeSwap as a new DeFi venue where users could trade dATOM assets.
Bootstrapping dATOM/ATOM LP [ShadeSwap](https://app.shadeprotocol.io/swap).
The size of liquidity for bootstrapping will be 10K ATOM.

The deployment breakdowns as:

* The bootstrapping Shade LP with 10k ATOM.
* The rest of the liquidity won in this round can be used for other Drop bids if needed

## Duration, Tribute, Yield & Target

The PoL target is 10,000 ATOM.
The deployment duration will be 3 months.
The current APR for dATOM/ATOM in ShadeSwap is 1.5%; we expect this to fluctuate around 1.5~2.5% for the next month (swap fee is 0.1% for this pair)

The tribute will be paid in Droplets (point system), which will be converted into DROP tokens upon the TGE.
In total, 100 Million DROP tokens will be distributed to the Droplets owners in proportion to their share of the overall Droplet amount.
While it is impossible to predict the future value of Droplets accurately, here is useful information that may be relevant to Hydro voters:

| % of the total token supply allocated to points | 10 to 20% of the total DROP supply will be distributed to Droplets holders |
| :---: | :---: |
| % of points provided to Hydro voters for this bid | 0.0007% (20M* points out of a total points supply of 39.92B** Droplets) |

*- This is the initial size of the tribute  
**- The amount of Droplets is changing daily; the figures provided are accurate as of the bid submission date.

For additional information on Droplets distribution, you can check out the [Unofficial Droplets Dashboards](https://dropletsdash.xyz/) built by the Drop community.
The dashboards provide the number of addresses receiving Droplets and the total daily emission.

## Risk Mitigation

Bootstrapping LPs will be subjected to a cap of 10K ATOM.

## Security

The Drop code is open-source and is available [here](https://github.com/hadronlabs-org/drop-contracts).
The current on-chain code is audited by OAK security and can be found [here](https://github.com/oak-security/audit-reports/tree/main/Drop).
The documentation for the Drop protocol can be found [here](https://docs.drop.money/).
Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee can monitor the ATOM / dATOM LP as well as their provided liquidity here ([app.shadeprotocol.io/swap/pools](http://app.shadeprotocol.io/swap/pools))

## Deployment

ATOM / dATOM AMM pair on ShadeSwap: `secret19du9gw49n6pxs0ddt29v9n854697j2wwrnfqat`
Codehash: `e88165353d5d7e7847f2c84134c3f7871b2eee684ffac9fcf8d99a4da39dc2f2`

ATOM SNIP20 contract:
`secret19e75l25r6sa6nhdf4lggjmgpw0vmpfvsw5cnpe`
Codehash: `638a3e1d50175fbcb8373cf801565283e3eb23d88a9b7b7f99fcc5eb1e6b561e`

dATOM SNIP20 contract:
`secret1x3cxgrwymk7yyelf2782r8ay020xyl96zq3rhh`
Codehash: `638a3e1d50175fbcb8373cf801565283e3eb23d88a9b7b7f99fcc5eb1e6b561e`

The Hydro committee can find details about the ATOM / dATOM LP on ShadeSwap via CLI by using this command:

`secretcli q compute query secret19du9gw49n6pxs0ddt29v9n854697j2wwrnfqat '{"get_pair_info": {}}'`

# Committee Review

The requested amount for this bid falls under the bootstrap framework of 10,000 ATOMs, therefore the full amount can be deployed, assuming a successful bid.

