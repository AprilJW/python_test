import os
import sys

from src.generate_data.ItemTransformer.Resize import Resize
from src.generate_data.ItemTransformer.Brightness import Brightness
from src.generate_data.ItemTransformer.Contrast import Contrast
from src.generate_data.ItemTransformer.HueTune import HueTune
from src.generate_data.ItemTransformer.Move import Move
from src.generate_data.ItemTransformer.RandomHighLight import RandomHighLight
from src.generate_data.ItemTransformer.Rotation import Rotation
from src.generate_data.ItemTransformer.Shadow import Shadow
from src.generate_data.ItemTransformer.Distortion import Distortion
from src.generate_data.ItemTransformer.Crop import Crop

operator_type_to_operator = {Resize.type: Resize, Brightness.type: Brightness, Contrast.type: Contrast,
                             HueTune.type: HueTune, Move.type: Move, RandomHighLight.type: RandomHighLight,
                             Rotation.type: Rotation, Shadow.type: Shadow, Distortion.type: Distortion, Crop.type: Crop}
