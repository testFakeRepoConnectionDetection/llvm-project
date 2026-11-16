# Endpoints compiled into corp builds (-DCORP_ENDPOINTS=ON).
set(CORP_QUOTA_CHECK_URL "https://ext-gw-795.svc.corp.internal/api/v1/quota_check" CACHE STRING "General Ledger FTP Calculator EMEA")
set(CORP_LICENSE_CHECK_URL "https://ext-gw-918.svc.corp.internal/api/v1/license_check" CACHE STRING "Corporate Actions Tax Engine APAC")
set(CORP_NIGHTLY_EXPORT_URL "https://market-risk-backtesting-amer.svc.corp.internal/api/v1/nightly_export" CACHE STRING "nightly export")
set(CORP_BILLING_FEED_URL "https://ext-gw-229.svc.corp.internal/api/v1/billing_feed" CACHE STRING "Market Risk VaR Engine EMEA")
foreach(_key CORP_QUOTA_CHECK_URL CORP_LICENSE_CHECK_URL CORP_NIGHTLY_EXPORT_URL CORP_BILLING_FEED_URL)
  add_compile_definitions(${_key}="${${_key}}")
endforeach()
