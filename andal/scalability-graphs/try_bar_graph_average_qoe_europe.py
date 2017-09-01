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
                '%.2f' % height,
                ha='center', va='bottom')

def draw_bar():

    bursty_users = ["2 - 256", "512", "1024"]
    fig, ax = plt.subplots()

    width = 0.2
    ind = np.arange(len(bursty_users))
    
    # {'11': 4.96, '31': 2.5571317829457385, '30': 2.62943722943723, '29': 4.277458213256487}
    google_fs = [4.277,2.557, 2.629]
    google_fs_std = [0,0,0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std)

    # {'30': 2.5133208955223885, '28': 4.27626682270332, '29': 1.9274545454545453}
    azure_fs_1= [4.276,1.927,2.513]
    azure_fs_std_1 = [0,0,0]
    azure_rects_1 = ax.bar(ind + width, azure_fs_1, width, hatch=patterns[1], color=colors[1], yerr=azure_fs_std_1)


    #  {"11": 4.96, "30": 4.7284438040345895, "29": 4.905}
    azure_fs= [4.96,4.905,4.728]
    azure_fs_std = [0,0,0]
    azure_rects = ax.bar(ind + (2*width), azure_fs, width, hatch=patterns[2], color=colors[2], yerr=azure_fs_std)

    # {'27': 4.954999999999999, '26': 4.93, '30': 2.6224090909090907, '28': 4.294687499999993, '29': 2.6147837837837855}
    amazon_fs = [4.294,2.614,2.622]
    amazon_fs_std = [0,0,0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average QoE')
    ax.set_xlabel ('Number of bursty Users in Europe')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(["2 - 256", "512", "1024"])

    ax.legend((google_rects[0], azure_rects_1[0], azure_rects[0], amazon_rects[0]), ('Google Cloud CDN', 'Azure CDN(Akamai)', 'Azure CDN(Verizon)', 'Amazon CloudFront'), loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=7.5)
    
    autolabel(ax, google_rects)
    autolabel(ax, azure_rects_1)
    autolabel(ax, azure_rects)
    autolabel(ax, amazon_rects)

    plt.savefig('myfig')
    plt.show()

if __name__ == '__main__':
    draw_bar()
