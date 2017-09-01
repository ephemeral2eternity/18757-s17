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
    
    # {29: [7], 30: [103]}
    google_fs = [0,7,103]
    google_fs_std = [0,0,0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std)

    # {28: [21], 29: [4], 30: [3]}
    azure_fs_1= [4,21,3]
    azure_fs_std_1 = [0,0,0]
    azure_rects_1 = ax.bar(ind + width, azure_fs_1, width, hatch=patterns[1], color=colors[1], yerr=azure_fs_std_1)

    #  {30: [38]}
    azure_fs= [0,0,38]
    azure_fs_std = [0,0,0]
    azure_rects = ax.bar(ind + (2*width), azure_fs, width, hatch=patterns[2], color=colors[2], yerr=azure_fs_std)

    # {}
    amazon_fs = [0,0,0]
    amazon_fs_std = [0,0,0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Number of sessions crashes')
    ax.set_xlabel ('Number of bursty Users, South America')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(["2 - 256", "512", "1024"])

    ax.legend((google_rects[0], azure_rects_1[0], azure_rects[0], amazon_rects[0]), ('Google Cloud CDN', 'Azure CDN(Akamai)', 'Azure CDN(Verizon)', 'Amazon CloudFront'), loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize = 7.5)
    
    autolabel(ax, google_rects)
    autolabel(ax, azure_rects_1)
    autolabel(ax, azure_rects)
    autolabel(ax, amazon_rects)

    plt.savefig('myfig')
    plt.show()

if __name__ == '__main__':
    draw_bar()
