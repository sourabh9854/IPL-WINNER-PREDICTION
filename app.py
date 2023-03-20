import streamlit as st
import pickle
import pandas as pd
st.title('IPL WIN PREDICTOR')
ipl = pickle.load(open('ipl.pkl','rb'))


Venue = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

teams = ['Sunrisers Hyderabad', 'Rajasthan Royals', 'Chennai Super Kings',
       'Royal Challengers Bangalore', 'Mumbai Indians',
       'Kolkata Knight Riders', 'Punjab Kings', 'Delhi Capitals',
       'Lucknow Super Giants', 'Gujarat Titans']
col1, col2 = st.columns(2)
with col1:
    BattingTeam = st.selectbox('BattingTeam',sorted(teams))
with col2:
    BowlingTeam = st.selectbox('BowlingTeam',sorted(teams))

selected_city = st.selectbox('Select Venue',sorted(Venue))
Target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = Target - score
    ball_left = 120 - (overs*6)
    wickets_remaining = 10 - wickets
    curr_RR = score/overs
    Req_RR  = (runs_left*6)/ball_left

    input_df = pd.DataFrame({'BattingTeam':[BattingTeam],'BowlingTeam':[BowlingTeam],'City':[selected_city],'runs_left':[runs_left],'ball_left':[ball_left],'wickets_remaining':[wickets_remaining],'Target':[Target],'curr_RR':[curr_RR],'Req_RR':[Req_RR]})
    result = ipl.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(BattingTeam + "- " + str(round(win*100)) + "%")
    st.header(BowlingTeam + "- " + str(round(loss*100)) + "%")



