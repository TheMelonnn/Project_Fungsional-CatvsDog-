from PIL import Image
import numpy as np
from keras.models import load_model

def detection_script (file_path) :

    def load_and_preprocess_image(file_path):
        img = Image.open(file_path)
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        img = img.resize((224, 224))  # Resize to match model input shape
        img_array = np.asarray(img)
        img_array = img_array / 255.0  # Normalize pixel values
        return np.expand_dims(img_array, axis=0)  # Add batch dimension

    def run_prediction(file_path):
        test_image = load_and_preprocess_image(file_path)

        # Load your trained model
        model = load_model("model.h5")

        # Assuming you have test_data for testing
        predictions = model.predict(test_image)

        # Example: print the first prediction
        print(predictions[0])

        if predictions[0] > 0.5:
            result = "Prediction: Dog"
        else:
            result = "Prediction: Cat"

        return result
    
    final_result= run_prediction(file_path)
    print(final_result)

    return final_result
