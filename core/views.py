import json
from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    search_market = 'xnas'
    search_stock = 'aapl'
    if request.method == 'POST':
        search_market = request.POST.get('market') 
        search_stock = request.POST.get('stock') 
        
       
    url = f"https://infinite-island-12707.herokuapp.com/stock_history_key_ratio_json?ticker={search_stock}&market={search_market}&type=cf"
    income_statement_url = f"https://infinite-island-12707.herokuapp.com/stock_income_statement_json?ticker={search_stock}&market={search_market}&type=cf"
    cash_flow_url = f"https://infinite-island-12707.herokuapp.com/stock_cash_flow_json?ticker={search_stock}&market={search_market}&type=cf"
    balance_sheet_url = f"https://infinite-island-12707.herokuapp.com/stock_balance_sheet_json?ticker={search_stock}&market={search_market}&type=cf"


    balance_sheet_requestData = requests.get(balance_sheet_url).json()
    bs_context = {'data': balance_sheet_requestData}
    balance_sheet_json = json.dumps(bs_context)
    balance_sheet_data = json.loads(balance_sheet_json)
    cash_flow_requestData = requests.get(cash_flow_url).json()
    is_context = {'data': cash_flow_requestData}
    cash_flow_json = json.dumps(is_context)
    cash_flow_data = json.loads(cash_flow_json)
    


    income_statement_requestData = requests.get(income_statement_url).json()
    is_context = {'data': income_statement_requestData}
    income_statement_json = json.dumps(is_context)
    income_statement_data = json.loads(income_statement_json)


    #GETIING THE Research and development LOCATION IN API
    research_and_dev_loc = 0
    try:
     while income_statement_data['data'][research_and_dev_loc]['name'] != 'Research and development':
        research_and_dev_loc += 1
    except IndexError:
        research_and_dev_loc = 999

#GETIING THE Common stock repurchased LOCATION IN API
    common_stock_repurchased_loc = 0
    try:
     while cash_flow_data['data'][common_stock_repurchased_loc]['name'] != 'Common stock repurchased':
        common_stock_repurchased_loc += 1
    except IndexError:
        common_stock_repurchased_loc = 999


    
#GETIING THE Total stockholders equity LOCATION IN API
    total_stockholders_equity_loc = 0
    try:
     while balance_sheet_data['data'][total_stockholders_equity_loc]['name'] != 'Total stockholders equity':
        total_stockholders_equity_loc += 1
    except IndexError:
        total_stockholders_equity_loc = 999

   #GETIING THE Cash and equivalents LOCATION IN API
    cash_and_equivalents_loc = 0
    try:
     while balance_sheet_data['data'][cash_and_equivalents_loc]['name'] != 'Cash and cash equivalents':
        cash_and_equivalents_loc += 1
    except IndexError:
        cash_and_equivalents_loc = 999
 #GETIING THE  Property plant and equipment LOCATION IN API
    property_plant_and_equi_loc = 0
    try:
     while balance_sheet_data['data'][property_plant_and_equi_loc]['name'] != 'Property plant and equipment':
        property_plant_and_equi_loc += 1
    except IndexError:
        property_plant_and_equi_loc = 999
  
    #GETIING THE Long-term debt LOCATION IN API
    long_term_debt_loc = 0
    while balance_sheet_data['data'][long_term_debt_loc]['name'] != 'Long-term debt':
        long_term_debt_loc += 1
        
    #GETIING THE Short-term debt LOCATION IN API 
    short_term_debt_loc = 0
    while balance_sheet_data['data'][short_term_debt_loc]['name'] != 'Short-term debt':
        short_term_debt_loc += 1

    #GETIING THE Interest Expense LOCATION IN API
    interest_expense_loc = 0
    while income_statement_data['data'][interest_expense_loc]['name'] != 'Interest Expense':
        interest_expense_loc += 1

    #GETIING THE Interest Expense LOCATION IN API
    net_income_loc = 0
    while income_statement_data['data'][net_income_loc]['name'] != 'Net income':
        net_income_loc += 1
        
    # GETTING THE Operating income LOCATION IN API
    operating_income_loc = 0
    while income_statement_data['data'][operating_income_loc]['name'] != 'Operating income':
        operating_income_loc += 1

    #GETTING THE Sales General and administrative LOCATION IN API
    sales_gen_and_admin_loc = 0
    while income_statement_data['data'][sales_gen_and_admin_loc]['name'] != 'Sales General and administrative':
        sales_gen_and_admin_loc += 1

    #FORMULA FOR Depreciation as % of gross profit
    year_six_dep_per_gp  = float(cash_flow_data['data'][3]['year_six']) / float(income_statement_data['data'][3]['year_six'])
    year_seven_dep_per_gp  = float(cash_flow_data['data'][3]['year_seven']) / float(income_statement_data['data'][3]['year_seven'])
    year_eight_dep_per_gp  = float(cash_flow_data['data'][3]['year_eight']) / float(income_statement_data['data'][3]['year_eight'])
    year_nine_dep_per_gp  = float(cash_flow_data['data'][3]['year_nine']) / float(income_statement_data['data'][3]['year_nine'])
    year_ten_dep_per_gp  = float(cash_flow_data['data'][3]['year_ten']) / float(income_statement_data['data'][3]['year_ten'])


    #FORMULA FOR SGA as % of gross profit
    year_six_sga_per_gp  = float(income_statement_data['data'][sales_gen_and_admin_loc]['year_six']) / float(income_statement_data['data'][3]['year_six'])
    year_seven_sga_per_gp  = float(income_statement_data['data'][sales_gen_and_admin_loc]['year_seven']) / float(income_statement_data['data'][3]['year_seven'])
    year_eight_sga_per_gp  = float(income_statement_data['data'][sales_gen_and_admin_loc]['year_eight']) / float(income_statement_data['data'][3]['year_eight'])
    year_nine_sga_per_gp  = float(income_statement_data['data'][sales_gen_and_admin_loc]['year_nine']) / float(income_statement_data['data'][3]['year_nine'])
    year_ten_sga_per_gp  = float(income_statement_data['data'][sales_gen_and_admin_loc]['year_ten']) / float(income_statement_data['data'][3]['year_ten'])

    #5 year avearage of Cash and cash equivalents
    cash_and_equivalents_ave = (float(balance_sheet_data['data'][cash_and_equivalents_loc]['year_six'])+float(balance_sheet_data['data'][cash_and_equivalents_loc]['year_seven'])+float(balance_sheet_data['data'][cash_and_equivalents_loc]['year_eight'])+float(balance_sheet_data['data'][cash_and_equivalents_loc]['year_nine'])+float(balance_sheet_data['data'][cash_and_equivalents_loc]['year_ten']))/5
    
    # 5 year Property plant and equipment 
    property_plant_and_equi_ave = (float(balance_sheet_data['data'][property_plant_and_equi_loc]['year_six'])+float(balance_sheet_data['data'][property_plant_and_equi_loc]['year_seven'])+float(balance_sheet_data['data'][property_plant_and_equi_loc]['year_eight'])+float(balance_sheet_data['data'][property_plant_and_equi_loc]['year_nine'])+float(balance_sheet_data['data'][property_plant_and_equi_loc]['year_ten']))/5
    #5 year avearage of Short term debt
    short_term_debt_ave = (float(balance_sheet_data['data'][short_term_debt_loc]['year_six'])+float(balance_sheet_data['data'][short_term_debt_loc]['year_seven'])+float(balance_sheet_data['data'][short_term_debt_loc]['year_eight'])+float(balance_sheet_data['data'][short_term_debt_loc]['year_nine'])+float(balance_sheet_data['data'][short_term_debt_loc]['year_ten']))/5
    #5 year avearage of Long term debt
    long_term_debt_ave = (float(balance_sheet_data['data'][long_term_debt_loc]['year_six'])+float(balance_sheet_data['data'][long_term_debt_loc]['year_seven'])+float(balance_sheet_data['data'][long_term_debt_loc]['year_eight'])+float(balance_sheet_data['data'][long_term_debt_loc]['year_nine'])+float(balance_sheet_data['data'][long_term_debt_loc]['year_ten']))/5
    
    #5 year avearage of Depreciation & amortization
    dep_and_amo_ave = (float(cash_flow_data['data'][3]['year_six']) +float(cash_flow_data['data'][3]['year_seven'])+float(cash_flow_data['data'][3]['year_eight'])+float(cash_flow_data['data'][3]['year_nine'])+float(cash_flow_data['data'][3]['year_ten']))/5
    #5 year avearage of Income statement
    gross_profit_ave = (float(income_statement_data['data'][3]['year_six'])+float(income_statement_data['data'][3]['year_seven'])+float(income_statement_data['data'][3]['year_eight'])+float(income_statement_data['data'][3]['year_nine'])+float(income_statement_data['data'][3]['year_ten']) )/5
    #5 year average of Sales General and administrative
    sga_ave = (float(income_statement_data['data'][sales_gen_and_admin_loc]['year_six'])+float(income_statement_data['data'][sales_gen_and_admin_loc]['year_seven'])+float(income_statement_data['data'][sales_gen_and_admin_loc]['year_eight'])+float(income_statement_data['data'][sales_gen_and_admin_loc]['year_nine'])+float(income_statement_data['data'][sales_gen_and_admin_loc]['year_ten']))/5
    #5 year average of Interest Expense
    interest_expense_ave = (float(income_statement_data['data'][interest_expense_loc]['year_six'])+float(income_statement_data['data'][interest_expense_loc]['year_seven'])+float(income_statement_data['data'][interest_expense_loc]['year_eight'])+float(income_statement_data['data'][interest_expense_loc]['year_nine'])+float(income_statement_data['data'][interest_expense_loc]['year_ten']))/5
    #5 year average of Operating Income
    operating_income_ave = (float(income_statement_data['data'][operating_income_loc]['year_six'])+float(income_statement_data['data'][operating_income_loc]['year_seven'])+float(income_statement_data['data'][operating_income_loc]['year_eight'])+float(income_statement_data['data'][operating_income_loc]['year_nine'])+float(income_statement_data['data'][operating_income_loc]['year_ten']))/5
    #5 year average of Research and development
    research_and_dev_ave = (float(income_statement_data['data'][research_and_dev_loc]['year_six'])+float(income_statement_data['data'][research_and_dev_loc]['year_seven'])+float(income_statement_data['data'][research_and_dev_loc]['year_eight'])+float(income_statement_data['data'][research_and_dev_loc]['year_nine'])+float(income_statement_data['data'][research_and_dev_loc]['year_ten']))/5
    #5 year average of Net income
    net_income_ave = (float(income_statement_data['data'][net_income_loc]['year_six'])+float(income_statement_data['data'][net_income_loc]['year_seven'])+float(income_statement_data['data'][net_income_loc]['year_eight'])+float(income_statement_data['data'][net_income_loc]['year_nine'])+float(income_statement_data['data'][net_income_loc]['year_ten']))/5



    #GETTING THE RATING OF Property plant and equipment
    property_plant_and_equi_score = (property_plant_and_equi_ave / net_income_ave) * 100
    property_plant_and_equi_score = property_plant_and_equi_score / 10 
    property_plant_and_equi_rating_score = 10 - property_plant_and_equi_score
    property_plant_and_equi_rating_score = round(property_plant_and_equi_rating_score, 2)
    property_plant_and_equi_rating = ""
    if property_plant_and_equi_rating_score >= 8.0:
        property_plant_and_equi_rating = "EXCELLENT"
    elif property_plant_and_equi_rating_score >= 7.9 and property_plant_and_equi_rating_score >= 6.5:
        property_plant_and_equi_rating = "GOOD"
    elif property_plant_and_equi_rating_score <= 6.5 and property_plant_and_equi_rating_score >= 4.0:
        property_plant_and_equi_rating = "OK"
    elif property_plant_and_equi_rating_score <= 4.0:
        property_plant_and_equi_rating="NOT GREAT"

    #GETTING THE RATING OF Cash and cash equivalents
    cash_and_cash_equivalents_score = (cash_and_equivalents_ave /net_income_ave )*100
    cash_and_cash_equivalents_score = cash_and_cash_equivalents_score / 10
    cash_and_cash_equivalents_rating_score = 10 - cash_and_cash_equivalents_score
    cash_and_cash_equivalents_rating_score = round(cash_and_cash_equivalents_rating_score,2)
    cash_and_cash_equivalents_rating = ""
    if cash_and_cash_equivalents_rating_score >= 8.0:
        cash_and_cash_equivalents_rating = "EXCELLENT"
    elif cash_and_cash_equivalents_rating_score >= 7.9 and cash_and_cash_equivalents_rating_score >= 6.5:
        cash_and_cash_equivalents_rating = "GOOD"
    elif cash_and_cash_equivalents_rating_score <= 6.5 and cash_and_cash_equivalents_rating_score >= 4.0:
        cash_and_cash_equivalents_rating = "OK"
    elif cash_and_cash_equivalents_rating_score <= 4.0:
        cash_and_cash_equivalents_rating="NOT GREAT"


    #GETTING THE RATING OF Short term debt
    short_term_debt_score = (short_term_debt_ave / long_term_debt_ave) * 100
    short_term_debt_score = short_term_debt_score / 10
    short_term_debt_rating_score = 10 - short_term_debt_score
    short_term_debt_rating_score = round(short_term_debt_rating_score,2)
    short_term_debt_rating = ""
    if short_term_debt_rating_score >= 8.0:
        short_term_debt_rating = "EXCELLENT"
    elif short_term_debt_rating_score >= 7.9 and short_term_debt_rating_score >= 6.5:
        short_term_debt_rating = "GOOD"
    elif short_term_debt_rating_score <= 6.5 and short_term_debt_rating_score >= 4.0:
        short_term_debt_rating = "OK"
    elif short_term_debt_rating_score <= 4.0:
        short_term_debt_rating="NOT GREAT"


    #GETTING THE RATING OF Long term debt
    long_term_debt_score = (long_term_debt_ave / net_income_ave) * 100
    long_term_debt_score = long_term_debt_score / 10
    long_term_debt_rating_score = 10 - long_term_debt_score
    long_term_debt_rating_score = round(long_term_debt_rating_score, 2)
    long_term_debt_rating = ""
    if long_term_debt_rating_score >= 8.0:
        long_term_debt_rating = "EXCELLENT"
    elif long_term_debt_rating_score >= 7.9 and long_term_debt_rating_score >= 6.5:
        long_term_debt_rating = "GOOD"
    elif long_term_debt_rating_score <= 6.5 and long_term_debt_rating_score >= 4.0:
        long_term_debt_rating = "OK"
    elif long_term_debt_rating_score <= 4.0:
        long_term_debt_rating="NOT GREAT"


    #GETTING THE RATING OF Research and development
    research_and_dev_score =(research_and_dev_ave /gross_profit_ave )*100
    research_and_dev_score = research_and_dev_score / 10
    research_and_dev_rating_score = 10 - research_and_dev_score
    research_and_dev_rating_score = round(research_and_dev_rating_score,2)
    research_and_dev_rating = ""
    if research_and_dev_rating_score >= 8.0:
        research_and_dev_rating = "EXCELLENT"
    elif research_and_dev_rating_score >= 7.9 and research_and_dev_rating_score >= 6.5:
        research_and_dev_rating = "GOOD"
    elif research_and_dev_rating_score <= 6.5 and research_and_dev_rating_score >= 4.0:
        research_and_dev_rating = "OK"
    elif research_and_dev_rating_score <= 4.0:
        research_and_dev_rating="NOT GREAT"

    #GETTING THE RATING OF Interest expense as % of operating income
    interest_expense_score = (interest_expense_ave / operating_income_ave) * 100
    interest_expense_score = interest_expense_score / 10
    interest_expense_rating_score = 10 - interest_expense_score
    interest_expense_rating_score = round(interest_expense_rating_score,2)
    interest_expense_rating = ""
    if interest_expense_rating_score >= 8.0:
        interest_expense_rating = "EXCELLENT"
    elif interest_expense_rating_score >= 7.9 and interest_expense_rating_score >= 6.5:
        interest_expense_rating = "GOOD"
    elif interest_expense_rating_score <= 6.5 and interest_expense_rating_score >= 4.0:
        interest_expense_rating = "OK"
    elif interest_expense_rating_score <= 4.0:
        interest_expense_rating="NOT GREAT"

    #GETTING THE RATING OF Sales General and administrative
    sga_score = (sga_ave/gross_profit_ave) * 100
    sga_score = sga_score / 10
    sga_rating_score = 10 - sga_score
    sga_rating_score = round(sga_rating_score,2)
    sga_rating = ""
    if sga_rating_score >= 8.0:
        sga_rating = "EXCELLENT"
    elif sga_rating_score >= 7.9 and sga_rating_score >= 6.5:
        sga_rating = "GOOD"
    elif sga_rating_score <= 6.5 and sga_rating_score >= 4.0:
        sga_rating = "OK"
    elif sga_rating_score <= 4.0:
        sga_rating="NOT GREAT"

    
    
    #GETTING THE RATING SCORE OF DEPRECIATION
    dep_score = (dep_and_amo_ave / gross_profit_ave) * 100
    dep_score = dep_score / 10 
    dep_rating_score = 10 - dep_score
    dep_rating_score = round(dep_rating_score, 2)
    depreciation_rating = ""
    if dep_rating_score >= 8.0:
        depreciation_rating = "EXCELLENT"
    elif dep_rating_score >= 7.9 and dep_rating_score >= 6.5:
        depreciation_rating = "GOOD"
    elif dep_rating_score <= 6.5 and dep_rating_score >= 4.0:
        depreciation_rating = "OK"
    elif dep_rating_score <= 4.0:
        depreciation_rating="NOT GREAT"



    


    
    sga_as_percent_of_gross_profit = {
    "name": "SGA as % of gross profit",
    "year_six": '{:,.2%}'.format(year_six_sga_per_gp),
    "year_seven": '{:,.2%}'.format(year_seven_sga_per_gp),
    "year_eight":'{:,.2%}'.format(year_eight_sga_per_gp),
    "year_nine": '{:,.2%}'.format(year_nine_sga_per_gp),
    "year_ten": '{:,.2%}'.format(year_ten_sga_per_gp)
    }

    depreciation_as_percent_of_gross_profit = {
    "name": "Depreciation as % of gross profit",
    "year_six": '{:,.2%}'.format(year_six_dep_per_gp),
    "year_seven": '{:,.2%}'.format(year_seven_dep_per_gp),
    "year_eight": '{:,.2%}'.format(year_eight_dep_per_gp),
    "year_nine":  '{:,.2%}'.format(year_nine_dep_per_gp),
    "year_ten": '{:,.2%}'.format(year_ten_dep_per_gp)
    }


    requestData = requests.get(url).json()
    requestData.append(income_statement_data['data'][3]) # Gross profit
    requestData.append(income_statement_data['data'][sales_gen_and_admin_loc]) #Sales General and administrative
    requestData.append(income_statement_data['data'][operating_income_loc]) #Operating Income   
    requestData.append(income_statement_data['data'][interest_expense_loc]) #Interest Expense
    if research_and_dev_loc != 999:
        requestData.append(income_statement_data['data'][research_and_dev_loc])
    if cash_and_equivalents_loc != 999:
        requestData.append(balance_sheet_data['data'][cash_and_equivalents_loc])
    if property_plant_and_equi_loc != 999:
        requestData.append(balance_sheet_data['data'][property_plant_and_equi_loc])
    if net_income_loc != 999:
        requestData.append(income_statement_data['data'][net_income_loc])


    if common_stock_repurchased_loc != 999:
        requestData.append(cash_flow_data['data'][common_stock_repurchased_loc])
        
    requestData.append(cash_flow_data['data'][3]) # Depreciation & amortization
    requestData.append(balance_sheet_data['data'][long_term_debt_loc])
    requestData.append(balance_sheet_data['data'][short_term_debt_loc])
    requestData.append(depreciation_as_percent_of_gross_profit)
    requestData.append(sga_as_percent_of_gross_profit)
    context = {'data': requestData}
  
    pretty_json = json.dumps(context)
    json_data = json.loads(pretty_json)

   

    sum_gross_margin = float(json_data['data'][1]['year_one']) + float(json_data['data'][1]['year_two']) + float(json_data['data'][1]['year_three'])+ float(json_data['data'][1]['year_four']) + float(json_data['data'][1]['year_five'])+ float(json_data['data'][1]['year_six'])  + float(json_data['data'][1]['year_seven'])+ float(json_data['data'][1]['year_eight']) + float(json_data['data'][1]['year_nine'])+ float(json_data['data'][1]['year_ten']) 
    three_year_gross_margin = float(json_data['data'][1]['year_eight']) + float(json_data['data'][1]['year_nine'])+ float(json_data['data'][1]['year_ten']) / 3
    three_year_average = three_year_gross_margin / 3
    ave_gross_margin = sum_gross_margin / 10
    
    first_three_years = (float(json_data['data'][1]['year_one']) + float(json_data['data'][1]['year_two']) + float(json_data['data'][1]['year_three']))/3
    second_three_years = (float(json_data['data'][1]['year_two']) + float(json_data['data'][1]['year_three']) + float(json_data['data'][1]['year_four'])) /3
    third_three_years = (float(json_data['data'][1]['year_three']) + float(json_data['data'][1]['year_four']) + float(json_data['data'][1]['year_five']))  /3
    fourth_three_years = (float(json_data['data'][1]['year_four']) + float(json_data['data'][1]['year_five']) + float(json_data['data'][1]['year_six'])) /3
    fifth_three_years = (float(json_data['data'][1]['year_five']) + float(json_data['data'][1]['year_six']) + float(json_data['data'][1]['year_seven'])) /3
    sixth_three_years = (float(json_data['data'][1]['year_six']) + float(json_data['data'][1]['year_seven']) + float(json_data['data'][1]['year_eight'])) /3
    seventh_three_years = (float(json_data['data'][1]['year_seven']) + float(json_data['data'][1]['year_eight']) + float(json_data['data'][1]['year_nine']))  /3
    eight_three_years = (float(json_data['data'][1]['year_eight']) + float(json_data['data'][1]['year_nine']) + float(json_data['data'][1]['year_ttm']))  /3
   

    #FOR BENCHMARK RATING
    first_computation = 100 - ave_gross_margin
    second_computation = first_computation / 20
    gross_margin_rating_score = (ave_gross_margin/10) + (second_computation * 0.8)
    gross_margin_rating_score = round(gross_margin_rating_score,2)
    gross_margin_rating = ""
    if gross_margin_rating_score >= 8.0:
        gross_margin_rating = "EXCELLENT"
    elif gross_margin_rating_score >= 7.9 and gross_margin_rating_score >= 6.5:
        gross_margin_rating = "GOOD"
    elif gross_margin_rating_score <= 6.5 and gross_margin_rating_score >= 4.0:
        gross_margin_rating = "OK"
    elif gross_margin_rating_score <= 4.0:
        gross_margin_rating="NOT GREAT"


#     39.39 = 39.39
# 100-39.39 = 60.61
# 60.61/20 = 3.03

# (39.39/10)+(3.03*0.8) = 6.36 


    # for value in gross_margins:
    #     print(value)
    #     
    #     if value.isdigit():
    #         totalvalue += 1
    #         newstr = value[-2:]
    #         this_year = this_year - 1
    #         dateTitle = str(this_year) + newstr
    #         dateTitles.append(dateTitle)
    #         gross_margin = json_data['data'][1][dateTitle] 
    #         sum_gross_margin = sum_gross_margin + float(gross_margin) 
    #         ave_gross_margin = sum_gross_margin / totalvalue
            
           



            
            # convertedValue = Decimal(value)
            # print(convertedValue)
            # totalvalue  = totalvalue + value
    return render(request, 'core/main.html', {'data': json_data , 'ten_year_ave_gm': ave_gross_margin, 'three_year_ave_gm': three_year_average, 
                                                'first_three_years' : first_three_years,
                                                'second_three_years' :second_three_years ,
                                                'third_three_years': third_three_years,
                                                'fourth_three_years':fourth_three_years ,
                                                'fifth_three_years' :fifth_three_years ,
                                                'sixth_three_years':sixth_three_years ,
                                                'seventh_three_years': seventh_three_years ,
                                                'eight_three_years' : eight_three_years, 
                                                'gross_margin_rating': gross_margin_rating, 
                                                'gross_margin_rating_score': gross_margin_rating_score,
                                                'depreciation_rating': depreciation_rating,
                                                'dep_rating_score': dep_rating_score,
                                                'sga_rating': sga_rating,
                                                'sga_rating_score': sga_rating_score,
                                                'interest_expense_rating': interest_expense_rating,
                                                'interest_expense_rating_score': interest_expense_rating_score,
                                                'research_and_dev_rating_score': research_and_dev_rating_score,
                                                'research_and_dev_rating': research_and_dev_rating, 
                                                'cash_and_cash_equivalents_rating_score': cash_and_cash_equivalents_rating_score,
                                                'cash_and_cash_equivalents_rating':cash_and_cash_equivalents_rating, 
                                                'short_term_debt_rating_score': short_term_debt_rating_score,
                                                'short_term_debt_rating': short_term_debt_rating,
                                                'long_term_debt_rating_score': long_term_debt_rating_score,
                                                'long_term_debt_rating': long_term_debt_rating,
                                                'property_plant_and_equi_rating_score': property_plant_and_equi_rating_score,
                                                'property_plant_and_equi_rating': property_plant_and_equi_rating})
     
