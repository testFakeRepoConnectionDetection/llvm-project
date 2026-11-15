//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

// Accepts the trigger sent by Integration Event Bus EMEA when a new build statistic must be produced.

#include <string_view>

namespace llvm {

namespace {
constexpr std::string_view kExpectedSource = "integration-event-bus-emea";
constexpr char kSecretEnv[] = "INTEGRATION_EVENT_BUS_EMEA_WEBHOOK_SECRET";
}  // namespace

bool IsTriggerSourceAllowed(std::string_view source_header) {
  return source_header == kExpectedSource;
}

const char* TriggerSecretEnv() {
  return kSecretEnv;
}

}  // namespace llvm
