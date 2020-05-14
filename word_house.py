###word cllection##

import random

list_1 = [
"ogawahideo","ipython","ros","opu1.85m","Se1k0u",
"onishi", "muraoka", "ueda", "kondo", "maezawa", "1p85m",
"opuastronomy", "apples","ogawalab","spart",
"nro45m", "alma" , "matsutake", "python3", "github" , "sis"
"iv", "atacama", "aste", "chile", "orion", "venus", "sun",
"galactic", "radec", "mac", "windows", "ls" , "cd",
"Desktop", "yfactor" , "power", "radio", "astronomy",
"nobeyama", "harada", "telescope", "resolution", "filament",
"spectrum", "local", "bias", "optics", "amp", "numpy", "matplotlib",
"casa", "casaviewer", "clouds", "radio", "freq", "GHz", "spectrometer",
"power", "voltage", "current"
 ]

list_2 = [
"よろしくおねがいします"
]

kana_dic ={
"あ": ["a"],
"い": ["i"],
"う": ["a"],
"え": ["e"],
"お": ["o"],
"か": ["ka"],
"き": ["ki"],
"く": ["ku"],
"け": ["ke"],
"こ": ["ko"],
"さ": ["sa"],
"し": ["shi","si"],
"す": ["su"],
"せ": ["se"],
"そ": ["so"],
"た": ["ta"],
"ち": ["ti","chi"],
"つ": ["tu","tsu"],
"て": ["te"],
"と": ["to"],
"な": ["na"],
"に": ["ni"],
"ぬ": ["nu"],
"ね": ["ne"],
"の": ["no"],
"は": ["ha"],
"ひ": ["hi"],
"ふ": ["hu"],
"へ": ["he"],
"ほ": ["ho"],
"ま": ["ma"],
"み": ["mi"],
"む": ["mu"],
"め": ["me"],
"も": ["mo"],
"や": ["ya"],
"ゆ": ["yu"],
"よ": ["yo"],
"ら": ["ra"],
"り": ["ri"],
"る": ["ru"],
"れ": ["re"],
"ろ": ["ro"],
"わ": ["wa"],
"を": ["wo"],
"ん": ["nn"],
"が": ["ga"],
"ぎ": ["gi"],
"ぐ": ["gu"],
"げ": ["ge"],
"ご": ["go"],
"ざ": ["za"],
"じ": ["zi","ji"],
"ず": ["zu"],
"ぜ": ["ze"],
"ぞ": ["zo"],
"だ": ["da"],
"ぢ": ["di"],
"づ": ["du"],
"で": ["de"],
"ど": ["do"],
"ば": ["ba"],
"び": ["bi"],
"ぶ": ["bu"],
"べ": ["be"],
"ぼ": ["bo"],
"ぱ": ["pa"],
"ぴ": ["pi"],
"ぷ": ["pu"],
"ぺ": ["pe"],
"ぽ": ["po"]
}

def select_list(type):
    word = []
    if type == 1:
        word += list_1

    if type == 2:
        word += list_2
    random.shuffle(word)
    return word

def kana():
    return kana_dic
