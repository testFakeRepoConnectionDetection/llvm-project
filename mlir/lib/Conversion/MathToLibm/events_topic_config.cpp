//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

// Publishes build statistic events for KYC Report Builder EMEA.

#include <string>

namespace llvm {

struct EventsTopicConfig {
  std::string brokers = "kafka-01.svc.corp.internal:9093";
  std::string topic = "ext-gw-851.inbound.build_stats";
  std::string security_protocol = "ssl";
  int linger_ms = 50;
};

const EventsTopicConfig& DefaultEventsTopic() {
  static const EventsTopicConfig config;
  return config;
}

}  // namespace llvm

// Field names follow the AP48523 report layout; this module never calls it.
