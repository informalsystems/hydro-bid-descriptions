---
title: "Neptune: USDC Lending Liquidity"
projectLogoUrl: "/images/logo-neptune.png"
projectUrl: "https://nept.finance/"
requestAmount: [[50000,"USDC"]]
minMaxTargetPolApr: [8,12]
---

# About the Project

[Neptune Finance](https://nept.finance) operates a modular lending protocol built to deliver the most competitive rates. To date, Neptune is the only lending protocol capable of cross-collateralization, multiple isolated sub accounts, instant settlement, and a dynamic interest rate model.

Q3 2025 represents Neptune's cross-chain expansion quarter, building across IBC-connected pathways via Skip and Eureka. This lending deposit provides much-needed liquidity depth for multi-chain integrations and expands Hydro’s ATOM allocations beyond entrenched ecosystem players. Additionally, Neptune's lending receipt tokens (nAssets) integrate seamlessly with other ecosystem protocols including Pryzm and Astroport for enhanced yield strategies.

# Bid Description

## Use case
USDC liquidity will be deposited in [Neptune Lend](https://app.nept.finance/lend/), which can be borrowed by third parties with over-collateralized positions to generate returns from the cost of borrowing. Deposits mint nUSDC, the yield-bearing receipt token.
## Duration, Tribute, Yield & Target
The tribute will be paid in USDC. The liquidity target is 50,000 USDC. The requested deployment duration is 1 month. The historic 30-day average return for USDC lending is between 8-12% APY.
## Risk mitigation
The allocation represents under 50% of projected pool capacity, respecting committee rules while maximizing impact. Neptune's PID-controlled interest rate system continuously optimizes equilibrium points for lenders and borrowers to maximize efficiency. Hydro Committee retains tradable nUSDC deposit tokens for additional liquidity options.
## Security
Oak Security has audited Neptune Finance; the audit can be found [here](https://github.com/oak-security/audit-reports/tree/master/Neptune). Neptune’s docs can be found [here](https://docs.nept.finance/). Emergency security contact has been provided to the Hydro committee.
## Monitoring
The committee may monitor the performance of USDC lending via the Neptune lending [page](https://app.nept.finance/lend/). Our venue queries can be viewed [here](https://hackmd.io/@jwEKz2IPTTqH3U9DC2aZ3A/BkShOvGc1x).
## Deployment
Neptune Money Market Contract:
```
Inj1nc7gjkf2mhp34a6gquhurg8qahnw5kxs5u3s4u
```
Our deployment example transaction can be viewed [here](https://explorer.injective.network/transaction/50720C355D377BB175F4CDE7004CBF90453854D0DCDF37C5FEC240A112C84221/) and [here](https://explorer.injective.network/transaction/B0AFFB880DCAA2FAD22A0536D110F1D47D9C27DD26A8D4CEC74DB85615185D82/).
## Security Review
Reviewed by Arlai on 3-June-2025: Based on the security review of Neptune Finance, this appears to be a MODERATE RISK opportunity for Hydro liquidity provision. While the protocol benefits from reputable auditing and operates on a trusted blockchain, there are some points to consider regarding audit recency, code transparency, and centralization that elevate the risk profile.
| **Category**          | **Details** |
|----------------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Audits**            | Neptune was audited by Oak Security in April 2023 and again in January 2024, covering core protocol and post-migration changes. A third audit is planned for 2025 after new features are completed. |
| **Code Transparency** | Neptune is closed source, preventing independent code review. As such, the team’s claim of minimal changes since the last audit cannot be confirmed. |
| **Security Concerns** | A trusted owner and bots can update prices without external checks, posing a centralization risk. This primarily threatens borrowers via potential sudden liquidations. |

# Committee Review

Reviewed by Phil_RX on 21-July-25: The project currently holds approximately 250,000 USDC in deposits. To prevent disrupting natural market dynamics and an excessive dilution of rewards, the committee has set a bid limit at 50% of overall shares, similar to other participants. Based on these figures, the requested amount can be deployed entirely, assuming a successful bid. 

