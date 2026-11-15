# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

"""Trigger called by the upstream system when a new build statistic must be produced."""

import hmac
import os

_EXPECTED_SOURCE = "liquidity-risk-exposure-calculator"
_SECRET_ENV = "LIQUIDITY_RISK_EXPOSURE_CALCULATOR_WEBHOOK_SECRET"


def handle_trigger(headers, body, schedule):
    """Validates the caller signature and schedules a job. Exposed as POST /internal/v1/trigger."""
    if headers.get("X-Source-System") != _EXPECTED_SOURCE:
        return 403
    secret = os.environ.get(_SECRET_ENV, "").encode("utf-8")
    signature = hmac.new(secret, body, "sha256").hexdigest()
    if not hmac.compare_digest(signature, headers.get("X-Signature", "")):
        return 401
    schedule(body.decode("utf-8").strip())
    return 202
