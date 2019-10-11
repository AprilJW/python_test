from src.generate_data.ItemIntegrator.ItemBlender import ItemBlender
from src.generate_data.ItemIntegrator.ItemsToImage import ItemsToImage
from src.generate_data.ItemIntegrator.Background import ColorBackground, RandomNoiseBackground, FileBackground
from src.generate_data.ItemIntegrator.SeedItemPicker import SeedItemPicker
from src.generate_data.ItemIntegrator.UpdateGenerateNum import UpdateGenerateNum
from src.generate_data.ItemIntegrator.LabelMapper import LabelMapper
from src.generate_data.ItemIntegrator.IlluminationNormalization import IlluminationNormalization

operator_type_to_operator = {ItemBlender.type: ItemBlender, ItemsToImage.type: ItemsToImage,
                             ColorBackground.type: ColorBackground, RandomNoiseBackground.type: RandomNoiseBackground,
                             FileBackground.type: FileBackground, SeedItemPicker.type: SeedItemPicker,
                             UpdateGenerateNum.type: UpdateGenerateNum, LabelMapper.type: LabelMapper,
                             IlluminationNormalization.type: IlluminationNormalization}