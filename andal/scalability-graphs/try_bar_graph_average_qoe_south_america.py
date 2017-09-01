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
    
    # {"11": 4.96, "30": 0.5003703703703702, "29": 4.4310389610389604, "23": 4.9350000000000005}
    google_fs = [4.935,4.431, 0.500]
    google_fs_std = [0,0,0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std)
    
    # {'27': 4.95, '30': 3.514761904761905, '28': 4.666026451983884, '29': 3.325542635658914}
    azure_fs_1 = [4.660,3.325,3.514]
    azure_fs_std_1 = [0,0,0]
    azure_rects_1 = ax.bar(ind + width, azure_fs_1, width, hatch=patterns[1], color=colors[1], yerr=azure_fs_std_1)

    #  {"30": 3.2985436893203905, "29": 1.4254545454545455, "23": 4.964500000000001}
    azure_fs= [4.964,1.425,3.298]
    azure_fs_std = [0,0,0]
    azure_rects = ax.bar(ind + (2*width), azure_fs, width, hatch=patterns[2], color=colors[2], yerr=azure_fs_std)

    # {"30": 4.939408866995087, "29": 4.965555555555557, "23": 4.972333333333336}
    amazon_fs = [4.97,4.965,4.939]
    amazon_fs_std = [0,0,0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average QoE')
    ax.set_xlabel ('Number of bursty Users in South America')
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
