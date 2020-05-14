import configparser
config = configparser.ConfigParser()
config['WalkerTracker']={}
config['WalkerTracker']['token']='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
config['WalkerTracker']['api_root'] = 'https:////api.walkertracker.com//api//2.1//'
config['WalkerTracker']['GetCompetitorsStats'] = 'admin_competition_data'
config['WalkerTracker']['competition_id'] = '55966'
config['WalkerTracer']['cookie'] = 'PROXYSESSID=https:////10.100.101.95:443'
with open('WalkerTracker.ini','w') as configfile:
    config.write(configfile)