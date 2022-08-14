import time
import streamlit
import streamlit as st
import requests
from streamlit_lottie import st_lottie,st_lottie_spinner
from streamlit_option_menu import option_menu
import pickle
import pandas as pd

st.set_page_config(page_title="Applied Machine learning in Oil and Gas Industry", page_icon="🛢️")
def lottie_url(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_hello = lottie_url('https://assets8.lottiefiles.com/packages/lf20_z6h8mj7v.json')
lottie_pipe= lottie_url('https://assets7.lottiefiles.com/private_files/lf30_28ozkmvt.json')
lottie_bbl=lottie_url('https://assets9.lottiefiles.com/packages/lf20_pqxofxw9.json')
lottie_wait = lottie_url('https://assets2.lottiefiles.com/packages/lf20_p8bfn5to.json')

fm = pickle.load(open('finalized_model.pkl','rb'))

#models for oil rate
oil_all = pickle.load(open('oil_all.pkl','rb'))
oil_c = pickle.load(open('oil_c.pkl','rb'))
oil_chock = pickle.load(open('oil_chock.pkl','rb'))
oil_flow = pickle.load(open('oil_flow.pkl','rb'))
oil_pt = pickle.load(open('oil_pt.pkl','rb'))
oil_vlp = pickle.load(open('oil_vlp.pkl','rb'))
oil_vlp_chock = pickle.load(open('oil_vlp_chock.pkl','rb'))

#models for gas rate
gas_all = pickle.load(open('gas_all.pkl','rb'))
gas_c = pickle.load(open('gas_c.pkl','rb'))
gas_chock = pickle.load(open('gas_chock.pkl','rb'))
gas_flow = pickle.load(open('gas_flow.pkl','rb'))
gas_pt = pickle.load(open('gas_pt.pkl','rb'))
gas_vlp = pickle.load(open('gas_vlp.pkl','rb'))
gas_vlp_chock = pickle.load(open('gas_vlp_chock.pkl','rb'))

#models for water rate
water_all = pickle.load(open('water_all.pkl','rb'))
water_c = pickle.load(open('water_c.pkl','rb'))
water_chock = pickle.load(open('water_chock.pkl','rb'))
water_flow = pickle.load(open('water_flow.pkl','rb'))
water_pt = pickle.load(open('water_pt.pkl','rb'))
water_vlp = pickle.load(open('water_vlp.pkl','rb'))
water_vlp_chock = pickle.load(open('water_vlp_chock.pkl','rb'))

#PVT model
bbl_pt = pickle.load(open("bbl_pt.pkl",'rb'))

selected = option_menu(
    menu_title="Application of Machine learning in Oil and Gas Industry",
    options=['Home','Critical oil Rate Prediction','Predicting Well rates','PVT Properties'],
    icons=['house','bezier2','activity','align-center'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
)


if selected=='Home':
    left,mid,right=st.columns(3)
    with mid:
        with st_lottie_spinner(lottie_wait,key='wait0'):
            with st.spinner("Loading... Please Wait"):
                time.sleep(1)

    st.title("Predictive Maintenance in Oil and Gas industry")
    col1,col2,col3=st.columns(3)
    with col1:
        st_lottie(lottie_hello, key='hello', height=150, width=150)
    with col2:
        st_lottie(lottie_pipe, key='pipe', height=150, width=150)
    with col3:
        st_lottie(lottie_bbl, key='bbl', height=150, width=150)

    st.markdown("**What is Predictive Maintenance in the Oil and Gas Industry?**")
    st.markdown("---")
    st.markdown("The oil and gas industry uses old machinery — at least 15 years old — for its upstream, midstream, and downstream operations. So, periodic inspection and maintenance activities are essential to keep them operational. However, such reactive maintenance doesn’t offer any guarantees against unplanned downtime.")
    st.markdown("Using predictive maintenance, oil and gas companies can rely on IIoT-enabled technology, such as sensor data, and leverage predictive analytics for real-time equipment inspection. This helps predict maintenance requirements, which cuts maintenance costs and reduces unplanned equipment failures.")
    st.image("https://images.unsplash.com/photo-1544860987-03cd01a2c6da?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80")
    st.markdown("**Why is Predictive Maintenance so Important in the Oil and Gas Industry?**")
    st.markdown("---")
    st.markdown("An average oil and gas company goes through at least 27 days of unplanned downtime each year, costing 38 million dollers. Even if the downtime lasts for just 3.65 days, the resulting losses can be as high as $5 million.")
    st.markdown("That’s why predictive maintenance is so important. Sophisticated predictive maintenance technologies use artificial intelligence, machine learning, and advanced analytics to spot issues and alert the relevant technicians, preventing potential equipment failure and safety risks. According to a McKinsey report, an offshore oil and gas company used a predictive maintenance solution to reduce downtime by 20%, leading to a production increase of more than 500,000 oil barrels annually.")

    st.markdown("**How Does Predictive Maintenance Work?**")
    st.markdown("---")
    st.markdown("Predictive maintenance technologies aggregate vast amounts of real-time operational data from sensors regarding equipment thermography, lubrication, circuitry, and more with data from other sources — ERP or MES — to spot patterns. IoT and AI facilitate such real-time data collection and monitoring automatically. Using machine learning algorithms and analytics, the software tracks the wear and tear of oil and gas equipment to predict potential failures and recommends precise maintenance tasks to fix anomalies, increase production, and prevent costly breakdowns.")
    st.markdown("For instance, if a machine crosses its pressure and temperature threshold, the system triggers an alarm. More sophisticated systems analyze sensor data to spot the signatures of known failure modes, according to McKinsey.")


    st.write("App created by Ronak Pandya.")
if selected=="Critical oil Rate Prediction":
    left, mid, right = st.columns(3)
    with mid:
        with st_lottie_spinner(lottie_wait, key='wait1'):
            with st.spinner("Loading... Please Wait"):
                time.sleep(1)
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        frac_perm=st.number_input("Fracture Permeability (md)",min_value=100,max_value=2000,key="1")
    with col2:
        mat_perm = st.number_input("Matrix Permeability (md)",min_value=0.1, max_value=50.0,key='2')
    with col3:
        mobility = st.number_input("Mobility ratio",min_value=1, max_value=5, key='3')
    with col4:
        frac_spac = st.number_input("Fracture Spacing (in)",min_value=0.1, max_value=18.0, key='4')
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        drain_r = st.number_input("drainage radius (in)", min_value=400, max_value=2000, key='5')
    with col2:
        ani_r = st.number_input("Anisotropy ratio",min_value=1,max_value=10,key='6')
    with col3:
        pen_r = st.number_input("Penetration ratio", min_value=0.35, max_value=0.8, key='7')
    predict = st.button("Predict Critical oil rate")
    Kf = frac_perm  # Fracture effective permeability
    Km = mat_perm  # Matrix permeability
    M = mobility  # Mobility
    Sp = frac_spac  # Fracture spacing
    re = drain_r  # Drainage radius
    I = ani_r  # Anisotropy ratio
    p = pen_r # Penetration ratio
    A = re / 40 * (I) ** 0.5
    if predict:
        left, mid, right = st.columns(3)
        with mid:
            with st_lottie_spinner(lottie_wait, key='wait2'):
                with st.spinner("Loading... Please Wait"):
                    time.sleep(1)
        val = fm.predict([[A]])[0]
        predict = (0.0783*(10**-4)*(Kf+Km*0.63)*40**2*(1-p**2)*(64-52)/(0.7*M)/1.1)*val
        st.header(f"**Predicted critical oil flow rate is: {int(predict)} BOPD**")
        st.title("Why critical rate is important?")
        st.markdown("---")
        st.markdown ("Water or gas coning can adversely affect oil production in oil reservoirs. In oil reservoirs, a large oil rate can cause upward coning of water or downward coning of gas into the well perforations. Once gas or water is produced, the oil rate decreases and the cost of water and/or gas handling is increased. There is a critical rate below which the cone remains stable and does not break through to the wellbore. In the present work, a simple-to-use approach, which is easier than existing approaches, less complicated with fewer calculations, is formulated to arrive at an appropriate estimation of critical oil rate for bottom water coning in anisotropic and homogeneous formations with the well completed from the top of the formation. This simple-to-use correlation can be of immense practical value for petroleum engineers to have a quick check on estimating the critical oil rate for wide range of conditions without the necessity of any field test trials. In particular, petroleum engineers would find the proposed approach to be user friendly involving transparent calculations with no complex expressions for their calculations.")
        st.image("https://ars.els-cdn.com/content/image/1-s2.0-S0920410512000344-gr1.jpg", caption ="Illustration of the boundary condition for Hoyland et al. (1989) analytical solution.")


if selected == "Predicting Well rates":
    left, mid, right = st.columns(3)
    with mid:
        with st_lottie_spinner(lottie_wait, key='wait3'):
            with st.spinner("Loading... Please Wait"):
                time.sleep(1)
    col1, col2, col3 = st.columns(3)
    with col1:
        bhp = st.number_input("Bottom hole Pressure (psi)",min_value=4075,max_value=5490,key='8')
    with col2:
        whp = st.number_input("Well head Pressure (psi)",min_value=608,max_value=3946,key='9')
    with col3:
        wht = st.number_input("Well head temperature (degree F)",min_value=75,max_value=182,key='10')

    col4,col5,col6=st.columns(3)
    with col4:
        tsep = st.number_input("Separator Temperature (degree F)",min_value=60,max_value=140, key='11')
    with col5:
        psep = st.number_input("Separator Pressure (psi)",min_value=100,max_value=600,key='12')
    with col6:
        ch = st.number_input("Chock size (inch)",min_value=0.25,max_value=2.5,key='13')
    oil = oil_all.predict([[bhp,whp,wht,tsep,psep,ch]])[0]
    gas = gas_all.predict([[bhp,whp,wht,tsep,psep,ch]])[0]
    water = water_all.predict([[bhp,whp,wht,tsep,psep,ch]])[0]
    calculate = st.button("Calculate", key='cal1')
    # if "Result" not in streamlit.session_state:
    #     streamlit.session_state.Result = False
    if calculate:
        left, mid, right = st.columns(3)
        with mid:
            with st_lottie_spinner(lottie_wait, key='wait5'):
                with st.spinner("Loading... Please Wait"):
                    time.sleep(1)
        #streamlit.session_state.Result = True
        data = [["Oil Flow Rate (BOPD)", oil],
                ["Gas Flow Rate (MMSCF)", gas],
                ["Water Flow Rate (BWPD)", water]]
        df = pd.DataFrame(data, columns=['Fluid', 'Flow rate'])
        st.table(df)
        st.write(" ")
        st.markdown("**Increasing Well Awareness with Virtual Sensors**")
        st.markdown("---")
        st.markdown('On many occasions, direct physical measurements are unavailable or inconsistent with process performance due to sensor failure, technology availability, instrument reliability, or economic reasons. In such situations, virtual sensors are convenient replacements of physical sensors that use available data during well-known conditions in instrumented wells to predict other measurements. Many technologies have been developed to estimate rates and pressures from other indirect measurements (e.g.,nvirtual metering or soft sensors).')
        st.markdown("For example, wellhead pressure (WHP) and temperature (WHT) are related to flow line pressure (FLP) for a specific choke diameter; therefore, it is convenient to establish a machine learning model among these four variables so that it can serve as a replacement whenever needed. Since most of the oil and gas wells exhibit a nonstationary process, where the")
        st.image("https://www.researchgate.net/profile/Sardam-Ahmed/publication/339327444/figure/fig1/AS:859902901747712@1582028236146/1-The-diagram-of-process-of-nodal-Analysis-in-petroleum-production-process.jpg", caption="Nodal analysis")
        st.markdown("**Virtual Rate Metering**")
        st.markdown("---")
        st.markdown("Well surveillance is essential for reservoir characterization, managing production potential, and selecting activities to enhance production. Keyto surveillance is to understand well flowing conditions (i.e., flow rates and flowing status). Typically, well rates (i.e., oil, water, and gas) are not directly measured all the time; however, with virtual sensors, it is possible to build and implement continuous well rate estimation (WRE), also known as virtual rate estimators (VRE). Virtual rate metering is one type of a virtual sensor.")
        st.markdown("One class of virtual rate estimators that is very well-known in the oil and gas industry is derived from physics-based nodal analysis models. This rate estimation requires consistent pressure-volume-temperature (PVT) data, fit-for-purpose production well tests, and reliable sensors.In these kinds of models, missing data, biased data, or failing sensors may break the rate estimation, and a new calibration is required. In addition, sensor input uncertainty and rate estimation confidence are commonly overlooked in these approaches")
        st.image("https://images.unsplash.com/photo-1624771002998-4aadfd43e7c4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80",caption="Sucker rod pump")
        st.markdown("Another approach is to focus on data-driven VRE, enabled by machine learning algorithms.The process involves prediction models for generating instantaneous predictions of multiphase flow rates, cumulative production, and other quantities of interest, such as GOR, WCT, using realtime sensor data at the surface, and historical production, and well test data. Data-driven VRE produces encouraging results when measured data is sufficient, including frequent well tests (e.g., 8–12 per year), permanent wellhead, and flowline sensors (pressure, temperature). The availability of downhole sensors is desirable but not required.")            # col1, col2, col3, col4 = st.columns(4)
    # with col1:
    #     well_rates = st.button("Predict well rates", key='well_rate')
    # with col2:
    #     flowline_performace= st.button("Flow line performance", key='flow')
    # with col3:
    #     flow_and_chock = st.button("Flow line and chock performance",key='fnc')
    # with col4:
    #     vlp = st.button("Vertical Lift Performace", key='vlp')
    #
    # col1,col2,col3,col4 =st.columns(4)
    # with col2:
    #     flow_pt = st.button("Flow and separator performace", key='flow_pt')
    # with col1:
    #     vlp_chock = st.button("VLP and chock performance", key='vlp_chock')
    # with col3:
    #     chock = st.button("chock performace", key='chock')
    # st.markdown("---")

    #Well rates using all parameters
    # if "WellRate" not in streamlit.session_state:
    #     streamlit.session_state.WellRate = False
    #
    # if well_rates or streamlit.session_state.WellRate:
    #     streamlit.session_state.WellRate=True
    #     left, mid, right = st.columns(3)
    #     with mid:
    #         with st_lottie_spinner(lottie_wait, key='wait4', height=150, width=150):
    #             with st.spinner("Loading... Please Wait"):
    #                 time.sleep(2)
    #     col1,col2,col3=st.columns(3)
    #     with col1:
    #         bhp = st.number_input("Bottom hole Pressure (psi)",min_value=4075,max_value=5490,key='8')
    #     with col2:
    #         whp = st.number_input("Well head Pressure (psi)",min_value=608,max_value=3946,key='9')
    #     with col3:
    #         wht = st.number_input("Well head temperature (degree F)",min_value=75,max_value=182,key='10')
    #
    #     col4,col5,col6=st.columns(3)
    #     with col4:
    #         tsep = st.number_input("Separator Temperature (degree F)",min_value=60,max_value=140, key='11')
    #     with col5:
    #         psep = st.number_input("Separator Pressure (psi)",min_value=100,max_value=600,key='12')
    #     with col6:
    #         ch = st.number_input("Chock size (inch)",min_value=0.25,max_value=2.5,key='13')
    #     oil = oil_all.predict([[bhp,whp,wht,tsep,psep,ch]])[0]
    #     gas = gas_all.predict([[bhp,whp,wht,tsep,psep,ch]])[0]
    #     water = water_all.predict([[bhp,whp,wht,tsep,psep,ch]])[0]
    #     calculate = st.button("Calculate", key='cal1')
    #     if "Result" not in streamlit.session_state:
    #         streamlit.session_state.Result = False
    #     if calculate or streamlit.session_state.Result:
    #         left, mid, right = st.columns(3)
    #         with mid:
    #             with st_lottie_spinner(lottie_wait, key='wait5'):
    #                 with st.spinner("Loading... Please Wait"):
    #                     time.sleep(1)
    #         streamlit.session_state.Result = True
    #         data = [["Oil Flow Rate (BOPD)", oil],
    #                 ["Gas Flow Rate (MMSCF)", gas],
    #                 ["Water Flow Rate (BWPD)", water]]
    #         df = pd.DataFrame(data, columns=['Fluid', 'Flow rate'])
    #         st.table(df)
    #
    # #Flowline performance
    # if "Flowline" not in streamlit.session_state:
    #     streamlit.session_state.Flowline = False
    #
    # if flowline_performace or streamlit.session_state.Flowline:
    #     left, mid, right = st.columns(3)
    #     with mid:
    #         with st_lottie_spinner(lottie_wait, key='wait6'):
    #             with st.spinner("Loading... Please Wait"):
    #                 time.sleep(1)
    #     streamlit.session_state.Flowline=True
    #     col1,col2=st.columns(2)
    #     with col1:
    #         whp = st.number_input("Well head Pressure (psi)",min_value=608,max_value=3946,key='14')
    #     with col2:
    #         psep = st.number_input("Separator Pressure (psi)",min_value=100,max_value=600,key='15')
    #
    #     oil = oil_flow.predict([[whp,psep]])[0]
    #     gas = gas_flow.predict([[whp,psep]])[0]
    #     water = water_flow.predict([[whp,psep]])[0]
    #     calculate = st.button("Calculate", key='cal2')
    #     if "Result" not in streamlit.session_state:
    #         streamlit.session_state.Result = False
    #     if calculate or streamlit.session_state.Result:
    #         left, mid, right = st.columns(3)
    #         with mid:
    #             with st_lottie_spinner(lottie_wait, key='wait7'):
    #                 with st.spinner("Loading... Please Wait"):
    #                     time.sleep(1)
    #         streamlit.session_state.Result = True
    #         data = [["Oil Flow Rate (BOPD)", oil],
    #                 ["Gas Flow Rate (MMSCF)", gas],
    #                 ["Water Flow Rate (BWPD)", water]]
    #         df = pd.DataFrame(data, columns=['Fluid', 'Flow rate'])
    #         st.table(df)
    #
    # #flowline with chock
    # if "Flowline_C" not in streamlit.session_state:
    #     streamlit.session_state.Flowline_C = False
    #
    # if flow_and_chock or streamlit.session_state.Flowline_C:
    #     left, mid, right = st.columns(3)
    #     with mid:
    #         with st_lottie_spinner(lottie_wait, key='wait8'):
    #             with st.spinner("Loading... Please Wait"):
    #                 time.sleep(1)
    #     streamlit.session_state.Flowline_C=True
    #     col1,col2,col3=st.columns(3)
    #     with col1:
    #         whp = st.number_input("Well head Pressure (psi)",min_value=608,max_value=3946,key='17')
    #     with col2:
    #         psep = st.number_input("Separator Pressure (psi)",min_value=100,max_value=600,key='16')
    #     with col3:
    #         ch = st.number_input("Chock size (inch)",min_value=0.25,max_value=2.5,key='18')
    #
    #     oil = oil_chock.predict([[whp,psep,ch]])[0]
    #     gas = gas_chock.predict([[whp,psep,ch]])[0]
    #     water = water_chock.predict([[whp,psep,ch]])[0]
    #     calculate = st.button("Calculate", key='cal3')
    #     if "Result" not in streamlit.session_state:
    #         streamlit.session_state.Result = False
    #     if calculate or streamlit.session_state.Result:
    #         left, mid, right = st.columns(3)
    #         with mid:
    #             with st_lottie_spinner(lottie_wait, key='wait9'):
    #                 with st.spinner("Loading... Please Wait"):
    #                     time.sleep(1)
    #         streamlit.session_state.Result = True
    #         data = [["Oil Flow Rate (BOPD)", oil],
    #                 ["Gas Flow Rate (MMSCF)", gas],
    #                 ["Water Flow Rate (BWPD)", water]]
    #         df = pd.DataFrame(data, columns=['Fluid', 'Flow rate'])
    #         st.table(df)
    #
    # #vertical lift performance
    # if "VLP" not in streamlit.session_state:
    #     streamlit.session_state.VLP = False
    #
    # if vlp or streamlit.session_state.VLP:
    #     left, mid, right = st.columns(3)
    #     with mid:
    #         with st_lottie_spinner(lottie_wait, key='wait10'):
    #             with st.spinner("Loading... Please Wait"):
    #                 time.sleep(1)
    #     streamlit.session_state.VLP=True
    #     col1,col2=st.columns(2)
    #     with col1:
    #         bhp = st.number_input("Bottom hole Pressure (psi)",min_value=4075,max_value=5490,key='20')
    #     with col2:
    #         whp = st.number_input("Well head Pressure (psi)",min_value=608,max_value=3946,key='19')
    #
    #
    #     oil = oil_vlp.predict([[bhp,whp]])[0]
    #     gas = gas_vlp.predict([[bhp,whp]])[0]
    #     water = water_vlp.predict([[bhp,whp]])[0]
    #     calculate = st.button("Calculate",key='cal4')
    #     if "Result" not in streamlit.session_state:
    #         streamlit.session_state.Result = False
    #     if calculate or streamlit.session_state.Result:
    #         left, mid, right = st.columns(3)
    #         with mid:
    #             with st_lottie_spinner(lottie_wait, key='wait11'):
    #                 with st.spinner("Loading... Please Wait"):
    #                     time.sleep(1)
    #         streamlit.session_state.Result = True
    #         data = [["Oil Flow Rate (BOPD)", oil],
    #                 ["Gas Flow Rate (MMSCF)", gas],
    #                 ["Water Flow Rate (BWPD)", water]]
    #         df = pd.DataFrame(data, columns=['Fluid', 'Flow rate'])
    #         st.table(df)
    #
    # #flowline with separator pressure temperature
    # if "PT" not in streamlit.session_state:
    #     streamlit.session_state.PT = False
    #
    # if flow_pt or streamlit.session_state.PT:
    #     left, mid, right = st.columns(3)
    #     with mid:
    #         with st_lottie_spinner(lottie_wait, key='wait12'):
    #             with st.spinner("Loading... Please Wait"):
    #                 time.sleep(1)
    #     streamlit.session_state.PT=True
    #     col1,col2,col3=st.columns(3)
    #     with col1:
    #         bhp = st.number_input("Bottom hole Pressure (psi)",min_value=4075,max_value=5490,key='23')
    #     with col2:
    #         whp = st.number_input("Well head Pressure (psi)",min_value=4075,max_value=5490,key='22')
    #     with col3:
    #         ch = st.number_input("Chock size (inch)",min_value=0.25,max_value=2.5,key='21')
    #
    #     oil = oil_pt.predict([[bhp,whp,ch]])[0]
    #     gas = gas_pt.predict([[bhp,whp,ch]])[0]
    #     water = water_pt.predict([[bhp,whp,ch]])[0]
    #     calculate = st.button("Calculate", key='cal5')
    #     if "Result" not in streamlit.session_state:
    #         streamlit.session_state.Result = False
    #     if calculate or streamlit.session_state.Result:
    #         left, mid, right = st.columns(3)
    #         with mid:
    #             with st_lottie_spinner(lottie_wait, key='wait13'):
    #                 with st.spinner("Loading... Please Wait"):
    #                     time.sleep(1)
    #         streamlit.session_state.Result = True
    #         data = [["Oil Flow Rate (BOPD)", oil],
    #                 ["Gas Flow Rate (MMSCF)", gas],
    #                 ["Water Flow Rate (BWPD)", water]]
    #         df = pd.DataFrame(data, columns=['Fluid', 'Flow rate'])
    #         st.table(df)
    #
    # #vertical lift performace with chock
    # if "VLP_C" not in streamlit.session_state:
    #     streamlit.session_state.VLP_C = False
    #
    # if vlp_chock or streamlit.session_state.VLP_C:
    #     left, mid, right = st.columns(3)
    #     with mid:
    #         with st_lottie_spinner(lottie_wait, key='wait14'):
    #             with st.spinner("Loading... Please Wait"):
    #                 time.sleep(1)
    #     streamlit.session_state.VLP_C=True
    #     col1,col2,col3=st.columns(3)
    #     with col1:
    #         bhp = st.number_input("Bottom hole Pressure (psi)",min_value=4075,max_value=5490,key='24')
    #     with col2:
    #         whp = st.number_input("Well head Pressure (psi)",min_value=608,max_value=3946,key='25')
    #     with col3:
    #         ch = st.number_input("Chock size (inch)",min_value=0.25,max_value=2.5,key='26')
    #
    #     oil = oil_vlp_chock.predict([[bhp,whp,ch]])[0]
    #     gas = gas_vlp_chock.predict([[bhp,whp,ch]])[0]
    #     water = water_vlp_chock.predict([[bhp,whp,ch]])[0]
    #     calculate = st.button("Calculate", key='cal6')
    #     if "Result" not in streamlit.session_state:
    #         streamlit.session_state.Result = False
    #     if calculate or streamlit.session_state.Result:
    #         streamlit.session_state.Result = True
    #         left, mid, right = st.columns(3)
    #         with mid:
    #             with st_lottie_spinner(lottie_wait, key='wait15'):
    #                 with st.spinner("Loading... Please Wait"):
    #                     time.sleep(1)
    #         data = [["Oil Flow Rate (BOPD)", oil],
    #                 ["Gas Flow Rate (MMSCF)", gas],
    #                 ["Water Flow Rate (BWPD)", water]]
    #         df = pd.DataFrame(data, columns=['Fluid', 'Flow rate'])
    #         st.table(df)
    #
    # #chock performance
    # if "Chock" not in streamlit.session_state:
    #     streamlit.session_state.Chock = False
    #
    # if chock or streamlit.session_state.Chock:
    #     streamlit.session_state.Chock=True
    #     left, mid, right = st.columns(3)
    #     with mid:
    #         with st_lottie_spinner(lottie_wait, key='wait16'):
    #             with st.spinner("Loading... Please Wait"):
    #                 time.sleep(1)
    #     col1,col2,col3=st.columns(3)
    #     with col1:
    #         whp = st.number_input("Well head Pressure (psi)",min_value=608,max_value=3946,key='27')
    #     with col2:
    #         wht = st.number_input("Well head temperature (degree F)",min_value=75,max_value=182,key='28')
    #     with col3:
    #         tsep = st.number_input("Separator Temperature (degree F)",min_value=60,max_value=140, key='29')
    #
    #     col4,col5= st.columns(2)
    #     with col4:
    #         psep = st.number_input("Separator Pressure (psi)",min_value=100,max_value=600,key='30')
    #     with col5:
    #         ch = st.number_input("Chock size (inch)",min_value=0.25,max_value=2.5,key='31')
    #
    #     oil = oil_c.predict([[whp,wht,tsep,psep,ch]])[0]
    #     gas = gas_c.predict([[whp,wht,tsep,psep,ch]])[0]
    #     water = water_c.predict([[whp,wht,tsep,psep,ch]])[0]
    #     calculate = st.button("Calculate", key='cal7')
    #     if "Result" not in streamlit.session_state:
    #         streamlit.session_state.Result = False
    #     if calculate or streamlit.session_state.Result:
    #         left, mid, right = st.columns(3)
    #         with mid:
    #             with st_lottie_spinner(lottie_wait, key='wait17'):
    #                 with st.spinner("Loading... Please Wait"):
    #                     time.sleep(1)
    #         streamlit.session_state.Result = True
    #         data = [["Oil Flow Rate (BOPD)", oil],
    #                 ["Gas Flow Rate (MMSCF)", gas],
    #                 ["Water Flow Rate (BWPD)", water]]
    #         df = pd.DataFrame(data, columns=['Fluid', 'Flow rate'])
    #         st.table(df)

if selected=='PVT Properties':
    left, mid, right = st.columns(3)
    with mid:
        with st_lottie_spinner(lottie_wait, key='wait18'):
            with st.spinner("Loading... Please Wait"):
                time.sleep(1)
    col1,col2= st.columns(2)
    with col1:
        temp=st.number_input("Temperature (defree F)",min_value=70, max_value=282,key='32')
    with col2:
        gor = st.number_input("Solution Gas-Oil Ratio (scf/stb)",min_value=290,max_value=1740,key='33')
    col3, col4 = st.columns(2)
    with col3:
        gas_grav=st.number_input("Gas Gravity",min_value=0.79, max_value=1.63,key='34')
    with col4:
        oil_grav = st.number_input("Oil API Gravity", min_value=17, max_value=40, key='35')
    cal = st.button("Calculate Bubble Point Pressure",key='cal8')

    if "PVT" not in streamlit.session_state:
        streamlit.session_state.PVT = False
    if cal or streamlit.session_state.PVT:
        streamlit.session_state.PVT = True
        left, mid, right = st.columns(3)
        with mid:
            with st_lottie_spinner(lottie_wait, key='wait19'):
                with st.spinner("Loading... Please Wait"):
                    time.sleep(1)
        bbl=bbl_pt.predict([[temp,gor,gas_grav,oil_grav]])[0]
        st.header(f"Bubble Point Pressure is {int(bbl)} psi")
        st.write(" ")
        st.markdown("**PVT properties of oil**")
        st.markdown("---")
        st.markdown("The PVT properties of crude oil are important to calculations of production and reservoir performance. These properties can be determined in the laboratory at specified conditions of pressure and temperature. To estimate PVT fluid properties at a wider range of conditions of pressure and temperature, an empirical correlation should be used where there are no laboratory measurements. These empirical correlations can, however, only be used after making the appropriate adjustments to the specified crude oil samples. In this study, the data from laboratory measurements of the PVT properties for five oil samples were used. These five samples were collected from different wells within the Luhais oil field. The measurements were taken at reservoir conditions with slight differencesfrom one sample to another. The five samples were then adjusted to the empirical correlations and the saturation pressure determined. Theresulting models of the samples after adjustment were combined to estimate a generalised model of the fluid properties that represented the properties of the studied crude oil.")

        st.markdown("**Bubble Point Pressure**")
        st.markdown("---")
        st.markdown("Bubble-point pressure is defined as the pressure at which the first bubble of gas appears at a specific temperature. The phase diagram of typical black oils shows that the bubble-point pressure could be different at different temperatures. In the petroleum industry, if bubble-point pressure value is mentioned without reference to a particular temperature, the temperature is implicitly assumed to be the reservoir temperature.")
        st.image("https://ars.els-cdn.com/content/image/3-s2.0-B9781933762388500083-f01-07-9781933762388.jpg", caption="Phase diagram")
        st.markdown("When the reservoir is depleted and its pressure falls below the bubble-point pressure, free gas starts to form in the reservoir. Since gas has higher mobility than oil, the producing GOR is expected to increase when the reservoir pressure decreases below the bubble-point pressure. Other PVT properties also undergo significant changes when the reservoir pressure passes through the bubble-point pressure.")









