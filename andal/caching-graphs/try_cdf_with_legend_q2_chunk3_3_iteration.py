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

azure_response_time_verizon = [1.3702080249786377, 3.8382961750030518, 0.4322547912597656, 0.4423360824584961, 0.23200702667236328, 0.3255331516265869, 0.18839621543884277, 0.29354000091552734, 0.02142810821533203, 0.021274089813232422, 0.021477937698364258, 0.011008024215698242, 0.009724140167236328, 0.010645866394042969, 0.2775700092315674, 0.006339073181152344, 0.006543159484863281, 0.6650168895721436, 0.1441500186920166, 0.11659884452819824, 3.4268720149993896, 3.0751290321350098, 0.0303800106048584, 0.05616307258605957, 0.05377912521362305, 0.018960952758789062, 0.48934412002563477, 0.1930229663848877, 0.018023014068603516, 0.01728200912475586, 0.017267942428588867, 0.01729297637939453, 3.0881340503692627, 0.6884357929229736, 0.07672405242919922, 0.048236846923828125, 0.04836606979370117, 0.04993295669555664, 0.023998022079467773, 0.023884057998657227, 0.0241391658782959, 0.3366670608520508, 0.3398289680480957, 0.039582014083862305, 0.1000981330871582, 0.09899115562438965, 0.09721589088439941, 0.02758002281188965, 0.028491973876953125, 0.029215097427368164, 0.13845396041870117, 0.13851189613342285, 0.1383199691772461, 0.01609516143798828, 0.016405105590820312, 0.016049861907958984, 0.027918100357055664, 0.02812814712524414, 0.02815699577331543, 0.0063800811767578125, 0.005713939666748047, 0.007133007049560547, 0.27332305908203125, 0.2591991424560547, 0.021963834762573242, 0.7802670001983643, 1.2205238342285156, 0.9458489418029785, 0.45876312255859375, 0.4553251266479492, 0.457287073135376, 0.01756596565246582, 0.017345905303955078, 0.01904010772705078, 0.015809059143066406, 0.01548314094543457, 0.015832185745239258, 0.2545619010925293, 0.2936739921569824, 0.015893936157226562, 0.034880876541137695, 0.032521963119506836, 0.007989168167114258, 0.031601905822753906, 0.03191208839416504, 0.031723976135253906, 1.8331398963928223, 0.6432478427886963, 0.8339879512786865, 0.14178204536437988, 0.0760641098022461, 0.06806612014770508, 0.1496431827545166, 0.11722683906555176, 0.09915995597839355, 0.09745502471923828, 0.09947013854980469, 0.09909796714782715, 0.3840792179107666, 0.028274059295654297, 0.026651859283447266, 0.004971027374267578, 0.005620002746582031, 0.005081892013549805, 1.7501270771026611, 0.4182109832763672, 0.28631114959716797, 0.020920991897583008, 0.020313024520874023, 0.02086496353149414, 0.041198015213012695, 0.036466121673583984, 0.037832021713256836, 0.13801097869873047, 0.13819217681884766, 0.13809609413146973, 0.9109790325164795, 0.8195741176605225, 0.8354001045227051, 0.011183023452758789, 0.011039018630981445, 0.01178121566772461, 0.052802085876464844, 0.0603179931640625, 0.05677986145019531, 0.0059359073638916016, 0.005847930908203125, 0.007668018341064453, 0.3668360710144043, 0.40962910652160645, 0.06656694412231445, 0.02387094497680664, 0.024448156356811523, 0.023441076278686523, 0.46001291275024414, 0.4846639633178711, 0.4551990032196045, 0.04816603660583496, 0.04827404022216797, 0.048229217529296875, 0.464061975479126, 0.10810303688049316, 0.08680891990661621, 0.0888829231262207, 0.09032011032104492, 0.022186994552612305, 0.12271904945373535, 0.11974620819091797, 0.012218952178955078, 0.03171110153198242, 0.03153800964355469, 0.03219199180603027, 0.03249502182006836, 0.032447099685668945, 0.009439945220947266, 0.00615692138671875, 0.00613093376159668, 0.008285999298095703, 0.006418943405151367, 0.006227016448974609, 0.006386995315551758]

azure_response_time_akamai = [0.032036781311035156, 0.03230786323547363, 0.03119802474975586, 0.47913193702697754, 0.10202598571777344, 0.10105204582214355, 0.40216803550720215, 0.2838170528411865, 0.2796649932861328, 2.4072771072387695, 1.2508518695831299, 0.6526620388031006, 0.008463859558105469, 0.008198022842407227, 0.0081939697265625, 1.7105259895324707, 0.5570080280303955, 0.46849894523620605, 0.34291505813598633, 0.34174108505249023, 0.34427618980407715, 0.04771995544433594, 0.04847097396850586, 0.04822587966918945, 0.4620800018310547, 0.6093900203704834, 0.46718621253967285, 0.865800142288208, 0.725412130355835, 0.7251451015472412, 0.8046519756317139, 3.005980968475342, 0.6100239753723145, 0.1701209545135498, 0.04871487617492676, 0.04993581771850586, 0.048544883728027344, 0.05260300636291504, 0.04960203170776367, 0.0589139461517334, 0.06558489799499512, 0.05720019340515137, 0.4888491630554199, 0.022644996643066406, 0.022452116012573242, 0.06889891624450684, 0.024992942810058594, 0.02084207534790039, 0.5986921787261963, 0.012600898742675781, 0.012351036071777344, 0.011753082275390625, 0.011561870574951172, 0.011245012283325195, 0.010974884033203125, 0.010909795761108398, 0.010286092758178711, 0.026417016983032227, 0.02128887176513672, 0.018718957901000977, 0.6936099529266357, 0.022571086883544922, 0.02275395393371582, 0.05741596221923828, 0.05791211128234863, 0.058072805404663086, 0.33307909965515137, 0.11952710151672363, 0.11979985237121582, 0.04522299766540527, 0.05330514907836914, 0.0469820499420166, 0.06187009811401367, 0.06264781951904297, 0.062091827392578125, 0.024374961853027344, 0.024605989456176758, 0.02424001693725586, 0.4119999408721924, 0.22423601150512695, 0.5188181400299072, 0.17023301124572754, 0.050740957260131836, 0.05267500877380371, 0.0075778961181640625, 0.007652997970581055, 0.021079063415527344, 0.6610548496246338, 0.11892104148864746, 0.11875200271606445, 0.609544038772583, 0.013108968734741211, 0.013128995895385742, 0.2639601230621338, 0.12071084976196289, 0.11913800239562988, 0.03133702278137207, 0.03168082237243652, 0.031638145446777344, 0.19205904006958008, 0.18838882446289062, 0.18722295761108398, 0.13077211380004883, 0.013125896453857422, 0.01305079460144043, 1.2738661766052246, 0.05569887161254883, 0.06083106994628906, 0.02529311180114746, 0.02418994903564453, 0.024161815643310547, 0.011539936065673828, 0.011852025985717773, 0.012455940246582031, 0.3086130619049072, 0.15136480331420898, 0.20572686195373535, 0.27233290672302246, 0.18656396865844727, 0.1870889663696289, 0.02899003028869629, 0.011348962783813477, 0.01040792465209961, 0.22607111930847168, 0.2274610996246338, 0.21668577194213867, 1.3082389831542969, 1.4414429664611816, 1.0719919204711914, 0.7174191474914551, 0.012942790985107422, 0.008056879043579102, 0.2442328929901123, 0.21698689460754395, 0.22684693336486816, 0.11249089241027832, 0.01911306381225586, 0.0188601016998291, 0.34378814697265625, 0.04219412803649902, 0.042874813079833984, 0.6197669506072998, 0.061914920806884766, 0.06211209297180176, 0.01770186424255371, 0.017860889434814453, 0.01708197593688965, 0.13515400886535645, 0.10684800148010254, 0.08787107467651367, 0.0527040958404541, 0.05416607856750488, 0.051811933517456055, 0.04561495780944824, 0.04947614669799805, 0.04523205757141113, 0.2009601593017578, 0.08713889122009277, 0.0950460433959961, 0.06242799758911133, 0.022989988327026367, 0.02253413200378418]

amazon_response_time = [0.020898818969726562, 0.010483026504516602, 0.01081395149230957, 0.017885923385620117, 0.01943182945251465, 0.019237995147705078, 0.13884520530700684, 0.14267206192016602, 0.1386110782623291, 0.09954714775085449, 0.15278196334838867, 0.06469011306762695, 0.04219508171081543, 0.01299595832824707, 0.01085209846496582, 0.024534940719604492, 0.024235010147094727, 0.027926206588745117, 0.01870107650756836, 0.017307043075561523, 0.01881694793701172, 0.3035459518432617, 0.11199212074279785, 0.09595203399658203, 1.0355949401855469, 0.8550260066986084, 0.5342710018157959, 0.05077695846557617, 0.022974014282226562, 0.025114059448242188, 0.02216196060180664, 0.013345003128051758, 0.011569023132324219, 0.01526498794555664, 0.014973878860473633, 0.014225959777832031, 0.013914823532104492, 0.012905120849609375, 0.020907163619995117, 0.04391789436340332, 0.044944047927856445, 0.04260993003845215, 0.010692119598388672, 0.01791214942932129, 0.01013803482055664, 0.016089916229248047, 0.010298967361450195, 0.010074853897094727, 0.01771402359008789, 0.01376795768737793, 0.01295614242553711, 0.03247499465942383, 0.014075994491577148, 0.009821176528930664, 0.01244807243347168, 0.009556055068969727, 0.01296687126159668, 0.0626070499420166, 0.04620003700256348, 0.04606890678405762, 0.007174968719482422, 0.009614944458007812, 0.009586095809936523, 1.2181508541107178, 0.5224509239196777, 1.2430329322814941, 0.04766988754272461, 0.024664878845214844, 0.025303125381469727, 0.03572201728820801, 0.03443002700805664, 0.037407875061035156, 0.07440710067749023, 0.08135700225830078, 0.07144308090209961, 0.3242640495300293, 0.3668708801269531, 0.3209569454193115, 0.010811090469360352, 0.008555173873901367, 0.00978708267211914, 0.6761789321899414, 0.020392894744873047, 0.017385005950927734, 0.07736778259277344, 0.0704500675201416, 0.07354402542114258, 0.6960229873657227, 0.694605827331543, 0.7153820991516113, 0.16202402114868164, 0.029532909393310547, 0.03293204307556152, 0.020657062530517578, 0.018162965774536133, 0.020694971084594727, 0.01505899429321289, 0.016685009002685547, 0.013434886932373047, 0.06256484985351562, 0.06316184997558594, 0.01968097686767578, 0.09782099723815918, 0.09794402122497559, 0.09757804870605469, 0.07806015014648438, 0.06128501892089844, 0.06618213653564453, 0.41755199432373047, 0.3418240547180176, 0.32111597061157227, 0.03379702568054199, 0.07031917572021484, 0.06466412544250488, 0.34357500076293945, 0.01749587059020996, 0.009103059768676758, 0.13927698135375977, 0.1400918960571289, 0.13903403282165527, 0.051680803298950195, 0.03621101379394531, 0.037429094314575195, 0.011850118637084961, 0.011687994003295898, 0.01051187515258789, 0.06133890151977539, 0.023240089416503906, 0.02367711067199707, 0.04371500015258789, 0.04564309120178223, 0.04654192924499512, 0.02259516716003418, 0.022455930709838867, 0.02293109893798828, 0.12004709243774414, 0.11509895324707031, 0.11417293548583984, 0.036624908447265625, 0.0341191291809082, 0.03218412399291992, 0.06160902976989746, 0.02957606315612793, 0.03838181495666504, 0.010663032531738281, 0.008183002471923828, 0.009804010391235352, 0.020354032516479492, 0.018174171447753906, 0.01736307144165039, 0.7168200016021729, 0.7097921371459961, 0.6961078643798828, 0.06979513168334961, 0.0698249340057373, 0.06991720199584961, 0.07085108757019043, 0.06891894340515137, 0.06991696357727051, 0.03479313850402832, 0.012426137924194336, 0.014805078506469727]

fig, ax = plt.subplots()

draw_cdf(google_response_time, styles[0], "Google Cloud CDN")
draw_cdf(azure_response_time_verizon, styles[1], "Azure CDN (Verizon)")
draw_cdf(azure_response_time_akamai, styles[2], "Azure CDN (Akamai)")
draw_cdf(amazon_response_time, styles[3], "Amazon CloudFront")

ax.set_xlabel(r'Response time at the start, middle & end of the experiment (Chunk 3)', fontsize=12)
ax.set_ylabel(r'Percentage of PlanetLab users', fontsize=12)
plt.xlim([0, 5])
plt.ylim([0, 1])
plt.legend(loc=4)

imgName = "percentusersresptime"
plt.savefig(imgName)
plt.show()
