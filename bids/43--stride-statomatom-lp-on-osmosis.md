---
title: 'Stride: stATOM/ATOM LP on Osmosis'
projectLogoUrl: '/images/logo-stride.png'
projectUrl: 'https://www.stride.zone/ '
requestAmount: [[100000, 'ATOM']]
minMaxTargetPolApr: [1, 5]
---

# About the Project

[Stride](https://www.stride.zone/%20) issues stATOM, the largest, most liquid, and most widely distributed ATOM LST. Stride handles liquid staking operations on its own sovereign appchain, secured by the Cosmos Hub via Interchain Security.

Stride LSTs allow users to unlock the full value of their staked assets. By staking with Stride, stakers receive a fungible token (stToken) that allows them to use their assets in DeFi while simultaneously earning staking rewards. This innovative feature makes Stride LSTs some of the most prominent and compelling collateral assets in the Cosmos ecosystem.

# Bid Description

## Use case

Provision of stATOM / ATOM liquidity on Osmosis in pool 1283. The liquidity will be maintained for 3 months.

## Duration, Tribute, Yield & Target

The tribute will be paid in STRD. The liquidity target is 100,000 ATOM to be deployed to Osmosis. The position will be managed by Margined Protocol, utilizing their locust vaults. The vault will be set with the following parameters:

```toml
strategy.config.position {
  ask_liquidity_profile = [ 1.0 ]
  ask_spread            = 100
  bid_liquidity_profile = [ 1.0 ]
  bid_spread            = 100
  max_spread            = 100
  sensitivity           = 25
}
```

The estimated APR for this range is 1-5%.

## Risk mitigation

LPing will be subject to cap the bid at 25% of the current circulating supply of the stATOM LST.

## Security

The Stride source code is open-source and can be found [here](https://github.com/Stride-Labs/stride). The Stride codebase is audited regularly by Informal Systems and has been audited by other security firms, including Oak Security. You can find more information on Stride's security practices [here](https://www.stride.zone/security). Stride's documentation can be found [here](https://docs.stride.zone/).

Osmosis is also open source/source available, and the codebase can be found below [here](https://github.com/osmosis-labs/osmosis).

Emergency security contact has been provided to the hydro committee.

## Monitoring

The committee may monitor the position using the Osmosis UI found [here](https://app.osmosis.zone/pool/1283).

Our venue queries can be viewed [here](https://hackmd.io/@XcVbaDPzSDaZ2crWZ2_smw/r1I5-pROJl).

## Deployment

Liquidity to be deployed to the stATOM / ATOM concentrated liquidity pool on Osmosis (Pool ID: 1283).

Pool address: osmo1z0j6zm4ndmwl27kekla8un73nfu8rh5dhfg2957yr0kg3uumd9rs9sv5kq

The concentrated liquidity range is to be set as follows:

- Upper bound: 10% above the stATOM redemption rate at the time the position is deployed
- Lower bound: 5% below the stATOM redemption rate at the time the position is deployed

Our deployment example transactions can be viewed [here](https://hackmd.io/@XcVbaDPzSDaZ2crWZ2_smw/r1I5-pROJl).

# Committee Review

Reviewed by PhilRX on 22-April-2025: The LST pairing shows no risk of impermanent loss for the funds, the protocol is audited and therefore the bid is subject to the rule allowing the deployment of up to 25% of the circulating supply of stATOM (this cap is shared across the entire stATOM eligible bids). Assuming a successful bid, Hydro will be able to deploy the entire amount assuming the aforementioned rule is respected.
