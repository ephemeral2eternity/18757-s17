import numpy as np
import matplotlib.pyplot as plt

patterns = ['-', '+', 'x', '\\', '*', 'o', 'O', '.', '/']
colors = ['r', 'g', 'y', 'b', 'm', 'c']

def autolabel(ax, rects):
    """
        Attach a text label above each bar displaying its height
        """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % height,
                ha='center', va='bottom')

def draw_bar():

    bursty_users = ["2 - 256", "512", "1024"]
    fig, ax = plt.subplots()

    width = 0.2
    ind = np.arange(len(bursty_users))
    
    # {"19": [71], "12": [3], "14": [11], "15": [20]}
    # {12: [3], 14: [11], 15: [20], 19: [71], 29: [14], 30: [1]}
    google_fs = [14,34,72]
    google_fs_std = [0,0,0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std)
    
    {28: [109], 30: [176]}
    azure_fs_1= [109,0,176]
    azure_fs_std_1 = [0,0,0]
    azure_rects_1 = ax.bar(ind + width, azure_fs_1, width, hatch=patterns[1], color=colors[1], yerr=azure_fs_std_1)

    # {"17": [5], "14": [1], "15": [2]}
    # {17: [5], 14: [1], 30: [9], 15: [2]}
    azure_fs= [1,2,14]
    azure_fs_std = [0,0,0]
    azure_rects = ax.bar(ind + (2*width), azure_fs, width, hatch=patterns[2], color=colors[2], yerr=azure_fs_std)

    # {"17": [4], "14": [2], "15": [5]}
    # {17: [4], 30: [1], 14: [2], 15: [5]}
    amazon_fs = [2,5,5]
    amazon_fs_std = [0,0,0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Number of sessions crashes')
    ax.set_xlabel ('Number of bursty Users, North America')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(["2 - 256", "512", "1024"])

    ax.legend((google_rects[0], azure_rects_1[0], azure_rects[0], amazon_rects[0]), ('Google Cloud CDN', 'Azure CDN(Akamai)', 'Azure CDN(Verizon)', 'Amazon CloudFront'), loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize = 7.5)
    
    autolabel(ax, google_rects)
    autolabel(ax, azure_rects)
    autolabel(ax, azure_rects)
    autolabel(ax, amazon_rects)

    plt.savefig('myfig')
    plt.show()

if __name__ == '__main__':
    draw_bar()
