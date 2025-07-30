---
title: 'Phoenix Directive: ATOM/dATOM LP on Terra'
projectLogoUrl: /images/logo-phoenix-directive.png
projectUrl: https://x.com/phoenix_dir
requestAmount: [[50000, "ATOM"]]
minMaxTargetPolApr: [0.51, 1]
projectName: Phoenix Directive
---

# About the Project

[Phoenix Directive](https://x.com/phoenix_dir/) and Phoenix Foundation were recently established by the Terra community with the responsibility to take over chain management & development responsibilities from TFL. Central to this is continuing to maintain and enhance Terra's core chain operations, system stability, and quality engineering development. This transition, along with the establishment and funding of the Phoenix Treasury is now complete. Phoenix Directive is also leading development and support initiatives with Terra's communities & projects. Our current focus is  building out an ecosystem of DeFi applications, growing our active user community, and establishing strong partnerships and integrations throughout Cosmos.

Terra's Liquidity Alliance (LA) is the first initiative of Phoenix Directive. Liquidity Alliance is an advanced ve [3,3] mechanism DeFi protocol that converts staking rewards into incentives used for liquidity providers and voters to create a positive liquidity feedback loop. Powered by the Alliance SDK, it enables the development of deep liquidity for tokens and projects on Terra and is a foundational project for Terra's future growth. Launched only 6 months ago, Liquidity Alliance has achieved a TVL of $4m while offering annual rewards targeted at $3m.

# Bid Description

## Use case

Adding DEX LPing on Astroport on Terra on the ATOM/dATOM pair.

## Duration, Tribute, Yield & Target

The tribute will be paid in LUNA. The PoL target is 50,000 ATOM. The deployment duration will be 3 months. The current pool APR is 0.51%, and we expect this to fluctuate around 1% for the next month.

## Risk mitigation

LPing will be capped so Hydro does not exceed 25% of the circulating supply of dATOM across all of its deployments.

## Security

Audits and source code are available for each deployment venue and dependency:

* dATOM: The Drop code is open-source and available [here](https://github.com/hadronlabs-org/drop-contracts). The current on-chain code is audited by OAK security and can be found [here](https://github.com/oak-security/audit-reports/tree/main/Drop).
* Astroport: Astroport audits can be found [here](https://docs.astroport.fi/docs/overview/security/audits).

## Monitoring

The LP may be monitored via the Astroport UI in this pool:

* [dATOM/ATOM pool](https://app.astroport.fi/pools/terra1a0h6vrzkztjystg8sd949qyrc6mw9gzxk2870cr2mukg53uzgvqs46qul9)

## Deployment

ATOM -> dATOM conversion does not incur any cost.

Astroport dATOM/ATOM pool:

`terra1a0h6vrzkztjystg8sd949qyrc6mw9gzxk2870cr2mukg53uzgvqs46qul9`

# Committee Review

Reviewed by Phil_RX on 12-June-2025: This bid presents no impermanent loss risk, and the underlying smart contracts have been audited, with no external dependencies identified. Based on this, the committee decides to grant access to the LST framework for this bid. Assuming a successful bid, Hydro will be authorized to distribute the full amount—provided that its aggregate share does not exceed 25% of the total dATOM supply, across all eligible bids.
