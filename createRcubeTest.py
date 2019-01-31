import unittest
import RCube.dispatch as RCube


class CreateCubeTest(unittest.TestCase):
# Acceptance Tests
#
# 200 dispatch -- op=create
# Desired level of confidence is BVA
# Analysis
#    inputs:  http:// ...myURL ... /rcube?op=create <options>
#        where <options> can be zero or one of:
#                f=<string>    string of length .GT. 0. Optional. Default to "green" Unvalidated
#                r=<string>    string of length .GT. 0. Optional. Default to "yellow" Unvalidated
#                b=<string>    string of length .GT. 0. Optional. Default to "blue" Unvalidated
#                l=<string>    string of length .GT. 0. Optional. Default to "white" Unvalidated
#                t=<string>    string of length .GT. 0. Optional. Default to "red" Unvalidated
#                u=<string>    string of length .GT. 0. Optional. Default to "orange" Unvalidated
#    outputs:    A JSON string containing, at a minimum, a key of "status"
#
#Happy path
#    inputs:  zero options
#        http:// ...myURL ... /rcube?op=create
#    outputs:    default model cube, which is JSON string:
#                '{'status': 'created', 'cube': [
#                'green',  'green', 'green',
#                'green', 'green', 'green', 
#                'green', 'green', 'green',
#                'yellow', 'yellow', 'yellow',
#                'yellow', 'yellow', 'yellow',
#                'yellow', 'yellow', 'yellow', 
#                'blue', 'blue', 'blue',
#                'blue', 'blue', 'blue',
#                'blue', 'blue', 'blue',
#                'white', 'white', 'white', 
#                'white', 'white', 'white', 
#                'white', 'white', 'white', 
#                'red', 'red', 'red', 
#                'red', 'red', 'red',
#                'red', 'red', 'red', 
#                'orange', 'orange', 'orange', 
#                'orange', 'orange', 'orange', 
#                'orange', 'orange', 'orange']}
#
#
#    inputs:  with options
#        http:// ...myURL ... /rcube?op=create &r=r&l=l&t=t&u=u&f=f& b=b
#     outputs:
#    '{'status': 'created', 'cube': 
#        ['f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',
#          'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 
#          'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 
#           'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 
#           't', 't', 't', 't', 't', 't', 't', 't', 't', 
#           'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u',]}
#    
#    inputs:  with options
#        http:// ...myURL ... /rcube?op=create &f=f&r=r&b=b&l=l&t=t
#     outputs:
#    {'status': 'created', 'cube': [
#    'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f', 
#     'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
#     'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 
#    'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l',
#     '1', '1', '1', '1', '1', '1', '1', '1', '1',
#     'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']}
#
#    inputs:  with options
#        http:// ...myURL ... /rcube?op=create &f=f&r=r&b=b&l=l&t=t&under=43
#     outputs:
#    {'status': 'created', 'cube': [
#    'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f',  'f', 
#     'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
#     'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 
#    'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l',
#     '1', '1', '1', '1', '1', '1', '1', '1', '1',
#     'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']} 
 
    def test200_030_ShouldCreateMultipleElementCube(self):
        parm = {'op': 'create'}
        actualResult = RCube.createCube(parm)
        actualFaceIndex = 0
        expectedFaces = ['green','yellow','blue','white','red','orange']
        for face in expectedFaces:
           for elementIndex in range(0,9):
               self.assertEqual(face, actualResult[actualFaceIndex])
               actualFaceIndex += 1 
    
    def test200_040_ShouldCreateMultipleElementCubeWithspecfiaction(self):
        parm = {'op': 'create','r': 'r','l':'l','t':'t','b':'b','u':'u','f':'f'}
        actualResult = RCube.createCube_(parm)
        expectedFaces = []
        actualFaceIndex = 0
        if 'f' in parm:
            expectedFaces.append ('f')
        else:
            expectedFaces.append ('green')
        if 'r' in parm:
            expectedFaces.append ('r')
        else:
            expectedFaces.append ('yellow')
        if 'b' in parm:
            expectedFaces.append ('b')
        else:
            expectedFaces.append ('blue')
        if 'l' in parm:
            expectedFaces.append ('l')
        else:
            expectedFaces.append ('white')
        if 't' in parm:
            expectedFaces.append ('t')
        else:
            expectedFaces.append ('red')
        if 'u' in parm:
            expectedFaces.append ('u')
        else:
            expectedFaces.append ('orange')
            
        for face in expectedFaces:
           for elementIndex in range(0,9):
               self.assertEqual(face, actualResult[actualFaceIndex])
               actualFaceIndex += 1 
               
    def test200_040_ShouldCreateMultipleElementCubeWithdefultUnder(self):
        parm = {'op': 'create','b':'b', 'r': 'r','l':'l','t':'t','f':'f'}
        actualResult = RCube.createCube2 (parm)
        expectedFaces = []
        actualFaceIndex = 0
        if 'f' in parm:
            expectedFaces.append ('f')
        else:
            expectedFaces.append ('green')
        if 'r' in parm:
            expectedFaces.append ('r')
        else:
            expectedFaces.append ('yellow')
        if 'b' in parm:
            expectedFaces.append ('b')
        else:
            expectedFaces.append ('blue')
        if 'l' in parm:
            expectedFaces.append ('l')
        else:
            expectedFaces.append ('white')
        if 't' in parm:
            expectedFaces.append ('t')
        else:
            expectedFaces.append ('red')
        if 'u' in parm:
            expectedFaces.append ('u')
        else:
            expectedFaces.append ('orange')
            
        for face in expectedFaces:
           for elementIndex in range(0,9):
               self.assertEqual(face, actualResult[actualFaceIndex])
               actualFaceIndex += 1 
               
    def test200_050_ShouldCreateMultipleElementCubeWithdefultValues(self):
        parm = {'op': 'create','b':'b', 'r': 'r','l':'l','t':'t','f':'f', 'under':'42'}
        actualResult = RCube.createCube3 (parm)
        expectedFaces = []
        actualFaceIndex = 0
        if 'f' in parm:
            expectedFaces.append ('f')
        else:
            expectedFaces.append ('green')
        if 'r' in parm:
            expectedFaces.append ('r')
        else:
            expectedFaces.append ('yellow')
        if 'b' in parm:
            expectedFaces.append ('b')
        else:
            expectedFaces.append ('blue')
        if 'l' in parm:
            expectedFaces.append ('l')
        else:
            expectedFaces.append ('white')
        if 't' in parm:
            expectedFaces.append ('t')
        else:
            expectedFaces.append ('red')
        if 'u' in parm:
            expectedFaces.append ('u')
        else:
            expectedFaces.append ('orange')
            
        for face in expectedFaces:
           for elementIndex in range(0,9):
               self.assertEqual(face, actualResult[actualFaceIndex])
               actualFaceIndex += 1 
    