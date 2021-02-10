import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse

colors=['orange', 'red', 'green', 'blue', 'yellow', 'magenta']

def Plot3D(file, aggregated=True, angle_H=45, angle_V=45):

    data=pd.read_csv(file, sep='\t')

    col_names=list(data.columns)
    sample=col_names[0]
    x=col_names[1]
    y=col_names[2]
    z=col_names[3]

    if aggregated:
        fig = plt.figure()
        ax = Axes3D(fig)
        for index, row in data.iterrows():
            ax.scatter(row[x], row[y], row[z], marker='.', c='orange',s=50)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_zlabel(z)
        ax.view_init(angle_H,angle_V)
        plt.show(block=True)
    else:
        fig = plt.figure()
        ax = Axes3D(fig)
        samples=list(data[sample].unique())
        for index, row in data.iterrows():
            s=row[sample]
            index=samples.index(s)%len(samples)
            color=colors[index]
            ax.scatter(row[x], row[y], row[z], marker='.', c=color, s=50)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_zlabel(z)
        ax.view_init(angle_H,angle_V)
        plt.show(block=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='3D Plot')
    parser.add_argument('file', metavar='f', type=str,
                    help='data file name. Data in the file should have 4 columns 1 sample type and 3 variables')
    parser.add_argument('--angle_H', type=int, default=45,
                    help='angle of view in horizontal plane')

    parser.add_argument('--angle_V', type=int, default=45,
                    help='angle of view in vertical plane')

    parser.add_argument('--agg',
                    help='plots aggregated data, if not, plots with different colors for each sample type')

    args = parser.parse_args()

    file=args.file
    angle_H=args.angle_H
    angle_V=args.angle_V
    agg=args.agg
    
    Plot3D(file, agg, angle_H, angle_V)