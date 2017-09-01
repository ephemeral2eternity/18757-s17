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

azure_response_time_verizon = [3.868006944656372, 0.4967350959777832, 0.8884530067443848, 0.022755861282348633, 0.0124359130859375, 0.8350059986114502, 0.39629411697387695, 3.4152729511260986, 0.24143600463867188, 1.1243789196014404, 0.019134998321533203, 0.5750858783721924, 0.32875800132751465, 0.02518606185913086, 0.9730441570281982, 0.45563197135925293, 0.320634126663208, 1.3409028053283691, 0.025674819946289062, 0.3156139850616455, 0.007899999618530273, 0.9108140468597412, 0.7674160003662109, 0.20074200630187988, 0.027215003967285156, 0.0177609920501709, 0.5104320049285889, 0.3465769290924072, 0.03288912773132324, 0.7293119430541992, 0.7356820106506348, 0.5893809795379639, 0.099822998046875, 0.5215210914611816, 0.007303953170776367, 1.029383897781372, 0.0216519832611084, 0.35130786895751953, 0.13961195945739746, 0.43355393409729004, 0.3134641647338867, 0.05647611618041992, 0.017661094665527344, 0.40199899673461914, 0.29987502098083496, 0.6661829948425293, 1.3189551830291748, 0.4429440498352051, 0.23591303825378418, 14.568732976913452, 0.40909409523010254, 0.010421037673950195, 0.6507930755615234, 0.008253097534179688]

azure_response_time_akamai = [0.3951148986816406, 0.6605570316314697, 0.714257001876831, 2.2852258682250977, 0.07421302795410156, 1.6702589988708496, 3.74129581451416, 0.5285050868988037, 0.6700301170349121, 0.7914719581604004, 0.5358560085296631, 0.9046499729156494, 0.32633519172668457, 0.0834808349609375, 1.1595139503479004, 0.524604082107544, 0.8338630199432373, 0.3346090316772461, 0.015960216522216797, 0.09988784790039062, 1.0265071392059326, 0.3504981994628906, 0.9192409515380859, 0.04752492904663086, 0.06344223022460938, 0.03601789474487305, 1.000230073928833, 0.7477450370788574, 0.2106781005859375, 0.5603969097137451, 0.7168600559234619, 0.637516975402832, 0.033499956130981445, 0.2660360336303711, 0.4727001190185547, 0.5129649639129639, 0.3003809452056885, 0.012352943420410156, 3.1074719429016113, 1.4905500411987305, 1.1053950786590576, 0.6044051647186279, 1.1318731307983398, 1.0893959999084473, 1.5182709693908691, 0.540510892868042, 3.0089590549468994, 1.1422441005706787, 0.16769695281982422, 0.8901159763336182, 0.05920600891113281, 0.4183201789855957, 0.7917881011962891, 0.4023110866546631]

amazon_response_time = [0.3493509292602539, 0.08656597137451172, 0.14359188079833984, 0.6379489898681641, 0.2929069995880127, 0.06438684463500977, 0.31141090393066406, 0.4034700393676758, 0.9425399303436279, 0.45599889755249023, 0.6377830505371094, 0.3152289390563965, 0.32305097579956055, 0.05581092834472656, 0.24599409103393555, 2.5534961223602295, 0.01748490333557129, 0.3616061210632324, 0.09871792793273926, 1.3832249641418457, 0.02453303337097168, 1.9776790142059326, 1.6605839729309082, 0.32185888290405273, 0.6120288372039795, 0.6104080677032471, 0.01960587501525879, 0.8753008842468262, 0.680549144744873, 1.9200689792633057, 0.30690598487854004, 0.0355679988861084, 0.18203401565551758, 0.08583784103393555, 0.40790700912475586, 0.2725338935852051, 0.468703031539917, 0.355849027633667, 0.4108870029449463, 1.2122859954833984, 0.2956058979034424, 0.594980001449585, 1.2399489879608154, 0.31847310066223145, 0.028089046478271484, 1.3385097980499268, 0.04295206069946289, 0.4495120048522949, 0.05712294578552246, 0.03364300727844238, 0.7338738441467285, 0.0825951099395752, 1.0415339469909668, 0.3202841281890869] 

fig, ax = plt.subplots()

draw_cdf(google_response_time, styles[0], "Google Cloud CDN")
draw_cdf(azure_response_time_verizon, styles[1], "Azure CDN (Verizon)")
draw_cdf(azure_response_time_akamai, styles[2], "Azure CDN (Akamai)")
draw_cdf(amazon_response_time, styles[3], "Amazon CloudFront")

ax.set_xlabel(r'Response time at the beginning of the experiment (Chunk 1)', fontsize=12)
ax.set_ylabel(r'Percentage of PlanetLab users', fontsize=12)
plt.xlim([0, 5])
plt.ylim([0, 1])
plt.legend(loc=4)

imgName = "percentusersresptime"
plt.savefig(imgName)
plt.show()
