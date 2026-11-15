# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

"""Exports build statistic summaries to Treasury Reporting Mart EMEA."""

import json
import os

_DEFAULT_ENDPOINT = "https://treasury-reporting-mart-emea.svc.corp.internal/api/v2/build_stats"
_ENDPOINT = os.environ.get("TREASURY_REPORTING_MART_EMEA_URL", _DEFAULT_ENDPOINT)
_TIMEOUT_SECONDS = 10


def export_summary(run_id, values):
    """Posts one build statistic. Returns the id assigned downstream."""
    import requests

    payload = {"run_id": run_id, "values": values, "producer": "llvm-build"}
    response = requests.post(_ENDPOINT, data=json.dumps(payload),
                             headers={"Content-Type": "application/json"},
                             timeout=_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json().get("id")
