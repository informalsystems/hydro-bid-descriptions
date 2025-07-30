---
title: "Neptune x Drop: nATOM/dATOM LP on Injective"
projectLogoUrl: "/images/logo-neptune.png"
projectUrl: "https://nept.finance/"
requestAmount: [[10000,"ATOM"]]
minMaxTargetPolApr: [2.1,7.5]
---

# About the Project

Neptune Finance is a next-generation credit network and high-yield lending protocol designed to provide unmatched capital efficiency for lenders, borrowers, and builders. Neptune rates lead the market by dynamically shifting to encourage borrowing and ultimately deliver a narrower spread between lend and borrow rates, constantly calibrating to the most competitive rate. Using DeFi modularity, Neptune's lend receipt tokens (or nAssets) can be reused in other protocols such as Pryzm and Astroport.

# Bid Description

## Use case

ATOM liquidity will be used in a strategic partnership between Drop and Neptune to bootstrap liquidity requirements for listing dATOM on Neptune. This will mark the first ATOM LST deployment on the Injective chain, and the second LST listing on Neptune after hINJ.

Once requirements are met, dATOM will be enabled as a yield-bearing collateral asset on Neptune, allowing users to borrow against it in cross-margin accounts. Supporting this deployment, an nATOM/dATOM pair will be seeded on Astroport Injective to be used as a liquidation route and as a yield-farming opportunity for ATOM on Injective.

First, ATOM liquidity will be deposited in [Neptune Lend](https://app.nept.finance/lend/), which can be borrowed by third parties with over-collateralized positions to generate returns from the cost of borrowing. Deposits mint nATOM, the yield-bearing receipt token.

Second, a maximum of 5,000 nATOM will be used to seed the nATOM/dATOM LP on Astroport, with the other half provided by Drop as dATOM for a total of 10,000 ATOM.

We intend to grow nATOM/dATOM liquidity through different incentive mechanisms in the coming months in order to meet the dATOM listing requirements. This Hydro bid marks the first step towards achieving that goal.

## Duration, Tribute, Yield & Target

The tribute will be paid in USDC. In this pilot phase, the PoL target is 10,000 ATOM. The deployment duration will be 3 months. The historic 30-day average return for ATOM lending is between 2.1% and 7.50% APY. nATOM deposited on Astroport in the nATOM/dATOM LP will earn additional yield based on swap fees.

## Risk mitigation

The target PoL will account for roughly 40% of the lending pool. Should ATOM loans exceed past target utilization levels, the dynamic Neptune interest rate model will increase exponentially and incentivize the return of loans.

The committee will also hold the nATOM receipt token for their deposit position and can trade it on the open market if needed.

## Security

Oak Security has audited Neptune Finance; the audit can be found [here](https://github.com/oak-security/audit-reports/tree/master/Neptune).  
Neptune's docs can be found [here](https://docs.nept.finance/).

Emergency security contact has been provided to the Hydro committee.

## Monitoring

The committee may monitor the performance of ATOM lending via the Neptune lending [page](https://app.nept.finance/asset-details/?denom=ibc%2FC4CFF46FD6DE35CA4CF4CE031E643C8FDC9BA4B99AE598E9B0ED98FE3A2319F9) and the nATOM/dATOM pool on Astroport UI [here](https://app.astroport.fi/pools/inj18ucwme9nyemev9cjhy6jtagtu4laxh7ztzeqqc).

Our venue queries can be viewed [here](https://hackmd.io/@jwEKz2IPTTqH3U9DC2aZ3A/BkShOvGc1x).

## Deployment

Neptune Money Market Contract:  
Inj1nc7gjkf2mhp34a6gquhurg8qahnw5kxs5u3s4u

Astroport nATOM/dATOM Contract:  
inj18ucwme9nyemev9cjhy6jtagtu4laxh7ztzeqqc

Our deployment example transaction can be viewed [here](https://explorer.injective.network/transaction/50720C355D377BB175F4CDE7004CBF90453854D0DCDF37C5FEC240A112C84221/) and [here](https://explorer.injective.network/transaction/B0AFFB880DCAA2FAD22A0536D110F1D47D9C27DD26A8D4CEC74DB85615185D82/).

# Committee Review

The project currently holds approximately 30K ATOMs in deposits. To prevent disrupting natural market dynamics and an excessive dilution of rewards, we propose a bid limit set at 50% of overall shares, similar to other participants. Based on these figures, we recommend capping the liquidity deployment to 30K ATOMs. As protocol utilization increases, we can consider introducing larger tranches in future bidding rounds. 

Regarding the nATOM/dATOM liquidity provision, the committee has agreed to set an initial cap of 10,000 ATOMs corresponding to this bid expectation due to the complex risk structure involved. It, therefore, allows for a quick deployment without extensively compromising community funds. This cap is temporarily set, waiting on a more thorough review by the committee, upon which the cap will be adjusted to allow the deposits to scale.

