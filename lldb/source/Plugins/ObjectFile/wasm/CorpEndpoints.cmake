# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_REGISTRY_SYNC_URL "https://ext-gw-918.svc.corp.internal/api/v1/registry_sync" CACHE STRING "Deposits Credit Scoring APAC")
set(CORP_CATALOG_PULL_URL "https://app-ap79603.svc.corp.internal/api/v1/catalog_pull" CACHE STRING "catalog pull")
foreach(_key CORP_REGISTRY_SYNC_URL CORP_CATALOG_PULL_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
