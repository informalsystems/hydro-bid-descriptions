---
title: "Shade: ATOM/stATOM LP"
projectLogoUrl: "/images/logo-shade.png"
projectUrl: "https://app.shadeprotocol.io/ "
requestAmount: [[30000,"ATOM"]]
minMaxTargetPolApr: [3.2,3.2]
---

# About the Project

Shade Protocol is a suite of DeFi applications built on Secret Network that provides data confidentiality by default. Shade's DeFi suite currently includes privacy preserving DEX, CDP stablecoin pegged to a basket of currencies and commodities, bonds, LSTs, and a privacy preserving money market. Value accrual for all the Shade apps goes back to the SHD token. All contract interaction data including token balances, tx history, and allowances are only visible to the data's owner by default, which provides protection from value extraction across all of Shade's apps.

# Bid Description

## Use case

Pairing ATOM/stATOM in Shade's DEX on Secret Network in the existing LP. Shade is focused on expanding and growing ATOM and ATOM LST liquidity to facilitate the demand for organic trading as well as trade flow from liquidations on Shade Protocol's money market.

## Duration, Tribute, Yield & Target

Shade Protocol is seeking a deployment of at least 30k ATOM for a 3 month period. The tribute for this bid will be paid in SHD. The expected APY is around 3.2%, with the addition of 1-3% in trading fees.

## Risk Mitigation

Since this is a DEX LP consisting of ATOM and an ATOM LST, Hydro's risk framework should allow a deployment of up to 25% of the circulating supply of stATOM.

## Security

Shade Protocol's code is open-source and is available [here](https://github.com/securesecrets/shade). The current on-chain code is audited by Certik, which can be found [here](https://skynet.certik.com/projects/shade-protocol). The documentation for Shade Protocol can be found [here](https://docs.shadeprotocol.io/shade-protocol). Emergency security contact is a member of the Hydro Committee, Carter Woetzel.

## Monitoring

The committee may monitor the position [here](https://app.shadeprotocol.io/swap/pools). Search for "stATOM" and select the appropriate pool. This will display assets held by the account and give projected performance.

## Deployment

The ATOM/stATOM pool contract address is `secret1a65a9xgqrlsgdszqjtxhz069pgsh8h4a83hwt0`

The SNIP20 contract address for ATOM is `secret19e75l25r6sa6nhdf4lggjmgpw0vmpfvsw5cnpe` (codehash: `638a3e1d50175fbcb8373cf801565283e3eb23d88a9b7b7f99fcc5eb1e6b561e`)

The SNIP20 contract address for stATOM is `secret155w9uxruypsltvqfygh5urghd5v0zc6f9g69sq` (codehash: `638a3e1d50175fbcb8373cf801565283e3eb23d88a9b7b7f99fcc5eb1e6b561e`)

# Committee Review

Reviewed by PhilRX on 21-April-2025: The LST pairing shows no risk of impermanent loss for the funds, the protocol is audited and therefore the bid is subject to the rule allowing the deployment of up to 25% of the circulating supply of stATOM (this cap is shared across the entire stATOM eligible bids). Assuming a successful bid, Hydro will be able to deploy the entire amount assuming the aforementioned rule is respected.

