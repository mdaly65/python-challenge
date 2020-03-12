import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path, "03-Python_homework_assignment_PyBank_Resources_budget_data.csv")

output_file = os.path.join(dir_path, "HW_Output.csv")

count = 0 

List1 = [1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1]        

for ele in range(0, len(List1)):
    count = count + List1[ele]

print("The number of dates is: ", count)


# Net Total Amount of Profit/Losses ober the Entire Period
total = 0

List2 = [867884, 984655, 322013, -69417, 310503, 522857, 1033096, 604885, -216386, 477532, 893810, -80353, 779806, -335203, 697845, 
793163, 485070, 584122, 62729, 668179, 899906, 834719, 132003, 309978, -755566, 1170593, 252788, 1151518, 817256, 570757, 506702, 
-1022534, 475062, 779976, 144175, 542494, 359333, 321469, 67780, 471435, 565603, 872480, 789480, 999942, -1196225, 268997, -687986, 
1150461, 6824580 ,617856, 824098, 581943, 132864, 448062, 689161, 800701, 1166643, 947333, 578668, 988505, 1139715, 1029471, 687533,
-524626, 158620, 87795, 423389, 840723, 568529, 332067, 989499, 778237, 650000, -1100387, -174946, 757143, 445709, 712961, -1163797,
569899, 768450, 102685, 795914, 60988, 138230, 671099]


for ele in range(0, len(List2)):
    total = total + List2[ele]

print("Sum of all Profit/Losses is :", total)

# Average of Changes in Profit/Loss over Entire Period

month_over_month_change = [List2[i + 1] - List2[i] for i in range(len(List2)-1)]
print ("The computed successive difference list is : " + str(month_over_month_change))

mean_mom_change = [month_over_month_change]
avg = sum(mean_mom_change)/len(mean_mom_change)
print("The Average MoM Profit/Losses Change is : ", round(avg, 2))

g_increase_profits = [month_over_month_change]
print("Greatest Increase in Profits is : ", max(g_increase_profits))

g_decrease_profits = [month_over_month_change]
print("Greatest Decrease in Profits is :", min([n for n in month_over_month_change if n>0]))