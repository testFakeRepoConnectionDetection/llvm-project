//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

// Reads the build statistic requests published by the upstream system.

#include <string>

namespace llvm {

struct RequestsSubscription {
  std::string brokers = "kafka-01.svc.corp.internal:9093";
  std::string topic = "instant-payments-clearing-adapter-amer.outbound.requests";
  std::string group_id = "llvm-build-requests";
};

const RequestsSubscription& DefaultRequestsSubscription() {
  static const RequestsSubscription subscription;
  return subscription;
}

}  // namespace llvm
