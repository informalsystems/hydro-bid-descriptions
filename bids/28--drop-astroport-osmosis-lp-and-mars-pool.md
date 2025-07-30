---
title: "Drop: Astroport & Osmosis LP and Mars pool"
projectLogoUrl: "/images/logo-drop.png"
projectUrl: "https://www.drop.money/"
requestAmount: [[80000,"ATOM"]]
minMaxTargetPolApr: [0,0]
points: [20000000,"DROPLETS"]
pointProgramUrl: "https://droplets.drop.money"
---

# About the Project

Drop is a liquid staking protocol for Interchain assets and a member of the Lido Alliance. Built on Neutron, Drop's smart contract architecture uses the IBC protocol and Neutron's ICTX and ICQ modules to provide liquid staking services and scale with minimal overhead and risk. Drop's architecture consists of CosmWasm contracts controlling the flow of assets between multiple blockchains using IBC, ICTX, and ICQ. Upon receipt of supported assets, the protocol mints liquid staking receipt tokens (called dAssets) using the Token Factory standard.

# Bid Description

## Use case

Drop protocol aims to strategically open up new venues for liquidity deployment by bootstrapping pool

Adding DEX LPing on Astroport and Osmosis on the ATOM/dATOM pairs, adding ATOM to Mars protocol borrowing pool. The Osmosis deployment is a part of bootstrapping strategy and will be limited to 10K ATOM, and the same is applied to Neptune

Strategically, we would also like to support Neptune with bootstrapping dATOM/ATOM LP on their platform. In case Neptune does not reach the required lend deployment to provide 5k nATOM into the nATOM/dATOM LP, the missing amount may be taken from Drop's bid to ensure we get a combined and balanced 10k ATOM deployment into the LP

The deployment breakdowns as:
* The bootstrapping LP's (Neptune and Osmosi) will receive 10k ATOM each.
* The rest of the won liquidity will be split between Mars and Astroport

## Duration, Tribute, Yield & Target

The PoL target is 80,000 ATOM.

The deployment duration will be 3 months.

ATOM -> dATOM conversion does not incur any cost. The current pool APR is 1.23%; we expect this to fluctuate around 1% for the next month.

The tribute will be paid in Droplets (point system), which will be converted into DROP tokens upon the TGE. In total, 100 Million DROP tokens will be distributed to the Droplets owners in proportion to their share of the overall Droplet amount. While it is impossible to predict the future value of Droplets accurately, here is useful information that may be relevant to Hydro voters:

| % of the total token supply allocated to points | 10 to 20% of the total DROP supply will be distributed to Droplets holders |
| :---: | :---: |
| % of points provided to Hydro voters for this bid | 0.0013% (20M* points out of a total points supply of 14.92B** Droplets) |

*- This is the initial size of the tribute  
**- The amount of Droplets is changing daily; the figures provided are accurate as of the bid submission date.

For additional information on Droplets distribution, you can check out the [Unofficial Droplets Dashboards](https://dropletsdash.xyz/) built by the Drop community. The dashboards provide the number of addresses receiving Droplets and the total daily emission.

## Risk Mitigation

LPing will be subject to cap the bid at 50% of total existing deposits.

Bootstrapping LPs will be subjected to a cap of 10K ATOM.

## Security

The Drop code is open-source and is available [here](https://github.com/hadronlabs-org/drop-contracts). The current on-chain code is audited by OAK security and can be found [here](https://github.com/oak-security/audit-reports/tree/main/Drop). The documentation for the Drop protocol can be found [here](https://docs.drop.money/). Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee may monitor the Astroport position via Astroport UI in [this pool](https://app.astroport.fi/pools/neutron1yem82r0wf837lfkwvcu2zxlyds5qrzwkz8alvmg0apyrjthk64gqeq2e98).

The committee may monitor the Mars position via [Mars Protocol's Red Bank UI](https://app.marsprotocol.io/earn).

Queries for our deployment venues can be found [here](https://hackmd.io/@fuVAsWArQUK74edzCTXdYA/BJ8QPfGYye).

The committee may monitor the Neptune position via the Neptune lending [page](https://app.nept.finance/asset-details/?denom=ibc%2FC4CFF46FD6DE35CA4CF4CE031E643C8FDC9BA4B99AE598E9B0ED98FE3A2319F9) and the nATOM/dATOM pool on Astroport UI [here](https://app.astroport.fi/pools/inj18ucwme9nyemev9cjhy6jtagtu4laxh7ztzeqqc).

## Deployment

The deployment will be sent to:

Astroport ATOM/dATOM pool  
Neutron1yem82r0wf837lfkwvcu2zxlyds5qrzwkz8alvmg0apyrjthk64gqeq2e98

Osmosis  
Pool [2371](https://app.osmosis.zone/pool/2371%20)

Mars  
neutron10xwzc88kefwtlup9c2tmw4mj4ng7u79g8lsapp0c9jc02xt247zqwzzghf

Neptune  
Neptune Money Market Contract:  
Inj1nc7gjkf2mhp34a6gquhurg8qahnw5kxs5u3s4u

Astroport nATOM/dATOM Contract:  
inj18ucwme9nyemev9cjhy6jtagtu4laxh7ztzeqqc

Example transactions for deployments can be found [here.](https://explorer.injective.network/transaction/B0AFFB880DCAA2FAD22A0536D110F1D47D9C27DD26A8D4CEC74DB85615185D82/)

# Committee Review

The risk from adding liquidity to the existing Astroport LP ATOM/dATOM is small. The committee will enforce the 50% cap on overall LP shares owned by Hydro.

There are no live dATOM LPs on Osmosis so bootstrapping new liquidity LPs won't be done during the first pilot round.

Regarding lending deposits into Mars, Hydro requires an LTV ratio of 50-60% for deposited ATOMs, translating to a maximum leverage of 2.5x for undercollateralized loans. This safety restriction will be gradually reduced over time. Additionally, lending facilities are subject to a 50% Hydro share deposit cap, whereas LP positions are capped at 33%.

