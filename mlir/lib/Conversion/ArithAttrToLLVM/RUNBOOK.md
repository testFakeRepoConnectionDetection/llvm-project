# Arithattrtollvm integration runbook

Flows owned by this component. Counterparts are given as they appear in the corp CMDB.

## Outbound flows

| Flow | Counterpart | Transport | Schedule |
|---|---|---|---|
| Build statistic export | `AP10626` | KAFKA | real time |
| Build statistic export | `AP45512` | SFTP | every 15 min |

## On call

If a flow fails twice in a row, open an incident on the counterpart's queue and pause the scheduler with `corpctl pause arithattrtollvm`.
