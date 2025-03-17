#import required libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib.dates as mdates
import math

#Create runner class

class Runner:
        
    @staticmethod
    def run(args):

        #Arguments passed through main program
        file_name = args[0]
        rows = int(args[1])

        data = pd.read_csv(file_name)
        #rename columns to make this easier for reading and plotting
        data.rename(columns={"Systolic (mmHg)":"Syst",
                            "Diastolic (mmHg)":"Dias"}, inplace=True)
        #change dates format for easier visibility when plotting
        data2 = data.copy()
        data2["Date"] = pd.to_datetime(data2["Date"])
        #group data and calculate values needed for plotting
        data3 = data2.groupby("Date")[["Syst", "Dias", "Pulse (bpm)"]].mean().reset_index()
        
        data4 = data3.sort_values(by="Date", ascending = True)

        collapsed_avg = data4[["Syst","Dias","Pulse (bpm)"]].mean()
        
        data4_rows = len(data4)

        row_data = data4.iloc[-rows:]
        row_avg = row_data[["Syst","Dias","Pulse (bpm)"]].mean()
        min_value = row_data[["Syst", "Dias", "Pulse (bpm)"]].min().min()
        max_value = row_data[["Syst", "Dias", "Pulse (bpm)"]].max().max()

        #display header for the output of the program along with specific values I am searching for based on arguments
        print ('args = [ ',file_name, ',', rows,' ]')
        print()
        print ('I certify that this program is my own work\n'
                'and is not the work of others.')
        print()
        print('Collapse the data into unique rows')
        print("Number of unique rows: ", data4_rows)
        print('Mean values of columns of interest in unique rows')
        print(collapsed_avg)
        print()

        
        print(f"Number of rows to plot: , {len(row_data)}")
        print("Minimum data value in rows to plot: ", min_value)
        print("Maximum data value in rows to plot: ", max_value)
        print()
        print("Mean values for columns of interest in rows to plot")
        print(row_avg)
        #plot the data and combine the line plots into one graph. 
        fig, ax = plt.subplots()

        myFmt = mdates.DateFormatter('%Y-%m-%d')
        ax.xaxis.set_major_formatter(myFmt)
        
        ax.plot(row_data["Date"], row_data["Syst"], marker = "o", markersize = 4, label ="Syst")
        ax.plot(row_data["Date"], row_data["Dias"], marker = "o", markersize = 4, label ="Dias")
        ax.plot(row_data["Date"], row_data["Pulse (bpm)"], marker = "o", markersize =4, label ="Pulse")                
        ax.legend(loc='center')
        ax.set_title("Ryan Maldonado")
        #set the x and y label parameters for easier visibility when reading plot. 
        ax.set_xlabel("Date")
        ax.tick_params(axis ='x', labelrotation = 90)

        num_ticks = rows // 5
        num_ticks = max(1, num_ticks)  
        tick_positions = np.linspace(0, len(row_data) - 1, num_ticks, dtype=int)
        x_ticks = row_data.iloc[tick_positions]["Date"] 

        ax.set_xticks(x_ticks)
        

        ax.set_ylabel("Value")
        y_min, y_max = min_value, max_value
        y_ticks = np.arange(y_min, y_max + 1, 10)
        ax.set_yticks(y_ticks)

        ax.grid(True)

        fig.savefig(f"Proj12-{rows}.jpg",bbox_inches = 'tight')

        return ax








    
