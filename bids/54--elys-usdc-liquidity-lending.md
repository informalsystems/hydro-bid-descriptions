---
title: "Elys: USDC Liquidity Lending"
projectLogoUrl: "/images/logo-elys.png"
projectUrl: "https://elys.network/"
requestAmount: [[50000,"USDC"]]
minMaxTargetPolApr: [45.5,45.5]
---

# About the Project

[Elys Network](https://elys.network/) is a proof-of-stake blockchain and Defi platform that provides a comprehensive suite of DeFi tools including: swaps, staking, liquidity mining, leverage LP, Perpetual trading, and more. In addition to liquidity pools, Elys Network offers single asset Earn Vaults, where a token may be deposited into a borrow pool. Users can borrow from this pool to participate in Leverage LP functions, currently up to 3x leverage.

# Bid Description

## Use case
Provision of USDC liquidity on USDC Vault on Elys Network.

## Duration, Tribute, Yield & Target
The deployment duration will be one month. The tribute will be paid in USDC. The liquidity target is $50,000 USDC. Current APR on the USDC Vault is approximately 1.22% USDC and 34.79% EDEN for a total of 45.582%. The USDC APR fluctuates based on borrow activity from the pool.

## Risk mitigation
The Elys Network Vault has a maximum borrow amount capped at 75% of the vault.

## Security
The Elys Network source code is open-source and can be found [here](https://github.com/elys-network/elys). The Elys Network codebase has been audited by Halborn, which can be found [here](https://www.halborn.com/audits/elys-network/elys-modules). Elys documentation can be found [here](https://elys-network.gitbook.io/docs).

Emergency security contact has been provided to the Hydro committee.

## Monitoring
The committee may monitor the position using the Elys Network UI [here](https://app.elys.network/earn/vaults#vault-positions).

Deployment venue queries:
`elysd q stablestake pool 32767 --node https://rpc.elys.network`

## Deployment
Liquidity to be deployed to the USDC Earn pool on Elys Network (Pool ID 32767).

Our example transactions can be viewed [here](https://elysscan.io/tx/4571dc37bb36b979edca77becbe49ad0a20f84f9c560fa9bccc18eba81bf0db2).

# Committee Review

Reviewed by Phil_RX on 28-May-2025: Regarding the new leveraged LP mechanism, the committee has reviewed the project's overall risk structure and determined it is acceptable for inclusion within Hydro's facility. As with any standard lending facility program within Hydro, the mechanism will be limited to a 50% weight in the lending pool (post-deposit). Based on the current pool deposits, the requested amount can be fully deployed, provided the bid is successful.

