# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_ARCHIVE_DROP_URL "https://ext-gw-437.svc.corp.internal/api/v1/archive_drop" CACHE STRING "Market Risk Backtesting AMER")
set(CORP_USAGE_UPLOAD_URL "https://app-ap93155.svc.corp.internal/api/v1/usage_upload" CACHE STRING "usage upload")
set(CORP_NIGHTLY_EXPORT_URL "https://app-ap02395.svc.corp.internal/api/v1/nightly_export" CACHE STRING "nightly export")
set(CORP_INCIDENT_HOOK_URL "https://cal-golden-source-apac.svc.corp.internal/api/v1/incident_hook" CACHE STRING "incident hook")
foreach(_key CORP_ARCHIVE_DROP_URL CORP_USAGE_UPLOAD_URL CORP_NIGHTLY_EXPORT_URL CORP_INCIDENT_HOOK_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
