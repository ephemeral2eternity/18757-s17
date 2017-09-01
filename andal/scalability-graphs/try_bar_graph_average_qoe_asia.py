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
    
    # {"11": 4.96, "29": 4.933387096774194, "23": 4.923333333333333}
    # {'11': 4.96, '31': 4.236666666666667, '29': 4.933387096774194, '23': 4.923333333333333}
    google_fs = [4.923,4.933,4.236]
    google_fs_std = [0,0,0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std)
    
    # {'31': 2.6466104868913853, '30': 2.554201930215292, '28': 3.3394662657395204, '29': 2.616245290916696}
    azure_akamai_fs= [2.61,2.55,2.64]
    azure_akamai_fs_std = [0,0,0]
    azure_akamai_rects = ax.bar(ind + width, azure_akamai_fs, width, hatch=patterns[1], color=colors[1], yerr=azure_akamai_fs_std)
    
    # {'30': 3.0797339246119835, '29': 4.963291139240512, '23': 4.97}
    azure_verizon_fs= [4.97,4.96,3.07]
    azure_verizon_fs_std = [0,0,0]
    azure_verizon_rects = ax.bar(ind + (2*width), azure_verizon_fs, width, hatch=patterns[2], color=colors[2], yerr=azure_verizon_fs_std)
    
    #{'31': 3.9330769230769227, '29': 4.955624999999999, '23': 4.96}
    amazon_fs = [4.96,4.955,3.93]
    amazon_fs_std = [0,0,0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std)
    

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average QoE')
    ax.set_xlabel ('Number of bursty Users in Asia')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(["2 - 256", "512", "1024"])

    ax.legend((google_rects[0], azure_akamai_rects[0], azure_verizon_rects[0], amazon_rects[0]), ('Google Cloud CDN', 'Azure CDN(Akamai)', 'Azure CDN(Verizon)', 'Amazon CloudFront'), loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize = 7.5)
    
    autolabel(ax, google_rects)
    autolabel(ax, azure_akamai_rects)
    autolabel(ax, azure_verizon_rects)
    autolabel(ax, amazon_rects)

    plt.savefig('myfig')
    plt.show()

if __name__ == '__main__':
    draw_bar()
