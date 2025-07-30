---
title: "Elys: ATOM Liquidity Lending"
projectLogoUrl: "/images/logo-elys.png"
projectUrl: "https://elys.network/"
requestAmount: [[100000,"ATOM"]]
minMaxTargetPolApr: [46.8,46.8]
---

# About the Project

Elys Network is a proof-of-stake blockchain and Defi platform that provides a comprehensive suite of DeFi tools including: swaps, staking, liquidity mining, leverage LP, Perpetual trading, and more. In addition to liquidity pools, Elys Network offers single asset Earn Vaults, where a token may be deposited into a borrow pool. Users can borrow from this pool to participate in Leverage LP functions, currently up to 3x leverage.

# Bid Description

## Use case

Provision of ATOM liquidity on ATOM Earn Vault on Elys Network.

Elys Network's Earn Vault program includes single token deposit pools that serve as borrow pools for users to engage in Leverage LP. Currently, a user may borrow from a Vault to leverage up to 3x in a pool. While the position is open, the Vault earns fees collected from margin interest, as well as a reward in EDEN, the reward token for Elys Network. EDEN can be claimed to be staked or vested. If vested, EDEN can be redeemed 1:1 for ELYS over a 90 day linear vesting period.

## Duration, Tribute, Yield & Target

The requested deployment duration is 3 months. The tribute will be paid in ELYS. The target amount of liquidity is 100,000 ATOM.

Current APR on the ATOM Earn Vault is approximately 1.88% USDC and 45% EDEN for a total of 46.88%. The USDC APR fluctuates based on borrow activity from the pool.

## Risk mitigation

The Elys Network Earn Vault's maximum borrow capacity is 80%.

## Security

The Elys Network source code is open-source and can be found [here](https://github.com/elys-network/elys). The Elys Network codebase has been audited by Halborn, which can be found [here](https://www.halborn.com/audits/elys-network/elys-modules). Elys documentation can be found [here](https://elys-network.gitbook.io/docs).

Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee may monitor the position using the Elys Network UI [here](https://app.elys.network/earn/staking), or via this CLI query:

`elysd q stablestake pool 32768 --node https://rpc.elys.network`

Performance can also be viewed via the [Elys Network block explorer](https://mainnet.itrocket.net/elys/), by searching for the Hydro wallet address.

## Deployment

The Hydro wallet can connect to Elys using the [Elys Earn UI](https://app.elys.network/earn/vaults). Once connected, locate ATOM, and tap "Deposit." From that screen, enter the amount of ATOM, tap "Deposit ATOM," and approve the transaction with your wallet. The ATOM Earn Vault ID is 32768.

An example transaction can be viewed [here](https://elysscan.io/tx/4571dc37bb36b979edca77becbe49ad0a20f84f9c560fa9bccc18eba81bf0db2).

# Committee Review

Reviewed by Phil_RX on 26-Apr: As with any standard lending facility program within Hydro, the mechanism will be limited to a 50% weight in the lending pool (post-deposit). Based on the current pool deposits (approximately 2,150 ATOMs), the requested amount of 50,000 can't be deployed until substantial improvement to the current deposits. Anyhow, the project will still be eligible to receive a minimum of 10,000 ATOMs under the bootstrap framework, provided the bid is successful of course.

