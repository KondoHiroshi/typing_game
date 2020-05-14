##

import word_house
import time
import readchar
import platform

class typing(object):
    def __init__(self):
        self.gametime = 0
        pass

    def select_word(self,genru):
        word = word_house.select_list(genru)
        return word

    def beep(self,freq, dur=100):
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(freq, dur)
        else:
            import os
            os.system('play -n synth %s sin %s' % (dur/1000, freq))

    def score():
        pass

    def check_result(self):
        level_dic = {
        "SS": "神",
        "S": "仏" ,
        "A": "超人" ,
        "B": "達人" ,
        "C": "一般人" ,
        "D": "素人" ,
        "E": "２歳児" ,
        "F": "人生やりなおした方がいい" ,
        "G": "ごきぶり"
        }
        count = self.miss_count
        numsum = sum(self.word_num)
        miss = len(count)
        speed = float((numsum-miss)/(self.gametime-sum(self.word_count)))
        if speed >= 5:
            level = "SS"
        if speed < 5.0 and speed >= 4.5 :
            level = "S"
        if speed < 4.5 and speed >= 4.0 :
            level = "A"
        if speed < 4.0 and speed >= 3.5:
            level = "B"
        if speed < 3.5 and speed >= 3.0:
            level = "C"
        if speed < 3.0 and speed >= 2.5:
            level = "D"
        if speed < 2.5 and speed >= 2.0:
            level = "E"
        if speed < 2.0:
            level = "F"

        print("==== Total time ====")
        print(str(self.game_t)+"[s]")
        print("==== Total word ====")
        print(str(numsum)+"[words]")
        print("==== Miss Times ====")
        print(str(miss))
        print("===== ACCURACY =====")
        print(str((1-round(miss/numsum,2))*100) + "%")
        print("==== Type speed ====")
        print(str(round(speed,2)) + "/s")
        print("====================")
        print("あなたのタイピング能力は、"+ str(level_dic[level]) + "レベルです。")
        pass

    def main(self):
        print("Select Stage")
        print("1 : TIME CHALENGE MODE")
        print("2 : ACCURACY MODE")
        genru = int(input("stage : 1 or 2 = "))

        if genru == 1:
            gametime = int(input("Select time = [s] "))
        elif genru == 2:
            gametime = 30
        else:
            pass
        self.gametime = gametime
        self.english(gametime)

        """
        print("Select Game mode")
        print("1 : English")
        print("2 : Japanese")
        type = int(input("stage : 1 or 2 ="))
        if type == 1:
            self.english(gametime)
        elif type == 2:
            self.japanese(gametime)
        else:
            pass
        """

    def japanese(self,gametime):
        self.game_t = gametime
        kana = word_house.kana()
        word_list = self.select_word(2)
        num = len(word_list)

        stime = time.time()

        self.miss_count = []
        self.word_count = []
        self.word_num = []

        while time.time() - stime < gametime:
            for i in range(num):
                if time.time() - stime > gametime:
                    break
                else:
                    pass
                word_single_list = list(word_list[i])
                print("===========")
                print(word_list[i])
                print("===========")
                num2 = len(word_single_list)
                self.word_num.append(num2)

                for ii in range(num2):
                    word = word_single_list[ii]
                    word_kana = kana[word]
                    now_list = word_single_list[:ii]
                    now_word = "".join(now_list)
                    print(now_word)

                    for i in list(word_kana):
                        while True:
                            word2 = readchar.readchar()
                            if word2 == word:
                                break
                            else:
                                print("\007")
                                self.miss_count.append(1)
                                continue
                continue
                #print("go to next word")
        print("======= Game End =====")
        print("======= RESULT =======")
        self.check_result()

    def english(self,gametime):
        self.game_t = gametime
        word_list = self.select_word(1)
        num = len(word_list)

        stime = time.time()

        self.miss_count = []
        self.word_count = []
        self.word_num = []

        while time.time() - stime < gametime:
            for i in range(num):
                if time.time() - stime > gametime:
                    break
                else:
                    pass
                word_single_list = list(word_list[i])
                print("===========")
                print(word_list[i])
                print("===========")
                num2 = len(word_single_list)
                self.word_num.append(num2)
                self.word_count.append(0.3)

                for ii in range(num2):
                    word = word_single_list[ii]

                    now_list = word_single_list[:ii]
                    now_word = "".join(now_list)
                    print(now_word)

                    while True:
                        word2 = readchar.readchar()
                        if word == word2:
                            break
                        else:
                            print("\007")
                            self.miss_count.append(1)
                            continue
                continue
                #print("go to next word")
        print("======= Game End =====")
        print("======= RESULT =======")
        self.check_result()



if __name__ == "__main__" :
    game = typing()
    game.main()
