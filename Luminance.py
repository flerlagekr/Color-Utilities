#  This code provides functions for calculating the luminance of an RGB color
#  and for calculating the contrast ratio between two colors.
#  Written by Ken Flerlage, May, 2023.

#--------------------------------------------------------------------------------
# Calculate the luminance of RGB values.
#--------------------------------------------------------------------------------
def Luminance(RValue, GValue, BValue):

    RsRGB = RValue/255
    GsRGB = GValue/255
    BsRGB = BValue/255

    if RsRGB <= 0.03928:
        R = RsRGB/12.92
    else:
        R = pow((RsRGB+0.055)/1.055, 2.4)

    if GsRGB <= 0.03928:
        G = GsRGB/12.92
    else:
        G = pow((GsRGB+0.055)/1.055, 2.4)

    if BsRGB <= 0.03928:
        B = BsRGB/12.92
    else:
        B = pow((BsRGB+0.055)/1.055, 2.4)

    # Calculate luminance.
    Lum = 0.2126 * R + 0.7152 * G + 0.0722 * B

    return Lum

#--------------------------------------------------------------------------------
# Calculate the contrast ratio of two sets of RGB colors.
#--------------------------------------------------------------------------------
def contrastRatio (R1, G1, B1, R2, G2, B2):

    Luminance1 = Luminance(R1, G1, B1)
    Luminance2 = Luminance(R2, G2, B2)

    if Luminance1 > Luminance2:
        lighterLuminance = Luminance1
        darkerLuminance = Luminance2
    else:
        lighterLuminance = Luminance2
        darkerLuminance = Luminance1

    cRatio = (lighterLuminance + 0.05) / (darkerLuminance + 0.05)

    return cRatio

#--------------------------------------------------------------------------------
# Test our functions.
#--------------------------------------------------------------------------------
cRatio = contrastRatio(255, 170, 226, 204, 204, 204)
print(cRatio)
