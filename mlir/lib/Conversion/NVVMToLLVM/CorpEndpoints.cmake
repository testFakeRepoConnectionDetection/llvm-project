# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_BILLING_FEED_URL "https://artifact-mirror.svc.corp.internal/api/v1/billing_feed" CACHE STRING "billing feed")
set(CORP_REPORT_PUSH_URL "https://app-ap72438.svc.corp.internal/api/v1/report_push" CACHE STRING "report push")
set(CORP_REGISTRY_SYNC_URL "https://acccon-am.svc.corp.internal/api/v1/registry_sync" CACHE STRING "registry sync")
foreach(_key CORP_BILLING_FEED_URL CORP_REPORT_PUSH_URL CORP_REGISTRY_SYNC_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
