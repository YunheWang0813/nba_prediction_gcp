from locust import HttpLocust, TaskSet, between
import random

'''
def index(l):
    l.client.get("/")
    
   
def fixed_play(l):
    l.client.get("/result/Brooklyn%20Nets/Chicago%20Bulls")
'''    
def random_play(l):
    nba_teams = ['Atlanta Hawks', 'Boston Celtics' , 'Brooklyn Nets', 'Charlotte Bobcats', 'Chicago Bulls', 'Cleveland Cavaliers', 'Dallas Mavericks', 
    'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'LA Clippers', 'LA Lakers', 'Memphis Grizzlies',
    'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Hornets', 'New York Knicks', 'Oklahoma City Thunder', 'Orlando Magic', 
    'Philadelphia Sixers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs' , 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']
    nba_teams_random = random.choices(nba_teams, k = 2)
    l.client.get("/result/" + nba_teams_random[0] + "/" + nba_teams_random[1])
   
class UserBehavior(TaskSet):
    #tasks = {index: 1}
    #tasks = {fixed_play: 1}
    tasks = {random_play: 1}
    
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(2.0, 5.0)
    
    