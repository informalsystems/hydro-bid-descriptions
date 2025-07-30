---
title: 'Shade: ATOM Lending Liquidity'
projectLogoUrl: '/images/logo-shade.png'
projectUrl: 'https://app.shadeprotocol.io/ '
requestAmount: [[10000, 'ATOM']]
minMaxTargetPolApr: [7, 8]
---

# About the Project

[ShadeX](https://app.shadeprotocol.io/lend) is an encrypted borrowing and lending protocol, built by Shade Protocol on Secret Network, that ensures all contract interactions, including borrowing, lending, collateral management, and yield generation are private by default.

This platform enables cross-margin borrowing positions with robust features for lenders and borrowers, providing flexibility and security for users and the protocol.

Lenders on ShadeX receive xTokens, which are liquid, yield-bearing tokens representing the underlying lent principal and auto-compounding interest paid by borrowers.

# Bid Description

## Use case

Shade Protocol seeks to bootstrap additional ATOM liquidity, as lent assets, on ShadeX to increase the borrowing capacity for ATOM within Private DeFi. The ATOM would be lent, and in return xATOM would be minted that represents the underlying ATOM principal as well as compounding interest.

## Duration, Tribute, Yield & Target

Shade Protocol is seeking a deployment of 10k ATOM for a 3 month period. The tribute for this bid will be paid in SHD. There are no costs other than SCRT required for gas in order to lend ATOM. Since ShadeX launch, supply APY (paid out in ATOM) has fluctuated between 2.7% and 11.1% APR, averaging ~7-8% APR over this time frame.

## Risk Mitigation

In order to provide maximum flexibility to lenders, ShadeX interest rate curve drastically increases variable borrow APR above optimal_utilization in order to encourage borrowers to repay debts or more lenders to supply assets, ensuring that if utilization increases beyond what is optimal, lenders are properly compensated. Additionally, ShadeSwap will have a concentrated liquidity pool for ATOM <-> xATOM, allowing lenders of ATOM to swiftly and efficiently exit lending positions on the fly without concern for current utilization rates.

## Security

ShadeX has received a 4 month internal audit, as well as an external audit by Halborn which can be found [here](https://drive.google.com/file/d/1F7Upscf3ynBpmDc0-h_YM9IJlBSauX9_/view?usp=drive_link).

[ShadeX documentation](https://docs.shadeprotocol.io/shade-protocol/advanced-topics-apps/shadex-money-market) includes details on key features for lenders and borrowers, liquidations, risk management, configurations, and fees.

## Monitoring

The committee can monitor the ATOM vault as well as their lent ATOM position on ShadeX [here](https://app.shadeprotocol.io/lend).

The committee can find details about the ATOM vault on ShadeX via CLI by using this command:

`Secretcli q compute query secret17xjvdnhxult4a0epa88cqyp8mh9z2y7jrlwkud '{"get_vault": {"token": "secret19e75l25r6sa6nhdf4lggjmgpw0vmpfvsw5cnpe"}}'`

## Deployment

The ShadeX contract address is `secret17xjvdnhxult4a0epa88cqyp8mh9z2y7jrlwkud` (codehash: `36823f966e139dc2d6c3ad7c8b0cb29a808d08daaf0957815369de8d925404ac`)

The SNIP20 contract address for ATOM is `secret19e75l25r6sa6nhdf4lggjmgpw0vmpfvsw5cnpe` (codehash: `638a3e1d50175fbcb8373cf801565283e3eb23d88a9b7b7f99fcc5eb1e6b561e`)

Example ATOM lending txs on ShadeX can be found here including decrypted tx logs:

Tx hash for lending ATOM on ShadeX: [https://secretnodes.com/secret/transactions/958E7B89D31BEB6B02B9BC8737D861E7A574795A8512DC89DA5C42A5436AB548](https://secretnodes.com/secret/transactions/958E7B89D31BEB6B02B9BC8737D861E7A574795A8512DC89DA5C42A5436AB548)

Execute Msg for ATOM SNIP20, where msg is Base64 encoded:

```json
{
  "send": {
    "recipient": "secret17xjvdnhxult4a0epa88cqyp8mh9z2y7jrlwkud",

    "recipient_code_hash": "36823f966e139dc2d6c3ad7c8b0cb29a808d08daaf0957815369de8d925404ac",

    "amount": "1000000",

    "msg": "eyJzdXBwbHkiOnt9fQ==",

    "padding": "TMWzfPRbLx2"
  }
}
```

# Committee Review

Reviewed by PhilRX on 30-June-2025: The proposed bid appears to present no significant risks, provided that the audits have been conducted in accordance with required standards. To align with Hydro's early-stage protocol standards, the liquidation engine must operate with a Loan-to-Value (LTV) cap of approximately 66% for lending facilities. This precautionary measure ensures stability and mitigates risk during the initial phase. The LTV cap will be gradually lifted as liquidity conditions within the Cosmos ecosystem improve. The requested bid amount can't be delivered as Hydro shares a currently limited to 50% participation ratio (after deposit). Current deposits in the pool are too low. As such, the committee approved to renew the previous bootstrap framework which is capped at 10,000.
