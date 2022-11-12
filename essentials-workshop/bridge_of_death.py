#ARTHUR: The Bridge of Death! 
import random
import sys
import codecs
import os

questions = ['What... is your name? ','What... is your favorite color? ','What... is your quest? ','What... is the air-speed velocity of an unladen swallow? ','What... is the capital of Assyria? ']

secret_word1 = "6e6f"
secret_word2 = "6166726963616e206f7220657572"
secret_word3 = "6173737572"
secret_word4 = """x\x9cmOAn\xc20\x10\xbc\xe7\x15\x93S\xc5\xa1\x91\xca\xa1\xd7*mL\x83J\x01\xa1\xb4\x88\xa3!Kb\xc5]Gq\x0c\xe4\xf7\xb5\t=T\xc2kYZ\xef\xcc\xec\xcc\xb6\x96\xfd\x0b0Gi\xf8\xa1G\xc3\xe6\x8c\xde\xff%I\x824\x9c\xe8~\xe5\xb7\x8a\xb6b\xb1@\xb6Z\x8a\x04\xbb\xd5\x17\xf2\xf4[ \x133\x91\x16"C\x91\x0b\xbcn\xe6\xd9\xbb\xf8\x10b-6q\x14\xe5\xd4\x11\x94\x85D>_\x168\x9a\xce\xef#\xbc\x15\xb3$\x8a\x9e&\xd8\x19\x87\xb3\xd2\x1a\x96\x08ti\xb5Q\xbd\xe2\n\x8a[\xd7\xfb\x17\xeb\xa1\xaf\rO!+\xe9;\x7f\xff\xe8\xc0\xa7\xec\x9ak\xdb\xca\x8a\xc2h0\xae\xc3\xde\x98&\x8e\xa6\x13\x14u\xd8\xfd#\x07\xec\t\xc6\xe3:\xd4\x8a{\x0b\xad\x1a\xf2<\xef\xcas\xc6\x01\x1b~l\x87\xad\xec\xfcT\xee\xed?1\x1b#-O\x92\x0fT\xc2Y\xf2\x10g\x9d\xd4z\x80\xaa\xd8tA\x8a,\x8d<\xc9%\xce\xc6\xdb\xa2\xcbA;\xabN\x14`\x8cQ;\xc1Lq\x19\xe2\x05\xd7\xa3\x99[\xa2+\xfb \x19\x9a<gL\xa5\xe5\x10\xb0GE\xba\x84ad>\xcas\xfc\x0bN\xf7\x8f\xc1"""

os.system("clear")
print "Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see." 

for qcount in range(3):
    qtxt = random.choice(questions)
    questions.remove(qtxt)
    answer = raw_input(qtxt)
    if secret_word1.decode('hex') in answer.lower() and "color" in qtxt:
        print "You are cast into the Gorge of Eternal Peril"
        sys.exit(1)
    if "swallow" in qtxt:
        if secret_word2.decode('hex') in answer.lower():
            print secret_word4.decode("zip")
        else:
            print "You are cast into the Gorge of Eternal Peril"
        sys.exit(1)
    if secret_word3.decode('hex') <> answer.lower() and "Assyria" in qtxt:
        print "You are cast into the Gorge of Eternal Peril"
        sys.exit(1)

print "Right. Off you go."


