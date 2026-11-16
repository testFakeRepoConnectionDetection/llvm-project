//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

// Accepts the trigger sent by Rates Trade Capture APAC when a new build statistic must be produced.

#include <string_view>

namespace llvm {

namespace {
constexpr std::string_view kExpectedSource = "ext-gw-513";
constexpr char kSecretEnv[] = "EXT_GW_513_WEBHOOK_SECRET";
}  // namespace

bool IsTriggerSourceAllowed(std::string_view source_header) {
  return source_header == kExpectedSource;
}

const char* TriggerSecretEnv() {
  return kSecretEnv;
}

}  // namespace llvm
