# Joshua Thompson - Student ID #: 000992212 - Contact: jtho840@wgu.edu
# Performance Assessment for C950 - Data Structures and Algorithms II
# Program Details can be found in README.md

import csv

from bookProfile import get_similarity_scores
from customerProfile import get_customer_preferences, get_customer_similarity


class Main:
    print("------------------------------------------------------------ \n"
          "       Timeless Pages Recommendation Generation System       \n"
          "------------------------------------------------------------ \n")
    userInput = input("To get recommendations for a customer, enter the Customer ID number:\n"
                      "To close the program, type 'Exit'. \n"
                      "(For purposes of this demo, enter any number from 150 to 159.)\n"
                      ">>>")
    flag = False
    customerName = ""
    while userInput is not None:
        if userInput == 'Exit':
            print("Program Complete")
            quit()
        else:
            try:
                with open("csvData/customer.csv") as csvfile:
                    read_csv = csv.reader(csvfile)
                    for row in read_csv:
                        if int(row[0]) == int(userInput):
                            customerName = row[1] + " " + row[2]
                            flag = True
                            break
                    if flag:
                        print("\nCustomer Name: " + customerName + "\n")
                        get_similarity_scores(get_customer_similarity(get_customer_preferences(userInput)))
                        userInput = input("To get recommendations for a different customer, enter the Customer ID number:\n"
                                          "To close the program, type 'Exit'. \n"
                                          "(For purposes of this demo, enter any number from 150 to 159.)\n"
                                          ">>>")
                        flag = False
                    else:
                        print("Customer Not Found, please try again! \n")
                        userInput = input("To get recommendations for a customer, enter the Customer ID number:\n"
                                          "To close the program, type 'Exit'. \n"
                                          "(For purposes of this demo, enter any number from 150 to 159.)\n"
                                          ">>>")

            except ValueError:
                print("Invalid Entry, please try again! \n")
                userInput = input("To get recommendations for a customer, enter the Customer ID number:\n"
                                  "To close the program, type 'Exit'. \n"
                                  "(For purposes of this demo, enter any number from 150 to 159.)\n"
                                  ">>>")
