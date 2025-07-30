---
title: Nolus Liquidity Provision stATOM LP
projectLogoUrl: /images/logo-nolus.png
projectUrl: https://nolus.io/
requestAmount: [[5000, "ATOM"]]
minMaxTargetPolApr: [0, 0]
projectName: Nolus Protocol
---

# Bid Description

## Use case

Utilizing stATOM to provide loans to borrowers aiming to leverage their equity and entering short positions. Borrowers on Nolus provide a deposit (down payment) in the form of a supported asset and they can borrow up to 150% of that deposit's value from the stATOM lending pool. The loan is denominated in stATOM and has a fixed interest rate. Both the deposit and the loan get transferred over to a supported network, in this case, Osmosis, and get swapped to USDC on the native decentralized exchange there, essentially shorting stATOM. This means that if the value of stATOM decreases, borrowers need less USDC to pay back their stATOM-denominated debt and they can keep the rest as profit. If the value of stATOM increases, the position may face partial liquidation(s) where a portion of the position would get swapped back to stATOM to pay back the lenders.

## Performance goals

The Annual Percentage Yield (APY) is projected to range between 4-6%. The position can be monitored at [https://app.nolus.io/stats](https://app.nolus.io/stats)

## Tribute & Target

The tribute will be paid in NLS tokens. The PoL target is 5,000 ATOM.

## Risk mitigation

Both the deposit and the loan in stATOM get swapped to USDC. The total amount acts as collateral for the position. A maximum 60% Loan-to-Value (LTV) ratio has been established as a safety precaution. Some borrowers may decide to have a lower initial LTV for their positions. A key advantage of the Nolus Protocol is its unique design of single-asset liquidity pools. Liquidity provided within these pools will not be subject to impermanent loss, nor will it be traded against borrowers. This design ensures that the lent liquidity remains secure.

## Security

The Nolus Protocol code is open-source and is available [here](https://github.com/nolus-protocol). The current on-chain code is audited by Oak Security and Halborn and can be found [here](https://hub.nolus.io/en/articles/9680739-security). The documentation for the Nolus protocol can be found [here](https://hub.nolus.io/en/collections/10034429-tech-documentation). Emergency security contact has been provided to the hydro committee.

## Deployment

- `nolus1jufcaqm6657xmfltdezzz85quz92rmtd88jk5x0hq9zqseem32ysjdm990` - stATOM lending pool

# Committee Review

The single-sided asset liquidity pool design in Nolus protocol will not be subjected to impermanent loss. Having in place a cap of 60% Loan-to-Value (LTV) ratio follows the committee guidelines for liquidity exports.
