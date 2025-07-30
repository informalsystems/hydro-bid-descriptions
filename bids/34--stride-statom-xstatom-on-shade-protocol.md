---
title: "Stride: stATOM / xstATOM on Shade Protocol"
projectLogoUrl: "/images/logo-stride.png"
projectUrl: "https://www.stride.zone/"
requestAmount: [[15000,"stATOM"]]
minMaxTargetPolApr: [0,0]
---

# About the Project

Stride is the largest liquid staking provider in the Cosmos ecosystem.
Stride handles liquid staking operations on its own sovereign appchain, secured by the Cosmos Hub via Interchain Security.

Stride LSTs allow users to unlock the full value of their staked assets.
By staking with Stride, stakers receive a fungible token (stToken) that allows them to use their assets in DeFi while simultaneously earning staking rewards.
This innovative feature makes Stride LSTs some of the most prominent and compelling collateral assets in the Cosmos ecosystem, with over $40 million in TVL deployed across DeFi protocols in Cosmos and beyond.

# Bid Description

## Use case

Provision of stATOM / xstATOM liquidity on Shade Protocol. The liquidity will be maintained for 3 months.

## Duration, Tribute, Yield & Target

The tribute will be paid in STRD and SHD. The liquidity target is 15k stATOM. Half of the stATOM will be lent on ShadeX, minting xstATOM in return, the resulting xstATOM will then be LPed with the remaining stATOM in the stATOM / xstATOM liquidity pool on Shade's DEX.

## Risk mitigation

In order to provide maximum flexibility to lenders, ShadeX interest rate curve drastically increases variable borrow APR above optimal_utilization in order to encourage borrowers to repay debts or more lenders to supply assets, ensuring that if utilization increases beyond what is optimal, lenders are properly compensated.

## Security

The Stride source code is open-source and can be found [here](https://github.com/Stride-Labs/stride). The Stride codebase is audited regularly by Informal Systems and has been audited by other security firms, including Oak Security. You can find more information on Stride's security practices [here](https://www.stride.zone/security). Stride's documentation can be found [here](https://docs.stride.zone/).

ShadeX has received a 4 month internal audit, as well as an external audit by Halborn which can be found [here](https://drive.google.com/file/d/1F7Upscf3ynBpmDc0-h_YM9IJlBSauX9_/view?usp=drive_link). Emergency security contact has been provided to the hydro committee.

## Monitoring

The committee can monitor the stATOM vault as well as their lent stATOM position on ShadeX [here](http://app.shadeprotocol.io/lend). The committee can monitor the stATOM / xstATOM LP as well as their provided liquidity [here](http://app.shadeprotocol.io/swap/pools)

The committee can find details about the stATOM vault on ShadeX via CLI by using this command:

`secretcli q compute query secret17xjvdnhxult4a0epa88cqyp8mh9z2y7jrlwkud '{"get_vault": {"token": "secret155w9uxruypsltvqfygh5urghd5v0zc6f9g69sq"}}'`

The committee can find details about the stATOM / xstATOM LP on ShadeSwap via CLI by using this command:

`secretcli q compute query secret1yzf9cm8jgdua4xlljkgt3rf9ffxpgkzgsyem3a '{"get_pair_info": {}}'`

## Deployment

Relevant Contract addresses and their code hashes:

* ShadeX contract address: `secret17xjvdnhxult4a0epa88cqyp8mh9z2y7jrlwkud`
  * codehash: `36823f966e139dc2d6c3ad7c8b0cb29a808d08daaf0957815369de8d925404ac`
* stATOM / xstATOM AMM pair on ShadeSwap: `secret1yzf9cm8jgdua4xlljkgt3rf9ffxpgkzgsyem3a`
  * codehash: `e88165353d5d7e7847f2c84134c3f7871b2eee684ffac9fcf8d99a4da39dc2f2`
* stATOM SNIP20 contract: `secret155w9uxruypsltvqfygh5urghd5v0zc6f9g69sq`
  * codehash: `638a3e1d50175fbcb8373cf801565283e3eb23d88a9b7b7f99fcc5eb1e6b561e`
* xstATOM SNIP20 contract: `secret1s5mf2pdcucaqe57ezj8vxa8t7qlk4k6pj77mzz`
  * codehash: `f639f9203684ca31f11faf4cc0c3d0de2c84695ae0272d219ed9864861c8b617`

Example Tx hash for lending 0.99 stATOM on ShadeX: `https://secretnodes.com/secret/transactions/C482B7AF31375818597F83F6A7F404EBFD3AF0B9A23BDF56F1237062E2DC6AB3`

Execute Msg for Lending 0.99 stATOM SNIP20, where msg is Base64 encoded:

`{`
  `"send": {`
    `"recipient": "secret17xjvdnhxult4a0epa88cqyp8mh9z2y7jrlwkud",`
    `"recipient_code_hash": "36823f966e139dc2d6c3ad7c8b0cb29a808d08daaf0957815369de8d925404ac",`
    `"amount": "990000",`
    `"msg": "eyJzdXBwbHkiOnt9fQ==",`
    `"padding": "TMWzfPRbLx2"`
  `}`
`}`  

# Committee Review

The proposed bid appears to present no significant risks, provided that the audits have been conducted in accordance with required standards. To align with Hydro's early-stage protocol standards, the liquidation engine must operate with a Loan-to-Value (LTV) cap of approximately 66% for lending facilities. This precautionary measure ensures stability and mitigates risk during the initial phase. The LTV cap will be gradually lifted as liquidity conditions within the Cosmos ecosystem improve. The requested bid amount can be deployed up to the current 50% participation rate, with a minimum of 10,000 ATOMs corresponding to the bootstrap framework.

