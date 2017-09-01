import os
import numpy as np
import matplotlib.pyplot as plt

styles = ['k-', 'b.-', 'r--', 'm:', 'ys-', 'go-', 'c^-',
          'k.-', 'b--', 'r:', 'ms-','yo-', 'g^-', 'c-',
          'k--', 'b:', 'rs-', 'mo-', 'y^-', 'g-', 'c.-',
          'k:', 'bs-', 'ro-', 'm^-', 'y-', 'g.-', 'c--',
          'ks-', 'bo-', 'r^-', 'm-', 'y.-', 'g--', 'c-',
          'ko-', 'b^-', 'r-', 'm.-', 'y--', 'g-', 'cs-']

def draw_cdf(data, ls, lg):
    sorted_data = np.sort(data)
    yvals = np.arange(len(sorted_data))/float(len(sorted_data))
    plt.plot(sorted_data, yvals, ls, label=lg, linewidth=2.0)
    plt.savefig('myfig')

google_response_time = []

azure_response_time_verizon = [0.8045530319213867, 0.24115586280822754, 0.18085598945617676, 0.021440982818603516, 0.01120901107788086, 0.00710606575012207, 0.11762595176696777, 3.071024179458618, 0.053588151931762695, 0.018199920654296875, 0.01734304428100586, 0.687870979309082, 0.0500788688659668, 0.024116992950439453, 0.03624391555786133, 0.09929704666137695, 0.011008024215698242, 0.1394498348236084, 0.016125202178955078, 0.028036117553710938, 0.020110130310058594, 0.022223949432373047, 0.34076499938964844, 0.07007598876953125, 0.0189359188079834, 0.015506982803344727, 0.015934228897094727, 0.00783085823059082, 0.03275108337402344, 1.2450029850006104, 0.06044602394104004, 0.10642504692077637, 0.0994260311126709, 0.012359857559204102, 0.005769014358520508, 0.286074161529541, 0.021338939666748047, 0.04024696350097656, 0.1386270523071289, 0.8240690231323242, 0.011452913284301758, 0.025454998016357422, 0.00864100456237793, 0.06608819961547852, 0.023813962936401367, 0.06930804252624512, 0.04854893684387207, 0.08640789985656738, 0.020993947982788086, 0.012600183486938477, 0.03187704086303711, 0.009463787078857422, 0.006067991256713867, 0.006318092346191406]

azure_response_time_akamai = [0.03275704383850098, 0.10410594940185547, 0.06955194473266602, 0.8900740146636963, 0.008051872253417969, 0.4673750400543213, 0.3423318862915039, 0.0484769344329834, 0.6273820400238037, 0.6301050186157227, 0.6341900825500488, 0.05148816108703613, 0.052206993103027344, 0.0573880672454834, 0.022556066513061523, 0.02599191665649414, 0.012651920318603516, 0.011707067489624023, 0.0104827880859375, 0.020601987838745117, 0.023370981216430664, 0.05799412727355957, 0.11937212944030762, 0.0492558479309082, 0.06257104873657227, 0.02863001823425293, 0.2118990421295166, 0.05010509490966797, 0.02032613754272461, 0.11812710762023926, 0.013416051864624023, 0.12165689468383789, 0.03329110145568848, 0.18624615669250488, 0.014392852783203125, 0.06122899055480957, 0.02521204948425293, 0.01229095458984375, 0.12858009338378906, 0.18669605255126953, 0.01067209243774414, 0.22641992568969727, 1.143183946609497, 0.008176088333129883, 0.21695995330810547, 0.019497156143188477, 0.04252195358276367, 0.062187910079956055, 0.017138957977294922, 0.08950185775756836, 0.053015947341918945, 0.045819997787475586, 0.09409403800964355, 0.023280858993530273]

amazon_response_time = [0.18155288696289062, 0.17659592628479004, 0.14211106300354004, 0.11223697662353516, 0.04533815383911133, 0.06447100639343262, 0.19310712814331055, 0.12211203575134277, 0.7618160247802734, 0.2655370235443115, 0.022114992141723633, 0.03524494171142578, 0.02089715003967285, 0.054141998291015625, 0.22895503044128418, 1.4345548152923584, 0.015708208084106445, 0.03186607360839844, 0.045571088790893555, 0.08212089538574219, 0.05112600326538086, 0.9422950744628906, 0.04819989204406738, 0.040183067321777344, 0.07892084121704102, 0.37222886085510254, 0.018529891967773438, 0.03599286079406738, 0.07304620742797852, 0.6940510272979736, 0.18984293937683105, 0.03451704978942871, 0.015096902847290039, 0.18442106246948242, 0.10198497772216797, 0.07618403434753418, 0.5491540431976318, 0.09914088249206543, 0.20675897598266602, 0.14213991165161133, 0.18334102630615234, 0.017818927764892578, 0.02693915367126465, 0.08138799667358398, 0.026562929153442383, 0.11903810501098633, 0.42891597747802734, 0.059686899185180664, 0.03507804870605469, 0.03165388107299805, 0.702934980392456, 0.080902099609375, 0.07193899154663086, 0.036023855209350586]

fig, ax = plt.subplots()

draw_cdf(google_response_time, styles[0], "Google Cloud CDN")
draw_cdf(azure_response_time_verizon, styles[1], "Azure CDN (Verizon)")
draw_cdf(azure_response_time_akamai, styles[2], "Azure CDN (Akamai)")
draw_cdf(amazon_response_time, styles[3], "Amazon CloudFront")

ax.set_xlabel(r'Response time at the middle of the experiment (Chunk 1)', fontsize=12)
ax.set_ylabel(r'Percentage of PlanetLab users', fontsize=12)
plt.xlim([0, 5])
plt.ylim([0, 1])
plt.legend(loc=4)

imgName = "percentusersresptime"
plt.savefig(imgName)
plt.show()
