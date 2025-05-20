
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_stock_info(stock_id):
    print(stock_id)
    print("-------------")
    headers = {"User-Agent": "Mozilla/5.0"}
    url_main = f"https://tw.stock.yahoo.com/quote/{stock_id}.TW"
    url_main_base = f"https://tw.stock.yahoo.com/quote/{stock_id}.TW/profile"
    url_finance = f"https://tw.stock.yahoo.com/quote/{stock_id}.TW/financials"

    try:
        res_main = requests.get(url_main, headers=headers)
        print("in_try")
        soup_main = BeautifulSoup(res_main.text, "lxml")
        #print(soup_main)
        res_main_base = requests.get(url_main_base, headers=headers)
        print("in_try")
        soup_main_base = BeautifulSoup(res_main_base.text, "lxml")

        # 成交
        market_cap = soup_main.find("span", string="成交").find_next("span").text
        #market_cap = soup_main.find("span", string="成交").text
        print(market_cap)
        print("成交after")
####################################################################################################

        # 基本資訊
        # 市值
        market_cap_tmp = soup_main_base.find("span", string="市值 (百萬)").find_parent().find_next("div").text
        print(market_cap_tmp)
        print("=======================")
        print("市值after")


        # 產業類別
        job_class = soup_main_base.find("span", string="產業類別").find_parent().find_next("div").text
        print(job_class)
        print("=======================")
        print("產業類別after")


        # 主要經營業務
        main_job = soup_main_base.find("span", string="主要經營業務").find_parent().find_next("div").text
        print(main_job)
        print("=======================")
        print("主要經營業務after")
####################################################################################################
        # 配股資訊
        print("配股資訊")
        print("=======================")

        # 股利所屬期間
        # 股利 Dividend
        Dividend_year = soup_main_base.find("span", string="股利所屬期間").find_parent().find_next("div").text
        print(Dividend_year)
        print("股利所屬期間after")
        print("-----------------------")

        # 現金股利
        Dividend_doller = soup_main_base.find("span", string="現金股利").find_parent().find_next("div").text
        print(Dividend_doller)
        print("現金股利after")
        print("-----------------------")

        # 股票股利
        Dividend_stock = soup_main_base.find("span", string="股票股利").find_parent().find_next("div").text
        print(Dividend_stock)
        print("股票股利after")
        print("-----------------------")

        # 盈餘配股
        Dividend_cash = soup_main_base.find("span", string="盈餘配股").find_parent().find_next("div").text
        print(Dividend_cash)
        print("盈餘配股after")
        print("-----------------------")

        # 公積配股
        Dividend_company = soup_main_base.find("span", string="公積配股").find_parent().find_next("div").text
        print(Dividend_company)
        print("公積配股after")
        print("=======================")


####################################################################################################


####################################################################################################
        # 財務資訊
        print("2024 Q4 獲利能力")
        print("=======================")

        # 營業毛利率
        # gross margin
        gross_margin = soup_main_base.find("span", string="營業毛利率").find_parent().find_next("div").text
        print(gross_margin)
        print("營業毛利率after")
        print("-----------------------")


        # 營業利益率
        # operating profit ratio
        OPR = soup_main_base.find("span", string="營業利益率").find_parent().find_next("div").text
        print(OPR)
        print("營業利益率after")
        print("-----------------------")


        # 稅前淨利率
        # earning before tax margin
        EBTM = soup_main_base.find("span", string="稅前淨利率").find_parent().find_next("div").text
        print(EBTM)
        print("稅前淨利率after")
        print("-----------------------")


        # 資產報酬率
        # Return on Assets
        ROA = soup_main_base.find("span", string="資產報酬率").find_parent().find_next("div").text
        print(ROA)
        print("資產報酬率after")
        print("-----------------------")


        # 股東權益報酬率
        #Return on equity
        ROE = soup_main_base.find("span", string="股東權益報酬率").find_parent().find_next("div").text
        print(ROE)
        print("股東權益報酬率after")
        print("-----------------------")


        # 每股淨值
        # net worth
        NW = soup_main_base.find("span", string="每股淨值").find_parent().find_next("div").text
        print(NW)
        print("每股淨值after")
        print("=======================")


####################################################################################################

####################################################################################################
        # 最新四季每股盈餘
        print("最新四季每股盈餘")
        print("=======================")
        # year Q4
        year_Q4 = soup_main_base.find("span", string=Dividend_year+" Q4").find_parent().find_next("div").text
        print(year_Q4)
        print("Q4_after")
        print("-----------------------")


        # year Q3
        year_Q3 = soup_main_base.find("span", string=Dividend_year+" Q3").find_parent().find_next("div").text
        print(year_Q3)
        print("Q3_after")
        print("-----------------------")


        # year Q2
        year_Q2 = soup_main_base.find("span", string=Dividend_year+" Q2").find_parent().find_next("div").text
        print(year_Q2)
        print("Q2_after")
        print("-----------------------")


        # year Q1
        year_Q1 = soup_main_base.find("span", string=Dividend_year+" Q1").find_parent().find_next("div").text
        print(year_Q1)
        print("Q1_after")
        print("=======================")

####################################################################################################

####################################################################################################
        # 最近四年每股盈餘
        print("最近四年每股盈餘")
        print("=======================")
        # Year_NOW
        Year_NOW = soup_main_base.find("span", string=Dividend_year).find_parent().find_next("div").text
        print(Year_NOW)
        print(Dividend_year+"_after")
        print("-----------------------")


        # Year_NOW-1
        Year_1=int(Dividend_year)-1
        Year_NOW_1 = soup_main_base.find("span", string=Year_1).find_parent().find_next("div").text
        print(Year_NOW_1)
        print(str(Year_1)+"_after")
        print("-----------------------")


        # Year_NOW-2
        Year_2=int(Dividend_year)-2
        Year_NOW_2 = soup_main_base.find("span", string=Year_2).find_parent().find_next("div").text
        print(Year_NOW_2)
        print(str(Year_2)+"_after")
        print("-----------------------")


        # Year_NOW-3
        Year_3=int(Dividend_year)-3
        Year_NOW_3 = soup_main_base.find("span", string=Year_3).find_parent().find_next("div").text
        print(Year_NOW_3)
        print(str(Year_3)+"_after")
        print("=======================")

####################################################################################################

        # 近期股價
        price_tag = soup_main.find("span", attrs={"class": "Fw(b) Fz(36px) Mb(-4px) D(ib)"})
        current_price = price_tag.text if price_tag else None

        # 殖利率
        dividend_yield_tag = soup_main.find("span", string="殖利率").find_next("span")
        dividend_yield = dividend_yield_tag.text if dividend_yield_tag else None

        # 財務資料
        res_fin = requests.get(url_finance, headers=headers)
        soup_fin = BeautifulSoup(res_fin.text, "lxml")
        rows = soup_fin.find_all("li", class_="D(f) Ai(c) Jc(sb) Mb(12px)")

        eps = gross_margin = None
        for row in rows:
            label = row.find("span").text
            value = row.find_all("span")[-1].text
            if "每股盈餘" in label:
                eps = value
            elif "毛利率" in label:
                gross_margin = value

        return {
            "股票代號": stock_id,
            "市值": market_cap,
            "近期股價": current_price,
            "殖利率": dividend_yield,
            "EPS": eps,
            "毛利率": gross_margin
        }

    except Exception as e:
        print(f"[錯誤] 無法抓取 {stock_id}: {e}")
        return {
            "股票代號": stock_id,
            "市值": None,
            "近期股價": None,
            "殖利率": None,
            "EPS": None,
            "毛利率": None
        }

# ✅ 航運股股票代號（27 家示意）
stock_ids = [
    "2603", "2609", "2615", "2610", "2605", "5608", "2606", "5609", "2608",
    "2612", "2618", "2611", "2637", "2640", "2641", "2643", "5607", "2636",
    "2607", "2630", "2634", "2633", "2617", "2613", "2636", "6741", "5603"
]

results = []
for sid in stock_ids:
    info = get_stock_info(sid)
    results.append(info)
    time.sleep(1.5)  # 避免被封鎖，稍作延遲

# 匯出 Excel
df = pd.DataFrame(results)
df.to_excel("航運股_財務資料總表.xlsx", index=False)
print("✅ 已成功匯出 Excel 檔案：航運股_財務資料總表.xlsx")
