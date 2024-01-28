import sys
sys.path.insert(1, "src")
import functions

def test_corner_enumerate(ori_x, ori_y, quad, it, d):
    temp = (ori_x, ori_y)
    # print(temp)
    for i in range(it):
      e = functions._enumerate_corner(ori_x,ori_y, temp[0], temp[1], quad, d)
      # print(e)
      temp = e
    # print("_____________")
    # print(temp)
    return temp


# (-1,1) (0,1) (1,1)
# (-1,0) (0,0) (1,0)
# (-1,-1) (0,-1) (1, -1)

# (1,1) (0,1) (1,0) (-1,1) (0,0) (1, -1) (-1,0) (0,-1) (-1,-1)
# test_corner_enumerate(1,1,1,8,3)
# (-1,1) (0,1) (-1,0) (1,1) (0,0) (-1, -1) (1,0) (0,-1) (1,-1)
# test_corner_enumerate(-1,1,2,8,3)
# (-1,-1) (0,-1) (-1,0) (1,-1) (0,0) (-1, 1) (1,0) (0,1) (1,1)
#test_corner_enumerate(-1,-1,3,8,3)
# (1,-1) (0,-1) (1,0) (-1,-1) (0,0) (1, 1) (-1,0) (0,1) (-1,1)
#test_corner_enumerate(1,-1,4,8,3)

# (-2,2) (-1,2) (0,2) (1,2) (2,2)
# (-2,1) (-1,1) (0,1) (1,1) (2,1)
# (-2,0) (-1,0) (0,0) (1,0) (2,0)
# (-2,-1) (-1,-1) (0,-1) (1,-1) (2,-1)
# (-2,-2) (-1,-2) (0,-2) (1,-2) (2,-2)




for i in range(1,9):
    f = i*2+1
    if test_corner_enumerate(i,i,1,f*f-1,f) != (-i,-i):
      print("error:" + str(i))
print("q1 done")
for i in range(1,9):
    f = i*2+1
    if test_corner_enumerate(-i,i,2,f*f-1,f) != (i,-i):
      print("error:" + str(i))
print("q2 done")
for i in range(1,9):
    f = i*2+1
    if test_corner_enumerate(-i,-i,3,f*f-1,f) != (i,i):
      print("error:" + str(i))
print("q3 done")
for i in range(1,9):
    f = i*2+1
    if test_corner_enumerate(i,-i,4,f*f-1,f) != (-i,i):
      print("error:" + str(i))
print("q4 done")

