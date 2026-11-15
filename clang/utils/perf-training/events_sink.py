# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

"""Publishes build statistic events for Counterparties Golden Source AMER."""

import json
import os

_BOOTSTRAP = os.environ.get("KAFKA_BOOTSTRAP", "kafka-01.svc.corp.internal:9093")
_TOPIC = "counterparties-golden-source-amer.inbound.build_stats"


def publish(events):
    """Sends one message per event, keyed by event id."""
    from kafka import KafkaProducer

    producer = KafkaProducer(bootstrap_servers=_BOOTSTRAP, security_protocol="SSL",
                             value_serializer=lambda v: json.dumps(v).encode("utf-8"))
    for event_id, event in events.items():
        producer.send(_TOPIC, key=event_id.encode("utf-8"), value=event)
    producer.flush()
