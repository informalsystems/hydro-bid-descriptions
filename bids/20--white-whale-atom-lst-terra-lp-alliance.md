---
title: "White Whale ATOM LST & Terra LP Alliance"
projectLogoUrl: "/images/logo-white-whale.svg"
projectUrl: "https://app.whitewhale.money/"
requestAmount: [[3600,"ATOM"]]
minMaxTargetPolApr: [0,0]
---

# About the Project

White Whale DEX is the flagship dApp by Migaloo Foundation, anchoring the ecosystem on Migaloo—a permissionless, layer-1 Cosmos SDK blockchain. Specializing in cross-chain liquidity, White Whale operates seamlessly across Migaloo, Osmosis, Terra, Injective, and other Cosmos chains.

# Bid Description

## Use case

Deploy dATOM<>ATOM LST LP to White Whale DEX on [Terra 2.0](https://app.whitewhale.money/terra/pools/manage_liquidity?poolId=ATOM-dATOM).

The LP token will then be staked on Terra LP Alliance via [Eris Protocol](https://www.erisprotocol.com/), earning yield in LUNA or have the LP auto-compound into more dATOM<>ATOM LSD LP.
We recommend the committee choose the auto-compounding option, as there is a 10% take rate on LP deposits when staking on [Terra LP Alliance](https://www.erisprotocol.com/terra/liquidity-hub?tab=liquidity).

## Duration, Tribute, Yield & Target

The tribute will be paid in USDC.
The PoL target is 3,600 ATOM.
The deployment duration will be 3 months.
Terra Liquidity Alliance, built by Eris Protocol, is a ve(3,3) mechanism that allows users to vote on where to direct native inflation on Terra 2.0.
The Migaloo Foundation, builders of White Whale DEX, control ~18% of the voting power on this Liquidity Alliance.
We have directed 10% of our controlled VP towards the dATOM/ATOM LP, building the liquidity up from $6k to $46k in just under one month.

The average APR for LST LPs on Eris Protocol (ampLUNA<>LUNA, bLUNA<>LUNA, dATOM<>ATOM, ampWHALE<>WHALE, bWHALE<>WHALE) is ~70%.

Below are yield ranges and the respective amount of total dATOM<>ATOM liquidity expected at those yields for dATOM<>ATOM:

**Highest**  |  *Net APR 126% = $23,071

**Average**  |  *Net APR 70% = $41,428

**Lowest**   |  *Net APR 28.09% = $78,000

**Net APR = Gross LP Alliance Yield + Trading APR - 10% Take Rate on LP**

Below are the trading APRs for LSD LPs on Terra LP Alliance across all DEXs:

**Highest**  | Trading APR = 2.92%
**Average**  | Trading APR =  0.41%
**Lowest**   | Trading APR = 0.09%

## Risk mitigation and Security

LPing will be subject to cap the bid at 33% of total existing deposits; we will monitor future deposits to the LP.

The White Whale Code can be found [here](https://github.com/White-Whale-Defi-Platform), while docs for White Whale are [here](https://docs.migaloo.zone/).
The on-chain code for White Whale is audited by SCV Security, and the audits can be found [here](https://github.com/White-Whale-Defi-Platform/white-whale-docs/blob/5f14678a7de9c3dc2ae28b62a22ca96072f93393/gitbook/smart-contracts/audits.md#L4).

The Eris Protocol code can be found [here](https://github.com/erisprotocol), while the docs for Eris Protocol are [here](https://docs.erisprotocol.com/).
The on-chain code for Eris Protocol is audited by SCV and Oak Security, and the audits can be found [here](https://github.com/SCV-Security/PublicReports/tree/main/Eris%20Protocol) and [here](https://github.com/oak-security/audit-reports/tree/master/Eris%20Protocol).

Emergency security contact has been provided to the Hydro committee.

## Monitoring

The Hydro Committee may monitor the LP position on the Eris Protocol UI [here](https://www.erisprotocol.com/terra/liquidity-hub?tab=liquidity).

## Deployment

White Whale DEX Terra 2.0 dATOM<>ATOM LP Contract:

terra1aa8nurhuk7rwedhjyzptggypuxd3y66qp4nsx6ph240g37esdm7qyheqkd

Eris Protocol Terra Liquidity Alliance - Single Gauge Contract:

terra16z3ksy6aqjkug8l3u48q0kvdaqk3dgaytl7ykt6vg2he9d6z9rgslr4k7l

# Committee Review

Given the increased liability risks associated with the 10% take rate on LP deposits under the Terra Liquidity Alliance protocol, the committee has decided to limit this bid to the minimum tranche amount of 10,000 ATOMs. This cap, applied at the protocol level, governs all deposits made through the Terra Liquidity Alliance. Since the current bid only requests 3,000 ATOMs, we can fulfill the entire bid while adhering to risk mitigation measures. Hydro will maintain this cap until the protocol incorporates slashing mechanisms in its v2 release. Additionally, Hydro's deployment will utilize the auto-compounding version to offset LP dilution through incentives.

