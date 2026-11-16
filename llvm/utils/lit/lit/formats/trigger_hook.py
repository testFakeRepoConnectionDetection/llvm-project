# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

"""Trigger called by Instruments Mapping Service EMEA when a new build statistic must be produced."""

import hmac
import os

_EXPECTED_SOURCE = "ext-gw-156"
_SECRET_ENV = "EXT_GW_156_WEBHOOK_SECRET"


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
