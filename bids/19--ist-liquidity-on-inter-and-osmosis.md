---
title: "IST liquidity on Inter and Osmosis"
projectLogoUrl: "/images/logo-IST.png"
projectUrl: "https://www.inter.protocol"
requestAmount: [[50000,"ATOM"]]
minMaxTargetPolApr: [0,0]
---

# About the Project

The Decentralized Cooperation Foundation (DCF) focuses on unlocking new opportunities for decentralized finance by creating innovative tools that enhance liquidity, scalability, and security.
With a strong foundation in the Cosmos ecosystem, DCF leverages technologies like Agoric's proof-of-stake chain and the Inter-Blockchain Communication (IBC) protocol to maximize the utility of assets like ATOM.
DCF plays a vital role in driving adoption and collaboration across Cosmos by supporting projects that deepen liquidity and expand access to financial opportunities.

Inter Protocol offers a unique way to unlock liquidity and deepen Cosmos DeFi integrations through the Inter Stable Token (IST).
By allowing users to mint IST against IBC assets like stATOM, Inter Protocol creates new opportunities to earn yield while providing critical support for ecosystem stability.
With IST as the native fee token for Agoric, Inter Protocol ensures seamless interaction across the ecosystem, aligning with Hydro's goals of amplifying DeFi impact.

# Bid Description

## Use case
This proposal involves piloting an allocation of Hydro-provided ATOM for liquid staking through Stride, generating staking rewards on the ATOM.
The resulting stATOM will be deposited into Inter Protocol Vaults to mint IST and subsequently deployed to provide liquidity in an Osmosis supercharged pool.

DCF will work with Osmosis to achieve further incentives on the pool, creating further yield on the deposited ATOM.

## Duration, Tribute, Yield & Target
The tribute will be paid in BLD tokens.
The PoL target is 50,000 ATOM.
The deployment duration will be 3 months.
The projected yield is 18-22% APY on a combination of:
* ATOM staking rewards through stATOM
* Liquidity incentives via the supercharged liquidity pool on Osmosis

## Risk mitigation and Security
The collateralization ratio will be set at a conservative 400%, and the multisig will have the opportunity to re-up collateral to avoid liquidation in a severe market downturn.
However, with a short time horizon of 90 days, this risk is mitigated mainly by the 400% collateralization ratio.
Inter Protocol's code is open-source, and audits can be found [here](https://community.agoric.com/t/inter-protocol-vaults-contract-implementations/261/6).
The Stride source code is open-source and can be found [here](https://github.com/Stride-Labs/stride).
The Stride codebase is audited regularly by Informal Systems and has been audited by other security firms, including Oak Security.
You can find more information on Stride's security practices [here](https://www.stride.zone/security).
Stride's documentation can be found [here](https://docs.stride.zone/).
Osmosis is also open-source / source-available; the codebase can be found [here](https://github.com/osmosis-labs/osmosis).
An emergency security contact has been provided to the Hydro committee.

## Monitoring
Monitoring will be available via the following tools:
* [Inter Protocol Vaults UI](https://inter.trade/vaults/)
* [Osmosis IST/USDC Pool](https://app.osmosis.zone/pool/1224)

## Deployment
The liquidity will be deployed to the Osmosis supercharged ATOM pool, leveraging the Inter Protocol and Stride's stATOM infrastructure for seamless integration and yield generation.

Osmosis Pool Details:
* Liquidity to be deployed to the stATOM / ATOM concentrated liquidity pool on Osmosis (Pool ID: 1283).
* Pool address: osmo1z0j6zm4ndmwl27kekla8un73nfu8rh5dhfg2957yr0kg3uumd9rs9sv5kq

Concentrated liquidity range to be set as follows:
* Upper bound: 10% above the stATOM redemption rate at the time the position is deployed
* Lower bound: 5% below the stATOM redemption rate at the time the position is deployed

Inter Protocol Vault contracts can be found [here](https://github.com/Agoric/agoric-sdk/tree/master/packages/inter-protocol/src/vaultFactory).

Vault positions are to be set as follows:
* Vault deployed with a collateralization ratio of 400%.
* If Vault collateral drops below 200%, the position is closed.

# Committee Review

The committee should allocate the requested 50,000 ATOM tranche to Inter Protocol to establish a vault IST position with delegated ATOM. Collateralization ratios will be monitored actively and adjusted to maintain a healthy range above 260%. If the ratio falls below 200%, the position will be reassessed to safeguard against liquidation risk.

