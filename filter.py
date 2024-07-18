#   filter ()

nums = [ 21, 98, 34, 77, 12, 5 ]

evens = filter ( lambda Anum : Anum % 2 == 0, nums )
print ( evens )
print ( list ( evens ) )

print ( "\n--------------Cleaning our Servers--------------\n" )

Users = [
    { 'Uname' : 'Aliz' , 'shop_List' : ['apple', 'orange', 'banana'] },
    { 'Uname' : 'Rezax', 'shop_List' : [] },
    { 'Uname' : 'morez', 'shop_List' : [] }
]

mustBeClean = filter ( lambda A_user : len ( A_user ['shop_List'] ) == 0 , Users )
forPayMoney = filter ( lambda A_user : A_user ['shop_List'] , Users )

print ( list ( mustBeClean ) )
print ( list ( forPayMoney ) )

print ( "\n--------------Passengers--------------\n" )

passengers = map ( lambda esmha : esmha['Uname'],
                   filter ( lambda user : user ['shop_List'], Users )
                 )

print ( list ( passengers ) )

anotherpassengers = [ user['Uname'] for user in Users if len ( user['shop_List'] ) != 0 ]
print ( "\n",list( anotherpassengers ) )

print ( "\n--------------all()--------------\n" )

print ( all ([0]), "\n\n" )

myname = 'aaaa aaaaaa'
isAin = print ( all ( harf == 'a' for harf in myname ) )

#print ( "\n\nMy Test :)\n" )
#for harf in myname :
#    if harf == 'a' :
#        print (f't becuase {harf}')
#    else :
#        print (f'f becuase {harf}')

print ( "\n--------------any()--------------\n" )
mytest = 'djkljgofdkpds; a'
isAin = print ( any ( harf == 'a' for harf in myname ) )