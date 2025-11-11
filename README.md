# 🎙️ Speech Emotion Recognition System

A real-time speech emotion recognition system that analyzes voice input and predicts emotions like happy, sad, angry, calm, etc.

## 🌟 Features

- **Real-time Audio Processing**: Record and analyze speech in real-time
- **Advanced ML Pipeline**: Uses multiple machine learning models (Random Forest, SVM, LightGBM, etc.)
- **Beautiful UI**: Modern React frontend with smooth animations
- **Comprehensive Analysis**: Shows emotion prediction with confidence scores
- **8 Emotion Categories**: neutral, calm, happy, sad, angry, fearful, disgust, surprised

## 🏗️ Architecture

```
Frontend (React) ←→ Backend (Flask) ←→ ML Models
     ↓                    ↓              ↓
  UI/UX              Audio Processing   Emotion Prediction
  Animations         Feature Extraction  Confidence Scores
  Results Display    Real-time Recording
```

## 📋 Prerequisites

- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **RAVDESS Dataset** (for training models)
- **Microphone** for recording

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

1. **Clone/Download** the project
2. **Place RAVDESS dataset** in the root directory (folder named `Audio_Speech_Actors_01-24`)
3. **Run the startup script**:
   ```bash
   python start_system.py
   ```
4. **Follow the instructions** shown in the terminal
5. **Open your browser** to the provided URL

### Option 2: Manual Setup

#### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train models** (if not already done):
   ```bash
   python save_models.py
   ```

4. **Start Flask server**:
   ```bash
   python app.py
   ```

#### Frontend Setup

1. **Open a new terminal** and navigate to client directory:
   ```bash
   cd client
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start development server**:
   ```bash
   npm run dev
   ```

4. **Open browser** to `http://localhost:5173`

## 🎯 How to Use

1. **Click the microphone button** to start recording
2. **Speak clearly** for 2-10 seconds
3. **Click the microphone button again** to stop recording
4. **View results** showing:
   - Predicted emotion
   - Confidence scores for all emotions
   - Recording duration

## 📁 Project Structure

```
SER/
├── backend/
│   ├── app.py              # Flask API server
│   ├── save_models.py      # Model training script
│   ├── requirements.txt    # Python dependencies
│   └── models/             # Trained ML models
├── client/
│   ├── src/
│   │   ├── App.jsx         # Main React component
│   │   ├── main.jsx        # React entry point
│   │   └── styles/         # CSS styles
│   ├── package.json        # Node.js dependencies
│   └── index.html          # HTML template
├── start_system.py         # Automated startup script
└── README.md              # This file
```

## 🔧 API Endpoints

- `POST /api/start_recording` - Start audio recording
- `POST /api/stop_recording` - Stop recording and get emotion prediction
- `GET /api/status` - Get current recording status
- `GET /api/health` - Health check

## 🧠 Machine Learning Details

### Feature Extraction
- **MFCC Features**: 40 coefficients + deltas
- **Spectral Features**: Centroid, bandwidth, rolloff, zero-crossing rate
- **Chroma & Contrast**: Musical and spectral contrast
- **Additional**: Tonnetz, RMS energy, Pitch estimation
- **Total Features**: ~200+ per audio sample

### Models Used
- **Random Forest**: 200 estimators, max depth 20
- **Logistic Regression**: L1 regularization
- **SVM**: RBF kernel with probability estimates
- **LightGBM**: Gradient boosting

### Dataset
- **RAVDESS**: Professional emotional speech database
- **8 Emotions**: neutral, calm, happy, sad, angry, fearful, disgust, surprised
- **Data Cleaning**: RMS filtering, duration checks, feature validation

## 🎨 UI Features

- **Gradient Background**: Beautiful radial gradient design
- **Animated Microphone**: Ripple effects and color changes
- **Wave Animation**: Real-time visual feedback during recording
- **Results Display**: Clean cards showing emotion and confidence scores
- **Error Handling**: User-friendly error messages
- **Responsive Design**: Works on different screen sizes

## 🐛 Troubleshooting

### Common Issues

1. **"Models not found" error**:
   - Ensure RAVDESS dataset is in the root directory
   - Run `python backend/save_models.py` manually

2. **Microphone permission denied**:
   - Grant microphone permissions in your browser
   - Check system microphone settings

3. **Backend connection failed**:
   - Ensure Flask server is running on port 5000
   - Check firewall settings

4. **Audio processing errors**:
   - Speak clearly and avoid background noise
   - Ensure recording duration is at least 1 second

### Performance Tips

- **Close other applications** using the microphone
- **Use a good quality microphone** for better results
- **Speak clearly** and avoid background noise
- **Record for 3-5 seconds** for optimal results

## 📊 Performance

- **Model Accuracy**: 70-85% depending on the model
- **Processing Time**: ~1-2 seconds for emotion prediction
- **Audio Quality**: Works best with clear speech, 48kHz sample rate
- **Supported Formats**: WAV, MP3, and other common audio formats

## 🔮 Future Enhancements

- [ ] Real-time emotion detection during recording
- [ ] Support for multiple languages
- [ ] Emotion history and trends
- [ ] Custom model training interface
- [ ] Mobile app version
- [ ] Voice activity detection
- [ ] Emotion-based music recommendations

## 📝 License

This project is for educational and research purposes.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the system.

---

**Enjoy analyzing emotions through speech! 🎉**
