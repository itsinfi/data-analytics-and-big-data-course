from src.config import *
from src import read_data
from tensorflow.keras.models import Sequential#, load_model TODO:

x_train, x_test, y_train, y_test = read_data(csv_cfg_list=CSV_CFG, label_cfg=LABEL_CFG, test_size=TEST_SIZE)

# TODO: create model
# model = Sequential(
#     MODEL_CFG.LAYERS
# )

# model.compile(
#     loss=COMPILER_CFG.LOSS,
#     optimizer=COMPILER_CFG.OPTIMIZER,
#     metrics=COMPILER_CFG.METRICS,
# )

# model.fit(
#     x_train,
#     y_train,
#     epochs=TRAINING_CFG.EPOCHS,
#     batch_size=TRAINING_CFG.BATCH_SIZE,
# )

# loss, accuracy = model.evaluate(x_test, y_test)
# if 'accuracy' in COMPILER_CFG.METRICS:
#     print('--- Accuracy:', accuracy)
# print('--- Loss:', loss)