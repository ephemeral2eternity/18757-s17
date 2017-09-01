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
    google_fs = [1.0934260129928588, 0.9994997382164001, 0.952347195148468, 1.131295907497406, 1.0497087717056275, 1.0812542676925658, 1.0549452543258666, 1.0815593242645263, 1.1027724385261535, 1.0874993324279785, 1.1471118927001953, 0.9857908606529235, 1.0660154700279236, 0.982298731803894, 1.1346540093421935, 1.0378262042999267, 1.0724816918373108, 1.0981983900070191, 1.0865800380706787, 1.4572653889656066]
    #google_fs_std = [0.13]
    google_fs_std = [0]
    google_rects = ax.bar(ind, google_fs, width, hatch=patterns[0], color=colors[0], yerr=google_fs_std[0])

    # {'12': 4.954901960784317, '15': 4.862477064220183, '14': 4.891549295774646, '17': 4.805099009900998}
    azure_fs_akamai= [0.9951162219047547, 0.4806452989578247, 0.40524848699569704, 0.48414567708969114, 0.6580042123794556, 0.5614627838134766, 0.3640915036201477, 0.4133684396743774, 0.40794417858123777, 0.6847898364067078, 0.4086969614028931, 0.5871332168579102, 0.6741928935050965, 0.8692870020866394, 0.48648288249969485, 0.39117316007614134, 0.4947276473045349, 0.8672959208488464, 0.36245806217193605, 0.4550388097763062]
    #azure_fs_std_akamai = [0.36]
    azure_fs_std_akamai = [0]
    azure_rects_akamai = ax.bar(ind + width, azure_fs_akamai, width, hatch=patterns[1], color=colors[1], yerr=azure_fs_std_akamai[0])
    
    azure_fs_verizon= [1.089189076423645, 0.8003864526748657, 0.5949392080307007, 0.6051760196685791, 0.8190504431724548, 0.6437192320823669, 0.4594258189201355, 0.47481708526611327, 0.67521733045578, 0.47499034404754636, 0.3762417912483215, 0.5999325275421142, 0.3047343254089355, 0.649055540561676, 0.4175720810890198, 0.4729729413986206, 0.474113392829895, 0.4803602576255798, 0.34511719942092894, 0.49646849632263185]
    #azure_fs_std_verizon = [0.38]
    azure_fs_std_verizon = [0]
    azure_rects_verizon = ax.bar(ind + (2*width), azure_fs_verizon, width, hatch=patterns[2], color=colors[2], yerr=azure_fs_std_verizon[0])

    # {'13': 4.960272108843544, '15': 4.762015503875968, '14': 4.814366197183099, '17': 4.837540983606566}
    amazon_fs = [0.6501625776290894, 0.4000380039215088, 0.31183992624282836, 0.42500083446502684, 0.4761744260787964, 0.511689293384552, 0.8521405339241028, 0.45032644271850586, 0.33198890686035154, 0.36355172395706176, 0.48529242277145385, 0.5308042883872985, 0.39808436632156374, 0.5078148722648621, 0.3426155924797058, 0.5015860080718995, 0.45564706325531007, 0.5556403040885926, 0.3186082601547241, 0.4864917755126953]
    #amazon_fs_std = [0.22]
    amazon_fs_std = [0]
    amazon_rects = ax.bar(ind+(3*width), amazon_fs, width, hatch=patterns[3], color=colors[3], yerr=amazon_fs_std[0])

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average Response Time requesting Chunk 2 (in sec)')
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
