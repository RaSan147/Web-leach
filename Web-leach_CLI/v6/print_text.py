from time import sleep, time
import re
import sys

wait_time = 0

class XprintClass:
    def __init__(self) -> None:
        self.normal_tx="0;"
        self.ul_tx="4;"
        self.neg_tx="7;"
        self.bold_tx="1;"

        self.ash_c="30;"
        self.red_c="31;"
        self.green_c="32;"
        self.yello_c="33;"
        self.blue_c="34;"
        self.pink_c="35;"
        self.cayan_c="36;"
        self.white_c="37;"

        self.normal_b="40m"
        self.red_b="41m"
        self.green_b="42m"
        self.yello_b="43m"
        self.blue_b="44m"
        self.pink_b="45m"
        self.cayan_b="46m"
        self.white_b="47m"
        self.black_b="48m"



        self.default_style=[self.white_c, self.black_b, self.normal_tx]
        self.custom_style=[self.white_c, self.black_b, self.bold_tx]

        self.custom_type_codes = ['/u/', '/a/', '/y/', '/g/', '/k/', '/b/', '/r/', '/h/', '/bu/', '/hu/', '/=/']

        
        self.no_code = False
        self.no_colors = False

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


    # def slowtype2(self, *text, sep= ' ', wait_time=wait_time, end='\n'):
    #     """main typing engine that prints inputted text
    #         slowly based on waiting time"""

        
    #     self.text= sep.join(map(str, text))
    #     self.wait_time=float(wait_time)
    #     self.end=str(end)

    #     self.tnt_helper()

    #     #custom_type_codes = ['/u/', '/a/', '/y/', '/g/', '/k/', '/b/', '/r/', '/h/', '/bu/', '/hu/', '/=/']
    #     i=0
    #     while  i<len(self.text):
    #         asd=1
    #         if self.text[i]=='/' and '/' in self.text[i+2:i+5]:
    #             asd=100
    #             if self.text[i+1] in ('a','r','g','y','b','p','c','w','=','u','i','h','_'):
    #                 x=self.text[i+1]
    #                 if x=='a': self.custom_style[0]=self.ash_c
    #                 elif x=='r': self.custom_style[0]=self.red_c
    #                 elif x=='g': self.custom_style[0]=self.green_c
    #                 elif x=='y': self.custom_style[0]=self.yello_c
    #                 elif x=='b': self.custom_style[0]=self.blue_c
    #                 elif x=='p': self.custom_style[0]=self.pink_c
    #                 elif x=='c': self.custom_style[0]=self.cayan_c
    #                 elif x=='w': self.custom_style[0]=self.white_c
    #                 elif x=='=':
    #                     sys.stdout.write('\u001b[0m')
    #                     sys.stdout.flush()
    #                     self.custom_style[:]=self.default_style[:]
    #                 elif x=='u': self.custom_style[2]=self.ul_tx
    #                 elif x=='i': self.custom_style[2]=self.neg_tx
    #                 elif x=='h': self.custom_style[2]=self.bold_tx
    #                 #sys.stdout.write('\u001b['+custom_style[0]+';'+custom_style[1]+';'+custom_style[2]+'m')
    #                 if self.text[i+2] in ('a','r','g','y','b','p','c','w','u','i','h','_'):
    #                     x=self.text[i+2]
    #                     if x=='a': self.custom_style[1]= self.normal_b
    #                     elif x=='r': self.custom_style[1]=self.red_b
    #                     elif x=='g': self.custom_style[1]=self.green_b
    #                     elif x=='y': self.custom_style[1]=self.yello_b
    #                     elif x=='b': self.custom_style[1]=self.blue_b
    #                     elif x=='p': self.custom_style[1]=self.pink_b
    #                     elif x=='c': self.custom_style[1]=self.cayan_b
    #                     elif x=='w': self.custom_style[1]=self.white_b
    #                     elif x=='u': self.custom_style[2]=self.ul_tx
    #                     elif x=='i': self.custom_style[2]=self.neg_tx
    #                     elif x=='h': self.custom_style[2]=self.bold_tx
    #                     if self.text[i+3] in ('u','i','h'):
    #                         x=self.text[i+3]
    #                         if x=='u': self.custom_style[2]=self.ul_tx
    #                         elif x=='i': self.custom_style[2]=self.neg_tx
    #                         elif x=='h': self.custom_style[2]=self.bold_tx

    #                         if self.text[i+4]=='/':
    #                             i+=4
    #                             asd=123
    #                     elif self.text[i+3]=='/':
    #                         i+=3
    #                         asd=12
    #                 elif self.text[i+2]=='/':
    #                     i+=2
    #                     asd=10

    #             elif self.text[i+1]=='s':
    #                 if self.text[i+3]=='/':
    #                     try:
    #                         sleep(float(self.text[i+2]))
    #                         i+=3
    #                         asd=2
    #                     except: pass
    #                 elif self.text[i+4]=='/':
    #                     try:
    #                         sleep(float(self.text[i+2:i+4]))
    #                         i+=4
    #                         asd=2
    #                     except: pass
    #                 elif self.text[i+5]=='/':
    #                     try:
    #                         sleep(float(self.text[i+2:i+5]))
    #                         i+=5
    #                         asd=0
    #                     except: pass
    #         if asd>1:
    #             sys.stdout.write('\033['+self.custom_style[2]+self.custom_style[0]+self.custom_style[1])
    #             sys.stdout.flush()
    #         elif asd==1:
    #             sys.stdout.write(self.text[i])
    #             sys.stdout.flush()
    #             sleep(self.wait_time)
    #         i+=1




    #     sys.stdout.write(self.end)
    #     sys.stdout.flush()


    def slowtype(self, *text, sep= ' ', wait_time=wait_time, end='\n'):
        """main typing engine that prints inputted text
            slowly based on waiting time"""

        
        self.text= sep.join(map(str, text))
        self.wait_time=float(wait_time)
        self.end=str(end)


        self.custom_style_temp = self.custom_style[:]

        self.tnt_helper()
        #custom_type_codes = ['/u/', '/a/', '/y/', '/g/', '/k/', '/b/', '/r/', '/h/', '/bu/', '/hu/', '/=/']
        i=0
        while  i<len(self.text):
            slept= False
            has_code= False

            if self.text[i:i+3] == '/~`':
                self.no_code = True
                i+=3
                continue

            if self.text[i:i+3] == '`~/':
                self.no_code = False
                i+=3    
                continue

            if self.text[i:i+3] == '/~~':
                self.no_colors = True
                i+=3
                continue

            if self.text[i:i+3] == '~~/':
                self.no_colors = False
                i+=3
                continue

            






            if self.no_code==False:
                if self.text[i]=='/' and '/' in self.text[i+2:i+5]:
                    if self.no_colors==False and self.text[i+1] in ('a','r','g','y','b','p','c','w','=','u','i','h','_'):
                        x=self.text[i+1]
                        if x=='a': self.custom_style_temp[0]=self.ash_c
                        elif x=='r': self.custom_style_temp[0]=self.red_c
                        elif x=='g': self.custom_style_temp[0]=self.green_c
                        elif x=='y': self.custom_style_temp[0]=self.yello_c
                        elif x=='b': self.custom_style_temp[0]=self.blue_c
                        elif x=='p': self.custom_style_temp[0]=self.pink_c
                        elif x=='c': self.custom_style_temp[0]=self.cayan_c
                        elif x=='w': self.custom_style_temp[0]=self.white_c
                        elif x=='=':
                            sys.stdout.write('\u001b[0m')
                            sys.stdout.flush()
                            self.custom_style_temp = self.default_style[:]
                        elif x=='u': self.custom_style_temp[2]=self.ul_tx
                        elif x=='i': self.custom_style_temp[2]=self.neg_tx
                        elif x=='h': self.custom_style_temp[2]=self.bold_tx
                        #sys.stdout.write('\u001b['+custom_style[0]+';'+custom_style[1]+';'+custom_style[2]+'m')
                        if self.text[i+2]=='/':
                            has_code=True
                            i+=2
                        elif self.text[i+2] in ('a','r','g','y','b','p','c','w','u','i','h','_'):
                            x=self.text[i+2]
                            if x=='a': self.custom_style_temp[1]= self.normal_b
                            elif x=='r': self.custom_style_temp[1]=self.red_b
                            elif x=='g': self.custom_style_temp[1]=self.green_b
                            elif x=='y': self.custom_style_temp[1]=self.yello_b
                            elif x=='b': self.custom_style_temp[1]=self.blue_b
                            elif x=='p': self.custom_style_temp[1]=self.pink_b
                            elif x=='c': self.custom_style_temp[1]=self.cayan_b
                            elif x=='w': self.custom_style_temp[1]=self.white_b
                            elif x=='u': self.custom_style_temp[2]=self.ul_tx
                            elif x=='i': self.custom_style_temp[2]=self.neg_tx
                            elif x=='h': self.custom_style_temp[2]=self.bold_tx

                            if self.text[i+3]=='/':
                                has_code=True
                                i+=3
                            elif self.text[i+3] in ('u','i','h'):
                                x=self.text[i+3]
                                if x=='u': self.custom_style_temp[2]=self.ul_tx
                                elif x=='i': self.custom_style_temp[2]=self.neg_tx
                                elif x=='h': self.custom_style_temp[2]=self.bold_tx

                                if self.text[i+4]=='/':
                                    has_code = True
                                    i+=4


                    elif self.text[i+1]=='s':
                        if self.text[i+3]=='/':
                            try:
                                sleep(float(self.text[i+2]))
                                i+=3
                                slept = True
                            except: pass
                        elif self.text[i+4]=='/':
                            try:
                                sleep(float(self.text[i+2:i+4]))
                                i+=4
                                slept = True
                            except: pass
                        elif self.text[i+5]=='/':
                            try:
                                sleep(float(self.text[i+2:i+5]))
                                i+=5
                                slept = True
                            except: pass
            if has_code==True:
                self.custom_style = self.custom_style_temp[:]

                sys.stdout.write('\033['+self.custom_style[2]+self.custom_style[0]+self.custom_style[1])
                sys.stdout.flush()
            elif slept==True:
                sys.stdout.flush()
            else:
                sys.stdout.write(self.text[i])
                if wait_time!=0:
                    sys.stdout.flush()
                    sleep(self.wait_time)
            i+=1
            # print(has_code, slept)

        sys.stdout.write(self.end)
        sys.stdout.flush()

