def menu():
    pass
def cube_volume():
    a=input('enter the edge of the cube in metres ')
    print 'volume of your cube is '+ str(a*a*a) + ' metre-cube'
def cube_surface_area():
    a=input('enter the edge of the cube in metres ')
    print 'surface area of your cube is '+ str(6*a*a) + 'metre square'
def cuboid_volume():
    a=input('enter the length in metres ')
    b=input('enter the breadth in metres ')
    c=input('enter the height in metres ')
    print 'volume of your cuboid is ' + str(a*b*c) + ' metre-cube'
def cuboid_surface_area():
    a=input('enter the length in metres ')
    b=input('enter the breadth in metres ')
    c=input('enter the height in metres ')
    print 'surface area of your cuboid is '+str(2*a*b+2*b*c+2*a*c) + 'metre square'


def menu():
    print('enter')
    print('1 for cube volume')
    print('2 for cube surface area')
    print('3 for cuboid volume ')
    print('4 for cuboid surface area')
    print('5 to exit')
    a=input('')

    if a==1:
        cube_volume()
    elif a==2:
        cube_surface_area()
    elif a==3:
        cuboid_volume()
    elif a==4:
        cuboid_surface_area()
    elif a==5:
        pass
        
    

menu()
