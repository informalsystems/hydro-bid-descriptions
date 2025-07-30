---
title: Margined Redemption Rate Arb Liquidity
projectLogoUrl: /images/logo-margined.png
projectUrl: https://www.margined.io/
requestAmount: [[50000, "ATOM"]]
minMaxTargetPolApr: [0, 0]
projectName: Margined
---

# Bid Description

## Use case

Redemption Rate Arbitrage and LPing in stATOM<>ATOM Pool. The liquidity would be deposited in [vaults](https://trade.margined.io/vaults/atom-redemption-rate) and then the liquidity would arbitrage LSDs including stATOM, dATOM and qATOM. Liquidity will be deposited into two vaults.

## Performance goals

The committee may monitor the position by navigating to trade.margined.io and selecting the appropriate vault (Neutron ATOM / Osmosis ATOM). This will display assets held by account and give projected performance.

The vaults are projected to earn:

- **Osmosis ATOM**: discount 1.13% APR (estimate): 23.65%
- **Neutron ATOM**: discount 0.42% APR (estimate): 8.73%

## Tribute & Target

The tribute will be paid in USDC. The PoL target is 50,000 ATOM.

## Risk mitigation

LP Bid Limitation: LPing will be subject to cap the bid at 33% of total existing deposits, we will monitor future deposits to the LP.

## Security

The Margined code is open-source and is available [here](https://github.com/margined-protocol), the current on-chain code is not audited. The documentation for the Margined protocol can be found [here](https://docs.margined.io/). Emergency security contact has been provided to the hydro committee.

## Deployment

- **Osmosis ATOM Redemption Rate Arbitrage Vault**: osmo1hvl5kj4xzdj4udxjv2dzk2zfqhzkd9afqygwq3t84tn53e0250zqrltj48
- **Neutron ATOM Redemption Rate Arbitrage Vault**: `neutron1puedrclm6rn33x3zv66xg6m23qcdagayqua6jj2wqzvfznlqef8qe53wr2`

# Committee Review

In the arbitrage strategy, we recommended limiting the tranche to 50,000 Atoms. Any proposition beyond that would likely hinder the profit factor.

In the LPing strategy, we required the project to bootstrap the pool first as the whitelisted allocation for Hydro will be sized to a maximum 33% of that pool's deposits. The Margined team didn't perform any security audits on their public on-chain code.
