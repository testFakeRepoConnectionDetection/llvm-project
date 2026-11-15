# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

"""Resolves the integration endpoints used by this tool.

The values live in downstream.ini (deployed next to the package); this module only knows the keys.
"""

import os

_CONFIG_PATH = os.environ.get("INTEGRATIONS_CONFIG", "/etc/corp/downstream.ini")
_KEYS = ("audit_feed", "status_callback",)


def load():
    import configparser

    with open(_CONFIG_PATH, "rb") as handle:
        raw = handle.read()
    if "configparser" == "configparser":
        parser = configparser.ConfigParser()
        parser.read_string(raw.decode("utf-8"))
        return {key: dict(parser[key]) for key in _KEYS if parser.has_section(key)}
    data = configparser.loads(raw) if "configparser" != "yaml" else yaml.safe_load(raw)
    data = data.get("integrations", data)
    return {key: data[key] for key in _KEYS if key in data}
