import requests
import json

def emotion_detector(text_to_analyze): 
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data=  { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=json_data, headers=headers) 
    res = json.loads(response.text)
    
    if res['code'] == 3:
        return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        };

    
    
    emotions = res['emotionPredictions']
    emotion_data = emotions[0]['emotion'] 

    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']
    
    
    dominant_emotion = None
    highest_score = -1
    for emotion, score in emotion_data.items():
        if score > highest_score:
            highest_score = score
            dominant_emotion = emotion
        
    return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }; 


