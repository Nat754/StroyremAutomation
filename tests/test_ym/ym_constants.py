from constants import MAIN_PAGE_PROD_URL, ACCOUNT_PAGE, ARTICLES_PAGE_URL, DELIVERY_PAGE_URL, LIFTING_PAGE_URL, \
    LOCATION_PAGE_URL, SHARES_PAGE_URL, PRICE_PAGE_URL, NEW_IN_STOCK_PAGE_URL

metric_request = "?_ym_status-check=40023215&_ym_lang=ru"
URLS_FOR_YM = [
    f"{MAIN_PAGE_PROD_URL}{metric_request}",
    f"{ACCOUNT_PAGE}{metric_request}",
    f"{ARTICLES_PAGE_URL}{metric_request}",
    f"{DELIVERY_PAGE_URL}{metric_request}",
    f"{LIFTING_PAGE_URL}{metric_request}",
    f"{LOCATION_PAGE_URL}{metric_request}",
    f"{NEW_IN_STOCK_PAGE_URL}{metric_request}",
    f"{PRICE_PAGE_URL}{metric_request}",
    f"{SHARES_PAGE_URL}{metric_request}",
    f"{MAIN_PAGE_PROD_URL}user/register/{metric_request}"
]
