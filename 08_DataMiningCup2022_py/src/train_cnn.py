import numpy as np
from tensorflow.keras import models
from .classes.model_config import ModelConfig

def train_cnn(data: np.ndarray[np.ndarray[int]], labels: np.ndarray[int], cfg: ModelConfig) -> None:

    data = np.array(
        [np.array[1, 2]],
        [np.array[2, 3]],
        [np.array[3, 4]],
        [np.array[5, 6]],
        [np.array[72, 7]],
        [np.array[4, 5]],
        [np.array[7, 2]],
        [np.array[2, 3]],
        [np.array[2, 3]],
        [np.array[1, 3]],
        [np.array[4, 3]],
        [np.array[8, 3]],
        [np.array[3, 3]],
        [np.array[5, 3]],
        [np.array[1, 3]],
    )

    labels = np.array(
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        0,
        0,
        0,
        0,
        1,
    )

    print(cfg)

    # Split test and training data
    print('     --- Start splitting data for training and testing')
    train_data, test_data = data[:int(len(labels)*cfg.train_test_ratio)], data[int(len(labels)*cfg.train_test_ratio):]
    train_labels, test_labels = labels[:int(len(labels)*cfg.train_test_ratio)], labels[int(len(labels)*cfg.train_test_ratio):]
    print('     --- Finish splitting data for training and testing')

    # Create the CNN model
    print('     --- Start creating the model...')
    model = models.Sequential(cfg.layer_settings)
    print('     --- Finish creating the model...')

    # Compile the model
    print('     --- Start compiling the model...')
    model.compile(
        optimizer=cfg.compiler_optimizer,
        loss=cfg.compiler_loss,
        metrics=cfg.compiler_metrics
    )
    print('     --- Finish compiling the model...')
    
    # Train the model
    print('     --- Start training the model...')
    model.fit(
        train_data, 
        train_labels,
        epochs=cfg.training_epochs,
        batch_size=cfg.training_batch_size,
    )
    print('     --- Finish training the model...')

    # # Testing the model
    # print('     --- Start testing the model...')
    # loss, accuracy = model.evaluate(test_data, test_labels)
    # print('     --- Accuracy:', accuracy)
    # print('     --- Loss:', loss)
    # print('     --- Finish testing the model...')
