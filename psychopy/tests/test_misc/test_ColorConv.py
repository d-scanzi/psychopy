from psychopy.colors import Color
import numpy

expectedHSV = numpy.array((
       (  0, 1.0, 1.0),
       (  0, 1.0, 0.5),
       (  0, 0.5, 0.5),
       ( 30, 1.0, 1.0),
       ( 60, 1.0, 1.0),
       ( 90, 1.0, 1.0),
       (120, 1.0, 1.0),
       (150, 1.0, 1.0),
       (180, 1.0, 1.0),
       (210, 1.0, 1.0),
       (240, 1.0, 1.0),
       (270, 1.0, 1.0),
       (300, 1.0, 1.0),
       (330, 1.0, 1.0),
       (360, 1.0, 1.0)))
expectedRGB = numpy.array([( 1.0, -1.0, -1.0),
                           ( 1.0, -1.0, -1.0),
                           ( 0.5, -0.5, -0.5),
                           ( 1.0,  0.0, -1.0),
                           ( 1.0,  1.0, -1.0),
                           ( 0.0,  1.0, -1.0),
                           (-1.0,  1.0, -1.0),
                           (-1.0,  1.0,  0.0),
                           (-1.0,  1.0,  1.0),
                           (-1.0,  0.0,  1.0),
                           (-1.0, -1.0,  1.0),
                           ( 0.0, -1.0,  1.0),
                           ( 1.0, -1.0,  1.0),
                           ( 1.0, -1.0,  0.0),
                           ( 1.0, -1.0, -1.0)])
expectedRGB1 = numpy.array([(1.0,  0.0,  0.0),
                            (1.0,  0.0,  0.0),
                            (0.75, 0.25, 0.25),
                            (1.0,  0.5,  0.0),
                            (1.0,  1.0,  0.0),
                            (0.5,  1.0,  0.0),
                            (0.0,  1.0,  0.0),
                            (0.0,  1.0,  0.5),
                            (0.0,  1.0,  1.0),
                            (0.0,  0.5,  1.0),
                            (0.0,  0.0,  1.0),
                            (0.5,  0.0,  1.0),
                            (1.0,  0.0,  1.0),
                            (1.0,  0.0,  0.5),
                            (1.0,  0.0,  0.0)])
expectedRGB255 = numpy.array([(255,   0,   0),
                              (255,   0,   0),
                              (191,  63,  63),
                              (255, 127,   0),
                              (255, 255,   0),
                              (127, 255,   0),
                              (  0, 255,   0),
                              (  0, 255, 127),
                              (  0, 255, 255),
                              (  0, 127, 255),
                              (  0,   0, 255),
                              (127,   0, 255),
                              (255,   0, 255),
                              (255,   0, 127),
                              (255,   0,   0)])
expectedHex = numpy.array(['#ff0000',
                           '#ff0000',
                           '#bf3f3f',
                           '#ff7f00',
                           '#ffff00',
                           '#7fff00',
                           '#00ff00',
                           '#00ff7f',
                           '#00ffff',
                           '#007fff',
                           '#0000ff',
                           '#7f00ff',
                           '#ff00ff',
                           '#ff007f',
                           '#ff0000'])
expectedNamed = numpy.array(['red',
                             'red',
                             None,
                             None,
                             'yellow',
                             'chartreuse',
                             'lime',
                             'springgreen',
                             'aqua',
                             None,
                             'blue',
                             None,
                             'fuchsia',
                             None,
                             'red'])


def test_HSV_RGB():
   RGB = [Color(col, 'hsv').rgb for col in expectedHSV]
   assert numpy.allclose(RGB, expectedRGB, 0.0001)


if __name__=='__main__':
    test_HSV_RGB()
