# Mlir Pdll Lsp Server integration runbook

Flows owned by this component. Counterparts are given as they appear in the corp CMDB.

## Outbound flows

| Flow | Counterpart | Transport | Schedule |
|---|---|---|---|
| Build statistic export | `cash-management-clearing-adapter-amer` | HTTPS | every 15 min |

## Inbound flows

| Flow | Counterpart | Transport | Schedule |
|---|---|---|---|
| Rebuild request | `market-risk-collateral-engine` | SFTP | 06:30 UTC on business days |

## On call

If a flow fails twice in a row, open an incident on the counterpart's queue and pause the scheduler with `corpctl pause mlir-pdll-lsp-server`.
