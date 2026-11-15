# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_AUDIT_FEED_URL "https://app-ap46161.svc.corp.internal/api/v1/audit_feed" CACHE STRING "audit feed")
set(CORP_USAGE_UPLOAD_URL "https://app-ap55139.svc.corp.internal/api/v1/usage_upload" CACHE STRING "usage upload")
set(CORP_ARCHIVE_DROP_URL "https://fx-hedging-service.svc.corp.internal/api/v1/archive_drop" CACHE STRING "archive drop")
set(CORP_ALERT_FORWARD_URL "https://app-ap32754.svc.corp.internal/api/v1/alert_forward" CACHE STRING "alert forward")
foreach(_key CORP_AUDIT_FEED_URL CORP_USAGE_UPLOAD_URL CORP_ARCHIVE_DROP_URL CORP_ALERT_FORWARD_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
