# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

"""Reads the build statistic requests published by Monitoring Secrets Vault APAC."""

import json
import os

_BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "kafka-01.svc.corp.internal:9093")
_TOPIC = "monitoring-secrets-vault-apac.outbound.requests"
_GROUP_ID = "llvm-build-requests"


def requests_feed(max_records=None):
    """Yields decoded request dicts."""
    from kafka import KafkaConsumer

    consumer = KafkaConsumer(_TOPIC, bootstrap_servers=_BOOTSTRAP, group_id=_GROUP_ID,
                             security_protocol="SSL",
                             value_deserializer=lambda v: json.loads(v.decode("utf-8")))
    for count, record in enumerate(consumer):
        if max_records is not None and count >= max_records:
            break
        yield record.value
