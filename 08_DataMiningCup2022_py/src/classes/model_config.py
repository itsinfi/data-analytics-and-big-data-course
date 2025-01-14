from tensorflow.keras.layers import Layer
from typing import List

class ModelConfig:

    layer_settings: List[Layer]
    train_test_ratio: float
    training_epochs: int
    training_batch_size: int
    compiler_optimizer: str
    compiler_loss: str
    compiler_metrics: str

    def __init__(self, model_settings: List[Layer], train_test_ratio: float, training_epochs: int, training_batch_size: int, compiler_optimizer: str, compiler_loss: str, compiler_metrics: str) -> None:
        self.layer_settings = model_settings
        self.train_test_ratio = train_test_ratio
        self.training_epochs = training_epochs
        self.training_batch_size = training_batch_size
        self.compiler_optimizer = compiler_optimizer
        self.compiler_loss = compiler_loss
        self.compiler_metrics = compiler_metrics

    def __str__(self):
        return '{\n' + f' model_settings: {self.layer_settings}\n' + f' train_test_ratio: {self.train_test_ratio}\n' + f' epochs: {self.training_epochs}\n' + f' compiler_optimizer: {self.compiler_optimizer}\n' + f' compiler_loss: {self.compiler_loss}\n' + f' compiler_metrics: {self.compiler_metrics}\n' + '}'