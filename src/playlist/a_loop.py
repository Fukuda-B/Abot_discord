"""a_loopで再生する楽曲一覧"""
# https://www.youtube.com/watch?v= は https://youtu.be/におきかえること

yoasobi = [
    # YOASOBI
    'https://youtu.be/wJQ9ig_d8yY', # 大正浪漫
    'https://youtu.be/mnta9Pp2LqA', # ラブレター
    'https://youtu.be/Eoe5IZHbarQ', # 怪物(English ver)
    'https://youtu.be/BS5YyieaXgc', # 三原色(English ver)
    'https://youtu.be/nhOhFOoURnE', # 三原色
    'https://youtu.be/b3K61cQ8_fg', # 夜に駆ける(English ver)
]

first_take = [
    # THE FIRST TAKE
    'https://youtu.be/5IU3DgA9LwY', # 気まぐれロマンティック-いきものがかり
    'https://youtu.be/41c9vRZ4mB4', # サウダージ-ポルノグラフィティ
    'https://youtu.be/z0uDEu-QQYM', # PARADOX-雨宮天
    'https://youtu.be/impSuIygMiQ', # 再会-LiSAxUru
    'https://youtu.be/bGx7WV96frM', # 366日-HY
    'https://youtu.be/8UP7V0UGR4c', # 正しくなれない-ずっと真夜中でいいのに。
    'https://youtu.be/Wdll9P9icJU', # 秒針を噛む-ずっと真夜中でいいのに。
    'https://youtu.be/qLHUlGk3W9M', # Catch the Moment-LiSA
    'https://youtu.be/4Q9DWZLaY2U', # 炎-LiSA
    'https://youtu.be/r-4XumkB2Yg', # ANIMA-ReoNa
    'https://youtu.be/1R5jREc_joY', # I will-藍井エイル
    'https://youtu.be/hNEC1NEfqLA', # IGNITE-藍井エイル
    'https://youtu.be/qIBWRPqJcGQ', # DADDY!DADDY!DO!-鈴木雅之
    'https://youtu.be/S-JC_oSwoY0', # 猫-DISH//
    'https://youtu.be/j1hft9Wjq9U', # 夜に駆ける-YOASOBI
    'https://youtu.be/GsLsBs4oW30', # unravel-TK from 凛として時雨
    'https://youtu.be/f8XUgBMSDWo', # 2億4千万の瞳 -エキゾチック・ジャパン-郷ひろみ
]

porno_g = [
    # ポルノグラフィティ
    'https://youtu.be/Th7MAZYFIMc', # THE DAY
    'https://youtu.be/0_Hns1hqBoA', # オー！リバル
    'https://youtu.be/chdM-Oo1WIY', # 瞬く星の下で
    'https://youtu.be/DXo_xX_Hqro', # メリッサ
    'https://youtu.be/zQq_cgH5_AI', # アゲハ蝶
    'https://youtu.be/VeYrhSSQuzI', # アゲハ蝶(Live ver)
    'https://youtu.be/lzsB4eKPdJI', # サウダージ
    'https://youtu.be/q_8ulbgIF5w', # アポロ
    'https://youtu.be/8ClfuCqHgvs', # ミュージック・アワー
]

anime = [
    'https://youtu.be/Aumyo47GuWQ', # 天鏡のアルデラミン-岸田教団＆THE明星ロケッツ
    'https://youtu.be/qVEVRTUAy0M', # GATE～それは暁のように～-岸田教団&THE明星ロケッツ
    'https://youtu.be/XLL68BLBLZk', # GATEⅡ～世界を超えて～-岸田教団&THE明星ロケッツ
    'https://youtu.be/E99MiQkKCpA', # HIGHSCHOOL OF THE DEAD-岸田教団&THE明星ロケッツ
    'https://youtu.be/P0fS2GyRaJQ', # ストライク・ザ・ブラッド-岸田教団&THE明星ロケッツ
    'https://youtu.be/5hxEwZWBflI', # EVERYBODY! EVERYBODY!-芹澤 優 with DJ KOO & MOTSU
    'https://youtu.be/8ZBxF1fqFU8', # YOU YOU YOU-芹澤 優 with DJ KOO & MOTSU
    'https://youtu.be/N_l_CVhMX4c', # デビきゅー-芹澤優
    'https://youtu.be/KzKm01OflVw', # アルティメット☆MAGIC-i☆Ris
    'https://youtu.be/E60gP_ozRmQ', # FANTASTIC ILLUSION-i☆Ris
    'https://youtu.be/L1roHIMK3tY', # DeCIDE-SUMMONERS 2+
    'https://youtu.be/4ow4ceGE0Wk', # EVERYBODY! EVERYBODY!-芹澤 優 with DJ KOO & MOTSU # short
    'https://youtu.be/_DBBENE0Q8E', # No! No! Satisfaction!-DA PUMP
    'https://youtu.be/qiSlWXCR5RU', # デビきゅー-芹澤 優 # short
    'https://youtu.be/CpT00cqD6SY', # Magical Babyrinth-DA PUMP
    'https://youtu.be/iwIZpIK4UFU', # ココロショータイム-天月
    'https://youtu.be/86QIn8SmN5k', # ココロショータイム-天月 # short
    'https://youtu.be/zOzy79zzEWA', # 凛-ASCA
    'https://youtu.be/Be-Gb9fum7w', # RESISTER-ASCA
    'https://youtu.be/TInRX_sIFGQ', # CHAIN-ASCA
    'https://youtu.be/Cf7piHkO_VU', # Howling-ASCA
    'https://youtu.be/0me_7B2rRIE', # SHINY DAYS-亜咲花
    'https://youtu.be/uwph0dv9E6U', # Sincerely-TRUE
    'https://youtu.be/lJ9twtxWieM', # WILL-TRUE
    'https://youtu.be/UKU4B05fPck', # みちしるべ-茅原実里
    'https://youtu.be/ZeSISQ9v4uc', # Violet Snow-結城アイラ
    'https://youtu.be/JLQTiFwBVyI', # Storyteller-TRUE
    'https://youtu.be/x2wUyP0l4bw', # Another colony-TRUE
    'https://youtu.be/FMln2YjLbIM', # Blast!-TRUE
    'https://youtu.be/X8QTW2gbME0', # colorless wind ~Piano ver.~-結城アイラ
    'https://youtu.be/D94MDszmlWg', # まほうのかぜ-熊田茜音
    'https://youtu.be/BxgIXq8H5n8', # colourless wind-結城アイラ
    'https://youtu.be/7lH7csKBnzY', # 一番の宝物-Lia
    'https://youtu.be/2sPDPr3S7Zg', # days-じん ft. Lia
    'https://youtu.be/wtlu84ARGwY', # 絆-kizunairo-色-Lia
    'https://youtu.be/_NZWYL3EFLk', # My Soul, Your Beats!-Lia
    'https://youtu.be/WhRsyIGN-cA', # Bravely You-Lia
    'https://youtu.be/t8vB1Xfj00E', # 君の知らない物語-Lia
    'https://youtu.be/NcDeFT1r83o', # 乙女のルートはひとつじゃない！-angela
    'https://youtu.be/uh8mL30Equk', # 君氏危うくも近うよれ-A応P
    'https://youtu.be/rxyKfLmZiOg', # 全力バタンキュー-A応P
    'https://youtu.be/iB4JdY2mQYc', # はなまるぴっぴはよいこだけ-A応P
    'https://youtu.be/3FlVlOyHIKM', # Another World-A応P
    'https://youtu.be/-_425NvP51w', # Brand new diary-熊田茜音
    'https://youtu.be/XIIqgWUtPpk', # STORYSEEKER-STEREO DIVE FOUNDATION
    'https://youtu.be/W2_V7X6fJ18', # Nameless Story-寺島拓篤
    'https://youtu.be/upKRAWGYuLE', # メグルモノ-寺島拓篤
    'https://youtu.be/FfwJ-ht4MfU', # starry-綾野ましろ
    'https://youtu.be/tXsqImRzm80', # 灯火のまにまに-東山奈央
    'https://youtu.be/94W5nENM0iM', # DEAREST DROP-田所あずさ
    'https://youtu.be/TIe-pQNAiNA', # SHINY DAYS-東山奈央
    'https://youtu.be/wdDL6IxOERk', # Against.-石原夏織
    'https://youtu.be/iUWng4JaQhA', # 歩いていこう！-東山奈央
    'https://youtu.be/_o5AmD3pykQ', # for...-逢田梨香子
    'https://youtu.be/fj-yX-kJ-fQ', # UP-DATE × PLEASE!!! 9姉妹 全員Ver
    'https://youtu.be/FCGCl8t4ENA', # UP-DATE × PLEASE!!!  ver 1.7.8-早乙女一千花・七樹・八雲(内山夕実/本渡楓/河瀬茉希)
    'https://youtu.be/yrFYVd8BiL8', # 青空のラプソディ-スーパーちょろゴンず ver.-スーパーちょろゴンず
    'https://youtu.be/39NPPMceSek', # メグメル-riya
    'https://youtu.be/7YlDQpHXZPk', # リフレクティア-eufonius
    #'https://youtu.be/5K9I7c9gQNg', # 比翼の羽根-eufonius # heroku X
    'https://soundcloud.com/despot0130/20mmzsypixms', # 比翼の羽根-eufonius
    'https://youtu.be/FIxyZLKFnpQ', # ココロニツボミ-eufonius
    'https://youtu.be/bqpEAIVqT6M', # YOU-YURIA
]

anime_2021_summer = [
    'https://youtu.be/XCs7FacjHQY', # 愛のシュプリーム！-fhána
    'https://youtu.be/J6_8EYrgk2Y', # めいど・うぃず・どらごんず❤︎-スーパーちょろゴンず
    'https://youtu.be/-SdEFi3yqOc', # New story-高野麻里佳
    'https://youtu.be/oAyY_NhZgqE', # Elder flower-大西亜玖璃
    'https://youtu.be/q8TGietS5Q0', # Like Flames-MindaRyn
    'https://youtu.be/bF2iwhO5tyQ', # HELLO HORIZON-水瀬いのり
    'https://youtu.be/r7WgNxoupO0', # カザニア-愛美
    'https://youtu.be/wdFAdCBcHVY', # Dream on-宮野真守
    'https://youtu.be/vtuxTWxQ_cc', # Missing Promise-鈴木このみ
    'https://youtu.be/Nf8Oa-GGTfQ', # アンダンテに恋をして！-angela
    'https://youtu.be/traMXzjqYTA', # たゆたえ、七色-ARCANA PROJECT
    'https://youtu.be/ByFGYwznw2c', # 月海の揺り籠-Mia REGINA
    'https://youtu.be/pP-cAsbjkys', # ココロハヤル-熊田茜音
    'https://youtu.be/7GBn6IuTQ6w', # ギャンブル-syudou
    'https://youtu.be/wS-PCSv7r2I', # ビューティフル・ドリーマー-Ezoshika Gourmet Club
    'https://youtu.be/RH8WtbhURyM', # 夜を越える足音-ミテイノハナシ
    'https://youtu.be/sCJVFAZ2hL8', # No Continue-鬼頭明里
    'https://youtu.be/Y0z_2C2LFfE', # Soul salvation-林原めぐみ
    'https://youtu.be/vryLhrwJAfA', # 101-三月のパンタシア
    'https://youtu.be/qx0JtUvIWtY', # 星のオーケストラ-saji
    'https://youtu.be/MvvyswgqkrU', # 染み-HOWL BE QUIET
    'https://youtu.be/ZRKLpHqwHjw', # ワールドイズマイン-ハンブレッダーズ
    'https://youtu.be/O1bhZgkC4Gw', # Cry Baby-Official髭男dism
    'https://youtu.be/RK8qJfYMlrM', # Naughty Love-女神寮生
    'https://youtu.be/ylxvggdxGjM', # ゼッタイ！キミ宣言♡-女神寮生
    'https://youtu.be/P0_-hE1OnBA', # ここから先は歌にならない-Poppin'Party
    'https://youtu.be/bsZ3WxnJaWw', # 可能性-Argonavis
    'https://youtu.be/1zEcaGwbHZs', # 空と虚-Sasanomaly（ササノマリイ）
    'https://youtu.be/YCIBb0ROXAo', # 満月とシルエットの夜-坊ちゃん（CV. 花江夏樹）＆アリス（CV. 真野あゆみ）
    'https://youtu.be/Ql6ouR2NqN0', # 夜想曲(ノクターン)-アリス（CV. 真野あゆみ）
    'https://youtu.be/0tKbJbLA1HM', # 雷火-ナナヲアカリ
    'https://youtu.be/3a7KuNsrwog', # Dark spiral journey-Q-MHz feat. 鈴華ゆう子
    'https://youtu.be/6SdxOgaEzDU', # Merry-Go-Round-MAN WITH A MISSION
]

ikimono = [
    # いきものがかり
    'https://youtu.be/5XCSt_0lwOE', # 気まぐれロマンティック
    'https://youtu.be/FLs2faYqoNU', # 熱情のスペクトラム
    'https://youtu.be/lz8frtP6_kk', # YELL
    'https://youtu.be/VZBU8LvZ91Q', # ありがとう
    'https://youtu.be/KpsJWFuVTdI', # ブルーバード
    'https://youtu.be/viQPExRmxdk', # じょいふる
    'https://youtu.be/fLcSUrlS9us', # キミがいる
    'https://youtu.be/61z-cqg28R8', # SAKURA
]

yorushika = [
    # ヨルシカ
    'https://youtu.be/-VKIqrvVOpo', # ただ君に晴れ
    'https://youtu.be/KTZ-y85Erus', # だから僕は音楽を辞めた
    'https://youtu.be/F64yFFnZfkI', # 言って。
    'https://youtu.be/9lVPAWLWtWc', # 花に亡霊
    'https://youtu.be/t7MBzMP4OzY', # ヒッチコック
    'https://youtu.be/Sw1Flgub9s8', # 春泥棒
    'https://youtu.be/PWbRleMGagU', # 雨とカプチーノ
    'https://youtu.be/j83OVgv6woA', # ノーチラス
    'https://youtu.be/DlyG6MAKUOA', # 心に穴が空いた
]
async def ck_data(ck_list:str):
    """要求されたものを返す"""
    if ck_list == 'yoasobi':
        use_play = yoasobi
    elif ck_list == 'first_take':
        use_play = first_take
    elif ck_list == 'porno':
        use_play = porno_g
    elif ck_list == 'anime':
        use_play = anime
    elif ck_list == 'a_2021_summer':
        use_play = anime_2021_summer
    elif ck_list == 'ikimono':
        use_play = ikimono
    elif ck_list == 'yorushika':
        use_play = yorushika
    else:
        use_play = yoasobi + first_take + porno_g + anime + anime_2021_summer + ikimono + yorushika
    
    return use_play

if __name__ == '__main__' :
    print(yoasobi[0])
    print(len(yoasobi))