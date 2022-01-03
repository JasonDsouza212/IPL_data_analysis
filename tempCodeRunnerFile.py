batsmen = matches[['id','season']].merge(delivery, left_on = 'id', right_on = 'match_id', how = 'left').drop('id', axis = 1)
# #merging the matches and delivery dataframe by referencing the id and match_id columns respectively
# season=batsmen.groupby(['season'])['total_runs'].sum()
# season.plot()
# mlt.show()