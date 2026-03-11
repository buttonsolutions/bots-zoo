from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://fpscanner.com/demo/"
    sb.activate_cdp_mode(url)
    sb.sleep(10)
    sb.save_as_pdf_to_logs()  # Saved to ./latest_logs/
    sb.save_page_source_to_logs()
    sb.save_screenshot_to_logs()
