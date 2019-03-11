ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]

tally = {}

def tally_ballots(ballots, tally):
    for ballot in ballots:
        gname, sname, bname = ballot['gold'], ballot['silver'], ballot['bronze']
        # add gold votes
        tally[gname] = tally.get(gname, 0) + 3
        # add silver votes
        tally[sname] = tally.get(sname, 0) + 2
        # add bronze votes (longer way to do it)
        if bname in tally:
            tally[bname] += 1
        else:
            tally[bname] = 1
# #
# if __name__ == '__main__':
#     def pr_fn(s):
#         print(f"Printer function says '{s}'")
#     def pr(fn, s):
#         fn(s)
#     pr(pr_fn, 'what is this madness')
# else:
    tally_ballots(ballots, tally)
    print(tally)
