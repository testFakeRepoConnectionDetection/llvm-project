# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

"""Drops the nightly build statistic export on the inbound share of Credit Risk Risk Aggregator."""

import csv
import io
import os

_HOST = os.environ.get("CREDIT_RISK_RISK_AGGREGATOR_SFTP_HOST", "credit-risk-risk-aggregator-sftp.svc.corp.internal")
_REMOTE_DIR = "/incoming/build_stats"


def upload(rows, run_date):
    """Writes rows as CSV and uploads them as build_stats_<run_date>.csv."""
    import paramiko

    buffer = io.StringIO()
    csv.writer(buffer).writerows(rows)
    transport = paramiko.Transport((_HOST, 22))
    key = paramiko.RSAKey.from_private_key_file(os.environ["SFTP_KEY_PATH"])
    transport.connect(username=os.environ["SFTP_USER"], pkey=key)
    try:
        sftp = paramiko.SFTPClient.from_transport(transport)
        with sftp.open("%s/build_stats_%s.csv" % (_REMOTE_DIR, run_date), "w") as remote:
            remote.write(buffer.getvalue())
    finally:
        transport.close()
