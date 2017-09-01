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
    
    # {"19": 3.681888111888113, "11": 4.96, "12": 4.8465942028985545, "15": 4.15444444444444, "14": 4.273703703703701}
    # {"11": 4.96, "12": 4.8465942028985545, "15": 4.15444444444444, "14": 4.273703703703701, "23": 4.954016393442624, "19": 3.681888111888113, "30": 4.8100000000000005, "29": 4.080243902439024}
    
    google_fs = [4.75,4.11, 4.24]
    google_fs_std = [0,0,0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std)

    # {'27': 4.96, '30': 1.964234693877551, '28': 3.1042767295597544}
    azure_fs_1= [4.96,3.10,1.96]
    azure_fs_std_1 = [0,0,0]
    azure_rects_1 = ax.bar(ind + width, azure_fs_1, width, hatch=patterns[1], color=colors[1], yerr=azure_fs_std_1)


    # {'12': 4.954901960784317, '15': 4.862477064220183, '14': 4.891549295774646, '17': 4.805099009900998}
    # {"12": 4.954901960784317, "15": 4.862477064220183, "14": 4.891549295774646, "17": 4.804328358208962, "23": 4.955796178343955, "30": 4.866687598116181, "29": 4.962019230769233}
    azure_fs= [4.93,4.91,4.83]
    azure_fs_std = [0,0,0]
    azure_rects = ax.bar(ind + (2*width), azure_fs, width, hatch=patterns[2], color=colors[2], yerr=azure_fs_std)

    # {'13': 4.960272108843544, '15': 4.762015503875968, '14': 4.814366197183099, '17': 4.837540983606566}
    # {"13": 4.960272108843544, "15": 4.762015503875968, "14": 4.814366197183099, "17": 4.837540983606566, "23": 4.9577192982456175, "30": 4.930721649484549, "29": 4.9681052631578995}
    amazon_fs = [4.91,4.86,4.88]
    amazon_fs_std = [0,0,0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average QoE')
    ax.set_xlabel ('Number of bursty Users in North America')
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
