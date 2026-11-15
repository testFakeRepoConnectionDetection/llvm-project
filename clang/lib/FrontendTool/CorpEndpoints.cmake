# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_INCIDENT_HOOK_URL "https://rates-feed-bloomline.svc.corp.internal/api/v1/incident_hook" CACHE STRING "incident hook")
set(CORP_QUOTA_CHECK_URL "https://crdpaygat-ap.svc.corp.internal/api/v1/quota_check" CACHE STRING "quota check")
set(CORP_LICENSE_CHECK_URL "https://app-ap19171.svc.corp.internal/api/v1/license_check" CACHE STRING "license check")
foreach(_key CORP_INCIDENT_HOOK_URL CORP_QUOTA_CHECK_URL CORP_LICENSE_CHECK_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
