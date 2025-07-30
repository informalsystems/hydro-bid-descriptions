---
title: "Nolus: ATOM Lending Liquidity"
projectLogoUrl: "/images/logo-nolus.png"
projectUrl: "https://nolus.io/"
requestAmount: [[5000,"ATOM"]]
minMaxTargetPolApr: [6.5,6.5]
---

# About the Project

[Nolus Protocol](https://nolus.io/%20) is a Web3 financial suite that offers an innovative approach to money markets with a novel Lease solution to develop the DeFi space further.
The DeFi Lease defines a money market between lenders looking to earn yield on stablecoins, and borrowers, looking to borrow more digital assets than their current equity.
To borrow assets, the borrower locks up a down payment as collateral and can leverage their holdings in a preferred digital asset.

# Bid Description

## Use case
Utilizing ATOM to provide loans to borrowers aiming to leverage their equity and entering short positions. Borrowers on Nolus provide a deposit (down payment) in the form of a supported asset and they can borrow up to 150% of that deposit's value from the ATOM lending pool. The loan is denominated in ATOM and has a fixed interest rate. Both the deposit and the loan get transferred over to a supported network, in this case, Osmosis, and get swapped to USDC on the native decentralized exchange there, essentially shorting ATOM. This means that if the value of ATOM decreases, borrowers need less USDC to pay back their ATOM-denominated debt and they can keep the rest as profit. If the value of ATOM increases, the position may face partial liquidation(s) where a portion of the position would get swapped back to ATOM to pay back the lenders.

## Duration, Tribute, Yield & Target
The tribute will be paid in NLS tokens. The PoL target is 5,000 ATOM. The deployment duration will be 3 months. The Annual Percentage Yield (APY) is projected to range around 6.5% at optimal utilization thresholds (70%) and is paid out in ATOM from the interest borrowers pay to lenders. There is no manual claiming of rewards, rewards are accrued to the position, so the withdrawable amount increases as time passes. The utilization levels can be monitored [here](https://app.nolus.io/stats).

## Risk Mitigation
Both the deposit and the loan in ATOM are swapped for USDC. The total amount acts as collateral for the position. A maximum 66% Loan-to-Value (LTV) ratio has been established as a safety precaution. Some borrowers may decide to have a lower initial LTV for their positions. A key advantage of the Nolus Protocol is its unique design of single-asset liquidity pools. Liquidity provided within these pools will not be subject to impermanent loss or traded against borrowers. This design ensures that the lent liquidity remains secure.

## Security
The Nolus Protocol code is open-source and is available [here](https://github.com/nolus-protocol). Oak Security and Halborn audit the current on-chain code, and their audits can be found [here](https://hub.nolus.io/en/articles/9680739-security). The documentation for the Nolus protocol can be found [here](https://hub.nolus.io/en/collections/10034429-tech-documentation).

Emergency security contact has been provided to the hydro committee.

## Monitoring
The committee may monitor the position using the Nolus dApp UI found [here](https://app.nolus.io/earn).

Our venue queries can be viewed [here](https://hackmd.io/Vz5ts3lUSSaND7m2WwBcMQ).

## Deployment
`nolus1u0zt8x3mkver0447glfupz9lz6wnt62j70p5fhhtu3fr46gcdd9s5dz9l6` - ATOM lending pool

Our deployment example transactions can be viewed [here](https://hackmd.io/Vz5ts3lUSSaND7m2WwBcMQ).

# Committee Review

Reviewed by RoboMcGobo on 4-July-2025: The single-sided asset liquidity pool design in Nolus protocol will not be subjected to impermanent loss. Having a cap of 66% Loan-to-Value (LTV) ratio follows the committee guidelines for liquidity exports. The requested amount is well within the acceptable deployment ratio, so the committee can deposit the full amount, assuming a successful bid.

