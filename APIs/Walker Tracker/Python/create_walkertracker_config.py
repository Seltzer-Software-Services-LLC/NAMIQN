import configparser
config = configparser.ConfigParser()
config['WalkerTracker']={}
config['WalkerTracker']['token']='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
config['WalkerTracker']['api_root'] = 'https:////api.walkertracker.com//api//2.1//'
config['WalkerTracker']['get_competitors_stats'] = 'admin_competition_data'
config['WalkerTracker']['competition_id'] = '55966'
config['WalkerTracker']['cookie'] = 'PROXYSESSID=https:////10.100.101.95:443'
with open('WalkerTracker.ini','w') as configfile:
    config.write(configfile)