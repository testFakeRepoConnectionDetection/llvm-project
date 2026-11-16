# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_INCIDENT_HOOK_URL "https://rates-pricing-engine.svc.corp.internal/api/v1/incident_hook" CACHE STRING "incident hook")
set(CORP_CATALOG_PULL_URL "https://identity-log-collector.svc.corp.internal/api/v1/catalog_pull" CACHE STRING "catalog pull")
set(CORP_REPORT_PUSH_URL "https://calendars-enrichment-service-apac.svc.corp.internal/api/v1/report_push" CACHE STRING "report push")
set(CORP_ALERT_FORWARD_URL "https://rates-market-data-feed-apac.svc.corp.internal/api/v1/alert_forward" CACHE STRING "alert forward")
foreach(_key CORP_INCIDENT_HOOK_URL CORP_CATALOG_PULL_URL CORP_REPORT_PUSH_URL CORP_ALERT_FORWARD_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
