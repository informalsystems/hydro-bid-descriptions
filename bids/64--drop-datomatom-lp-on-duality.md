---
title: "Drop: dATOM/ATOM LP on Duality"
projectLogoUrl: "/images/logo-drop.png"
projectUrl: "https://www.drop.money/"
requestAmount: [[50000,"ATOM"]]
minMaxTargetPolApr: [4,7]
points: [20000000,"DROPLETS"]
pointProgramUrl: "https://droplets.drop.money"
---

# About the Project

[Drop](https://www.drop.money/) is a liquid staking protocol for Interchain assets and a member of the Lido Alliance. Built on Neutron, Drop's smart contract architecture uses the IBC protocol and Neutron's ICTX and ICQ modules to provide liquid staking services and scale with minimal overhead and risk.
Drop's architecture consists of CosmWasm contracts controlling the flow of assets between multiple blockchains using IBC, ICTX, and ICQ.
Upon receipt of supported assets, the protocol mints liquid staking receipt tokens (called dAssets) using the Token Factory standard.

# Bid Description

## Use Case
We aim to support Duality Supervaults by bootstrapping dATOM/ATOM. The LP will be managed by Duality, automatically [rebalancing the pair and capturing arbitrage](https://hadron.notion.site/Supervaults-Explainer-16485d6b9b1080a78d9dd60dfefed4d9#16485d6b9b1080518aaae92858288bbb) to optimize yield.  [Duality Supervaults](https://hadron.notion.site/Supervaults-Explainer-16485d6b9b1080a78d9dd60dfefed4d9) are CosmWasm contracts that leverage the price feeds from Neutron's enshrined oracle, Slinky, and native automation via the CRON module to provide liquidity with tight spreads on the Duality orderbook.

## Duration, Tribute, Yield & Target
The target deployment amount is 50,000 ATOM. The deployment duration will be 3 months. The expected pool APR for Duality Supervaults dATOM/ATOM is around 5%; we expect this to fluctuate between 4-7% for the next month. 

The tribute will be paid in Droplets (point system), which will be converted into DROP tokens upon the TGE. In total, 100 Million DROP tokens will be distributed to the Droplets owners in proportion to their share of the overall Droplet amount. While it is impossible to predict the future value of Droplets accurately, here is useful information that may be relevant to Hydro voters:

| % of the total token supply allocated to points | 10 to 20% of the total DROP supply will be distributed to Droplets holders |
| :---: | :---: |
| % of points provided to Hydro voters for this bid | 0.0013% (20M* points out of a total points supply of 14.92B** Droplets) |

*- This is the initial size of the tribute  
**- The amount of Droplets is changing daily; the figures provided are accurate as of the bid submission date.

For additional information on Droplets distribution, you can check out the [Unofficial Droplets Dashboards](https://dropletsdash.xyz/) built by the Drop community. The dashboards provide the number of addresses receiving Droplets and the total daily emission. 

## Risk Mitigation
There are no specific financial risks involved with this bid.

## Security
The Duality Supervaults code is open sourced and can be found [here](https://github.com/neutron-org/neutron/tree/main/x/dex); it has also been audited by Informal Systems and OtterSec. The audit report can be found [here](https://github.com/neutron-org/duality-audits/blob/main/Informal%20Systems%20SuperVaults%20Audit%204%3A16%3A25.pdf). Emergency security contact has been provided to the Hydro committee.

## Monitoring
Balances can be queried via CLI with:

`neutrond q wasm contract-state smart [ContractAddress] '{"get_balance": {}}'`

Or via HTTP curl:
`https://rest-lb.neutron.org/cosmwasm/wasm/v1/contract/[CONTRACTADDRESS]/smart/eyJnZXRfYmFsYW5jZSI6e319`

dATOM/ATOM contract address is:
`neutron18ua532r8lpy8scvysrgcjneyrwuj4x0ne4t2azphxksya596l4cq23lkp9`

## Deployment
The liquidity should be split 50/50. If we're able to get the full 50k target, it should be deployed as 25k dATOM and 25k ATOM to the LP.

The deployment can be sent using this command:

`neutrond tx wasm execute [CONTRACTADDRESS] '{"deposit": {}}' --chain-id neutron-1 --amount [DepositAmount] --gas-adjustment 2.5 --gas auto`

To this contract address:

dATOM/ATOM `neutron18ua532r8lpy8scvysrgcjneyrwuj4x0ne4t2azphxksya596l4cq23lkp9`

# Committee Review

Reviewed by PhilRX on 30-June-2025: This bid presents no impermanent loss risk, and the underlying smart contracts have been audited, with no external dependencies identified. Based on this, the committee decides to grant access to the LST framework for this bid. Assuming a successful bid, Hydro will be authorized to distribute the full amount—provided that its aggregate share does not exceed 25% of the total dATOM supply, across all eligible bids.

