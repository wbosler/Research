import streamlit as st

st.header("**Econometric and Machine Learning Research**")
st.write("*By Will Bosler*")
st.write("Browse a selection of group research tasks I have completed by expanding the below sections.")
st.write("")
st.write("")

#Ride share Research
Ride_Share = st.beta_expander("Ridesharing Platforms - A framework for understanding driver and trip behaviour")
with Ride_Share:
    st.write("")
    st.write("**Overview**")
    st.write("This paper leverages data published by the Government of Chicago to provide insights into the factors influencing how \
    many trips a rideshare driver completes per month and how likely a driver is to work for multiple rideshare companies. \
    It also provides analysis exploring what factors influence the duration of a trip and methods for duration prediction.")
    st.write("")
    st.write("**Link to the research**")
    st.write("[Rideshare Analysis](https://drive.google.com/file/d/1PD_rChDEF6WwarQ-eUn2gWbrTTcISCVX/view?usp=sharing)")
    st.write("")
    st.write("**Modelling Techniques**")
    st.write("Poisson Regression, Negative Binomial Regression, Logistic Regression, Probit Regression, Exponential Regression, \
    Weibull Regression, Markov Chain Monte Carlo, Random Walk Metropolis Hastings Algorithm, Natural Gradient Descent, Survival \
    Analysis, Bayesian Analysis")
    st.write("")
    st.write("**Coding Language**")
    st.write("Matlab, Python, R")
    st.write("Analysis was conducted without the use of pre built packages.")
st.write("")

#Mutual Fund Performance
Mutual_Fund = st.beta_expander("How do Fund Manager's personal characteristics impact financial performance? ")
with Mutual_Fund:
    st.write("")
    st.write("**Overview**")
    st.write("This paper explores whether personal characteristics of a Fund Manager such as education, experience and gender \
    impact the performance of the mutual funds they manage.")
    st.write("**Link to the research**")
    st.write("[Fund performance and manager characteristics](https://drive.google.com/file/d/1BKlaQFk2OS8z6YEaK1mX8fxEE6wV29nM/view?usp=sharing)")
    st.write("**Modelling Techniques**")
    st.write("Pooled OLS, Random Effects, Fixed Effects, Hybrid Model, Panel Data Analysis")
    st.write("**Coding Language**")
    st.write("Stata, Python, Matlab")
st.write("")

#Airbnb listing prices
Airbnb = st.beta_expander("Airbnb - What price should you list your property at?")
with Airbnb:
    st.write("")
    st.write("**Overview**")
    st.write("This paper uses a kaggle dataset containing information on Airbnb listings in Melbourne to train machine learning models \
    that can predict listing prices.")
    st.write("**Link to the research**")
    st.write("[Airbnb Price Forecast](https://drive.google.com/file/d/1xxqv_dXdhzZjMUCS366RNu8gJ04KF0uN/view?usp=sharing)")
    st.write("**Modelling Techniques**")
    st.write("Gradient Boosting Machines - LightGBM, XGBoost, Random Forest, KNN, LASSO, Ridge, Model Stacking, Elastic Net")
    st.write("**Coding Language**")
    st.write("Python")
st.write("")

#Commodity price forecasts
Com = st.beta_expander("Commodity Prices - Simple forecasting approaches")
with Com:
    st.write("")
    st.write("**Overview**")
    st.write("This paper builds ARIMA forecasts for Maize and compares them to a random walk benchmark.")
    st.write("**Link to the research**")
    st.write("[Commodity Forecast](https://drive.google.com/file/d/1Mo3jtoC3KlhstLoEdRLt0cMTyWnOzDqb/view?usp=sharing)")
    st.write("**Modelling Techniques**")
    st.write("Random Walk, ARIMA")
    st.write("**Coding Language**")
    st.write("R")
st.write("")
#Foreign aid
Aid = st.beta_expander("Foreign Aid - Adressing a simultaneity problem in existing literature")
with Aid:
    st.write("")
    st.write("**Overview**")
    st.write("This paper provides a critical review of Bruckner's 2013 paper that seeks to identify the causal effect of foreign \
    aid on aid-recepient country economic growth. This paper includes a methodology review, additional descriptive analysis and \
    replication of results.")
    st.write("Bruckners paper can be found at this [link](https://www.researchgate.net/publication/227682873_On_the_Simultaneity_Problem_in_the_Aid_and_Growth_Debate)")
    st.write("**Link to the research**")
    st.write("[Foreign Aid and Simultaneity](https://drive.google.com/file/d/1xBE_YcktAJIx5TTGZnG1amosG_HDYrZT/view?usp=sharing)")
    st.write("**Modelling Techniques**")
    st.write("Two Stage Least Squares")
    st.write("**Coding Language**")
    st.write("R, Python")
