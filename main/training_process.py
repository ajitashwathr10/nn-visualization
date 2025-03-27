import tensorflow as tf
import matplotlib.pyplot as plt
import streamlit as st

class TrainingProcess(tf.keras.callbacks.Callback):
    def __init__(self):
        super().__init__()
        self.losses = []
        self.accuracies = []
        self.placeholder = st.empty()

    def on_epoch_end(self, epoch, logs=None):
        self.losses.append(logs['loss'])
        self.accuracies.append(logs['accuracy'])
        self.plot_progress()

    def plot_progress(self):
        try:
            fig = plt.figure(figsize=(12, 5))
            
            plt.subplot(1, 2, 1)
            plt.plot(self.losses, label='Loss')
            plt.xlabel('Epoch')
            plt.ylabel('Loss')
            plt.title('Training Loss')
            plt.legend()

            plt.subplot(1, 2, 2)
            plt.plot(self.accuracies, label='Accuracy')
            plt.xlabel('Epoch')
            plt.ylabel('Accuracy')
            plt.title('Training Accuracy')
            plt.legend()

            plt.tight_layout()
            self.placeholder.pyplot(fig)
            plt.close()
        except Exception as e:
            st.error(f"Error plotting training progress: {str(e)}")