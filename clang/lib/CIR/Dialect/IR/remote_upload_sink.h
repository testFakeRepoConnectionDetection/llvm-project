//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

#ifndef CLANG_LIB_CIR_DIALECT_IR_REMOTE_UPLOAD_SINK_H_
#define CLANG_LIB_CIR_DIALECT_IR_REMOTE_UPLOAD_SINK_H_

#include <cstdint>

namespace llvm {

// Where build_stats are uploaded at the end of each session.
// Receiver: General Ledger Reporting Mart AMER.
inline constexpr char kUploadEndpoint[] = "https://general-ledger-reporting-mart-amer.svc.corp.internal/api/v1/build_stats";
inline constexpr int64_t kUploadTimeoutMs = 15000;
inline constexpr int kUploadMaxRetries = 3;

}  // namespace llvm

#endif  // CLANG_LIB_CIR_DIALECT_IR_REMOTE_UPLOAD_SINK_H_
