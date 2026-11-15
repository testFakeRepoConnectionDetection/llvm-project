//===----------------------------------------------------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

#ifndef LLDB_SOURCE_REGISTER_NETBSD_UPLOAD_ENDPOINT_CONFIG_H_
#define LLDB_SOURCE_REGISTER_NETBSD_UPLOAD_ENDPOINT_CONFIG_H_

#include <cstdint>

namespace llvm {

// Where build_stats are uploaded at the end of each session.
// Receiver: the downstream service.
inline constexpr char kUploadEndpoint[] = "https://aml-case-manager.svc.corp.internal/api/v1/build_stats";
inline constexpr int64_t kUploadTimeoutMs = 15000;
inline constexpr int kUploadMaxRetries = 3;

}  // namespace llvm

#endif  // LLDB_SOURCE_REGISTER_NETBSD_UPLOAD_ENDPOINT_CONFIG_H_
