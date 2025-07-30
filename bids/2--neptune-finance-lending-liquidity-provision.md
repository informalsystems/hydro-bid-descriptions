---
title: "Neptune Finance Lending Liquidity Provision"
projectLogoUrl: "/images/logo-neptune.png"
projectUrl: "https://nept.finance/"
requestAmount: [[5000,"ATOM"]]
minMaxTargetPolApr: [0,0]
---

# Bid Description

## Use case

ATOM liquidity would be deposited in the [Neptune Lend](https://app.nept.finance/lend/) where it can be borrowed by third parties with over-collateralized positions to generate returns from the cost of borrowing. Deposits mint nATOM, the yield bearing receipt token.

Performance goals
The committee may monitor the performance of ATOM lending on the ATOM details page of Neptune. And in the Neptune lending [page](https://app.nept.finance/asset-details/?denom=ibc%2FC4CFF46FD6DE35CA4CF4CE031E643C8FDC9BA4B99AE598E9B0ED98FE3A2319F9)

The historic 30 day average return for ATOM lending is 5.5% APY

## Tribute & Target

The tribute will be paid in USDC. In this pilot phase, the PoL target is 5,000 ATOM.

## Risk mitigation

The target PoL will account for only ~15% of the lending pool, reducing the liquidity risk due to excess loans. Should ATOM loans exceed past target utilization levels, the dynamic Neptune interest rate model will increase exponentially and incentivize the return of loans.

The committee will also hold the nATOM receipt token for their deposit position and can trade it on the open market if needed.

## Security

Neptune Finance has been audited by Oak Security [here](https://github.com/oak-security/audit-reports/tree/master/Neptune)
Docs can be found [here](https://docs.nept.finance/)
Emergency security contact has been provided to the Hydro committee.

## Deployment

Neptune Money Market Contract
**inj1nc7gjkf2mhp34a6gquhurg8qahnw5kxs5u3s4u**

# Committee Review

The project currently holds approximately 30K ATOMs in deposits. To prevent disrupting natural market dynamics and an excessive dilution of rewards, we propose a bid limit set at 50% of overall shares, similar to other participants. Based on these figures, we recommend capping the liquidity deployment to 30K ATOMs. As protocol utilization increases, we can consider introducing larger tranches in future bidding rounds.

