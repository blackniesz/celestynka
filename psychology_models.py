'percentile': self._score_to_percentile(score),
                'career_implications': self.career_implications[trait][level if level != 'medium' else 'high']
            }
        
        # Analiza kombinacji cech
        profile['combinations'] = self._analyze_combinations(big_five_scores)
        profile['overall_assessment'] = self._generate_overall_assessment(big_five_scores)
        
        return profile
    
    def _categorize_score(self, score: float) -> str:
        """Kategoryzacja wyniku na poziomy"""
        if score >= 4.0:
            return 'high'
        elif score >= 2.5:
            return 'medium'
        else:
            return 'low'
    
    def _score_to_percentile(self, score: float) -> int:
        """Konwersja score na percentyl"""
        return int((score / 5.0) * 100)
    
    def _analyze_combinations(self, scores: Dict[str, float]) -> List[Dict[str, str]]:
        """Analiza kombinacji cech"""
        combinations = []
        
        # Natural Leader (High E + High C)
        if scores.get('extraversion', 3) >= 3.5 and scores.get('conscientiousness', 3) >= 3.5:
            combinations.append({
                'type': 'Natural Leader',
                'description': 'Kombinacja wysokiej ekstrawersji i sumienności wskazuje na naturalne predyspozycje przywódcze',
                'implications': 'Idealne role: Team Leader, Project Manager, Operations Director'
            })
        
        # Innovation Driver (High O + Moderate A)
        if scores.get('openness', 3) >= 3.8 and scores.get('agreeableness', 3) <= 3.5:
            combinations.append({
                'type': 'Innovation Driver',
                'description': 'Kreatywność połączona z asertywnym podejściem do zmian',
                'implications': 'Idealne role: Innovation Manager, Product Developer, Strategy Lead'
            })
        
        # Reliable Executor (High C + High ES)
        if scores.get('conscientiousness', 3) >= 4.0 and scores.get('emotional_stability', 3) >= 3.5:
            combinations.append({
                'type': 'Reliable Executor',
                'description': 'Wysoka niezawodność i stabilność emocjonalna',
                'implications': 'Idealne role: Operations Manager, Quality Assurance, Senior Specialist'
            })
        
        # Creative Collaborator (High O + High A)
        if scores.get('openness', 3) >= 3.5 and scores.get('agreeableness', 3) >= 3.8:
            combinations.append({
                'type': 'Creative Collaborator',
                'description': 'Łączy kreatywność z umiejętnościami współpracy',
                'implications': 'Idealne role: UX Designer, Creative Director, Team Facilitator'
            })
        
        # Analytical Thinker (Low E + High O + High C)
        if (scores.get('extraversion', 3) <= 3.0 and 
            scores.get('openness', 3) >= 3.5 and 
            scores.get('conscientiousness', 3) >= 3.5):
            combinations.append({
                'type': 'Analytical Thinker',
                'description': 'Głęboka analiza i systematyczne podejście do problemów',
                'implications': 'Idealne role: Data Scientist, Research Analyst, Strategy Consultant'
            })
        
        return combinations
    
    def _generate_overall_assessment(self, scores: Dict[str, float]) -> Dict[str, Any]:
        """Generowanie ogólnej oceny"""
        avg_score = np.mean(list(scores.values()))
        
        # Identyfikacja dominującego wzorca
        highest_trait = max(scores.keys(), key=lambda k: scores[k])
        lowest_trait = min(scores.keys(), key=lambda k: scores[k])
        
        # Obliczenie balansu osobowości
        score_range = max(scores.values()) - min(scores.values())
        balance_score = 5 - score_range  # Im mniejszy rozstęp, tym lepszy balans
        
        return {
            'average_score': round(avg_score, 2),
            'dominant_trait': highest_trait,
            'development_area': lowest_trait,
            'personality_balance': max(0, round(balance_score, 2)),
            'overall_profile': self._determine_overall_profile(scores),
            'strengths_summary': self._generate_strengths_summary(scores),
            'development_recommendations': self._generate_development_recommendations(scores)
        }
    
    def _determine_overall_profile(self, scores: Dict[str, float]) -> str:
        """Określenie ogólnego profilu osobowości"""
        e = scores.get('extraversion', 3)
        a = scores.get('agreeableness', 3)
        c = scores.get('conscientiousness', 3)
        es = scores.get('emotional_stability', 3)
        o = scores.get('openness', 3)
        
        if e >= 3.5 and c >= 3.5 and es >= 3.5:
            return "Natural Leader - Pewny siebie lider z wysokimi kompetencjami wykonawczymi"
        elif o >= 4.0 and c >= 3.5:
            return "Innovation Catalyst - Kreatywny myśliciel z umiejętnością realizacji pomysłów"
        elif c >= 4.0 and es >= 3.5 and a >= 3.5:
            return "Reliable Partner - Niezawodny współpracownik i ekspert w swojej dziedzinie"
        elif o >= 3.8 and a >= 3.8:
            return "Creative Collaborator - Kreatywny zespołowiec z silnymi kompetencjami interpersonalnymi"
        elif e <= 3.0 and o >= 3.5 and c >= 3.5:
            return "Deep Thinker - Analityczny umysł z skłonnością do głębokiej refleksji"
        else:
            return "Balanced Achiever - Wszechstronny profil z potencjałem w różnych obszarach"
    
    def _generate_strengths_summary(self, scores: Dict[str, float]) -> List[str]:
        """Generowanie listy mocnych stron"""
        strengths = []
        
        if scores.get('extraversion', 3) >= 3.5:
            strengths.append("Naturalne umiejętności interpersonalne i przywódcze")
        if scores.get('agreeableness', 3) >= 3.5:
            strengths.append("Silne kompetencje zespołowe i empatia")
        if scores.get('conscientiousness', 3) >= 3.5:
            strengths.append("Wysoka niezawodność i umiejętności organizacyjne")
        if scores.get('emotional_stability', 3) >= 3.5:
            strengths.append("Odporność na stres i stabilność emocjonalna")
        if scores.get('openness', 3) >= 3.5:
            strengths.append("Kreatywność i otwartość na innowacje")
        
        return strengths
    
    def _generate_development_recommendations(self, scores: Dict[str, float]) -> List[str]:
        """Generowanie rekomendacji rozwoju"""
        recommendations = []
        
        if scores.get('extraversion', 3) < 3.0:
            recommendations.append("Rozwijaj umiejętności prezentacji i public speaking")
        if scores.get('agreeableness', 3) < 3.0:
            recommendations.append("Pracuj nad współpracą zespołową i empatią")
        if scores.get('conscientiousness', 3) < 3.0:
            recommendations.append("Wzmacniaj samodyscyplinę i umiejętności organizacyjne")
        if scores.get('emotional_stability', 3) < 3.0:
            recommendations.append("Rozwijaj techniki zarządzania stresem")
        if scores.get('openness', 3) < 3.0:
            recommendations.append("Eksperymentuj z nowymi podejściami i metodami pracy")
        
        return recommendations


class MotivationAnalyzer:
    """Analiza motywatorów według teorii autodeterminacji (SDT)"""
    
    def __init__(self):
        self.motivation_categories = {
            'autonomy': {
                'description': 'Potrzeba kontroli nad własną pracą i decyzjami',
                'indicators': ['Autonomia w działaniu', 'Kontrola nad metodami pracy', 'Swoboda decyzyjna']
            },
            'mastery': {
                'description': 'Dążenie do doskonałości i ciągłego rozwoju',
                'indicators': ['Uczenie się nowych rzeczy', 'Rozwój umiejętności', 'Doskonalenie się']
            },
            'purpose': {
                'description': 'Potrzeba sensu i wpływu na świat',
                'indicators': ['Pomaganie innym ludziom', 'Wpływ na społeczeństwo', 'Znacząca praca']
            },
            'achievement': {
                'description': 'Dążenie do osiągania celów i sukcesów',
                'indicators': ['Osiąganie celów', 'Uznanie za osiągnięcia', 'Konkurencja', 'Wyniki']
            },
            'affiliation': {
                'description': 'Potrzeba przynależności i relacji społecznych',
                'indicators': ['Współpraca w zespole', 'Budowanie relacji', 'Przynależność do grupy']
            },
            'security': {
                'description': 'Potrzeba stabilności i bezpieczeństwa',
                'indicators': ['Stabilność zatrudnienia', 'Przewidywalność', 'Bezpieczeństwo finansowe']
            }
        }
    
    def analyze(self, energy_sources: List[str], values_importance: Dict[str, int]) -> Dict[str, Any]:
        """Analiza profilu motywacyjnego"""
        
        # Mapowanie źródeł energii na kategorie motywacyjne
        motivation_scores = self._calculate_motivation_scores(energy_sources, values_importance)
        
        # Identyfikacja głównych motywatorów
        top_motivators = self._identify_top_motivators(motivation_scores)
        
        # Analiza trwałości motywacji
        sustainability_analysis = self._analyze_sustainability(motivation_scores)
        
        # Rekomendacje środowiska pracy
        work_environment = self._recommend_work_environment(motivation_scores)
        
        # Analiza potencjalnych konfliktów
        motivation_conflicts = self._analyze_conflicts(motivation_scores)
        
        return {
            'motivation_scores': motivation_scores,
            'top_motivators': top_motivators,
            'sustainability_analysis': sustainability_analysis,
            'ideal_work_environment': work_environment,
            'potential_conflicts': motivation_conflicts,
            'motivation_profile_summary': self._generate_profile_summary(top_motivators)
        }
    
    def _calculate_motivation_scores(self, energy_sources: List[str], 
                                   values_importance: Dict[str, int]) -> Dict[str, float]:
        """Obliczanie wyników motywacyjnych"""
        scores = {category: 0.0 for category in self.motivation_categories.keys()}
        
        # Mapowanie źródeł energii na kategorie
        energy_mapping = {
            'Rozwiązywanie skomplikowanych problemów': ['mastery', 'achievement'],
            'Pomaganie innym ludziom': ['purpose', 'affiliation'],
            'Tworzenie czegoś nowego': ['mastery', 'autonomy'],
            'Optymalizacja procesów': ['mastery', 'achievement'],
            'Budowanie relacji': ['affiliation', 'purpose'],
            'Uczenie się nowych rzeczy': ['mastery'],
            'Osiąganie celów': ['achievement'],
            'Współpraca w zespole': ['affiliation'],
            'Autonomia w działaniu': ['autonomy'],
            'Uznanie za osiągnięcia': ['achievement']
        }
        
        # Punktacja na podstawie źródeł energii
        for source in energy_sources:
            if source in energy_mapping:
                for category in energy_mapping[source]:
                    scores[category] += 1.0
        
        # Normalizacja wyników (0-1)
        max_possible = len(energy_sources)
        if max_possible > 0:
            scores = {k: v / max_possible for k, v in scores.items()}
        
        return scores
    
    def _identify_top_motivators(self, scores: Dict[str, float]) -> List[Dict[str, Any]]:
        """Identyfikacja głównych motywatorów"""
        sorted_motivators = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        top_motivators = []
        for motivator, score in sorted_motivators[:3]:  # Top 3
            top_motivators.append({
                'name': motivator,
                'score': score,
                'description': self.motivation_categories[motivator]['description'],
                'strength_level': self._categorize_motivation_strength(score)
            })
        
        return top_motivators
    
    def _categorize_motivation_strength(self, score: float) -> str:
        """Kategoryzacja siły motywatora"""
        if score >= 0.7:
            return 'Bardzo silny'
        elif score >= 0.5:
            return 'Silny'
        elif score >= 0.3:
            return 'Umiarkowany'
        else:
            return 'Słaby'
    
    def _analyze_sustainability(self, scores: Dict[str, float]) -> Dict[str, Any]:
        """Analiza trwałości motywacji"""
        
        # Motywatory intrinsic (bardziej trwałe) vs extrinsic
        intrinsic_motivators = ['autonomy', 'mastery', 'purpose']
        extrinsic_motivators = ['achievement', 'affiliation', 'security']
        
        intrinsic_score = sum(scores[m] for m in intrinsic_motivators) / len(intrinsic_motivators)
        extrinsic_score = sum(scores[m] for m in extrinsic_motivators) / len(extrinsic_motivators)
        
        sustainability_rating = (intrinsic_score * 0.7 + extrinsic_score * 0.3)
        
        return {
            'intrinsic_motivation_level': round(intrinsic_score, 2),
            'extrinsic_motivation_level': round(extrinsic_score, 2),
            'overall_sustainability': round(sustainability_rating, 2),
            'sustainability_rating': self._rate_sustainability(sustainability_rating),
            'recommendations': self._generate_sustainability_recommendations(intrinsic_score, extrinsic_score)
        }
    
    def _rate_sustainability(self, score: float) -> str:
        """Ocena trwałości motywacji"""
        if score >= 0.7:
            return 'Bardzo wysoka - motywacja długoterminowo stabilna'
        elif score >= 0.5:
            return 'Wysoka - dobra stabilność motywacyjna'
        elif score >= 0.3:
            return 'Średnia - wymaga regularnego odnowienia'
        else:
            return 'Niska - potrzebne zewnętrzne wsparcie motywacji'
    
    def _generate_sustainability_recommendations(self, intrinsic: float, extrinsic: float) -> List[str]:
        """Rekomendacje dla podtrzymania motywacji"""
        recommendations = []
        
        if intrinsic < 0.5:
            recommendations.extend([
                'Znajdź głębszy sens w swojej pracy',
                'Negocjuj większą autonomię w podejmowaniu decyzji',
                'Ustaw cele rozwoju osobistego'
            ])
        
        if extrinsic > intrinsic * 1.5:
            recommendations.extend([
                'Zbalansuj external rewards z internal satisfaction',
                'Fokus na long-term growth zamiast short-term wins',
                'Buduj connections między pracą a personal values'
            ])
        
        recommendations.extend([
            'Regularnie reflektuj nad swoimi motivations',
            'Szukaj variety w zadaniach i projektach',
            'Buduj support network w workplace'
        ])
        
        return recommendations
    
    def _recommend_work_environment(self, scores: Dict[str, float]) -> Dict[str, List[str]]:
        """Rekomendacje optymalnego środowiska pracy"""
        recommendations = {
            'culture_type': [],
            'management_style': [],
            'work_structure': [],
            'team_dynamics': [],
            'avoid': []
        }
        
        # Autonomy-driven recommendations
        if scores['autonomy'] >= 0.5:
            recommendations['culture_type'].append('Kultura zaufania i empowerment')
            recommendations['management_style'].append('Delegujący styl przywództwa')
            recommendations['work_structure'].append('Elastyczne godziny i metody pracy')
            recommendations['avoid'].append('Mikrozarządzanie i sztywne procedury')
        
        # Mastery-driven recommendations
        if scores['mastery'] >= 0.5:
            recommendations['culture_type'].append('Learning organization z focus na rozwój')
            recommendations['work_structure'].append('Możliwości uczenia się i eksperymentowania')
            recommendations['team_dynamics'].append('Mentoring i knowledge sharing')
        
        # Purpose-driven recommendations
        if scores['purpose'] >= 0.5:
            recommendations['culture_type'].append('Mission-driven organization')
            recommendations['work_structure'].append('Projekty z social impact')
            recommendations['avoid'].append('Czysto komercyjne role bez wyższego celu')
        
        # Achievement-driven recommendations
        if scores['achievement'] >= 0.5:
            recommendations['culture_type'].append('Performance-oriented culture')
            recommendations['management_style'].append('Goal-setting i regular feedback')
            recommendations['work_structure'].append('Jasne metryki sukcesu i recognition')
        
        # Affiliation-driven recommendations
        if scores['affiliation'] >= 0.5:
            recommendations['team_dynamics'].append('Collaborative teams z strong bonds')
            recommendations['culture_type'].append('People-first culture')
            recommendations['avoid'].append('Isolating work arrangements')
        
        return recommendations
    
    def _analyze_conflicts(self, scores: Dict[str, float]) -> List[Dict[str, str]]:
        """Analiza potencjalnych konfliktów motywacyjnych"""
        conflicts = []
        
        # Autonomy vs Affiliation conflict
        if scores['autonomy'] >= 0.6 and scores['affiliation'] >= 0.6:
            conflicts.append({
                'type': 'Autonomy-Affiliation Tension',
                'description': 'Konflikt między potrzebą niezależności a potrzebą przynależności',
                'management_strategy': 'Szukaj ról pozwalających na independent work w team setting'
            })
        
        # Achievement vs Purpose conflict
        if scores['achievement'] >= 0.6 and scores['purpose'] >= 0.6:
            conflicts.append({
                'type': 'Achievement-Purpose Balance',
                'description': 'Napięcie między personal success a serving higher purpose',
                'management_strategy': 'Znajdź organizacje gdzie personal achievement serves larger mission'
            })
        
        # Security vs Autonomy conflict
        if scores['security'] >= 0.5 and scores['autonomy'] >= 0.6:
            conflicts.append({
                'type': 'Security-Autonomy Dilemma',
                'description': 'Konflikt między potrzebą stabilności a potrzebą swobody',
                'management_strategy': 'Gradualne zwiększanie autonomii przy zachowaniu core security'
            })
        
        return conflicts
    
    def _generate_profile_summary(self, top_motivators: List[Dict]) -> str:
        """Generowanie podsumowania profilu motywacyjnego"""
        if not top_motivators:
            return "Profil motywacyjny wymaga dalszej analizy"
        
        primary = top_motivators[0]['name']
        
        profile_descriptions = {
            'autonomy': 'Independent Achiever - najlepiej pracujesz gdy masz control over your work',
            'mastery': 'Growth-Oriented Professional - napędza Cię continuous learning i improvement',
            'purpose': 'Mission-Driven Individual - szukasz meaningful work z positive impact',
            'achievement': 'Results-Oriented Performer - motywują Cię clear goals i recognition',
            'affiliation': 'People-Focused Collaborator - thriving w team environments',
            'security': 'Stability-Seeking Professional - values predictability i long-term security'
        }
        
        return profile_descriptions.get(primary, 'Unique motivational profile')


class CognitiveProfiler:
    """Analiza stylów kognitywnych i myślenia"""
    
    def __init__(self):
        self.thinking_styles = {
            'sequential': {
                'description': 'Sekwencyjne przetwarzanie - krok po kroku',
                'strengths': ['Systematyczna analiza', 'Dokładność', 'Metodyczność'],
                'ideal_tasks': ['Project planning', 'Process design', 'Quality assurance']
            },
            'holistic': {
                'description': 'Holistyczne myślenie - całościowy obraz',
                'strengths': ['Widzenie connections', 'Strategic thinking', 'Pattern recognition'],
                'ideal_tasks': ['Strategy development', 'System design', 'Innovation']
            },
            'visual': {
                'description': 'Wizualne przetwarzanie - obrazy i schematy',
                'strengths': ['Data visualization', 'Spatial reasoning', 'Design thinking'],
                'ideal_tasks': ['UX design', 'Architecture', 'Data presentation']
            },
            'kinesthetic': {
                'description': 'Praktyczne uczenie - przez działanie',
                'strengths': ['Hands-on problem solving', 'Experimentation', 'Implementation'],
                'ideal_tasks': ['Prototyping', 'Field work', 'Training delivery']
            }
        }
        
        self.decision_styles = {
            'analytical': {
                'description': 'Decyzje oparte na analizie danych',
                'approach': 'Systematic evaluation of options',
                'best_for': ['Complex problems', 'High-stakes decisions', 'Technical choices']
            },
            'intuitive': {
                'description': 'Decyzje oparte na intuicji',
                'approach': 'Quick pattern recognition and gut feelings',
                'best_for': ['Time pressure', 'People decisions', 'Creative choices']
            },
            'collaborative': {
                'description': 'Decyzje poprzez konsultacje',
                'approach': 'Seeking input and building consensus',
                'best_for': ['Team decisions', 'Change management', 'Stakeholder alignment']
            },
            'directive': {
                'description': 'Szybkie, zdecydowane działanie',
                'approach': 'Quick decisions based on experience',
                'best_for': ['Crisis situations', 'Routine decisions', 'Leadership moments']
            }
        }
    
    def analyze(self, processing_style: str, decision_style: str, 
                cognitive_strengths: Dict[str, int]) -> Dict[str, Any]:
        """Analiza profilu kognitywnego"""
        
        # Wyciągnij clean style names
        processing_clean = self._extract_style_name(processing_style)
        decision_clean = self._extract_style_name(decision_style)
        
        # Analiza mocnych stron kognitywnych
        cognitive_analysis = self._analyze_cognitive_strengths(cognitive_strengths)
        
        # Identyfikacja optimal career fits
        career_fit_analysis = self._analyze_career_fit(
            processing_clean, decision_clean, cognitive_analysis
        )
        
        # Rekomendacje rozwoju
        development_recommendations = self._generate_development_recommendations(
            processing_clean, decision_clean, cognitive_analysis
        )
        
        return {
            'processing_style': {
                'type': processing_clean,
                'description': self.thinking_styles.get(processing_clean, {}).get('description', ''),
                'strengths': self.thinking_styles.get(processing_clean, {}).get('strengths', []),
                'ideal_tasks': self.thinking_styles.get(processing_clean, {}).get('ideal_tasks', [])
            },
            'decision_style': {
                'type': decision_clean,
                'description': self.decision_styles.get(decision_clean, {}).get('description', ''),
                'approach': self.decision_styles.get(decision_clean, {}).get('approach', ''),
                'best_for': self.decision_styles.get(decision_clean, {}).get('best_for', [])
            },
            'cognitive_strengths_analysis': cognitive_analysis,
            'career_fit_analysis': career_fit_analysis,
            'development_recommendations': development_recommendations,
            'cognitive_efficiency_score': self._calculate_efficiency_score(cognitive_strengths)
        }
    
    def _extract_style_name(self, style_string: str) -> str:
        """Wyciągnij clean style name z description"""
        style_mapping = {
            'sekwencyjnie': 'sequential',
            'krok po kroku': 'sequential',
            'holistycznie': 'holistic',
            'całościowy': 'holistic',
            'wizualnie': 'visual',
            'obrazami': 'visual',
            'praktycznie': 'kinesthetic',
            'działanie': 'kinesthetic',
            'analitycznie': 'analytical',
            'dane': 'analytical',
            'intuicyjnie': 'intuitive',
            'gut feeling': 'intuitive',
            'kolaboracyjnie': 'collaborative',
            'konsultuje': 'collaborative',
            'dyrektywnie': 'directive',
            'szybko': 'directive'
        }
        
        style_lower = style_string.lower()
        for keyword, style in style_mapping.items():
            if keyword in style_lower:
                return style
        
        return 'holistic'  # Default
    
    def _analyze_cognitive_strengths(self, strengths: Dict[str, int]) -> Dict[str, Any]:
        """Analiza mocnych stron kognitywnych"""
        if not strengths:
            return {'top_strengths': [], 'average_level': 5.0, 'development_areas': []}
        
        # Sortuj strengths według score
        sorted_strengths = sorted(strengths.items(), key=lambda x: x[1], reverse=True)
        
        top_strengths = [
            {
                'name': name,
                'score': score,
                'level': self._categorize_cognitive_level(score),
                'description': self._get_cognitive_description(name)
            }
            for name, score in sorted_strengths[:3]
        ]
        
        average_level = np.mean(list(strengths.values()))
        
        development_areas = [
            {
                'name': name,
                'current_score': score,
                'improvement_potential': 10 - score,
                'development_priority': 'High' if score < 6 else 'Medium'
            }
            for name, score in sorted_strengths if score < 7
        ]
        
        return {
            'top_strengths': top_strengths,
            'average_level': round(average_level, 1),
            'development_areas': development_areas,
            'cognitive_balance': self._assess_cognitive_balance(strengths)
        }
    
    def _categorize_cognitive_level(self, score: int) -> str:
        """Kategoryzacja poziomu kognitywnego"""
        if score >= 8:
            return 'Expert'
        elif score >= 6:
            return 'Proficient'
        elif score >= 4:
            return 'Developing'
        else:
            return 'Novice'
    
    def _get_cognitive_description(self, strength_name: str) -> str:
        """Opis mocnej strony kognitywnej"""
        descriptions = {
            'strategic': 'Zdolność do długoterminowego planowania i przewidywania trendów',
            'creative': 'Generowanie innowacyjnych rozwiązań i niestandardowego myślenia',
            'analytical': 'Systematyczna analiza problemów i logical reasoning',
            'systemic': 'Rozumienie złożonych systemów i ich wzajemnych powiązań',
            'operational': 'Praktyczne wykonanie i optymalizacja procesów'
        }
        
        # Find matching description
        for key, desc in descriptions.items():
            if key in strength_name.lower():
                return desc
        
        return 'Specialized cognitive ability'
    
    def _assess_cognitive_balance(self, strengths: Dict[str, int]) -> Dict[str, Any]:
        """Ocena balansu kognitywnego"""
        if not strengths:
            return {'balance_score': 5.0, 'assessment': 'Balanced'}
        
        scores = list(strengths.values())
        score_range = max(scores) - min(scores)
        balance_score = 10 - score_range  # Im mniejszy rozstęp, tym lepszy balans
        
        if balance_score >= 7:
            assessment = 'Bardzo zbalansowany profil kognitywny'
        elif balance_score >= 5:
            assessment = 'Dobrze zbalansowany z wyraźnymi mocnymi stronami'
        else:
            assessment = 'Wyspecjalizowany profil z distinct peaks and valleys'
        
        return {
            'balance_score': max(0, balance_score),
            'assessment': assessment,
            'recommendation': self._get_balance_recommendation(balance_score)
        }
    
    def _get_balance_recommendation(self, balance_score: float) -> str:
        """Rekomendacja na podstawie balansu"""
        if balance_score >= 7:
            return 'Utilize your balanced profile for versatile roles'
        elif balance_score >= 5:
            return 'Leverage your strengths while gradually developing weaker areas'
        else:
            return 'Consider specialist roles that maximize your peak strengths'
    
    def _analyze_career_fit(self, processing_style: str, decision_style: str, 
                           cognitive_analysis: Dict) -> Dict[str, List[str]]:
        """Analiza dopasowania do karier"""
        career_recommendations = {
            'ideal_roles': [],
            'good_fit_roles': [],
            'challenging_roles': []
        }
        
        # Kombinacje stylów i rekomendacje ról
        style_combinations = {
            ('holistic', 'analytical'): {
                'ideal': ['Strategy Consultant', 'Business Analyst', 'Systems Architect'],
                'good': ['Product Manager', 'Research Director', 'Management Consultant']
            },
            ('holistic', 'intuitive'): {
                'ideal': ['Innovation Director', 'Creative Director', 'Entrepreneur'],
                'good': ['Design Lead', 'Vision Strategy', 'Change Agent']
            },
            ('sequential', 'analytical'): {
                'ideal': ['Data Scientist', 'Financial Analyst', 'Quality Manager'],
                'good': ['Project Manager', 'Operations Analyst', 'Compliance Officer']
            },
            ('visual', 'collaborative'): {
                'ideal': ['UX Designer', 'Design Thinking Facilitator', 'Visual Communicator'],
                'good': ['Marketing Manager', 'Training Designer', 'Brand Strategist']
            },
            ('kinesthetic', 'directive'): {
                'ideal': ['Operations Manager', 'Field Manager', 'Implementation Lead'],
                'good': ['Sales Manager', 'Team Leader', 'Delivery Manager']
            }
        }
        
        combination = (processing_style, decision_style)
        if combination in style_combinations:
            career_recommendations['ideal_roles'] = style_combinations[combination]['ideal']
            career_recommendations['good_fit_roles'] = style_combinations[combination]['good']
        
        # Dodaj challenging roles (opposite combinations)
        if processing_style == 'sequential' and decision_style == 'intuitive':
            career_recommendations['challenging_roles'] = ['Creative roles requiring quick intuitive decisions']
        elif processing_style == 'holistic' and decision_style == 'directive':
            career_recommendations['challenging_roles'] = ['Detail-oriented implementation roles']
        
        return career_recommendations
    
    def _generate_development_recommendations(self, processing_style: str, decision_style: str,
                                            cognitive_analysis: Dict) -> List[Dict[str, str]]:
        """Generowanie rekomendacji rozwoju"""
        recommendations = []
        
        # Development based on processing style
        if processing_style == 'sequential':
            recommendations.append({
                'area': 'Strategic Thinking',
                'recommendation': 'Practice big-picture analysis and long-term planning',
                'methods': ['Case study analysis', 'Strategic planning workshops', 'Systems thinking training']
            })
        elif processing_style == 'holistic':
            recommendations.append({
                'area': 'Detail Orientation',
                'recommendation': 'Strengthen attention to implementation details',
                'methods': ['Project management training', 'Quality control processes', 'Structured methodologies']
            })
        
        # Development based on decision style
        if decision_style == 'analytical':
            recommendations.append({
                'area': 'Intuitive Decision Making',
                'recommendation': 'Develop trust in gut feelings and rapid assessment',
                'methods': ['Mindfulness training', 'Speed decision exercises', 'Pattern recognition practice']
            })
        elif decision_style == 'intuitive':
            recommendations.append({
                'area': 'Analytical Rigor',
                'recommendation': 'Strengthen data-driven decision making',
                'methods': ['Data analysis courses', 'Statistics training', 'Evidence-based frameworks']
            })
        
        # Development based on cognitive weaknesses
        development_areas = cognitive_analysis.get('development_areas', [])
        for area in development_areas[:2]:  # Top 2 development areas
            recommendations.append({
                'area': area['name'],
                'recommendation': f"Focus on improving {area['name']} skills",
                'methods': self._get_development_methods(area['name'])
            })
        
        return recommendations
    
    def _get_development_methods(self, skill_area: str) -> List[str]:
        """Metody rozwoju dla konkretnych obszarów"""
        methods_mapping = {
            'strategic': ['Business strategy courses', 'Long-term planning exercises', 'Scenario planning'],
            'creative': ['Design thinking workshops', 'Brainstorming techniques', 'Innovation challenges'],
            'analytical': ['Data analysis training', 'Critical thinking courses', 'Statistical methods'],
            'systemic': ['Systems thinking training', 'Process mapping', 'Complexity science'],
            'operational': ['Process optimization', 'Lean methodology', 'Implementation frameworks']
        }
        
        for key, methods in methods_mapping.items():
            if key in skill_area.lower():
                return methods
        
        return ['Professional development courses', 'Mentoring', 'Practical application']
    
    def _calculate_efficiency_score(self, cognitive_strengths: Dict[str, int]) -> Dict[str, Any]:
        """Obliczanie ogólnej efektywności kognitywnej"""
        if not cognitive_strengths:
            return {'score': 5.0, 'rating': 'Average', 'potential': 'Moderate'}
        
        scores = list(cognitive_strengths.values())
        average_score = np.mean(scores)
        max_score = max(scores)
        score_variance = np.var(scores)
        
        # Efficiency score combines average performance with peak performance
        efficiency_score = (average_score * 0.7) + (max_score * 0.3)
        
        # Rating based on efficiency score
        if efficiency_score >= 8:
            rating = 'Exceptional'
            potential = 'Very High'
        elif efficiency_score >= 7:
            rating = 'High'
            potential = 'High'
        elif efficiency_score >= 6:
            rating = 'Good'
            potential = 'Moderate'
        elif efficiency_score >= 5:
            rating = 'Average'
            potential = 'Developing'
        else:
            rating = 'Developing'
            potential = 'Needs Focus'
        
        return {
            'score': round(efficiency_score, 1),
            'rating': rating,
            'potential': potential,
            'variance': round(score_variance, 1),
            'interpretation': self._interpret_efficiency(efficiency_score, score_variance)
        }
    
    def _interpret_efficiency(self, score: float, variance: float) -> str:
        """Interpretacja wyniku efektywności"""
        if score >= 7 and variance <= 1:
            return 'Consistently high performance across all cognitive areas'
        elif score >= 7 and variance > 1:
            return 'Strong cognitive abilities with distinct specializations'
        elif score >= 5 and variance <= 1:
            return 'Balanced cognitive profile with room for development'
        elif score >= 5 and variance > 1:
            return 'Mixed cognitive profile - leverage strengths while developing weak areas'
        else:
            return 'Emerging cognitive capabilities with significant development potential'# psychology_models.py - Modele psychologiczne
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
