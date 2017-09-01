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
    google_fs = [1.0131966829299928, 1.0030974626541138, 1.0741042494773865, 1.2323712587356568, 1.0896029472351074, 1.0769350409507752, 1.1029942989349366, 1.1048568844795228, 1.0521971106529235, 1.0024854063987731, 1.364628517627716, 0.9450328588485718, 0.9443252205848693, 1.05441734790802, 1.226779544353485, 1.1500066876411439, 1.1143462300300597, 1.2149098634719848, 1.0868255972862244, 1.0166221261024475]
    #google_fs_std = [0.13]
    google_fs_std = [0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std[0])

    # {'12': 4.954901960784317, '15': 4.862477064220183, '14': 4.891549295774646, '17': 4.805099009900998}
    azure_fs_akamai= [0.9373626708984375, 0.6467434406280518, 0.5968819856643677, 0.4734746694564819, 0.5641060948371888, 0.3689194917678833, 0.36424578428268434, 0.3403637528419495, 0.3934487342834473, 0.5573398113250733, 0.8554522037506104, 0.4279147505760193, 0.36069599390029905, 0.41898307800292967, 0.39412442445755, 0.41878141164779664, 0.31827889680862426, 0.323118793964386, 0.5303624868392944, 0.39329413175582884]
    #azure_fs_std_akamai = [0.36]
    azure_fs_std_akamai = [0]
    azure_rects_akamai = ax.bar(ind + width, azure_fs_akamai, width, hatch=patterns[1], color=colors[1], yerr=azure_fs_std_akamai[0])
    
    azure_fs_verizon= [0.6552880525588989, 0.8880940675735474, 0.5928993463516236, 0.5391397953033448, 0.5175945281982421, 0.5756867051124572, 0.34196120500564575, 0.3768095850944519, 0.6602454423904419, 0.4961774706840515, 0.7464391231536865, 0.5281240582466126, 0.6566399216651917, 0.34683135747909544, 0.4994401216506958, 0.7211133599281311, 0.3247283697128296, 0.5012822628021241, 0.3436389803886414, 0.9298182964324951]
    #azure_fs_std_verizon = [0.38]
    azure_fs_std_verizon = [0]
    azure_rects_verizon = ax.bar(ind + (2*width), azure_fs_verizon, width, hatch=patterns[2], color=colors[2], yerr=azure_fs_std_verizon[0])

    # {'13': 4.960272108843544, '15': 4.762015503875968, '14': 4.814366197183099, '17': 4.837540983606566}
    amazon_fs = [0.39353530406951903, 0.30668388605117797, 0.4551555871963501, 0.33776257038116453, 0.33132354021072385, 0.5389376282691956, 0.5367645263671875, 0.3553434729576111, 0.2617467284202576, 0.2731562614440918, 0.26271992921829224, 0.2605835318565369, 0.6975317239761353, 0.3880773425102234, 0.4842317223548889, 0.3559951066970825, 0.33016101121902464, 0.38206279277801514, 0.35722755193710326, 0.2824808120727539]
    #amazon_fs_std = [0.22]
    amazon_fs_std = [0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std[0])

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average Response Time requesting Chunk 3 (in sec)')
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
