#!/usr/bin/python
# coding: utf-8

import sys
from weibo import APIClient
import webbrowser

reload(sys)
sys.setdefaultencoding('utf-8')

APP_KEY = '693325458' # app key
APP_SECRET = '12e2ed1ee9884b703e5436ec756f9ba9' # app secret
CALLBACK_URL = 'http://open.weibo.com/apps/693325458/privilege/oauth' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
# TODO: redirect to url

#webbrowser.open_new(url)
code= '9b28e9fafd4b36bc5e6a7f9231d47692'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

r = client.request_access_token(code)
access_token = r.access_token  # access token，e.g., abc123xyz456
expires_in = r.expires

client.set_access_token(access_token, expires_in)

#print client.statuses.user_timeline.get()
print client.statuses.update.post(status=u'豫章故郡，洪都新府。星分翼軫，地接衡廬。襟三江而帶五湖，控蠻荊而引甌越。物華天寶，龍光射牛斗之墟；人傑地靈，徐孺下陳蕃之榻。雄州霧列，俊彩星馳。臺隍枕夷夏之交，賓主盡東南之美。都督閻公之雅望，棨戟遙臨；宇文新州之懿範，襜帷暫駐。十旬休暇，勝友如雲。千里逢迎，高朋滿座。騰蛟起鳳，孟學士之詞宗；紫電青霜，王將軍之武庫。家君作宰，路出名區。童子何知？躬逢勝餞。\
時維九月，序屬三秋。潦水盡而寒潭清，煙光凝而暮山紫。儼驂騑於上路，訪風景於崇阿。臨帝子之長洲，得仙人之舊館。層臺聳翠，上出重霄；飛閣流丹，下臨無地。鶴汀鳧渚，窮島嶼之縈廻；桂殿蘭宮，即岡巒之體勢。\
披繡闥，俯雕甍。山原曠其盈視，川澤紆其駭矚。閭閻撲地，鐘鳴鼎食之家；舸艦迷津，青雀黃龍之舳。雲銷雨霽，彩徹區明。落霞與孤鶩齊飛，秋水共長天一色。漁舟唱晚，響窮彭蠡之濱；雁陣驚寒，聲斷衡陽之浦。\
遙襟甫暢，逸興遄飛。爽籟發而清風生，纖歌凝而白雲遏。睢園綠竹，氣凌彭澤之樽；鄴水朱華，光照臨川之筆。四美具，二難并。窮睇眄於中天，極娛遊於暇日。天高地迥，覺宇宙之無窮；興盡悲來，識盈虛之有數。望長安於日下，指吳會於雲間。地勢極而南溟深，天柱高而北辰遠。關山難越，誰悲失路之人；萍水相逢，盡是他鄉之客。懷帝閽而不見，奉宣室以何年？')