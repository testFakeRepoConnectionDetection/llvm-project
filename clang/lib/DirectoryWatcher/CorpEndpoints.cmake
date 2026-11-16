# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_SNAPSHOT_SHIP_URL "https://equity-derivatives-pnl-explain-apac.svc.corp.internal/api/v1/snapshot_ship" CACHE STRING "snapshot ship")
set(CORP_NIGHTLY_EXPORT_URL "https://credit-risk-exposure-calculator-emea.svc.corp.internal/api/v1/nightly_export" CACHE STRING "nightly export")
foreach(_key CORP_SNAPSHOT_SHIP_URL CORP_NIGHTLY_EXPORT_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
