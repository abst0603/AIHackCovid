import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

def diff(col):
    colout = np.zeros(len(col))
    col = col.to_numpy()
    for i in range(len(col)-1):
        temp = col[i+1]-col[i]
        colout[i] = temp
    return colout

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def policy_DE(data):
    # data = pd.read_csv('../covid-policy-tracker/data/OxCGRT_latest.csv',low_memory=False)
    # Preview the first 5 lines of the loaded data
    Germany = data[data['CountryName']=='Germany']
    colomn = Germany['ConfirmedCases']# ConfirmedDeaths
    colout = diff(colomn)
    colout = moving_average(colout,7)
    figure(figsize=(16, 8), dpi=80)
    plt.plot(colout)

    schoolc = Germany['C1_School closing']
    schoolc_diff = diff(schoolc)
    restrict = schoolc_diff > 0
    x = np.argwhere(restrict)
    plt.vlines(x,1000,10000,colors='k')

    loos = schoolc_diff < 0
    x = np.argwhere(loos)
    plt.vlines(x,1000,10000,colors='k',linestyles = 'dashed')

    schoolc = Germany['C2_Workplace closing']
    schoolc_diff = diff(schoolc)
    restrict = schoolc_diff > 0
    x = np.argwhere(restrict)
    plt.vlines(x,1000,10000,colors='r')

    loos = schoolc_diff < 0
    x = np.argwhere(loos)
    plt.vlines(x,1000,10000,colors='r',linestyles = 'dashed')
    plt.legend(['Confirmed cases per day', 'School closing', 'Relax School closing', 'Workplace closing', 'Relax Workplace closing'])
    plt.title('Germany')
    plt.savefig('Germany_SchoolWorkplacePolicies', dpi=80)
# plt.show()