import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Unit tests for the emotion_detector function"""

    def test_emotion_detector_returns_dict(self):
        """Test that emotion_detector returns a dictionary"""
        result = emotion_detector("I love this!")
        self.assertIsInstance(result, dict)

    def test_emotion_detector_has_required_keys(self):
        """Test that the result contains all required emotion keys"""
        result = emotion_detector("I love this!")
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)

    def test_joy_emotion_prediction(self):
        """Test that the function correctly identifies joy emotion"""
        result = emotion_detector("I love this new technology")
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertIsNotNone(result['joy'])
        self.assertGreater(result['joy'], 0)

    def test_fear_emotion_prediction(self):
        """Test that the function correctly identifies fear emotion"""
        result = emotion_detector("I am really afraid and scared")
        self.assertEqual(result['dominant_emotion'], 'fear')
        self.assertIsNotNone(result['fear'])
        self.assertGreater(result['fear'], 0)

    def test_anger_emotion_prediction(self):
        """Test that the function correctly identifies anger emotion"""
        result = emotion_detector("I hate this so much")
        self.assertEqual(result['dominant_emotion'], 'anger')
        self.assertIsNotNone(result['anger'])
        self.assertGreater(result['anger'], 0)

    def test_sadness_emotion_prediction(self):
        """Test that the function correctly identifies sadness emotion"""
        result = emotion_detector("I am very sad and depressed")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertIsNotNone(result['sadness'])
        self.assertGreater(result['sadness'], 0)

    def test_disgust_emotion_prediction(self):
        """Test that the function correctly identifies disgust emotion"""
        result = emotion_detector("This is disgusting and repulsive")
        self.assertEqual(result['dominant_emotion'], 'disgust')
        self.assertIsNotNone(result['disgust'])
        self.assertGreater(result['disgust'], 0)

    def test_empty_string_returns_none(self):
        """Test that empty string returns None values"""
        result = emotion_detector("")
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])
        self.assertIsNone(result['dominant_emotion'])

    def test_invalid_text_returns_none(self):
        """Test that invalid text returns None values"""
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
