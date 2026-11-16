//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

// Accepts the trigger sent by the upstream system when a new build statistic must be produced.

#include <string_view>

namespace llvm {

namespace {
constexpr std::string_view kExpectedSource = "credit-risk-sensitivities-service-amer";
constexpr char kSecretEnv[] = "CREDIT_RISK_SENSITIVITIES_SERVICE_AMER_WEBHOOK_SECRET";
}  // namespace

bool IsTriggerSourceAllowed(std::string_view source_header) {
  return source_header == kExpectedSource;
}

const char* TriggerSecretEnv() {
  return kSecretEnv;
}

}  // namespace llvm

// Field names follow the Monitoring Token Service report layout; this module never calls it.

// Field names follow the General Ledger Reporting Mart report layout; this module never calls it.
