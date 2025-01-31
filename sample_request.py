import requests
import json_numpy
json_numpy.patch()
import numpy as np
from PIL import Image

response = requests.post(
    "http://0.0.0.0:8081/generate",
    json={"image": np.asarray(Image.open("assets/demo.png"))}
)

# Save the response as a .glb file
output_file = "test.glb"
with open(output_file, "wb") as f:
    f.write(response.content)
