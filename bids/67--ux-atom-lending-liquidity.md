---
title: 'UX: ATOM Lending Liquidity'
projectLogoUrl: /images/logo-ux.png
projectUrl: https://app.ux.xyz/
requestAmount: [[50000, "ATOM"]]
minMaxTargetPolApr: [6, 6]
projectName: UX
---

# About the Project

[UX](https://app.ux.xyz/) is a programmable, safety-first lending algorithm built as a blockchain.

As a base layer blockchain, applications and money lego primitives can be built on top of UX to access cross chain leverage, liquidity, and debt instruments.

The UX chain facilitates interoperability between the Cosmos ecosystem, Ethereum, side chain architectures, layer two scaling solutions, rollups, and alternative base layer protocols.

# Bid Description

## Use case

Adding ATOM liquidity to the ATOM lending pool on the UX money market, which will allow more users to borrow ATOM and utilize it in their DeFi strategies.

## Duration, Tribute, Yield & Target

The requested deployment duration is 3 months. The tribute will be paid in USDC. The estimated yield that this pool will provide is 6%. The target amount of liquidity for this deployment is 50,000 ATOM.

## Risk Mitigation

The UX protocol uses a comprehensive set of risk parameters to ensure the stability of its lending markets and protect both users and the platform from volatility, manipulation, and systemic risk. They apply over 20 asset-specific and protocol-level parameters, including:

* Collateral Weight – defines how much of an asset's value contributes to borrow power  
* Liquidation Threshold - the point at which a position becomes eligible for liquidation  
* Reserve Factor - portion of borrow interest redirected to reserves to absorb risk  
* Dynamic Interest Rates - borrowing rates increase with utilization to balance supply & demand  
* Max Supply Utilization - caps how much of an asset can be borrowed relative to its supply  
* Min Collateral Liquidity - ensures assets remain redeemable during liquidations  
* Historic Median Pricing - borrow limits are based on the lower of spot price or 3-day price medians to mitigate oracle manipulation

[All parameters](https://github.com/umee-network/umee/blob/main/proto/umee/leverage/v1/leverage.proto) are enforced at the smart contract level and configurable through governance.

## Security

UX has received several audits, all of which can be found [here](https://learning.ux.xyz/overview/UX-overview/security-audits.html). The [UX documentation](https://learning.ux.xyz/overview/) contains additional information on how the protocol works.

## Monitoring

All ATOM lending activity related to Hydro occurs through the following lending pool contract address on the UX Chain:

Leverage Module Pool Address:  

[umee185vjuy55vukn8fdz8fax4rs5xnhl3ufmsul2ks](https://explorer.chainroot.io/ux/accounts/umee185vjuy55vukn8fdz8fax4rs5xnhl3ufmsul2ks)

This is the only address used for deposits, withdrawals, and borrowing interactions through the leverage module.

## Deployment

The ATOM lending pool contract address is `umee185vjuy55vukn8fdz8fax4rs5xnhl3ufmsul2ks`

Example ATOM lending txs can be found [here](https://explorer.chainroot.io/ux/transactions/D4EF3A0C5724834F27E47DCA380B2E26F5FCC2C90900C636A5CB98EF1668279E).

# Committee Review

Reviewed by PhilRX on 4-July-2025: This deployment is subject to the 50% participation cap that the Hydro committee sets for all lending protocols. The amount Hydro can deposit will be limited to the amount of liquidity in the pool at the time of deployment. Currently this is 32,000 ATOM, but this may change between now and the time of deployment. The committee may also reassess the pool on a monthly basis throughout the 3 month deployment, and decrease Hydro's position if necessary. The committee is also aware that the UX chain enforces governance-controlled IBC rate limits. If these limits are reached, withdrawal of the liquidity will be staggered over time.
