---
title: "Nolus: USDC Liquidity Lending"
projectLogoUrl: "/images/logo-nolus.png"
projectUrl: "https://nolus.io/"
requestAmount: [[57500,"USDC"]]
minMaxTargetPolApr: [16,16]
---

# About the Project

Nolus Protocol is a Web3 financial suite that offers an innovative approach to money markets with a novel Lease solution to develop the DeFi space further. The DeFi Lease defines a money market between lenders looking to earn yield on stablecoins, and borrowers, looking to borrow more digital assets than their current equity. To borrow assets, the borrower locks up a down payment as collateral and can leverage their holdings in a preferred digital asset.

# Bid Description

## Use case

Utilizing USDC to provide loans to borrowers aiming to leverage their equity and enter long positions. Borrowers on Nolus provide a deposit (down payment) in the form of a supported asset and they can borrow up to 150% of that deposit's value from the USDC lending pool. The loan is denominated in USDC and has a fixed interest rate. Both the deposit and the loan get transferred over to a supported network, in this case, Osmosis, and get swapped to USDC on the native decentralized exchange there, essentially longing the asset of choice by a maximum of 2.5x leverage. This means that if the asset's value increases, borrowers can profit from the price appreciation. If the value of the leveraged asset decreases, the position may face partial liquidation(s) where a portion of the position would get swapped back to USDC to pay back the lenders.

## Duration, Tribute, Yield & Target

The tribute will be paid in USDC tokens. The PoL target is the full 57.5k bucket. The deployment duration will be 1 month. The Annual Percentage Yield (APY) is projected to range around 16% at current utilization thresholds (94%) and is paid out in USDC from the interest borrowers pay to lenders. There is no manual claiming of rewards, rewards are accrued to the position, so the withdrawable amount increases as time passes. The utilization levels can be monitored [here](https://app.nolus.io/stats).

## Risk Mitigation

Both the deposit and the loan in USDC are swapped for a supported asset of choice for longing on Nolus. The total amount acts as collateral for the position. A maximum 60% Loan-to-Value (LTV) ratio has been established as a safety precaution. Some borrowers may decide to have a lower initial LTV for their positions. A key advantage of the Nolus Protocol is its unique design of single-asset liquidity pools. Liquidity provided within these pools will not be subject to impermanent loss or traded against borrowers. This design ensures that the lent liquidity remains secure.

## Security

The Nolus Protocol code is open-source and is available [here](https://github.com/nolus-protocol). Oak Security and Halborn audit the current on-chain code, and their audits can be found [here](https://hub.nolus.io/en/articles/9680739-security). The documentation for the Nolus protocol can be found [here](https://hub.nolus.io/en/collections/10034429-tech-documentation).

Emergency security contact has been provided to the hydro committee.

## Monitoring

The committee may monitor the position using the Nolus dApp UI found [here](https://app.nolus.io/earn).

Our venue queries can be viewed [here](https://hackmd.io/Vz5ts3lUSSaND7m2WwBcMQ).

## Deployment

`nolus1ueytzwqyadm6r0z8ajse7g6gzum4w3vv04qazctf8ugqrrej6n4sq027cf` - USDC lending pool

Our deployment example transactions can be viewed [here](https://hackmd.io/Vz5ts3lUSSaND7m2WwBcMQ).

# Committee Review

The single-sided asset liquidity pool design in Nolus protocol will not be subjected to impermanent loss. Having a cap of 60% Loan-to-Value (LTV) ratio follows the committee guidelines for liquidity exports. This deployment is subject to the 50% participation rate limitation applied to every lending protocol. Regarding the current deposits exceeding 1,500,000$, the requested amount can be deployed entirely, assuming a successful bid.

