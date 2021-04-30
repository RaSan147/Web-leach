from time import sleep
import re
import sys

wait_time = 0

class xprint:
    def __init__(self, *text, sep= ' ', wait_time=wait_time, end='\n') -> None:
        self.text= sep.join(map(str, text))
        self.wait_time=float(wait_time)
        self.end=str(end)

        self.slowtype()
    def text_styling_markup(self): #not in use
        ''' for custom text stypling like html
        print(tnt_helper('/<style= col: red>/ 69'))'''
        if '/<' not in self.text:
            return 0
        while re.search('/<(.*)>/', self.text):
            a = re.search('/<(.*?)>/', self.text)
            if a:
                style = a.group(1)

                self.text = self.text.replace(a.group(0), '')

    custom_type_codes = ['/u/', '/a/', '/y/', '/g/', '/k/', '/b/', '/r/', '/h/', '/bu/', '/hu/', '/=/']


    def tnt_helper(self):
        ''' i) custom_type_codes are used for custom commands to
        simplify the code
        ii) other text modifications are made here and passes optimized
        text for the typing and speaking engine respectively'''

        while re.search('==(.*)==', self.text):
            a = re.search('===([^(==)]*)===', self.text)
            if a:
                self.text = self.text.replace('==='+a.group(0)+'===', '/hu/' + a.group(1) + '/=/')
            a = re.search('==(.*?)==', self.text)
            if a:
                self.text = self.text.replace('=='+a.group(0)+'==', '/u/' + a.group(1) + '/=/')

        self.text_styling_markup()

    normal_tx="0;"
    ul_tx="4;"
    neg_tx="7;"
    bold_tx="1;"

    ash_c="30;"
    red_c="31;"
    green_c="32;"
    yello_c="33;"
    blue_c="34;"
    pink_c="35;"
    cayan_c="36;"
    white_c="37;"

    normal_b="40m"
    red_b="41m"
    green_b="42m"
    yello_b="43m"
    blue_b="44m"
    pink_b="45m"
    cayan_b="46m"
    white_b="47m"
    black_b="48m"



    default_style=[white_c, black_b,bold_tx]
    custom_style=[white_c, black_b,bold_tx]

    def slowtype(self):
        """main typing engine that prints inputted text
            slowly based on waiting time"""

        self.tnt_helper()
        #custom_type_codes = ['/u/', '/a/', '/y/', '/g/', '/k/', '/b/', '/r/', '/h/', '/bu/', '/hu/', '/=/']
        i=0
        while  i<len(self.text):
            asd=1
            if self.text[i]=='/' and '/' in self.text[i+2:i+5]:
                asd=100
                if self.text[i+1] in ('a','r','g','y','b','p','c','w','=','u','i','h','_'):
                    x=self.text[i+1]
                    if x=='a': self.custom_style[0]=self.ash_c
                    elif x=='r': self.custom_style[0]=self.red_c
                    elif x=='g': self.custom_style[0]=self.green_c
                    elif x=='y': self.custom_style[0]=self.yello_c
                    elif x=='b': self.custom_style[0]=self.blue_c
                    elif x=='p': self.custom_style[0]=self.pink_c
                    elif x=='c': self.custom_style[0]=self.cayan_c
                    elif x=='w': self.custom_style[0]=self.white_c
                    elif x=='=':
                        sys.stdout.write('\u001b[0m')
                        sys.stdout.flush()
                        self.custom_style[:]=self.default_style[:]
                    elif x=='u': self.custom_style[2]=self.ul_tx
                    elif x=='i': self.custom_style[2]=self.neg_tx
                    elif x=='h': self.custom_style[2]=self.bold_tx
                    #sys.stdout.write('\u001b['+custom_style[0]+';'+custom_style[1]+';'+custom_style[2]+'m')
                    if self.text[i+2] in ('a','r','g','y','b','p','c','w','u','i','h','_'):
                        x=self.text[i+2]
                        if x=='a': self.custom_style[1]= self.normal_b
                        elif x=='r': self.custom_style[1]=self.red_b
                        elif x=='g': self.custom_style[1]=self.green_b
                        elif x=='y': self.custom_style[1]=self.yello_b
                        elif x=='b': self.custom_style[1]=self.blue_b
                        elif x=='p': self.custom_style[1]=self.pink_b
                        elif x=='c': self.custom_style[1]=self.cayan_b
                        elif x=='w': self.custom_style[1]=self.white_b
                        elif x=='u': self.custom_style[2]=self.ul_tx
                        elif x=='i': self.custom_style[2]=self.neg_tx
                        elif x=='h': self.custom_style[2]=self.bold_tx
                        if self.text[i+3] in ('u','i','h'):
                            x=self.text[i+3]
                            if x=='u': self.custom_style[2]=self.ul_tx
                            elif x=='i': self.custom_style[2]=self.neg_tx
                            elif x=='h': self.custom_style[2]=self.bold_tx

                            if self.text[i+4]=='/':
                                i+=4
                                asd=123
                        elif self.text[i+3]=='/':
                            i+=3
                            asd=12
                    elif self.text[i+2]=='/':
                        i+=2
                        asd=10

                elif self.text[i+1]=='s':
                    if self.text[i+3]=='/':
                        try:
                            sleep(float(self.text[i+2]))
                            i+=3
                            asd=2
                        except: pass
                    elif self.text[i+4]=='/':
                        try:
                            sleep(float(self.text[i+2:i+4]))
                            i+=4
                            asd=2
                        except: pass
                    elif self.text[i+5]=='/':
                        try:
                            sleep(float(self.text[i+2:i+5]))
                            i+=5
                            asd=0
                        except: pass
            if asd>1:
                sys.stdout.write('\033['+self.custom_style[2]+self.custom_style[0]+self.custom_style[1])
                sys.stdout.flush()
            elif asd==1:
                sys.stdout.write(self.text[i])
                sys.stdout.flush()
                sleep(self.wait_time)
            i+=1




        sys.stdout.write(self.end)
        sys.stdout.flush()
