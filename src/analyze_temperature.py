import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    """ Load the Monterey Bay Aquarium seawater intake data and process it """
    # Load the data
    data = pd.read_csv('../data/monterey-bay-aquarium-seawater-intake.csv',parse_dates=[0], index_col=[0])
    data.columns = ['DO_SAT','sw_temp']
    
    # Low pass filter
    data['sw_temp_detide'] = data['sw_temp'].rolling(window=60*40,win_type='hann',center=True).mean()
    data['sw_DO_detide'] = data['DO_SAT'].rolling(window=60*40,win_type='hann',center=True).mean()
    
    return data


def make_plots(data):
    """ Make plots from the data """

    # Plot the Temperature
    fig,ax = plt.subplots()
    ax.plot(data.index, data['sw_temp'], label='Raw')
    ax.plot(data.index, data['sw_temp_detide'], label='detided')
    ax.legend(frameon=False)
    ax.set_title('Intake Temperature\nMonterey Bay Aquarium', fontsize=12, fontweight='bold',loc='left')
    ax.set_ylabel('Temperature (°C)')
    fig.autofmt_xdate()
    plt.savefig('../results/temperature.png')


    # Plot the Temperature
    fig,ax = plt.subplots()
    ax.plot(data['sw_temp_detide'],data['sw_DO_detide'],marker='o',linestyle='None',color='k',label='Detided')
    ax.plot(data['sw_temp'],data['DO_SAT'],marker='.',linestyle='None',color='.75',zorder=-1,label='Raw')
    ax.legend(frameon=False)
    ax.set_title('Temperature vs Dissolved Oxygen\nMonterey Bay Aquarium', fontsize=12, fontweight='bold',loc='left')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Dissolved Oxygen (%)')
    fig.autofmt_xdate()
    plt.savefig('../results/swtemp_do.png')
    
    
if __name__ == '__main__':
    data = load_data()
    make_plots(data)