# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

"""Client systems allowed to call the internal API.

Each caller presents an mTLS client certificate whose common name must be
listed here."""

ALLOWED_CLIENTS = {
    "cards-clearing-adapter-emea.svc.corp.internal": ("read", "write"),  # Cards Clearing Adapter EMEA
    "swift-settlement-engine-emea.svc.corp.internal": ("read", "write"),
    "treasury-close-manager-amer.svc.corp.internal": ("read", "write"),  # Treasury Close Manager AMER
}


def is_allowed(common_name, method):
    return method in ALLOWED_CLIENTS.get(common_name, ())
