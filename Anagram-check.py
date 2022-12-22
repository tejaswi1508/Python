"""to find out if the given two strings are anagrams or not
At frist we check the length of both strings; if they are equal we continue and if not we print they are not anagrams. 
Sort both of the strings after converting them to character arrays. Verify that the sorted arrays are all equal. 
Print anagrams if they are equal; otherwise, do not."""

import numpy as np 

st1 = "@#$%&"
st2 = "@&$%#"

if len(st1) != len(st2):
    print("not anagrams")
else:
    st1_arr = np.array(st1)
    st2_arr = np.array(st2)
    n1 = sorted(st1)
    n2 = sorted(st2)
    if n1 == n2:
        print("anagrams")
    else:
        print("no")
   
