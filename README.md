![Example of AmbiPanner~ and AmbiDecoderCube~ working in Pure Data](https://github.com/cpmpercussion/SimpleAmbisonics/raw/master/pd-example.jpg)

SimpleAmbisonics
================

Some simple (and bad) Pd objects for 3D ambisonics.

All I wanted was a simple 3D ambisonic panner and a deocder to an 8 speaker cube - available examples didn't seem to work, so I'm making my own pure-Pd emergency solution for doing a little bit of 3D surround. See [Wikipedia](http://en.wikipedia.org/wiki/Ambisonics) for basic details of this terrible implementation, more detailed information about making Ambisonic decoders is in the appendix of this great paper:

[Heller, Aaron, Richard Lee, and Eric Benjamin. "Is my decoder ambisonic?." Audio Engineering Society Convention 125. Audio Engineering Society, 2008.
 APA](http://decoy.iki.fi/dsound/ambisonic/motherlode/source/blah-decoder.pdf) 

"calculatingdecodermatrix.py" is my Python script for calculating B-Format decoder matrices. 

The Pd objects are as follows:

- *AmbiPanner~* Pans a mono source in 3D, azimuth and elevation parameters are entered from -1 to 1.
- *AmbiDecoderQuad~* A first order B-Format decoder for a square speaker array.
- *AmbiDecoderCube~* A first order B-Format decoder for a cubic speaker array.

I'm not sure anybody should use these for any reason, but if you want to help improve them, jump in.
