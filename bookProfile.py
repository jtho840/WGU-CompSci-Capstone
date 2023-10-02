# Joshua Thompson Student ID #: 000992212

# Uses the customer profile created in customerProfile.py to create similarity scores for books in inventory

import csv


def get_similarity_scores(customer_similarity):
    recommendation_scores = []
    top_three_books = ["", "", ""]
    top_three_scores = ["", "", ""]

    # As the similarity scores are created, the top three scores will be tracked in these lists.
    # Once the scores are completed, the top three will be returned to the user.

    with open("csvData/books.csv") as csvfile:
        read_csv = csv.reader(csvfile)
        for row in read_csv:
            score = 0
            matrix_row = 0
            while matrix_row <= 19:
                matrix_column = 0
                while matrix_column <= 9:
                    if matrix_column == 1:
                        #  Check Author, adds 10 points if match
                        if customer_similarity[matrix_row][matrix_column] == row[2]:
                            score += 10
                    elif matrix_column == 2:
                        #  Check Genre, adds 10 points if match
                        if customer_similarity[matrix_row][matrix_column] == row[4]:
                            score += 10
                    else:
                        #  Checks each of the tags for its presence in the customer profile, adds 4 point for each match
                        i = 8
                        while i <= 14:
                            if customer_similarity[matrix_row][matrix_column] == row[i]:
                                score += 4
                            i += 1

                    matrix_column += 1
                matrix_row += 1
            recommendation_scores.append(str("{:02d}".format(score)) + ":" + row[0])

    recommendation_scores.sort(reverse=True)

    counter = 0
    while counter <= 2:
        string = recommendation_scores[counter]
        top_three_books[counter] = string[3:]
        top_three_scores[counter] = string[:2]
        with open("csvData/books.csv") as csvfile:
            read_csv = csv.reader(csvfile)
            for row in read_csv:
                if str(row[0]) == top_three_books[counter]:
                    print("Recommendation " + str(counter + 1) + ":")
                    print("'" + row[1]+"'")
                    print("By: " + row[2] + "")
                    print("Similarity Score: " + top_three_scores[counter] + "\n")
                    break
            counter += 1

    return recommendation_scores
