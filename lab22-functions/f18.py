
# Error observations


def show(id = 1 , name = "AT" , marks = 99) :
    return id,name,marks # if we return more than 1 value then values are return in tuple data type
# as return values are unique thus they are stored in immutable data type


show(1,"KT", 56,id = 2)


# TypeError: show() got multiple values for argument 'id'