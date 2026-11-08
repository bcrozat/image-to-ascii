import numpy as np
from PIL import Image

img = Image.open("images/<image>.png") # load image
img = img.convert("L") # convert to grayscale
# img.show()
nda = np.array(img) # get array
# nda_crop = nda[400:1000, 1000:1600, :4] # crop if rgba
nda_crop = nda[400:1000, 1000:1600] # crop if grayscale
img_crop = Image.fromarray(nda_crop)
# img_crop.show()

ramp = { # ramp: [@ % # * + = - : . ] # define ascii ramp
    0: "@",
    1: "%",
    2: "#",
    3: "*",
    4: "+",
    5: "=",
    6: "-",
    7: ":",
    8: ".",
    9: " "
}

def print_ascii(nda):
    scaled = nda / nda.max() * 9 # scale to [0, 9] # note: scale "brightness" too
    rounded = np.round(scaled)
    print("# printing ascii image #\n")
    for pixel in rounded:
        mapped =  [*map(ramp.get, pixel)]
        print("".join(mapped))

def save_ascii(nda):
    scaled = nda / nda.max() * 9  # scale to [0, 9] # note: scale "brightness" too
    rounded = np.round(scaled)
    with open ("ascii.txt", "w") as file:
        for line in rounded:
            mapped =  [*map(ramp.get, line)]
            file.write("".join(mapped)+"\n")

print_ascii(nda_crop)
save_ascii(nda_crop)