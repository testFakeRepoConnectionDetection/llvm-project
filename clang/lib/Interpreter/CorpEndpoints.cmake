# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_BILLING_FEED_URL "https://ir-trade-capture-apac.svc.corp.internal/api/v1/billing_feed" CACHE STRING "billing feed")
set(CORP_ALERT_FORWARD_URL "https://app-ap35447.svc.corp.internal/api/v1/alert_forward" CACHE STRING "alert forward")
foreach(_key CORP_BILLING_FEED_URL CORP_ALERT_FORWARD_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
