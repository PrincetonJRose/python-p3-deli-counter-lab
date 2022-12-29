katz_deli = []

def line( katz_deli ):
    if katz_deli:
        message = 'The line is currently:'
        for index, person in enumerate( katz_deli ):
            message = message + f" {index + 1}. {person.title()}"
        print( message )
    else: print( "The line is currently empty." )

def take_a_number( katz_deli, name ) :
    katz_deli.append( name.title() )
    print( f"Welcome, {name}. You are number { katz_deli.index( name ) + 1 } in line." )

def now_serving( katz_deli ) :
    if katz_deli:
        print( f"Currently serving { katz_deli[0] }." )
        katz_deli.remove( katz_deli[0] )
    else:
        print( "There is nobody waiting to be served!" )

