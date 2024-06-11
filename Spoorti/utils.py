

member_count = {
    "Cricket Male":15,
    "Cricket Female":15,
    "Football male":12,
    "Football Female":12,
    "Basketball Male":7,
    "Basketball Female":7,
    "Badminton Single Male":1,
    "Badminton Single Female":1,
    "Badminton Double Male":2,
    "Badminton Double Female":2,
    "Badminton Mixed":2,
    "Volleyball Male":8,
    "Volleyball Female":8,
    "Kabaddi Male":6,
    "Kabaddi Female":6,
    "TT Single Male":1,
    "TT Single Female":1,
    "TT Double Male":2,
    "TT Double Female":2,
    "TT Mixed":2,
    "TugOfWar Male":8,
    "TugOfWar Female":8,
    "Chess":1
}

team_amount = {
    "Cricket Male":5000,
    "Cricket Female":3100,
    "Football male":2000,
    "Football Female":1500,
    "Basketball Male":2000,
    "Basketball Female":1500,
    "Badminton Single Male":500,
    "Badminton Single Female":500,
    "Badminton Double Male":800,
    "Badminton Double Female":800,
    "Badminton Mixed":800,
    "Volleyball Male":2000,
    "Volleyball Female":1500,
    "Kabaddi Male":2000,
    "Kabaddi Female":1500,
    "TT Single Male":500,
    "TT Single Female":500,
    "TT Double Male":800,
    "TT Double Female":800,
    "TT Mixed":800,
    "TugOfWar Male":800,
    "TugOfWar Female":800,
    "Chess":200
}

def get_member(game):
    member=[]
    meb=member_count[game]     #for fetching members from utils.py
    for i in range(1,meb):
        member.append(i+1)
    return member

def get_amount(game):
    
    return team_amount[game]
