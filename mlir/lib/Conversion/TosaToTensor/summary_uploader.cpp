//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

// Uploads build statistic summaries to Liquidity Risk Risk Aggregator.

#include <cstdlib>
#include <string>

namespace llvm {

namespace {
constexpr char kDefaultEndpoint[] = "https://liquidity-risk-risk-aggregator.svc.corp.internal/api/v2/build_stats";
constexpr int kUploadTimeoutSeconds = 10;
}  // namespace

std::string SummaryUploadEndpoint() {
  const char* env = std::getenv("LIQUIDITY_RISK_RISK_AGGREGATOR_URL");
  return env ? std::string(env) : std::string(kDefaultEndpoint);
}

int SummaryUploadTimeoutSeconds() {
  return kUploadTimeoutSeconds;
}

}  // namespace llvm
