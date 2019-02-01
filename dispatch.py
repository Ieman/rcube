'''
    file for producted code, Assignments 4,5,6,7
    Created on Aug 27, 2018
    
    @author:    Eman Albader
'''


from random import randint
import random


def dispatch(parm={}):
    httpResponse = {}
    

    if(not('op' in parm)):
        httpResponse['status'] = 'error: missing op' 
                 
    elif(parm['op'] == 'create') and (('f' in parm) or ('r' in parm) or ('b' in parm) or('l' in parm) or('t' in parm) or ('u' in parm)) :
        if ((('f' in parm) and (not(parm['f'])))or (('r' in parm) and (not(parm['r'])))or(('b' in parm) and (not(parm['b'])))or(('l' in parm) and (not(parm['l'])))or(('t' in parm) and (not(parm['t'])))or(('u' in parm) and (not(parm['u'])))):
            httpResponse['status'] = 'error:'
        else:
            httpResponse['status'] = 'created'
            httpResponse['cube'] = createCube1(parm)
       
    elif(parm['op'] == 'create'):
        httpResponse['status'] = 'created'
        httpResponse['cube'] = createCube(parm)
        
    #elif (parm['op'] != 'create'):
        #httpResponse['status'] = 'error: missing op'
        
    #  assignment 5   
    elif((parm['op'] == 'check') and ('cube' in parm)):
        
        cubelist = (parm['cube'].split(','))
        length = len(cubelist)

        if (length == 54):
            f= 'green'
            r= 'yellow'
            b= 'blue'
            l= 'white'
            t= 'red'
            u= 'orange'
        
            if (('f' in parm) or ('r' in parm) or ('b' in parm) or('l' in parm) or('t' in parm) or ('u' in parm)):
                if ((('f' in parm) and (not(parm['f'])))or (('r' in parm) and (not(parm['r'])))or(('b' in parm) and (not(parm['b'])))or(('l' in parm) and (not(parm['l'])))or(('t' in parm) and (not(parm['t'])))or(('u' in parm) and (not(parm['u'])))):
                    httpResponse['status'] = 'error:'
                else:
                    if ('f' in parm):
                        f= parm['f']
                    if ('r' in parm):
                        r= parm['r']
                    if ('b' in parm):
                        b= parm['b']
                    if ('l' in parm):
                        l= parm['l']
                    if ('t' in parm):
                        t= parm['t']
                    if ('u' in parm):
                        u= parm['u']
                
           
            
            invalidColors= 0   
            for i in range(length):
                if ((cubelist[i]!= f) and (cubelist[i]!= r)and (cubelist[i]!= b)and (cubelist[i]!= l)and (cubelist[i]!= t)and (cubelist[i]!= u)):
                    invalidColors += 1
                    
            if (invalidColors > 0 ):
                httpResponse['status'] = 'error:'
            
            elif ((cubelist[4]!= f) or (cubelist[13]!= r)or (cubelist[22]!= b)or (cubelist[31]!= l)or (cubelist[40]!= t)or (cubelist[49]!= u)):
                httpResponse['status'] = 'error:'
                
            elif ((cubelist[0]== f) and (cubelist[1]== f) and (cubelist[2]== f)and (cubelist[3]== f)and (cubelist[4]== f)and (cubelist[5]== f)and (cubelist[6]== f)and (cubelist[7]== f)and (cubelist[8]== f)
                    and (cubelist[9]== r)and (cubelist[10]== r)and (cubelist[11]== r)and (cubelist[12]== r)and (cubelist[13]== r)and (cubelist[14]== r)and (cubelist[15]== r)and (cubelist[16]== r)and (cubelist[17]== r)
                    and (cubelist[18]== b)and (cubelist[19]== b)and (cubelist[20]== b)and (cubelist[21]== b)and (cubelist[22]== b)and (cubelist[23]== b)and (cubelist[24]== b)and (cubelist[25]== b)and (cubelist[26]== b)
                    and (cubelist[27]== l)and (cubelist[28]== l)and (cubelist[29]== l)and (cubelist[30]== l)and (cubelist[31]== l)and (cubelist[32]== l)and (cubelist[33]== l)and (cubelist[34]== l)and (cubelist[35]== l)
                    and (cubelist[36]== t)and (cubelist[37]== t)and (cubelist[38]== t)and (cubelist[39]== t)and (cubelist[40]== t)and (cubelist[41]== t)and (cubelist[42]== t)and (cubelist[43]== t)and (cubelist[44]== t)
                    and (cubelist[45]== u)and (cubelist[46]== u)and (cubelist[47]== u)and (cubelist[48]== u)and (cubelist[49]== u)and (cubelist[50]== u)and (cubelist[51]== u)and (cubelist[52]== u)and (cubelist[53]== u)):
                httpResponse['status'] = 'full'
                
            
            elif ((cubelist[0]== t) and (cubelist[1]== f) and (cubelist[2]== t)and (cubelist[3]== f)and (cubelist[4]== f)and (cubelist[5]== f)and (cubelist[6]== t)and (cubelist[7]== f)and (cubelist[8]== t)
                    and (cubelist[9]== f)and (cubelist[10]== r)and (cubelist[11]== f)and (cubelist[12]== r)and (cubelist[13]== r)and (cubelist[14]== r)and (cubelist[15]== f)and (cubelist[16]== r)and (cubelist[17]== f)
                    and (cubelist[18]== u)and (cubelist[19]== b)and (cubelist[20]== u)and (cubelist[21]== b)and (cubelist[22]== b)and (cubelist[23]== b)and (cubelist[24]== u)and (cubelist[25]== b)and (cubelist[26]== u)
                    and (cubelist[27]== b)and (cubelist[28]== l)and (cubelist[29]== b)and (cubelist[30]== l)and (cubelist[31]== l)and (cubelist[32]== l)and (cubelist[33]== b)and (cubelist[34]== l)and (cubelist[35]== b)
                    and (cubelist[36]== r)and (cubelist[37]== t)and (cubelist[38]== r)and (cubelist[39]== t)and (cubelist[40]== t)and (cubelist[41]== t)and (cubelist[42]== r)and (cubelist[43]== t)and (cubelist[44]== r)
                    and (cubelist[45]== l)and (cubelist[46]== u)and (cubelist[47]== l)and (cubelist[48]== u)and (cubelist[49]== u)and (cubelist[50]== u)and (cubelist[51]== l)and (cubelist[52]== u)and (cubelist[53]== l)):
                httpResponse['status'] = 'crosses'
                
            elif ((cubelist[0] == cubelist[1]== cubelist[2]== cubelist[3]== cubelist[5]== cubelist[6]== cubelist[7]== cubelist[8])
                    and (cubelist[9]== cubelist[10]== cubelist[11]== cubelist[12]==cubelist[14]== cubelist[15]== cubelist[16]== cubelist[17])
                    and (cubelist[18] == cubelist[19]== cubelist[20]== cubelist[21]== cubelist[23]== cubelist[24]== cubelist[25]== cubelist[26])
                    and (cubelist[27]== cubelist[28]== cubelist[29]== cubelist[30]== cubelist[32]== cubelist[33]== cubelist[34]== cubelist[35])
                    and (cubelist[36] == cubelist[37]== cubelist[38]== cubelist[39]== cubelist[41]== cubelist[42]== cubelist[43]== cubelist[44])
                    and (cubelist[45]== cubelist[46]== cubelist[47]== cubelist[48]== cubelist[50]== cubelist[51]== cubelist[52]== cubelist[53])
                and (cubelist[4]== f)and (cubelist[13]== r)and (cubelist[22]== b)and (cubelist[31]== l)and (cubelist[40]== t)and (cubelist[49]== u)):
                httpResponse['status'] = 'spots'
                
            else:
                httpResponse['status'] ='unknown'
                
        else:
            httpResponse['status'] = 'error:'
 
    #  assignment 6 
    elif ((parm['op'] == 'rotate')and ('cube' in parm)and ('face' in parm)):
        
        
        cubelist = (parm['cube'].split(','))
        length = len(cubelist)

        if (length == 54):
            
            f= 'green'
            r= 'yellow'
            b= 'blue'
            l= 'white'
            t= 'red'
            u= 'orange'
            
            f1= cubelist[0]
            f2= cubelist[1]
            f3 = cubelist[2] 
            f4=cubelist[3]
            f5=cubelist[4]
            f6=cubelist[5]
            f7 = cubelist[6] 
            f8 =cubelist[7]
            f9=cubelist[8]
            r1 = cubelist[9]
            r2= cubelist[10]
            r3= cubelist[11]
            f3 = cubelist[2]
            r4 = cubelist[12]
            r5= cubelist[13]
            r6=cubelist[14]
            r7=cubelist[15]
            r8= cubelist[16]
            r9= cubelist[17]
            b1= cubelist[18]
            b2=cubelist[19]
            b3=cubelist[20]
            b4=cubelist[21]
            b5=cubelist[22]
            b6=cubelist[23]
            b7=cubelist[24]
            b8=cubelist[25]
            b9=cubelist[26]
            l1=cubelist[27]
            l2= cubelist[28]
            l3 = cubelist[29]
            l4= cubelist[30]
            l5=cubelist[31]
            l6 = cubelist[32]
            l7= cubelist[33]
            l8= cubelist[34]
            l9=cubelist[35]
            t1=cubelist[36]
            t2=cubelist[37]
            t3= cubelist[38]
            t4= cubelist[39]
            t5=cubelist[40]
            t6=cubelist[41]
            t7 = cubelist[42]
            t8 = cubelist[43]
            t9=cubelist[44]
            u1 = cubelist[45]
            u2 = cubelist[46]
            u3=cubelist[47]
            u4= cubelist[48]
            u5=cubelist[49]
            u6= cubelist[50]
            u7= cubelist[51]
            u8= cubelist[52]
            u9=cubelist[53] 
            
            if (('f' in parm) or ('r' in parm) or ('b' in parm) or('l' in parm) or('t' in parm) or ('u' in parm)):
                if ((('f' in parm) and (not(parm['f'])))or (('r' in parm) and (not(parm['r'])))or(('b' in parm) and (not(parm['b'])))or(('l' in parm) and (not(parm['l'])))or(('t' in parm) and (not(parm['t'])))or(('u' in parm) and (not(parm['u'])))):
                    httpResponse['status'] = 'error:'
                    
                else:
                    if ('f' in parm):
                        f= parm['f']
                    if ('r' in parm):
                        r= parm['r']
                    if ('b' in parm):
                        b= parm['b']
                    if ('l' in parm):
                        l= parm['l']
                    if ('t' in parm):
                        t= parm['t']
                    if ('u' in parm):
                        u= parm['u']
                
            invalidColors= 0   
            for i in range(length):
                if ((cubelist[i]!= f) and (cubelist[i]!= r)and (cubelist[i]!= b)and (cubelist[i]!= l)and (cubelist[i]!= t)and (cubelist[i]!= u)):
                    invalidColors += 1
                    
            if (invalidColors > 0 ):
                httpResponse['status'] = 'error:'
                
            elif ((cubelist[4]!= f) or (cubelist[13]!= r)or (cubelist[22]!= b)or (cubelist[31]!= l)or (cubelist[40]!= t)or (cubelist[49]!= u)):
                httpResponse['status'] = 'error:'
                                    
            elif (parm['face']=='f'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [f7 , f4, f1, f8,f5, f2, f9, f6, f3,t7, r2, r3, t8,r5,r6, t9, r8,r9,b1 , b2, b3, b4,b5, b6, b7, b8, b9,
                                        l1, l2, u1, l4,l5, u2, l7, l8, u3,t1,t2,t3,t4,t5,t6,l9,l6,l3,r7,r4,r1, u4,u5,u6,u7,u8,u9]
            elif (parm['face']=='F'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [f3 , f6, f9, f2,f5, f8, f7, f4, f1,u3, r2, r3, u2,r5,r6, u1, r8,r9,b1 , b2, b3, b4,b5, b6, b7, b8, b9,
                                        l1, l2, t9, l4,l5, t8, l7, l8, t7,t1,t2,t3,t4,t5,t6,r1,r4,r7,l3,l6,l9, u4,u5,u6,u7,u8,u9]
            elif (parm['face']=='r'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [f1 , f2, u3, f4,f5, u6, f7, f8, u9,r7,r4,r1,r8,r5,r2,r9,r6,r3,t9 , b2, b3,t6,b5, b6, t3, b8, b9,
                                        l1, l2, l3, l4,l5, l6, l7, l8, l9,t1,t2,f3,t4,t5,f6,t7,t8,f9,u1,u2,b7,u4,u5,b4,u7,u8,b1]    
            elif (parm['face']=='R'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [f1 , f2, t3, f4,f5, t6, f7, f8, t9,r3,r6,r9,r2,r5,r8,r1,r4,r7,u9, b2, b3,u6,b5, b6, u3, b8, b9,
                                        l1, l2, l3, l4,l5, l6, l7, l8, l9,t1,t2,b7,t4,t5,b4,t7,t8,b1,u1,u2,f3,u4,u5,f6,u7,u8,f9]
            elif (parm['face']=='l'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [t1,f2,f3,t4,f5,f6,t7,f8,f9,r1,r2,r3,r4,r5,r6,r7,r8,r9,b1,b2,u7,b4,b5,u4,b7,b8,u1,l7,l4,l1,l8,l5,l2,l9,l6,l3,
                                        b9,t2,t3,b6,t5,t6,b3,t8,t9,f1,u2,u3,f4,u5,u6,f7,u8,u9] 
            elif (parm['face']=='L'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [u1,f2,f3,u4,f5,f6,u7,f8,f9,r1,r2,r3,r4,r5,r6,r7,r8,r9,b1,b2,t7,b4,b5,t4,b7,b8,t1,l3,l6,l9,l2,l5,l8,l1,l4,l7,
                                        f1,t2,t3,f4,t5,t6,f7,t8,t9,b9,u2,u3,b6,u5,u6,b3,u8,u9]
            
            elif (parm['face']=='b'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [f1,f2,f3,f4,f5,f6,f7,f8,f9,r1,r2,u9,r4,r5,u8,r7,r8,u7,b7,b4,b1,b8,b5,b2,b9,b6,b3,t3,l2,l3,t2,l5,l6,t1,l8,l9,
                                        r3,r6,r9,t4,t5,t6,t7,t8,t9,u1,u2,u3,u4,u5,u6,l1,l4,l7]
            elif (parm['face']=='B'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [f1,f2,f3,f4,f5,f6,f7,f8,f9,r1,r2,t1,r4,r5,t2,r7,r8,t3,b3,b6,b9,b2,b5,b8,b1,b4,b7,u7,l2,l3,u8,l5,l6,u9,l8,l9,
                                        l7,l4,l1,t4,t5,t6,t7,t8,t9,u1,u2,u3,u4,u5,u6,r9,r6,r3]
            elif (parm['face']=='t'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [r1,r2,r3,f4,f5,f6,f7,f8,f9,b1,b2,b3,r4,r5,r6,r7,r8,r9,l1,l2,l3,b4,b5,b6,b7,b8,b9,f1,f2,f3,l4,l5,l6,l7,l8,l9,
                                        t7,t4,t1,t8,t5,t2,t9,t6,t3,u1,u2,u3,u4,u5,u6,u7,u8,u9]
            elif (parm['face']=='T'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [l1,l2,l3,f4,f5,f6,f7,f8,f9,f1,f2,f3,r4,r5,r6,r7,r8,r9,r1,r2,r3,b4,b5,b6,b7,b8,b9,b1,b2,b3,l4,l5,l6,l7,l8,l9,
                                        t3,t6,t9,t2,t5,t8,t1,t4,t7,u1,u2,u3,u4,u5,u6,u7,u8,u9]
            
            elif (parm['face']=='u'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [f1,f2,f3,f4,f5,f6,l7,l8,l9,r1,r2,r3,r4,r5,r6,f7,f8,f9,b1,b2,b3,b4,b5,b6,r7,r8,r9,l1,l2,l3,l4,l5,l6,b7,b8,b9,
                                        t1,t2,t3,t4,t5,t6,t7,t8,t9,u7,u4,u1,u8,u5,u2,u9,u6,u3]
            elif (parm['face']=='U'):
                httpResponse['status'] = 'rotated'
                httpResponse['cube'] = [f1,f2,f3,f4,f5,f6,r7,r8,r9,r1,r2,r3,r4,r5,r6,b7,b8,b9,b1,b2,b3,b4,b5,b6,l7,l8,l9,l1,l2,l3,l4,l5,l6,f7,f8,f9,
                                        t1,t2,t3,t4,t5,t6,t7,t8,t9,u3,u6,u9,u2,u5,u8,u1,u4,u7]
            else:
                httpResponse['status'] = 'error:' 
        else:
            httpResponse['status'] = 'error:' 
    #  assignment 7
     
    elif (parm['op'] == 'scramble') :
                          
        if (((not('n' in parm)) or (parm['n']==0))):
            if ('method' in parm) and ((not(parm['method'])) or (parm['method'] != "transition" )or (parm['method'] != "random" )):
                    httpResponse['status'] = 'error:'
            
            else:
                httpResponse['status'] = 'scrambled 100'
                httpResponse['rotations'] = []
            
        elif ('n' in parm):
            
            if (not(parm['n'])) or (not(str.isdigit(parm['n']))):
                httpResponse['status'] = 'error:'
            else:
                n= int (parm['n'])
                
                if (n > 99 ):
                    httpResponse['status'] = 'error:'
            
                elif ('method' in parm) and ((not(parm['method'])) or (parm['method'] != "transition" )or (parm['method'] != "random" )):
                    httpResponse['status'] = 'error:' 
                 
                elif (not('method' in parm)) or (parm['method'] == "random") : # random scramble
                    rotationslist = rotations (parm) 
                    httpResponse['rotlist'] = rotationslist  
                    httpResponse['status'] = 'scrambled' #randomness(rotationslist)
                    httpResponse['random'] = randomness(rotationslist)
                
            #elif (parm['method'] == "transition") ://transition scramble
                        
        
        else:
            httpResponse['status'] = 'error:'       
           
    else:
        httpResponse['status'] = 'error:'                
        
                          
    return httpResponse
        

def rotations (parm):
    
    faces = ["f","F","r","R","b","B","l","L","t","T","u","U"]
    n= int (parm['n'])
    
    scramble = []
    for i in range(0,n):
        sample = random.choice(faces)
        sample1= sample.lower()
        scramble1=''
        scramble2=''
        if (i>0):
            scramble1=scramble[i-1].lower()
            if (i>1):
                scramble2=scramble[i-2].lower()
    
        while (sample1 == scramble1) or (sample1 == scramble2):
            sample = random.choice(faces)
            sample1= sample.lower()

        scramble.append(sample)
    
    return scramble

def randomness (rotationslist):
    
    cube = ["f","f","f","f","f","f","f","f","f",
            "r","r","r","r","r","r","r","r","r",
            "b","b","b","b","b","b","b","b","b",
            "l","l","l","l","l","l","l","l","l",
            "t","t","t","t","t","t","t","t","t",
            "u","u","u","u","u","u","u","u","u"]
    
        
    length = len(rotationslist)
    Index = 0
    newCube =[]
    for _ in range(0,length):
        
        if (rotationslist[Index]=='F'):
        
            newCube =[cube[6] , cube[3], cube[0], cube[7],cube[4], cube[1], cube[8], cube[5], cube[2],cube[42], cube[10], cube[11], cube[43],cube[13],cube[14], cube[44], cube[16],cube[17],cube[18] , cube[19], cube[20], cube[21],
        cube[22], cube[23], cube[24], cube[25], cube[26],cube[27], cube[28], cube[45], cube[30],cube[31], cube[46], cube[33], cube[34], cube[47],cube[36],cube[37],cube[38],cube[49],cube[40],cube[41],cube[35],cube[32],cube[29],
        cube[15],cube[12],cube[9],cube[48],cube[49],cube[50],cube[51],cube[52],cube[53]]
            
        elif (rotationslist[Index]=='f'): 
            newCube = [cube[2] , cube[5], cube[8], cube[1],cube[4], cube[7], cube[6], cube[3], cube[0],cube[47], cube[10], cube[11], cube[46],cube[13],cube[14], cube[45], cube[16],cube[17],cube[18] , cube[19], cube[20], cube[21],
        cube[22], cube[23], cube[24], cube[25], cube[26],cube[27], cube[28], cube[44], cube[30],cube[31], cube[43], cube[33], cube[34], cube[42],cube[36],cube[37],cube[38],cube[39],cube[40],cube[41],cube[9],cube[12],
        cube[15],cube[29],cube[31],cube[35], cube[48],cube[49],cube[50],cube[51],cube[52],cube[53]]
        
        elif (rotationslist[Index]=='r'):
            newCube = [cube[0] , cube[1], cube[47], cube[3],cube[4], cube[50], cube[6], cube[7], cube[53],cube[15],cube[12],cube[9],cube[16],cube[13],cube[10],cube[17],cube[14],cube[11],cube[44] , cube[19], cube[20],cube[41],cube[22],
                        cube[23], cube[38], cube[25], cube[26],cube[27], cube[28], cube[29], cube[30],cube[31], cube[32], cube[33], cube[34], cube[35],cube[36],cube[37],cube[2],cube[39],cube[40],cube[5],cube[42],cube[43],cube[5],
                        cube[45],cube[46],cube[24],cube[48],cube[49],cube[21],cube[51],cube[52],cube[18]] 
               
        elif (rotationslist[Index]=='R'):
            newCube = [cube[0] , cube[1], cube[38], cube[3],cube[4], cube[41], cube[6], cube[7], cube[44],cube[11],cube[14],cube[17],cube[10],cube[13],cube[16],cube[9],cube[12],cube[15],cube[53], cube[19], cube[20],cube[50],cube[22], 
                        cube[23], cube[49],cube[25], cube[26],cube[27], cube[28], cube[29], cube[30],cube[31], cube[32], cube[33], cube[34], cube[35],cube[36],cube[37],cube[24],cube[39],cube[40],cube[21],cube[42],cube[43],cube[18],
                        cube[45],cube[46],cube[2],cube[48],cube[49],cube[5],cube[51],cube[52],cube[8]]
                        
        elif (rotationslist[Index]=='l'):
            newCube = [cube[36],cube[1],cube[2],cube[39],cube[4],cube[5],cube[42],cube[7],cube[8],cube[9],cube[10],cube[11],cube[12],cube[13],cube[14],cube[15],cube[16],cube[17],cube[18],cube[19],cube[51],cube[21],cube[23],cube[48],
                       cube[24],cube[25],cube[45],cube[33],cube[30],cube[27],cube[34],cube[31],cube[28],cube[35],cube[32],cube[29],cube[26],cube[37],cube[38],cube[23],cube[40],cube[41],cube[20],cube[43],cube[44],cube[0],cube[46],
                       cube[47],cube[3],cube[49],cube[50],cube[6],cube[52],cube[53]]
                                         
        elif (rotationslist[Index]=='L'):
            newCube = [cube[45],cube[1],cube[2],cube[48],cube[4],cube[5],cube[51],cube[7],cube[8],cube[9],cube[10],cube[11],cube[12],cube[13],cube[14],cube[15],cube[16],cube[17],cube[18],cube[19],cube[42],cube[21],cube[22],cube[39],
                       cube[24],cube[25],cube[36],cube[29],cube[32],cube[35],cube[28],cube[31],cube[34],cube[27],cube[30],cube[33],cube[0],cube[37],cube[38],cube[3],cube[40],cube[41],cube[6],cube[43],cube[44],cube[26],cube[46],
                       cube[47],cube[23],cube[49],cube[50],cube[20],cube[52],cube[53]]
            
        elif (rotationslist[Index]=='b'):
            newCube = [cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8],cube[9],cube[10],cube[53],cube[12],cube[13],cube[52],cube[15],cube[16],cube[51],cube[24],cube[21],cube[18],cube[25],cube[22],cube[19],cube[26],cube[23],cube[20],cube[38],cube[28],cube[29],cube[37],cube[31],cube[32],cube[36],cube[34],cube[35],
                                        cube[11],cube[14],cube[17],cube[39],cube[40],cube[41],cube[42],cube[43],cube[44],cube[45],cube[46],cube[47],cube[48],cube[49],cube[50],cube[27],cube[30],cube[33]]
                                        
        elif (rotationslist[Index]=='B'):
            newCube = [cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8],cube[9],cube[10],cube[36],cube[12],cube[13],cube[37],cube[15],cube[16],cube[38],cube[20],cube[23],cube[26],cube[19],cube[22],cube[25],cube[18],cube[21],cube[24],cube[51],cube[28],cube[29],cube[52],cube[31],cube[32],cube[53],cube[34],cube[35],
                                        cube[33],cube[30],cube[27],cube[39],cube[40],cube[41],cube[42],cube[43],cube[44],cube[45],cube[46],cube[47],cube[48],cube[49],cube[50],cube[17],cube[14],cube[11]]
                                        
        elif (rotationslist[Index]=='t'):
            newCube = [cube[9],cube[10],cube[11],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8],cube[18],cube[19],cube[20],cube[12],cube[13],cube[14],cube[15],cube[16],cube[17],cube[27],cube[28],cube[29],cube[21],cube[22],cube[23],cube[24],cube[25],cube[26],cube[0],cube[1],cube[2],cube[30],cube[31],cube[32],cube[33],cube[34],cube[35],
                                        cube[42],cube[39],cube[36],cube[43],cube[40],cube[37],cube[44],cube[41],cube[38],cube[45],cube[46],cube[47],cube[48],cube[49],cube[50],cube[51],cube[52],cube[53]]
                                        
        elif (rotationslist[Index]=='T'):
            newCube = [cube[27],cube[28],cube[29],cube[3],cube[4],cube[5],cube[6],cube[7],cube[8],cube[0],cube[1],cube[2],cube[12],cube[13],cube[14],cube[15],cube[16],cube[17],cube[9],cube[10],cube[11],cube[21],cube[22],cube[23],cube[24],cube[25],cube[26],cube[18],cube[19],cube[20],cube[30],cube[31],cube[32],cube[33],cube[34],cube[35],
                                        cube[38],cube[41],cube[44],cube[37],cube[40],cube[43],cube[36],cube[39],cube[42],cube[45],cube[46],cube[47],cube[48],cube[49],cube[50],cube[51],cube[52],cube[53]]
            
        elif (rotationslist[Index]=='u'):
            newCube= [cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[33],cube[34],cube[35],cube[9],cube[10],cube[11],cube[12],cube[12],cube[14],cube[6],cube[7],cube[8],cube[18],cube[19],cube[20],cube[21],cube[22],cube[23],cube[15],cube[16],cube[17],cube[27],cube[28],cube[29],cube[30],cube[31],cube[32],cube[24],cube[25],cube[26],
                                        cube[36],cube[37],cube[38],cube[39],cube[40],cube[41],cube[42],cube[43],cube[44],cube[51],cube[48],cube[45],cube[52],cube[49],cube[46],cube[53],cube[50],cube[47]]
        else: #elif (rotationslist[Index]=='U'):
            newCube = [cube[0],cube[1],cube[2],cube[3],cube[4],cube[5],cube[15],cube[16],cube[17],cube[9],cube[10],cube[11],cube[12],cube[12],cube[14],cube[24],cube[25],cube[26],cube[18],cube[19],cube[20],cube[21],cube[22],cube[23],cube[33],cube[34],cube[35],cube[27],cube[28],cube[29],cube[30],cube[31],cube[32],cube[6],cube[7],cube[8],
                                        cube[36],cube[37],cube[38],cube[39],cube[40],cube[41],cube[42],cube[43],cube[44],cube[47],cube[50],cube[53],cube[46],cube[49],cube[52],cube[45],cube[48],cube[51]]
            
        del cube[:]                          
        cube = newCube
        Index += 1
        
    elementIndex = 0
    matchedcolor=0
    
    for _ in range(0,6):
        temp =[]
        for _ in range(0,9):
            temp.append(cube[elementIndex])
            elementIndex += 1
        i= 0
        for _ in range(0,8):
            j= i+1
            while (j< 9):
                if (temp[i] == temp[j]):
                    matchedcolor += 1
                j += 1
            
            i += 1
        del temp[:]    
    faces  = 0.004629629629629629   # 1/216    
    total = round ( faces * matchedcolor * 100)
    return round(total)
            
            
    
    #total =round ( 1/216 * matchedcolor * 100)
    return total
              

def createCube (parm):
    cube = ['green',  'green', 'green', 
        'green', 'green', 'green', 
        'green', 'green', 'green',
        'yellow', 'yellow', 'yellow',
        'yellow', 'yellow', 'yellow', 
        'yellow', 'yellow', 'yellow',  
        'blue', 'blue', 'blue', 
        'blue', 'blue', 'blue',
        'blue', 'blue', 'blue',
        'white', 'white', 'white', 
        'white', 'white', 'white',
        'white', 'white', 'white',
        'red', 'red', 'red', 'red',
        'red', 'red', 'red', 'red',
        'red', 'orange', 'orange',
        'orange', 'orange', 'orange',
        'orange', 'orange', 'orange', 'orange']
    return cube

def createCube1 (parm):
    
    f= 'green'
    r= 'yellow'
    b= 'blue'
    l= 'white'
    t= 'red'
    u= 'orange'
    
    if ('f' in parm):
        f= parm['f']
    if ('r' in parm):
        r= parm['r']
    if ('b' in parm):
        b= parm['b']
    if ('l' in parm):
        l= parm['l']
    if ('t' in parm):
        t= parm['t']
    if ('u' in parm):
        u= parm['u']
        
    cube = [f,f,f,f,f,f,f,f,f,
            r,r,r,r,r,r,r,r,r,
            b,b,b,b,b,b,b,b,b,
            l,l,l,l,l,l,l,l,l,
            t,t,t,t,t,t,t,t,t,
            u,u,u,u,u,u,u,u,u]
    return cube






