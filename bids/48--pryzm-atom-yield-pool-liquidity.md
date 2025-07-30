---
title: 'Pryzm: ATOM Yield Pool Liquidity'
projectLogoUrl: '/images/logo-pryzm.png'
projectUrl: 'https://pryzm.zone/'
requestAmount: [[10000, 'ATOM']]
minMaxTargetPolApr: [30, 30]
points: [140000000, 'PHOTONS']
pointProgramUrl: 'https://app.pryzm.zone/points/pryzm_photons_3'
---

# About the Project

[Pryzm](https://pryzm.zone/) is a layer-1 blockchain that lets you tokenize and trade your future yields from any asset. Built using the Cosmos SDK, Pryzm offers a variety of DeFi tools to optimize a user's ability to participate and profit in yield trading.

Yield-bearing assets represent a revolution in DeFi, pairing an asset and its yield in one token. But what if you could unlock the yield from an underlying asset? By splitting yield-bearing assets ([cTokens](https://academy.pryzm.zone/docs/how-it-works/ctokens)) into their principal ([pTokens](https://academy.pryzm.zone/docs/how-it-works/ptokens)) and yield ([yTokens](https://academy.pryzm.zone/docs/how-it-works/ytokens)) components via [refraction](https://academy.pryzm.zone/docs/how-it-works/ctokens#refraction), Pryzm opens up a whole new market for trading. Pryzm allows users to optimize their exposure to yield, price, and governance in a ground-breaking new way, unlocking the full power of yield.

# Bid Description

## Use case

Provision of ATOM liquidity on Pryzm in the [ATOM yield pool](https://app.pryzm.zone/pools/0).

## Amount, Duration, Yield & Tribute

The target amount is 10,000 ATOM. The requested duration is 1 month. The tribute will be paid in Photons, which are points that will be redeemable for PRYZM at the end of [Pryzm Season 3](https://app.pryzm.zone/points/pryzm_photons_3) (August 31st, 2025). Photons are distributed based on the USD value of liquidity provided, and would be earned by Hydro's deployment. The tribute amount can fluctuate with the price of ATOM, but using the current price of ATOM, we estimate the deployment will earn ~140m Photons (100 PHOTONS per USD of Liquidity per day). The Hydro UI will initially display the static 140m Photon estimate (although future bids will display a dynamically tribute value).

Photons will be allocated to voters at the end of the deployment. The redemption value of Photons to PRYZM can also fluctuate, as 50m PRYZM tokens are allocated to Photon points, which will be split proportionally between all liquidity providers on Pryzm throughout the liquidity campaign. Learn more about Photons in the FAQ section of [this page](https://app.pryzm.zone/points/pryzm_photons_3).

Separate from the tribute, the estimated deployment APR is expected to be around 30%

## Security

Pryzm has been audited by [Certik](https://storage.googleapis.com/pryzm-zone/audits/Certik-Audit-2024-07-01.pdf) and [Oak Security](https://github.com/oak-security/audit-reports/tree/main/Prism).

## Monitoring

The committee may monitor the position using the Pryzm UI found [here](https://app.pryzm.zone/pools/0).

## Deployment

Liquidity to be deployed to the ATOM yield pool on Pryzm ([Pool ID: 0](https://app.pryzm.zone/pools/0)).

Pool address: `https://chainsco.pe/pryzm/address/pryzm1y7d08j5uy7kgurnv4pwag8h34m2cgptcwe75wn`

Here's documentation for both the [deposit](https://academy.pryzm.zone/docs/guides/earn/liquidity#yamm-pool-lp) and [withdrawal](https://academy.pryzm.zone/docs/guides/earn/liquidity#yamm-pool-lp) process.

Example transaction of deploying into this pool can be seen [here](https://chainsco.pe/pryzm/address/pryzm1y7d08j5uy7kgurnv4pwag8h34m2cgptcwe75wn).

You can DCA [here](https://app.pryzm.zone/pulsetrade) with a limit price giving full price protection and zero price impact when matched against opposing orders and minimal price impact when executing DCA orders against the AMM.

# Committee Review

Reviewed by Phil_RX on 5-May-2025 : Given the specific design of Pryzm's DeFi mechanisms, we believe a more thorough risk assessment is required before considering any large-scale deployment to the protocol. In the interim, this bid will proceed under the liquidity bootstrapping risk framework, which limits the allocation to a maximum of 10,000 ATOM. Additionally, the deployment will be capped at a one-month duration. This allows the committee to evaluate protocol stability and usage over time and revisit both the eligibility and the cap based on observed utilization and evolving risk parameters.
