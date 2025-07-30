---
title: Stride stATOM Liquidity on Osmosis
projectLogoUrl: /images/logo-stride.png
projectUrl: https://www.stride.zone/
requestAmount: [[100000, "ATOM"]]
minMaxTargetPolApr: [0, 0]
projectName: Stride
---

# About the Project

Stride is the largest liquid staking provider in the Cosmos ecosystem, supporting 16 host-zones and over $100 million in total value locked.

Stride handles liquid staking operations on its own sovereign appchain, secured by the Cosmos Hub via Interchain Security.

Stride LSTs allow users to unlock the full value of their staked assets.

By staking with Stride, stakers receive a fungible token (stToken) that allows them to use their assets in DeFi while simultaneously earning staking rewards.

This innovative feature makes Stride LSTs some of the most prominent and compelling collateral assets in the Cosmos ecosystem, with over $40 million in TVL deployed across DeFi protocols in Cosmos and beyond.

# Bid Description

## Use case

Provision of stATOM / ATOM liquidity on Osmosis in pool 1283.

The liquidity will be maintained for 3 months.

## Duration, Tribute, Yield & Target

The tribute will be paid in STRD, and will amount to $400 worth of STRD per month for the 3 month period, for a total of $1,200 in STRD across the duration of the deployment.

The liquidity target is 100,000 ATOM, to be deployed to Osmosis.

Current APR on the Osmosis pool is estimated at 0.2%-200%.

The range will be set wide to accommodate the long time period.

The estimated APR for this range is 5-20%.

## Risk mitigation and Security

The Osmosis LP deployment will proceed with the requested amount, provided that Hydro's share remains capped at a maximum of 33% of the pool.

The Stride source code is open-source and can be found [here](https://github.com/Stride-Labs/stride).

The Stride codebase is audited regularly by Informal Systems and has been audited by other security firms including Oak security.

You can find more information on Stride's security practices [here](https://www.stride.zone/security).

Stride's documentation can be found [here](https://docs.stride.zone/).

Osmosis is also open source / source available, and the codebase can be found below:

- Osmosis: [https://github.com/osmosis-labs/osmosis](https://github.com/osmosis-labs/osmosis)

Emergency security contact has been provided to the hydro committee.

## Monitoring

The committee may monitor the position using the Osmosis UI found below:

- Osmosis: [https://app.osmosis.zone/pool/1283](https://app.osmosis.zone/pool/1283)

## Deployment

Liquidity to be deployed to the stATOM / ATOM concentrated liquidity pool on Osmosis (Pool ID: 1283).

Pool address: osmo1z0j6zm4ndmwl27kekla8un73nfu8rh5dhfg2957yr0kg3uumd9rs9sv5kq

Concentrated liquidity range to be set as follows:

- Upper bound: 10% above the stATOM redemption rate at the time the position is deployed
- Lower bound: 5% below the stATOM redemption rate at the time the position is deployed

# Committee Review

For the Osmosis LP deployment, the requested amount will proceed under the condition that Hydro's share does not exceed 33% of the pool.

If this threshold is reached, the committee will periodically review the allocation, making adjustments by adding or removing liquidity as needed to maintain the target balance.
