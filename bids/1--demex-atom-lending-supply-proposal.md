---
title: Demex ATOM Lending Supply Proposal
projectLogoUrl: /images/logo-demex.png
projectUrl: https://dem.exchange/
requestAmount: [[10000, "ATOM"]]
minMaxTargetPolApr: [0, 0]
projectName: Demex
---

# Bid Description

## Use case

Deploying ATOM liquidity to Demex's lending market through a phased implementation approach. This will increase the available ATOM for borrowing, potentially reducing borrowing rates and improving overall market efficiency. The supplied ATOM will be used exclusively within Demex's lending protocol, allowing users to borrow ATOM at more competitive rates.

This bid aims to enhance Demex's ATOM lending market liquidity through a cautious, phased approach. It prioritizes transparency and community involvement while seeking to benefit both lenders and borrowers in the Cosmos ecosystem.

## Performance goals

The performance of this proposal can be monitored through Demex's lending market interface called [Nitron](<[https://app.dem.exchange/nitron](https://app.dem.exchange/nitron)>), which will display:

1. Total ATOM supplied
2. Utilization rate
3. Supply APY
4. Borrow APY

The current lending APY for ATOM is at 14% and the borrowing rate is at 23% due to high borrowing demand and insufficient lending supply. The additional ATOM supply will help reduce the ATOM borrowing rate while keeping the lending APY competitive.

Hydro Committee can also monitor the performance of deployed liquidity on the following [link](https://scan.carbon.network/cdp/ibc%2FA4DB47A9D3CF9A068D454513891B526702455D3EF08FB9EB558C561F9DC2B701?net=main).

We project the supply APY for ATOM to be competitive with other lending platforms, estimated at 5-8% APY (variable based on market conditions).

## Tribute & Target

The tribute will be paid in SWTH. The PoL target is 10,000 ATOM.

Phased Supply Target

- Phase 1 (Initial): 10,000 ATOM
- Phase 2 (Evaluation): Monitor for 1 month
- Phase 3 (Scaling): Gradually increase the target in the coming rounds to 50,000 ATOM, based on performance and demand

## Risk mitigation

We will start with a smaller supply to assess the market dynamic. We will monitor the utilization rate to ensure it remains at a healthy level, with a target at 70-80%. Demex also uses a dynamic interest rate model that adjusts based on utilization, helping to maintain market balance

ATOM's LTV (Loan-to-value ratio) on Demex is set at 70% which is competitive while remaining safe due to the deep liquidity that ATOM possess

Demex will also provide a withdrawal guarantee. If ATOM cannot be withdrawn at the end of the loan period due to high utilization, additional ATOM will be added to the pool to ensure all loans are repaid.

We will also have a dedicated team that will monitor the market health and performance of the Demex platform.

## Security

The Demex code is open-source and is available [here](https://github.com/Switcheo/carbon-js-sdk), the current on-chain code is audited by Peck Shield and can be found [here](https://drive.google.com/drive/folders/1BCgTTyFNW946Z1N-Hxqyz7uGLApF75EM). The documentation for the Demex can be found [here](https://guide.dem.exchange/) and [here](https://docs.carbon.network/carbon-core/collateralized-debt-position-cdp-module/cdp-operations/borrow). Emergency security contact has been provided to the hydro committee.

## Deployment

The ATOM will be supplied to the following Demex lending market contract address:

[swth1wq9ts6l7atfn45ryxrtg4a2gwegsh3xh7w83xl](https://scan.carbon.network/account/swth1wq9ts6l7atfn45ryxrtg4a2gwegsh3xh7w83xl)

# Committee Review

The risk from adding liquidity to the existing borrowing LP for ATOM on Demex is small. The committee will enforce the 50% cap on LTV, on the overall borrowing LP, shares owned by Hydro.
