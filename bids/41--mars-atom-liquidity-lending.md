---
title: "Mars: ATOM Liquidity Lending"
projectLogoUrl: "/images/logo-mars.png"
projectUrl: "https://marsprotocol.io"
requestAmount: [[150000,"ATOM"]]
minMaxTargetPolApr: [6,7]
---

# About the Project

Mars Protocol is a DeFi credit and trading platform designed to unlock capital efficiency and drive liquidity across Cosmos ecosystems. Operating on Neutron and Osmosis, the protocol enables over-collateralized borrowing, leveraged staking, and advanced trading strategies via its Red Bank and Rover functionalities. Mars Protocol has been instrumental in driving adoption for ATOM liquid staking tokens (LSTs) such as dATOM and stATOM and aims to continue expanding ATOM-based DeFi strategies across the AEZ (Atom Economic Zone).

# Bid Description

## Use Case

This proposal seeks to leverage ATOM from Hydro to enhance liquidity within Mars Protocol's lending pools on Neutron. By increasing ATOM liquidity, Mars will attract borrower demand, reduce borrowing rates, and support DeFi products that require ATOM as collateral. The borrowed ATOM will power the following initiatives:

* **Leveraged Staking Vaults:** Enable users to deposit liquid staking tokens (e.g., dATOM or stATOM) to borrow ATOM, restake, and repeat, creating a compounding effect. This strategy enhances returns for LST holders and bolsters adoption of liquid staking across Cosmos.
* **Single-Sided LP Vaults:** Provide automated strategies for single-sided liquidity provisioning with hedging capabilities via Mars Perps, enabling Cosmos Hub to supply liquidity without exposure to price fluctuations of paired assets.
* **Delta-Neutral Strategies:** Build automated vaults to optimize LPing returns while hedging against market volatility, driving deeper liquidity and higher trading volumes.

These strategies are modeled after successful DeFi use cases on Ethereum, aiming to establish Mars Protocol as a key player in ATOM-based DeFi.

## Duration, Tribute, Yield & Target

The tribute will be paid in MARS and NTRN. The PoL target is 150k ATOM and the expected APR is 6-7 (ATOM lending APY)%. The deployment duration will be 3 months.

## Risk Mitigation

**Overcollateralization:** Lending on Mars Protocol is overcollateralized, minimizing the risk of default. Borrowers are required to maintain a collateralization ratio above the protocol-defined thresholds.

**Liquidity Caps:** Lending caps ensure sustainable usage of funds.

## Security

Mars Protocol's contracts have undergone rigorous [audits](https://github.com/mars-protocol/mars-audits) by industry-leading firms. dATOM (Drop) is audited by OAK Security, and Mars V2 Perps and lending systems are open-source and fully transparent.

Emergency security contact has been provided to the Hydro committee.

## Monitoring

All positions can be monitored via [Mars Protocol's Red Bank UI](https://app.marsprotocol.io/earn). Borrowing rates, utilization, and performance metrics will be transparently reported. Additional liquidity metrics for LSTs can be tracked on Neutron and Astroport dashboards.

Our venue queries can be viewed here.

## Deployment

Liquidity to be deployed to:

[https://daodao.zone/dao/neutron10xwzc88kefwtlup9c2tmw4mj4ng7u79g8lsapp0c9jc02xt247zqwzzghf/apps?url=https%3A%2F%2Fapp.marsprotocol.io](https://daodao.zone/dao/neutron10xwzc88kefwtlup9c2tmw4mj4ng7u79g8lsapp0c9jc02xt247zqwzzghf/apps?url=https%3A%2F%2Fapp.marsprotocol.io) and it should load the Mars app and you could see in that CA # 403 there is ~203,840 ATOM deposited into Mars

[https://neutron.celat.one/neutron-1/contracts/neutron1qdzn3l4kn7gsjna2tfpg3g3mwd6kunx4p50lfya59k02846xas6qslgs3r](https://neutron.celat.one/neutron-1/contracts/neutron1qdzn3l4kn7gsjna2tfpg3g3mwd6kunx4p50lfya59k02846xas6qslgs3r) is the Mars Credit Manager - this is where all transactions will be executed against (including through the DAODAO link above)

[https://neutron.celat.one/neutron-1/contracts/neutron1n97wnm7q6d2hrcna3rqlnyqw2we6k0l8uqvmyqq6gsml92epdu7quugyph](https://neutron.celat.one/neutron-1/contracts/neutron1n97wnm7q6d2hrcna3rqlnyqw2we6k0l8uqvmyqq6gsml92epdu7quugyph) is the red bank - this is the money market portion of Mars, when you do the lend of ATOM so it can earn yield (via being borrowed out to depositors) the credit manager essentially deposits this amount into the red bank contract.

# Committee Review

Reviewed by PhilRX on 22-April-2025: Based on the current utilization rate and existing deposits (375K ATOMs), we recommend maintaining the previous bid cap set at 400,000 ATOMs. This is according to the committee rule to limit lending protocol deposits to 50% participation rate (after deposit). The committee will deploy liquidity up to this cap, while any excess liquidity will remain on standby. The committee will gradually introduce this reserve as utilization levels increase.

