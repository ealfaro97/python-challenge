import csv

with open('budget_data.csv') as budget_data:
    budget_csv = csv.DictReader(budget_data)
    date_lst = []
    p_l_lst = []
    num_rows = 0
    net_sum = 0
    first_row = True
    delta_PL_total = 0
    great_inc = 0
    great_inc_month = ''
    great_dec = 0
    great_dec_month = ''
    for row in budget_csv:

        date_lst.append(row['Date'])
        p_l_lst.append(row['Profit/Losses'])
        num_rows += 1

        # 2. Net total amount of Profit/Losses = net_sum
        net_sum += int(row['Profit/Losses'])

        # 3. Average change in P/L
        if first_row == True:
            prev_PL = int(row['Profit/Losses'])
            first_row = False
        elif first_row == False:
            delta_PL = int(row['Profit/Losses']) - prev_PL
            delta_PL_total += delta_PL
            prev_PL = int(row['Profit/Losses'])
            # 4. Greatest Increase
            if delta_PL > great_inc:
                great_inc = delta_PL
                great_inc_month = row['Date']

            # 5. Greatest Decreases
            if delta_PL < great_dec:
                great_dec = delta_PL
                great_dec_month = row['Date']

    # 1. Total Number of Months
    total_months = num_rows

    # 3. Average change in P/L
    average_delta_PL = delta_PL_total / (num_rows - 1)
    average_delta_PL = round(average_delta_PL, 2)

    print(f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_sum}
Average  Change: ${average_delta_PL}
Greatest Increase in Profits: {great_inc_month} (${great_inc})
Greatest Decrease in Profits: {great_dec_month} (${great_dec})""")

    # Export .txt File with results
    with open('PyBank_analysis.txt', 'w') as analysis_txt:
        analysis_txt.write("Financial Analysis\n")
        analysis_txt.write("----------------------\n")
        analysis_txt.write("Total months: " + str(total_months) + "\n")
        analysis_txt.write(("Total: $" + str(net_sum) + "\n"))
        analysis_txt.write("Average Change: $" +
                           str(average_delta_PL) + "\n")
        analysis_txt.write("Greatest Increase in Profits: " +
                           str(great_inc_month) + " " + "($" + str(great_inc) + ")" + "\n")
        analysis_txt.write("Greatest Decrease in Profits: " +
                           str(great_dec_month) + " " + "($" + str(great_dec) + ")" + "\n")
