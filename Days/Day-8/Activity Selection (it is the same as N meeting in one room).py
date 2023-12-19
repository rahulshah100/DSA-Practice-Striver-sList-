# It is just exactly same as N meeting in one room
# In activity selection and N meetings in one room we cant use the same approach as we did in Minimum number of platforms required, because in MinNumberOfPlatfReq we could differently sort the arrival and departure arrays, the new combinations of train times thus formed did not matter as such the max intersection of times will still stay the same. We just wanted to see at any given time how many max trains will be there so shuffle of arrival and departure times worked. Conversely, in Activity Selection and NMeetings, starting time mattered too. By differently sorting the arrays and thus shuffling the Job times does affect the answer.

# EG:
# start[] = {1,3,0,5,8,5}
# end[]   = {2,4,6,7,9,9}

#     0----------------- to ------------------6
#           1-----to-----2   3---to--4   5---to----7   8---to---9
#                                        5----------to----------9
# Jobs=4 (We check max consecutive)
# Trains=3 (We check max Intersection)

# sorted
# start = {0,1,3,5,8,5}
# end   = {2,4,6,7,9,9}

#    0---to---2                   5----------to-----------9
#            1------to-----4      5----to-----7  8---to---9
#                   3--------to--------6
# Jobs = 3
# Trains = 3