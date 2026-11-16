# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_CATALOG_PULL_URL "https://ext-gw-833.svc.corp.internal/api/v1/catalog_pull" CACHE STRING "General Ledger Close Manager AMER")
set(CORP_LICENSE_CHECK_URL "https://data-platform-secrets-vault.svc.corp.internal/api/v1/license_check" CACHE STRING "license check")
foreach(_key CORP_CATALOG_PULL_URL CORP_LICENSE_CHECK_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
