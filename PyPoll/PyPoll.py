import csv

with open('election_data.csv') as election_data:
    election_csv = csv.DictReader(election_data)
    total_votes = 0
    candidates = {}

    for row in election_csv:
        total_votes += 1
        row_candidate = row['Candidate']
        try:
            candidates[row_candidate] += 1
        except KeyError:
            candidates[row_candidate] = 1

    candidates_lst = []
    percent_lst = []
    votes_lst = []
    for key, value in candidates.items():
        candidates_lst.append(key)
        votes_lst.append(value)
        percent_lst.append(round((value / total_votes)*100, 3))

    winner = ''
    max_votes = 0
    count = 0
    count_winner = 0
    for votes in votes_lst:
        if votes > max_votes:
            max_votes = votes
            count_winner = count
        count += 1

    winner = candidates_lst[count_winner]


    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    for i in range(0,count):
        print(f'{candidates_lst[i]}: {percent_lst[i]}% ({votes_lst[i]})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")

    with open('PyPoll_analysis.txt', 'w') as pypoll_analysis:
        pypoll_analysis.write("Election Results\n")
        pypoll_analysis.write("-------------------------\n")
        pypoll_analysis.write("Total Votes: " + str(total_votes)+ "\n")
        pypoll_analysis.write("-------------------------\n")
        pypoll_analysis.write("")
        for i in range(0,count):
            pypoll_analysis.write(str(candidates_lst[i]) + ': ' + str(percent_lst[i]) + '% (' + str(votes_lst[i]) + ') \n')
        pypoll_analysis.write("-------------------------\n")
        pypoll_analysis.write('Winner: ' + (winner) + "\n")
        pypoll_analysis.write("-------------------------")
