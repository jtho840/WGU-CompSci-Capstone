# Initialize lists to hold books that the customer has previously purchased
import csv


def get_customer_preferences(customer_id):
    customer_history = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    row_count = 1
    file_path = "csvData/purchaseHistories/" + str(customer_id) + ".csv"
    with open(file_path) as csvfile:
        read_csv = csv.reader(csvfile)
        for row in read_csv:
            customer_history[row_count-1] = row[1]
            # print(customer_history[row_count])
            row_count = row_count + 1
            if row_count >= 21:  # limits the customer history to the 20 most recently purchased books
                break
    return customer_history


def get_customer_similarity(customer_history):
    # Nested lists hold the tags for all the books in the customer's purchase history.
    # customer_similarity[n][0] is the book ID
    # customer_similarity[n][1] is the book author
    # customer_similarity[n][2] is the book genre
    # customer_similarity[n][3...9] are the book tags

    customer_similarity = [[customer_history[0], "", "", "", "", "", "", "", "", ""],
                           [customer_history[1], "", "", "", "", "", "", "", "", ""],
                           [customer_history[2], "", "", "", "", "", "", "", "", ""],
                           [customer_history[3], "", "", "", "", "", "", "", "", ""],
                           [customer_history[4], "", "", "", "", "", "", "", "", ""],
                           [customer_history[5], "", "", "", "", "", "", "", "", ""],
                           [customer_history[6], "", "", "", "", "", "", "", "", ""],
                           [customer_history[7], "", "", "", "", "", "", "", "", ""],
                           [customer_history[8], "", "", "", "", "", "", "", "", ""],
                           [customer_history[9], "", "", "", "", "", "", "", "", ""],
                           [customer_history[10], "", "", "", "", "", "", "", "", ""],
                           [customer_history[11], "", "", "", "", "", "", "", "", ""],
                           [customer_history[12], "", "", "", "", "", "", "", "", ""],
                           [customer_history[13], "", "", "", "", "", "", "", "", ""],
                           [customer_history[14], "", "", "", "", "", "", "", "", ""],
                           [customer_history[15], "", "", "", "", "", "", "", "", ""],
                           [customer_history[16], "", "", "", "", "", "", "", "", ""],
                           [customer_history[17], "", "", "", "", "", "", "", "", ""],
                           [customer_history[18], "", "", "", "", "", "", "", "", ""],
                           [customer_history[19], "", "", "", "", "", "", "", "", ""]]

    file_path = "csvData/books.csv"
    with open(file_path) as csvfile:
        read_csv = csv.reader(csvfile)
        counter = 0
        while counter <= 19:
            csvfile.seek(0)
            for row in read_csv:
                if str(row[0]) == customer_history[counter]:
                    customer_similarity[counter][1] = row[2]
                    customer_similarity[counter][2] = row[4]
                    customer_similarity[counter][3] = row[8]
                    customer_similarity[counter][4] = row[9]
                    customer_similarity[counter][5] = row[10]
                    customer_similarity[counter][6] = row[11]
                    customer_similarity[counter][7] = row[12]
                    customer_similarity[counter][8] = row[13]
                    customer_similarity[counter][9] = row[14]
                    break
            counter += 1
    print("Data")

    return customer_similarity
