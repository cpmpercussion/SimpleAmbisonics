import numpy as np

# Calculating Decoding coefficients for a cubic speaker array
# For details, see "Is My Decoder Ambisonic?", Heller, Lee, and Benjamin, 2008.

# Directions of Speakers from centre of array
speakers = [
[np.pi / 4,np.pi /4],
[3 * np.pi / 4,np.pi /4],
[5 * np.pi / 4,np.pi /4],
[7 * np.pi / 4,np.pi /4],
[np.pi / 4, -np.pi /4],
[3 * np.pi / 4, -np.pi /4],
[5 * np.pi / 4, -np.pi /4],
[7 * np.pi / 4, -np.pi /4],
]

# Definitions
def x_i(azi,ele):
	return np.cos(azi) * np.cos(ele)

def y_i(azi,ele):
	return np.sin(azi) * np.cos(ele)

def z_i(azi,ele):
	return np.sin(ele)

def w_i(azi,ele):
	return np.sqrt(2)/2

# Calculate coefficients
K = []
for l in speakers:
	K.append([w_i(l[0],l[1]),x_i(l[0],l[1]),y_i(l[0],l[1]),z_i(l[0],l[1])])

# Find pseudo-inverse matrix
K = np.matrix(K).round(4)
M = (np.linalg.pinv(K)).T.round(4)


# Results for cubic speaker array.
In [52]: K
Out[52]: 
array([[ 0.7071,  0.5   ,  0.5   ,  0.7071],
       [ 0.7071, -0.5   ,  0.5   ,  0.7071],
       [ 0.7071, -0.5   , -0.5   ,  0.7071],
       [ 0.7071,  0.5   , -0.5   ,  0.7071],
       [ 0.7071,  0.5   ,  0.5   , -0.7071],
       [ 0.7071, -0.5   ,  0.5   , -0.7071],
       [ 0.7071, -0.5   , -0.5   , -0.7071],
       [ 0.7071,  0.5   , -0.5   , -0.7071]])

In [53]: M
Out[53]: 
array([[ 0.1768,  0.25  ,  0.25  ,  0.1768],
       [ 0.1768, -0.25  ,  0.25  ,  0.1768],
       [ 0.1768, -0.25  , -0.25  ,  0.1768],
       [ 0.1768,  0.25  , -0.25  ,  0.1768],
       [ 0.1768,  0.25  ,  0.25  , -0.1768],
       [ 0.1768, -0.25  ,  0.25  , -0.1768],
       [ 0.1768, -0.25  , -0.25  , -0.1768],
       [ 0.1768,  0.25  , -0.25  , -0.1768]])

In [54]: 


# Results for 2D square speaker array:
speakers = [
[np.pi / 4,0],
[3 * np.pi / 4,0],
[5 * np.pi / 4,0],
[7 * np.pi / 4,0]
]

In [61]: K
Out[61]: 
array([[ 0.7071,  0.7071,  0.7071,  0.    ],
       [ 0.7071, -0.7071,  0.7071,  0.    ],
       [ 0.7071, -0.7071, -0.7071,  0.    ],
       [ 0.7071,  0.7071, -0.7071,  0.    ]])

In [62]: M
Out[62]: 
array([[ 0.3536,  0.3536,  0.3536,  0.    ],
       [ 0.3536, -0.3536,  0.3536,  0.    ],
       [ 0.3536, -0.3536, -0.3536,  0.    ],
       [ 0.3536,  0.3536, -0.3536,  0.    ]])

In [63]: 

