# psychology_models.py - Modele psychologiczne
import numpy as np
from typing import Dict, List, Any

class BigFiveAnalyzer:
    """Analiza profilu Big Five"""
    
    def __init__(self):
        self.trait_descriptions = {
            'extraversion': {
                'high': 'Energetyczny, towarzyski, asertywny',
                'medium': 'Zbalansowany między ekstrawersją a introwersją',
                'low': 'Spokojny, refleksyjny, niezależny'
            },
            'agreeableness': {
                'high': 'Współpracujący, ufający, empatyczny',
                'medium': 'Balans między współpracą a asertywością',
                'low': 'Konkurencyjny, obiektywny, asertywny'
            },
            'conscientiousness': {
                'high': 'Zorganizowany, niezawodny, zdyscyplinowany',
                'medium': 'Umiarkowanie systematyczny i elastyczny',
                'low': 'Elastyczny, spontaniczny, adaptacyjny'
            },
            'emotional_stability': {
                'high': 'Spokojny, odporny na stres, zrównoważony',
                'medium': 'Umiarkowana odporność na stres',
                'low': 'Wrażliwy, emocjonalny, potrzebuje wsparcia'
            },
            'openness': {
                'high': 'Kreatywny, innowacyjny, abstrakcyjny',
                'medium': 'Balans między kreatywnością a praktycznością',
                'low': 'Praktyczny, tradycyjny, konkretny'
            }
        }
        
        self.career_implications = {
            'extraversion': {
                'high': ['Team leadership', 'Sales', 'Public speaking', 'Client relations'],
                'low': ['Research', 'Analysis', 'Independent work', 'Technical roles']
            },
            'agreeableness': {
                'high': ['HR', 'Counseling', 'Team support', 'Mediation'],
                'low': ['Tough decisions', 'Negotiations', 'Competitive roles', 'Critical analysis']
            },
            'conscientiousness': {
                'high': ['Project management', 'Quality control', 'Administration', 'Planning'],
                'low': ['Creative work', 'Adaptive roles', 'Crisis management', 'Innovation']
            },
            'emotional_stability': {
                'high': ['High-pressure roles', 'Crisis management', 'Leadership', 'Public roles'],
                'low': ['Supportive environments', 'Structured roles', 'Predictable work']
            },
            'openness': {
                'high': ['Innovation', 'Creative roles', 'Research', 'Strategic planning'],
                'low': ['Operations', 'Traditional roles', 'Routine work', 'Implementation']
            }
        }
    
    def analyze(self, big_five_scores: Dict[str, float]) -> Dict[str, Any]:
        """Analiza profilu Big Five"""
        profile = {}
        
        for trait, score in big_five_scores.items():
            level = self._categorize_score(score)
            profile[trait] = {
                'score': score,
                'level': level,
                'description': self.trait_descriptions[trait][level],
                'percentile': self._score_to_percentile
