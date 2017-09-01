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

    bursty_users = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    fig, ax = plt.subplots()

    width = 0.2
    ind = np.arange(len(bursty_users))
    
    # {"19": 3.681888111888113, "11": 4.96, "12": 4.8465942028985545, "15": 4.15444444444444, "14": 4.273703703703701}
    google_fs = [1.6021815180778503, 1.0202183246612548, 1.0109647274017335, 1.1666810035705566, 1.1102512717247008, 1.0294212460517884, 1.2053154230117797, 1.1012976050376893, 1.0700672388076782, 1.1490641593933106, 1.101333749294281, 0.9888251304626465, 0.9749863028526307, 0.9982170581817627, 1.0809095621109008, 1.0527014493942262, 1.0970365285873414, 1.2831533670425415, 1.0998566269874572, 1.0377084732055664]
    #google_fs_std = [0.13]
    google_fs_std = [0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std[0])

    # {'12': 4.954901960784317, '15': 4.862477064220183, '14': 4.891549295774646, '17': 4.805099009900998}
    azure_fs_akamai= [2.086639904975891, 0.4688375949859619, 0.40642346143722535, 0.4067069530487061, 0.6502123713493347, 0.4424693942070007, 0.39329774379730226, 0.48618054389953613, 0.30911163091659544, 0.38483051061630247, 0.4351806044578552, 0.4515931248664856, 0.4540520071983337, 0.38045401573181153, 0.5506499171257019, 0.46560648679733274, 0.49640086889266966, 0.44541106224060056, 0.3142728090286255, 0.40823320150375364]
    #azure_fs_std_akamai = [0.36]
    azure_fs_std_akamai = [0]
    azure_rects_akamai = ax.bar(ind + width, azure_fs_akamai, width, hatch=patterns[1], color=colors[1], yerr=azure_fs_std_akamai[0])
    
    azure_fs_verizon= [2.1280742645263673, 0.5718906402587891, 0.5317671775817872, 0.34461010694503785, 0.5334519505500793, 0.5669979691505432, 0.7182860732078552, 0.3398860692977905, 0.43890005350112915, 0.4723642706871033, 0.7426918029785157, 0.509566581249237, 0.46197147369384767, 0.2905667543411255, 0.2504081726074219, 0.43958317041397094, 0.7403206706047059, 0.437348461151123, 0.508381450176239, 0.28019784688949584]
    #azure_fs_std_verizon = [0.38]
    azure_fs_std_verizon = [0]
    azure_rects_verizon = ax.bar(ind + (2*width), azure_fs_verizon, width, hatch=patterns[2], color=colors[2], yerr=azure_fs_std_verizon[0])

    # {'13': 4.960272108843544, '15': 4.762015503875968, '14': 4.814366197183099, '17': 4.837540983606566}
    amazon_fs = [1.4349410891532899, 0.4914458990097046, 0.5813831329345703, 0.3501826047897339, 0.4445191740989685, 0.3769575357437134, 0.3835597038269043, 0.5128201723098755, 0.39631139039993285, 0.49460453987121583, 0.4431292176246643, 0.45172940492630004, 0.4745698213577271, 0.38924665451049806, 0.5250598430633545, 0.3880103349685669, 0.6161814570426941, 0.37607330083847046, 0.5815804958343506, 0.6893388748168945]
    #amazon_fs_std = [0.22]
    amazon_fs_std = [0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std[0])

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average Response Time requesting Chunk 1 (in sec)')
    ax.set_xlabel ('Number of Iterations')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"])

    ax.legend((google_rects[0], azure_rects_akamai[0], azure_rects_verizon[0], amazon_rects[0]), ('Google Cloud CDN', 'Azure CDN(Akamai)', 'Azure CDN(Verizon)','Amazon CloudFront'), loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3)
#    
#    autolabel(ax, google_rects)
#    autolabel(ax, azure_rects_akamai)
#    autolabel(ax, azure_rects_verizon)
#    autolabel(ax, amazon_rects)

    plt.savefig('myfig')
    plt.show()

if __name__ == '__main__':
    draw_bar()
