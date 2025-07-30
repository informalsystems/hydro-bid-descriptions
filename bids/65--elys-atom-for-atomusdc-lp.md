---
title: 'Elys: ATOM for ATOM/USDC LP'
projectLogoUrl: '/images/logo-elys.png'
projectName: 'Elys Network'
projectUrl: 'https://elys.network/'
requestAmount: [[15000, 'ATOM']]
minMaxTargetPolApr: [37, 37]
atomic_bid_pair: 66
---

# About the Project

[Elys Network](https://elys.network/) is a proof-of-stake blockchain and Defi platform that provides a comprehensive suite of DeFi tools including: swaps, staking, liquidity mining, leverage LP, Perpetual trading, and more. In addition to liquidity pools, Elys Network offers single asset Earn Vaults, where a token may be deposited into a borrow pool. Users can borrow from this pool to participate in Leverage LP functions, currently up to 3x leverage.

# Bid Description

## Use case

Elys is requesting both ATOM & USDC in two separate bids for the provision in the ATOM/USDC liquidity pool on Elys Network. The amount of liquidity deployed in each token will be equal, and determined by the bid that receives the lowest amount of votes.

## Duration, Tribute, Yield & Target

The deployment duration will be one month. The tribute will be paid in ELYS. The liquidity target is $60,000 in ATOM. Current APR on the ATOM/USDC liquidity pool is 37%, paid in USDC (1% + price impact, and may increase/decrease based on trading volume) and EDEN (36%).

## Risk mitigation

Elys Network will be providing ATOM collateral in the amount of 10% of the $50,000 ATOM liquidity target. This can be used by Hydro to swap tokens back and make up for the loss if the deployment experiences impermanent loss at the time of withdrawal. Additionally, the Hydro team has agreed to cover any losses past 10% with the Hydro treasury, due to this being the first test run for atomic bids.

## Security

The Elys Network source code is open-source and can be found [here](https://github.com/elys-network/elys). The Elys Network codebase has been audited by Halborn, which can be found [here](https://www.halborn.com/audits/elys-network/elys-modules). Elys documentation can be found [here](https://elys-network.gitbook.io/docs).

Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee may monitor the position using the Elys Network UI [here](https://app.elys.network/earn/mining#liquidity-positions).

To get the ATOM position value in the ATOM/USDC pool, you can query all commitments and find the denom for the AMM pool ID 1. Use this CLI query:

`elysd q commitment show-commitments <user_address>`

Or using the REST API:

`curl -X GET "https://api.elys.network/elys-network/elys/commitment/show_commitments/<user_address>" -H  "accept: application/json"`

This share is expressed in 10\*\*18 units and it's the share of the pool. It can be multiplied by the LP token price to understand the USD position value. Pool LP token price can be found in query:

`elysd q amm show-pool 1 --node https://rpc.elys.network`

Performance can also be viewed via the [Elys Network block explorer](https://mainnet.itrocket.net/elys/), by searching for the Hydro wallet address.

## Deployment

Liquidity to be deployed to the ATOM/USDC liquidity pool on Elys Network (Pool ID #1).

Our example transactions can be viewed [here](https://elysscan.io/tx/4571dc37bb36b979edca77becbe49ad0a20f84f9c560fa9bccc18eba81bf0db2).

# Committee Review

Reviewed by PhilRX on 30-June-2025: Despite Elys shielded pools offering reduced risk, impermanent loss potential remains for Hydro since it must withdraw liquidity at the end of the deployment. If the pool is unbalanced, Hydro would take an immediate loss. In order to prevent this, we recommend that Elys provides some collateral up front, which would be used to make Hydro's position whole in the event of a loss. Our recommendation is a minimum 20% collateral in the form of USDC or ATOM. The Hydro team has agreed to cover any losses over 10% for this pilot test, so 10% collateral will be deposited by the Elys team into the Hydro committee DAO, with the Hydro treasury making up for any losses over 10%. Elys' collateral will only be used to make up for losses, and the remainder (if any) will be returned to Elys at the end of the deployment.
