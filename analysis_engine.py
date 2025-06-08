def _identify_career_opportunities(self, big_five_scores: Dict[str, float], 
                                      user_data: Dict) -> List[Dict[str, str]]:
        """Identyfikacja możliwości zawodowych"""
        opportunities = []
        
        # Opportunities based on personality strengths
        if big_five_scores['openness'] >= 4.0:
            opportunities.append({
                'type': 'Innovation Leadership',
                'description': 'Twoja kreatywność i otwartość pozwalają na prowadzenie initiatives in emerging technologies',
                'timeframe': '6-12 miesięcy',
                'action_required': 'Build expertise w AI/ML, sustainability, lub other emerging fields'
            })
        
        if big_five_scores['extraversion'] >= 4.0 and big_five_scores['emotional_stability'] >= 3.5:
            opportunities.append({
                'type': 'Thought Leadership',
                'description': 'Natural communication skills i confidence make you ideal dla building industry presence',
                'timeframe': '12-18 miesięcy',
                'action_required': 'Start content creation, speaking at events, building professional brand'
            })
        
        if big_five_scores['conscientiousness'] >= 4.0:
            opportunities.append({
                'type': 'Process Excellence Leadership',
                'description': 'Exceptional organization skills position you dla operational excellence roles',
                'timeframe': '3-6 miesięcy',
                'action_required': 'Gain Lean Six Sigma certification, lead efficiency projects'
            })
        
        # Experience-based opportunities
        experience = user_data.get('experience', '0-1 lat')
        
        if experience in ['7-10 lat', 'Powyżej 10 lat']:
            opportunities.append({
                'type': 'Executive Transition',
                'description': 'Your experience level opens doors do C-suite i senior leadership roles',
                'timeframe': '12-24 miesiące',
                'action_required': 'Executive coaching, board readiness, strategic network building'
            })
        elif experience in ['4-6 lat']:
            opportunities.append({
                'type': 'Specialization Leadership',
                'description': 'Perfect timing do becoming recognized expert w your domain',
                'timeframe': '6-12 miesięcy', 
                'action_required': 'Develop thought leadership, obtain advanced certifications'
            })
        
        # Industry opportunities
        current_position = user_data.get('position', '').lower()
        if any(tech_keyword in current_position for tech_keyword in ['analyst', 'data', 'tech']):
            opportunities.append({
                'type': 'AI/ML Transition',
                'description': 'Growing demand dla AI expertise creates opportunities dla technical professionals',
                'timeframe': '8-12 miesięcy',
                'action_required': 'ML courses, AI certifications, portfolio projects'
            })
        
        # Market opportunities
        opportunities.append({
            'type': 'Remote/Global Market Access',
            'description': 'Digital transformation opens access do global opportunities',
            'timeframe': '3-6 miesięcy',
            'action_required': 'Enhance digital collaboration skills, build international network'
        })
        
        return opportunities
    
    def _identify_career_threats(self, big_five_scores: Dict[str, float], 
                                user_data: Dict) -> List[Dict[str, str]]:
        """Identyfikacja zagrożeń zawodowych"""
        threats = []
        
        # Personality-based vulnerabilities
        if big_five_scores['emotional_stability'] < 3.0:
            threats.append({
                'type': 'Stress Management Risk',
                'description': 'Lower emotional stability może impact performance w high-pressure environments',
                'likelihood': 'Medium-High',
                'mitigation': 'Develop stress management techniques, seek supportive work environments'
            })
        
        if big_five_scores['agreeableness'] > 4.0:
            threats.append({
                'type': 'Decision-Making Challenges',
                'description': 'High agreeableness może make difficult decisions involving conflict or unpopular choices',
                'likelihood': 'Medium',
                'mitigation': 'Assertiveness training, decision-making frameworks, executive coaching'
            })
        
        if big_five_scores['openness'] < 2.5:
            threats.append({
                'type': 'Adaptability Gap',
                'description': 'Low openness może limit ability do adapt do rapidly changing work environments',
                'likelihood': 'Medium',
                'mitigation': 'Gradual exposure do new technologies, change management training'
            })
        
        if big_five_scores['conscientiousness'] < 3.0:
            threats.append({
                'type': 'Execution Consistency',
                'description': 'Lower conscientiousness może impact reliability i follow-through on commitments',
                'likelihood': 'Medium',
                'mitigation': 'Project management tools, accountability systems, habit formation'
            })
        
        # Industry threats
        current_position = user_data.get('position', '').lower()
        
        if any(routine_keyword in current_position for routine_keyword in ['data entry', 'administrative', 'routine']):
            threats.append({
                'type': 'Automation Risk',
                'description': 'Routine tasks are increasingly subject do automation',
                'likelihood': 'High',
                'mitigation': 'Upskill do higher-value activities, focus na uniquely human capabilities'
            })
        
        # Economic threats
        threats.append({
            'type': 'Economic Uncertainty',
            'description': 'Economic downturns może impact job security across industries',
            'likelihood': 'Medium',
            'mitigation': 'Build diverse skill set, maintain emergency fund, strong professional network'
        })
        
        # Skills obsolescence
        threats.append({
            'type': 'Skills Obsolescence',
            'description': 'Rapid technological change może make current skills less relevant',
            'likelihood': 'Medium-High',
            'mitigation': 'Continuous learning mindset, regular skills assessment, technology adoption'
        })
        
        return threats
    
    def _develop_risk_management_strategy(self, risk_tolerance: Dict, 
                                        opportunities: List[Dict], 
                                        threats: List[Dict]) -> Dict[str, List[str]]:
        """Strategia zarządzania ryzykiem"""
        strategy = {
            'diversification_strategies': [],
            'safety_net_building': [],
            'opportunity_pursuit': [],
            'threat_monitoring': []
        }
        
        tolerance_level = risk_tolerance['level']
        
        # Diversification based on risk tolerance
        if tolerance_level in ['Bardzo wysoka', 'Wysoka']:
            strategy['diversification_strategies'].extend([
                'Portfolio career approach - multiple revenue streams',
                'Invest w emerging skills i technologies',
                'Build global professional network'
            ])
        else:
            strategy['diversification_strategies'].extend([
                'Gradual skill diversification within current domain',
                'Build relationships across different departments',
                'Develop backup career plans'
            ])
        
        # Safety nets
        strategy['safety_net_building'].extend([
            'Maintain 6-12 months emergency fund',
            'Build strong professional references',
            'Keep resume i LinkedIn updated quarterly',
            'Maintain industry certifications'
        ])
        
        # Opportunity pursuit strategy
        if tolerance_level in ['Bardzo wysoka', 'Wysoka']:
            strategy['opportunity_pursuit'].extend([
                'Aggressively pursue stretch assignments',
                'Apply dla roles slightly beyond current qualifications',
                'Consider entrepreneurial ventures'
            ])
        else:
            strategy['opportunity_pursuit'].extend([
                'Take calculated risks z clear fallback plans',
                'Pilot new approaches w current role',
                'Gradually expand comfort zone'
            ])
        
        # Threat monitoring
        strategy['threat_monitoring'].extend([
            'Regular industry trend analysis',
            'Skills relevance assessment (annually)',
            'Network pulse checks dla market sentiment',
            'Technology disruption monitoring'
        ])
        
        return strategy
    
    def _create_opportunity_action_plan(self, opportunities: List[Dict]) -> List[Dict[str, str]]:
        """Plan działania dla możliwości"""
        action_plan = []
        
        for i, opportunity in enumerate(opportunities[:3]):  # Top 3 opportunities
            action_plan.append({
                'opportunity': opportunity['type'],
                'priority': f"Priority {i+1}",
                'immediate_actions': opportunity.get('action_required', 'Research i planning'),
                'timeline': opportunity.get('timeframe', '6-12 miesięcy'),
                'success_criteria': f"Clear progress towards {opportunity['type']} within timeline",
                'resources_needed': 'Time investment, possibly financial dla courses/certifications'
            })
        
        return action_plan
    
    def _create_threat_mitigation_plan(self, threats: List[Dict]) -> List[Dict[str, str]]:
        """Plan mitygacji zagrożeń"""
        mitigation_plan = []
        
        for threat in threats:
            if threat.get('likelihood') in ['High', 'Medium-High']:
                mitigation_plan.append({
                    'threat': threat['type'],
                    'urgency': 'High' if threat.get('likelihood') == 'High' else 'Medium',
                    'mitigation_actions': threat.get('mitigation', 'Develop coping strategies'),
                    'monitoring_approach': 'Regular self-assessment i feedback',
                    'timeline': '3-6 miesięcy dla initial improvements'
                })
        
        return mitigation_plan
    
    def _generate_career_projections(self, recommended_paths: List[Dict], 
                                   user_data: Dict) -> Dict[str, Any]:
        """Generowanie projekcji kariery"""
        
        if not recommended_paths:
            return {'message': 'No career paths available dla projection'}
        
        projections = {}
        
        for path in recommended_paths[:3]:  # Top 3 paths
            career_title = path['title']
            
            # Career progression timeline
            progression = self._calculate_career_progression(career_title, user_data)
            
            # Salary projections
            salary_projection = self._calculate_salary_projections(path, user_data)
            
            # Market demand forecast
            market_forecast = self._forecast_market_demand(career_title)
            
            # Success probability over time
            success_probability = self._project_success_probability(path, user_data)
            
            projections[career_title] = {
                'career_progression': progression,
                'salary_projections': salary_projection,
                'market_forecast': market_forecast,
                'success_probability': success_probability,
                'key_milestones': self._define_career_milestones(career_title, user_data)
            }
        
        return projections
    
    def _calculate_career_progression(self, career_title: str, user_data: Dict) -> Dict[str, str]:
        """Obliczanie progresji kariery"""
        
        experience = user_data.get('experience', '0-1 lat')
        exp_mapping = {
            '0-1 lat': 1,
            '2-3 lata': 2.5,
            '4-6 lat': 5,
            '7-10 lat': 8.5,
            'Powyżej 10 lat': 12
        }
        
        current_years = exp_mapping.get(experience, 1)
        
        # Career ladders dla różnych ścieżek
        progressions = {
            'Product Manager': {
                0: 'Associate Product Manager',
                2: 'Product Manager',
                4: 'Senior Product Manager', 
                7: 'Principal Product Manager',
                10: 'Director of Product',
                15: 'VP Product'
            },
            'Strategy Consultant': {
                0: 'Business Analyst',
                2: 'Consultant',
                4: 'Senior Consultant',
                7: 'Manager/Principal', 
                10: 'Partner',
                15: 'Senior Partner'
            },
            'Data Scientist': {
                0: 'Junior Data Scientist',
                2: 'Data Scientist',
                4: 'Senior Data Scientist',
                7: 'Lead Data Scientist',
                10: 'Data Science Manager',
                15: 'Chief Data Officer'
            }
        }
        
        career_ladder = progressions.get(career_title, {
            0: 'Junior Level',
            2: 'Mid Level', 
            4: 'Senior Level',
            7: 'Lead Level',
            10: 'Director Level',
            15: 'Executive Level'
        })
        
        # Znajdź current i next levels
        current_level = 'Entry Level'
        next_level = 'Senior Level'
        years_to_next = 2
        
        for years, level in sorted(career_ladder.items()):
            if current_years >= years:
                current_level = level
            elif current_years < years:
                next_level = level
                years_to_next = years - current_years
                break
        
        return {
            'current_projected_level': current_level,
            'next_level': next_level,
            'years_to_next_level': str(max(1, int(years_to_next))),
            '5_year_projection': self._get_level_at_years(career_ladder, current_years + 5),
            '10_year_projection': self._get_level_at_years(career_ladder, current_years + 10)
        }
    
    def _get_level_at_years(self, career_ladder: Dict[int, str], target_years: float) -> str:
        """Znajdź poziom na określonym etapie kariery"""
        level = 'Senior Executive'
        for years, position in sorted(career_ladder.items()):
            if target_years >= years:
                level = position
            else:
                break
        return level
    
    def _calculate_salary_projections(self, path: Dict, user_data: Dict) -> Dict[str, int]:
        """Obliczanie projekcji zarobków"""
        
        min_salary, max_salary = path['salary_range']
        experience = user_data.get('experience', '0-1 lat')
        
        # Experience multipliers
        exp_multipliers = {
            '0-1 lat': 0.7,
            '2-3 lata': 0.85,
            '4-6 lat': 1.0,
            '7-10 lat': 1.25,
            'Powyżej 10 lat': 1.5
        }
        
        current_multiplier = exp_multipliers.get(experience, 1.0)
        
        # Annual growth assumptions
        annual_growth = 0.08  # 8% annual growth
        
        return {
            'current_range_min': int(min_salary * current_multiplier),
            'current_range_max': int(max_salary * current_multiplier),
            '3_year_projection_min': int(min_salary * current_multiplier * (1 + annual_growth) ** 3),
            '3_year_projection_max': int(max_salary * current_multiplier * (1 + annual_growth) ** 3),
            '5_year_projection_min': int(min_salary * current_multiplier * (1 + annual_growth) ** 5),
            '5_year_projection_max': int(max_salary * current_multiplier * (1 + annual_growth) ** 5),
            '10_year_projection_min': int(min_salary * current_multiplier * (1 + annual_growth) ** 10),
            '10_year_projection_max': int(max_salary * current_multiplier * (1 + annual_growth) ** 10)
        }
    
    def _forecast_market_demand(self, career_title: str) -> Dict[str, str]:
        """Prognoza zapotrzebowania rynkowego"""
        
        market_forecasts = {
            'Product Manager': {
                'short_term': 'Very High - digital transformation drives demand',
                'medium_term': 'High - sustained growth w tech sector',
                'long_term': 'High - product-centric approaches expanding',
                'growth_rate': '+15% annually'
            },
            'Strategy Consultant': {
                'short_term': 'High - post-pandemic transformation needs',
                'medium_term': 'Moderate - market stabilization',
                'long_term': 'Moderate - specialized expertise required',
                'growth_rate': '+8% annually'
            },
            'Data Scientist': {
                'short_term': 'Very High - AI/ML boom continues',
                'medium_term': 'Very High - data-driven decisions mainstream',
                'long_term': 'High - specialization w domain expertise',
                'growth_rate': '+22% annually'
            },
            'UX Designer': {
                'short_term': 'High - digital experience focus',
                'medium_term': 'Moderate - market saturation concerns',
                'long_term': 'Moderate - evolution towards specialized UX',
                'growth_rate': '+5% annually'
            }
        }
        
        return market_forecasts.get(career_title, {
            'short_term': 'Moderate',
            'medium_term': 'Moderate', 
            'long_term': 'Stable',
            'growth_rate': '+3% annually'
        })
    
    def _project_success_probability(self, path: Dict, user_data: Dict) -> Dict[str, int]:
        """Projekcja prawdopodobieństwa sukcesu"""
        
        base_probability = path['match_score']
        experience_bonus = self._get_experience_bonus(user_data.get('experience', '0-1 lat'))
        
        return {
            'year_1': min(95, int(base_probability * 0.8 + experience_bonus)),
            'year_3': min(95, int(base_probability * 0.9 + experience_bonus + 5)),
            'year_5': min(95, int(base_probability + experience_bonus + 10)),
            'year_10': min(95, int(base_probability + experience_bonus + 15))
        }
    
    def _get_experience_bonus(self, experience: str) -> int:
        """Bonus do prawdopodobieństwa na podstawie doświadczenia"""
        bonuses = {
            '0-1 lat': 0,
            '2-3 lata': 3,
            '4-6 lat': 5,
            '7-10 lat': 8,
            'Powyżej 10 lat': 10
        }
        return bonuses.get(experience, 0)
    
    def _define_career_milestones(self, career_title: str, user_data: Dict) -> List[Dict[str, str]]:
        """Definicja kamieni milowych kariery"""
        
        milestones_mapping = {
            'Product Manager': [
                {'milestone': 'First product launch', 'timeframe': '6-12 miesięcy'},
                {'milestone': 'Lead cross-functional team', 'timeframe': '12-18 miesięcy'},
                {'milestone': 'Product strategy ownership', 'timeframe': '18-24 miesiące'},
                {'milestone': 'Mentoring other PMs', 'timeframe': '3-4 lata'}
            ],
            'Strategy Consultant': [
                {'milestone': 'First client presentation', 'timeframe': '3-6 miesięcy'},
                {'milestone': 'Lead project workstream', 'timeframe': '12-18 miesięcy'},
                {'milestone': 'Client relationship management', 'timeframe': '2-3 lata'},
                {'milestone': 'Practice area expertise', 'timeframe': '4-5 lat'}
            ],
            'Data Scientist': [
                {'milestone': 'First ML model w production', 'timeframe': '6-9 miesięcy'},
                {'milestone': 'Business impact measurement', 'timeframe': '12-15 miesięcy'},
                {'milestone': 'Technical thought leadership', 'timeframe': '2-3 lata'},
                {'milestone': 'Data science team leadership', 'timeframe': '4-6 lat'}
            ]
        }
        
        return milestones_mapping.get(career_title, [
            {'milestone': 'Professional competency', 'timeframe': '6-12 miesięcy'},
            {'milestone': 'Independent execution', 'timeframe': '12-24 miesiące'},
            {'milestone': 'Leadership responsibilities', 'timeframe': '2-4 lata'},
            {'milestone': 'Industry recognition', 'timeframe': '5+ lat'}
        ])
    
    def _calculate_success_probability(self, personality_profile: Dict, 
                                     motivation_profile: Dict, 
                                     cognitive_profile: Dict) -> Dict[str, Any]:
        """Obliczanie prawdopodobieństwa sukcesu zawodowego"""
        
        # Success factors assessment
        success_factors = {
            'personality_optimization': self._assess_personality_for_success(personality_profile),
            'motivation_sustainability': self._assess_motivation_sustainability(motivation_profile),
            'cognitive_effectiveness': self._assess_cognitive_effectiveness(cognitive_profile),
            'adaptability_quotient': self._assess_adaptability_factor(personality_profile),
            'execution_reliability': self._assess_execution_capability(personality_profile)
        }
        
        # Weighted success score
        weights = {
            'personality_optimization': 0.25,
            'motivation_sustainability': 0.25,
            'cognitive_effectiveness': 0.25,
            'adaptability_quotient': 0.15,
            'execution_reliability': 0.10
        }
        
        overall_success_score = sum(
            score * weights[factor] for factor, score in success_factors.items()
        )
        
        return {
            'overall_success_probability': round(overall_success_score, 1),
            'success_factors_breakdown': success_factors,
            'key_success_drivers': self._identify_success_drivers(success_factors),
            'improvement_areas': self._identify_improvement_areas(success_factors),
            'success_accelerators': self._recommend_success_accelerators(success_factors)
        }
    
    def _assess_personality_for_success(self, personality_profile: Dict) -> float:
        """Ocena osobowości dla sukcesu zawodowego"""
        
        # Extract scores
        scores = {}
        for trait in ['extraversion', 'agreeableness', 'conscientiousness', 'emotional_stability', 'openness']:
            if trait in personality_profile and isinstance(personality_profile[trait], dict):
                scores[trait] = personality_profile[trait].get('score', 3.0)
            else:
                scores[trait] = 3.0
        
        # Conscientiousness najbardziej predykcyjne dla sukcesu
        conscientiousness_impact = scores['conscientiousness'] * 30
        
        # Emotional stability kluczowa dla performance under pressure
        stability_impact = scores['emotional_stability'] * 25
        
        # Moderate extraversion optimal dla większości ról
        extraversion_optimal = 5 - abs(scores['extraversion'] - 3.5)
        extraversion_impact = extraversion_optimal * 15
        
        # Openness wspiera adaptację i learning
        openness_impact = scores['openness'] * 15
        
        # Moderate agreeableness (za wysokie może być problematyczne w leadership)
        agreeableness_optimal = 5 - abs(scores['agreeableness'] - 3.5)
        agreeableness_impact = agreeableness_optimal * 10
        
        total_score = (conscientiousness_impact + stability_impact + 
                      extraversion_impact + openness_impact + agreeableness_impact)
        
        return min(total_score, 100)
    
    def _assess_motivation_sustainability(self, motivation_profile: Dict) -> float:
        """Ocena trwałości motywacji"""
        
        sustainability_analysis = motivation_profile.get('sustainability_analysis', {})
        
        if sustainability_analysis:
            sustainability_score = sustainability_analysis.get('overall_sustainability', 0.5) * 100
            return min(sustainability_score, 100)
        
        # Fallback assessment
        top_motivators = motivation_profile.get('top_motivators', [])
        if not top_motivators:
            return 60
        
        # Intrinsic motivators bardziej sustainable
        intrinsic_count = sum(1 for m in top_motivators 
                             if m.get('name') in ['autonomy', 'mastery', 'purpose'])
        
        sustainability_score = 40 + (intrinsic_count * 20)  # Base 40 + 20 per intrinsic motivator
        return min(sustainability_score, 100)
    
    def _assess_cognitive_effectiveness(self, cognitive_profile: Dict) -> float:
        """Ocena efektywności kognitywnej"""
        
        efficiency_data = cognitive_profile.get('cognitive_efficiency_score', {})
        
        if efficiency_data and 'score' in efficiency_data:
            return min(efficiency_data['score'] * 10, 100)  # Convert to percentage
        
        # Fallback assessment
        cognitive_analysis = cognitive_profile.get('cognitive_strengths_analysis', {})
        average_level = cognitive_analysis.get('average_level', 5.0)
        
        return min(average_level * 20, 100)  # Convert to percentage
    
    def _assess_adaptability_factor(self, personality_profile: Dict) -> float:
        """Ocena zdolności adaptacyjnych"""
        
        # Extract relevant traits
        openness = 3.0
        emotional_stability = 3.0
        
        if 'openness' in personality_profile and isinstance(personality_profile['openness'], dict):
            openness = personality_profile['openness'].get('score', 3.0)
        
        if 'emotional_stability' in personality_profile and isinstance(personality_profile['emotional_stability'], dict):
            emotional_stability = personality_profile['emotional_stability'].get('score', 3.0)
        
        # Openness crucial dla adaptacji
        openness_contribution = openness * 40
        
        # Emotional stability pomaga w coping ze zmianą
        stability_contribution = emotional_stability * 35
        
        # Base adaptability score
        base_adaptability = 25
        
        total_adaptability = openness_contribution + stability_contribution + base_adaptability
        
        return min(total_adaptability, 100)
    
    def _assess_execution_capability(self, personality_profile: Dict) -> float:
        """Ocena zdolności wykonawczych"""
        
        # Extract conscientiousness i emotional stability
        conscientiousness = 3.0
        emotional_stability = 3.0
        
        if 'conscientiousness' in personality_profile and isinstance(personality_profile['conscientiousness'], dict):
            conscientiousness = personality_profile['conscientiousness'].get('score', 3.0)
        
        if 'emotional_stability' in personality_profile and isinstance(personality_profile['emotional_stability'], dict):
            emotional_stability = personality_profile['emotional_stability'].get('score', 3.0)
        
        # Conscientiousness primary driver of execution
        conscientiousness_impact = conscientiousness * 50
        
        # Emotional stability supports consistent performance
        stability_impact = emotional_stability * 30
        
        # Base execution capability
        base_execution = 20
        
        total_execution = conscientiousness_impact + stability_impact + base_execution
        
        return min(total_execution, 100)
    
    def _identify_success_drivers(self, success_factors: Dict[str, float]) -> List[str]:
        """Identyfikacja kluczowych drivers sukcesu"""
        
        drivers = []
        
        for factor, score in success_factors.items():
            if score >= 75:
                factor_descriptions = {
                    'personality_optimization': 'Exceptional personality fit dla professional success',
                    'motivation_sustainability': 'Strong, sustainable motivation drivers',
                    'cognitive_effectiveness': 'High cognitive capabilities i effectiveness',
                    'adaptability_quotient': 'Outstanding adaptability i change management',
                    'execution_reliability': 'Exceptional execution i delivery capabilities'
                }
                drivers.append(factor_descriptions.get(factor, f'Strong {factor}'))
        
        if not drivers:
            drivers.append('Balanced foundation across multiple success factors')
        
        return drivers
    
    def _identify_improvement_areas(self, success_factors: Dict[str, float]) -> List[str]:
        """Identyfikacja obszarów do poprawy"""
        
        improvement_areas = []
        
        for factor, score in success_factors.items():
            if score < 60:
                factor_improvements = {
                    'personality_optimization': 'Focus na developing self-awareness i leveraging personality strengths',
                    'motivation_sustainability': 'Strengthen intrinsic motivation i find deeper meaning w work',
                    'cognitive_effectiveness': 'Enhance cognitive skills through targeted learning i practice',
                    'adaptability_quotient': 'Build change management skills i comfort z uncertainty',
                    'execution_reliability': 'Improve planning, organization, i follow-through capabilities'
                }
                improvement_areas.append(factor_improvements.get(factor, f'Develop {factor}'))
        
        return improvement_areas
    
    def _recommend_success_accelerators(self, success_factors: Dict[str, float]) -> List[str]:
        """Rekomendacje akceleratorów sukcesu"""
        
        accelerators = []
        
        # Find lowest scoring factor dla targeted improvement
        lowest_factor = min(success_factors.keys(), key=lambda k: success_factors[k])
        
        factor_accelerators = {
            'personality_optimization': [
                'Executive coaching dla personality-career alignment',
                'Strengths-based role design i job crafting',
                'Personality assessment feedback i development planning'
            ],
            'motivation_sustainability': [
                'Values clarification workshop',
                'Purpose-driven career planning',
                'Regular motivation i engagement assessment'
            ],
            'cognitive_effectiveness': [
                'Cognitive skills training programs',
                'Executive education w strategic thinking',
                'Mentoring relationships dla cognitive development'
            ],
            'adaptability_quotient': [
                'Change management certification',
                'Exposure do diverse projects i challenges',
                'Resilience training i stress management'
            ],
            'execution_reliability': [
                'Project management certification',
                'Productivity i organization systems',
                'Accountability partnerships i coaching'
            ]
        }
        
        accelerators.extend(factor_accelerators.get(lowest_factor, [
            'General professional development',
            'Skills assessment i targeted improvement',
            'Career coaching i mentoring'
        ]))
        
        # Universal accelerators
        accelerators.extend([
            'Build strong professional network w target industry',
            'Establish regular learning i development routine',
            'Create personal brand i thought leadership presence'
        ])
        
        return accelerators[:5]  # Return top 5 recommendations
    
    def _generate_actionable_recommendations(self, recommended_paths: List[Dict],
                                           skill_development_plan: Dict) -> List[Dict[str, str]]:
        """Generowanie wykonalnych rekomendacji"""
        
        recommendations = []
        
        # Career direction recommendation
        if recommended_paths:
            top_path = recommended_paths[0]
            recommendations.append({
                'category': 'Career Focus',
                'action': f"Target career progression towards {top_path['title']}",
                'rationale': f"Strongest match ({top_path['match_score']}%) z excellent growth potential",
                'timeline': top_path.get('time_to_transition', '12-18 miesięcy'),
                'priority': 'Wysoki'
            })
        
        # Skill development recommendations
        prioritized_skills = skill_development_plan.get('prioritized_skills', [])
        for i, skill in enumerate(prioritized_skills[:3]):
            priority_levels = ['Wysoki', 'Średni', 'Średni']
            recommendations.append({
                'category': 'Skill Development',
                'action': f"Develop {skill['skill']} capabilities",
                'rationale': f"Critical dla {len([p for p in recommended_paths if skill['skill'] in p.get('key_skills', [])])} top career paths",
                'timeline': skill.get('time_to_proficiency', '3-6 miesięcy'),
                'priority': priority_levels[i]
            })
        
        # Quick wins
        quick_wins = skill_development_plan.get('quick_wins', [])
        if quick_wins:
            recommendations.append({
                'category': 'Quick Wins',
                'action': quick_wins[0],
                'rationale': 'High impact opportunity z relatively low effort required',
                'timeline': '30-60 dni',
                'priority': 'Wysoki'
            })
        
        # Network building
        recommendations.append({
            'category': 'Professional Network',
            'action': 'Establish mentoring relationships w target industry',
            'rationale': 'Professional guidance significantly accelerates career progression',
            'timeline': '60-90 dni',
            'priority': 'Wysoki'
        })
        
        # Market positioning
        if recommended_paths:
            industry = recommended_paths[0].get('industry', 'your target industry')
            recommendations.append({
                'category': 'Market Positioning',
                'action': f'Build thought leadership presence w {industry}',
                'rationale': 'Industry visibility opens doors do better opportunities',
                'timeline': '6-12 miesięcy',
                'priority': 'Średni'
            })
        
        # Risk management
        recommendations.append({
            'category': 'Risk Management',
            'action': 'Diversify skill portfolio i build backup career options',
            'rationale': 'Career resilience protects against market volatility',
            'timeline': 'Ongoing',
            'priority': 'Średni'
        })
        
        return recommendations    def _estimate_transition_time(self, career_title: str, user_data: Dict) -> str:
        """Oszacowanie czasu przejścia do nowej kariery"""
        current_position = user_data.get('position', '').lower()
        experience = user_data.get('experience', '0-1 lat')
        
        # Base transition times w miesiącach
        base_times = {
            'Product Manager': 12,
            'Strategy Consultant': 9,
            'Data Scientist': 15,
            'UX Designer': 10,
            'Innovation Director': 18,
            'Operations Manager': 6,
            'Sales Director': 8,
            'Research Scientist': 24
        }
        
        base_time = base_times.get(career_title, 12)
        
        # Adjustments based na doświadczeniu
        exp_multipliers = {
            '0-1 lat': 1.3,
            '2-3 lata': 1.1,
            '4-6 lat': 1.0,
            '7-10 lat': 0.9,
            'Powyżej 10 lat': 0.8
        }
        
        multiplier = exp_multipliers.get(experience, 1.0)
        
        # Adjustment based na podobieństwie current role
        if any(keyword in current_position for keyword in ['manager', 'lead', 'director']):
            multiplier *= 0.8  # Leadership experience helps
        
        if any(keyword in current_position for keyword in ['analyst', 'consultant', 'specialist']):
            multiplier *= 0.9  # Analytical experience helps
        
        adjusted_time = int(base_time * multiplier)
        
        if adjusted_time <= 6:
            return '3-6 miesięcy'
        elif adjusted_time <= 12:
            return '6-12 miesięcy'
        elif adjusted_time <= 18:
            return '12-18 miesięcy'
        else:
            return '18-24 miesiące'
    
    def _analyze_work_environments(self, personality_profile: Dict, 
                                 motivation_profile: Dict) -> Dict[str, Any]:
        """Analiza optymalnych środowisk pracy"""
        
        # Extract Big Five scores
        big_five_scores = {}
        for trait in ['extraversion', 'agreeableness', 'conscientiousness', 'emotional_stability', 'openness']:
            if trait in personality_profile and isinstance(personality_profile[trait], dict):
                big_five_scores[trait] = personality_profile[trait].get('score', 3.0)
            else:
                big_five_scores[trait] = 3.0
        
        # Extract top motivators
        top_motivators = motivation_profile.get('top_motivators', [])
        motivator_names = [m.get('name', '') for m in top_motivators]
        
        environment_analysis = {
            'company_size': self._recommend_company_size(big_five_scores, motivator_names),
            'culture_type': self._recommend_culture_type(big_five_scores, motivator_names),
            'work_structure': self._recommend_work_structure(big_five_scores, motivator_names),
            'team_dynamics': self._recommend_team_dynamics(big_five_scores),
            'leadership_style': self._recommend_leadership_style(motivator_names),
            'physical_environment': self._recommend_physical_environment(big_five_scores),
            'work_life_balance': self._assess_work_life_preferences(big_five_scores, motivator_names)
        }
        
        return environment_analysis
    
    def _recommend_company_size(self, big_five_scores: Dict[str, float], motivators: List[str]) -> Dict[str, str]:
        """Rekomendacja rozmiaru firmy"""
        extraversion = big_five_scores.get('extraversion', 3)
        openness = big_five_scores.get('openness', 3)
        autonomy_motivated = 'autonomy' in motivators
        
        if extraversion >= 4.0 and openness >= 3.5 and not autonomy_motivated:
            return {
                'recommendation': 'Duże korporacje (1000+ pracowników)',
                'reasoning': 'Twoja wysoka ekstrawersja i otwartość będą docenione w dużych, dynamicznych organizacjach z wieloma możliwościami networkingu'
            }
        elif autonomy_motivated and openness >= 3.5:
            return {
                'recommendation': 'Startupy i scale-upy (10-200 pracowników)',
                'reasoning': 'Potrzeba autonomii i otwartość na innowacje idealnie pasują do elastycznego środowiska startupów'
            }
        elif big_five_scores.get('conscientiousness', 3) >= 4.0:
            return {
                'recommendation': 'Średnie firmy (200-1000 pracowników)',
                'reasoning': 'Twoja sumienność pozwoli Ci prosperować w organizacjach z ustalonymi procesami, ale wciąż oferującymi możliwości wpływu'
            }
        else:
            return {
                'recommendation': 'Małe do średnie firmy (50-500 pracowników)',
                'reasoning': 'Balans między strukturą a elastycznością, możliwość budowania bliskich relacji zawodowych'
            }
    
    def _recommend_culture_type(self, big_five_scores: Dict[str, float], motivators: List[str]) -> Dict[str, str]:
        """Rekomendacja typu kultury organizacyjnej"""
        
        if 'purpose' in motivators:
            return {
                'recommendation': 'Mission-driven culture',
                'reasoning': 'Twoja orientacja na cel wymaga organizacji z jasną misją społeczną lub środowiskową'
            }
        elif 'mastery' in motivators and big_five_scores.get('openness', 3) >= 3.5:
            return {
                'recommendation': 'Innovation-first culture',
                'reasoning': 'Fokus na rozwój i otwartość na nowe doświadczenia pasują do kultury ciągłych innowacji'
            }
        elif 'achievement' in motivators and big_five_scores.get('conscientiousness', 3) >= 3.5:
            return {
                'recommendation': 'Performance-driven culture',
                'reasoning': 'Orientacja na osiągnięcia i wysoka sumienność idealnie pasują do kultury meritokratycznej'
            }
        elif big_five_scores.get('agreeableness', 3) >= 4.0:
            return {
                'recommendation': 'Collaborative, people-first culture',
                'reasoning': 'Twoja naturalną skłonność do współpracy będzie doceniona w kulturze stawiającej ludzi na pierwszym miejscu'
            }
        else:
            return {
                'recommendation': 'Balanced, professional culture',
                'reasoning': 'Kultura łącząca profesjonalizm z możliwością rozwoju osobistego'
            }
    
    def _recommend_work_structure(self, big_five_scores: Dict[str, float], motivators: List[str]) -> Dict[str, str]:
        """Rekomendacja struktury pracy"""
        conscientiousness = big_five_scores.get('conscientiousness', 3)
        autonomy_motivated = 'autonomy' in motivators
        extraversion = big_five_scores.get('extraversion', 3)
        
        if autonomy_motivated and conscientiousness >= 3.5:
            return {
                'recommendation': 'Wysoka autonomia z flexible working arrangements',
                'reasoning': 'Twoja potrzeba autonomii i sumienność pozwalają na efektywną samodzielną pracę'
            }
        elif extraversion >= 4.0:
            return {
                'recommendation': 'Hybrid model z dużą ilością zespołowej współpracy',
                'reasoning': 'Twoja ekstrawersja wymaga regularnych interakcji, ale z możliwością focused work'
            }
        elif conscientiousness >= 4.0:
            return {
                'recommendation': 'Strukturalna praca z jasnymi procesami i deadlines',
                'reasoning': 'Twoja sumienność prosperuje w środowisku z clear expectations i organized workflows'
            }
        else:
            return {
                'recommendation': 'Flexible structure z możliwością dostosowania do preferencji',
                'reasoning': 'Zbalansowane podejście pozwala na optymalizację based on task requirements'
            }
    
    def _recommend_team_dynamics(self, big_five_scores: Dict[str, float]) -> Dict[str, str]:
        """Rekomendacja dynamiki zespołowej"""
        agreeableness = big_five_scores.get('agreeableness', 3)
        extraversion = big_five_scores.get('extraversion', 3)
        emotional_stability = big_five_scores.get('emotional_stability', 3)
        
        if agreeableness >= 4.0 and extraversion >= 3.5:
            return {
                'recommendation': 'Highly collaborative teams z consensus-building approach',
                'reasoning': 'Twoja ugodowość i ekstrawersja idealnie pasują do team environments opartych na współpracy'
            }
        elif emotional_stability >= 4.0 and extraversion >= 3.5:
            return {
                'recommendation': 'High-performance teams z ambitious goals',
                'reasoning': 'Twoja stabilność emocjonalna i społeczność pozwalają na thriving w competitive team environments'
            }
        elif agreeableness <= 3.0 and big_five_scores.get('conscientiousness', 3) >= 3.5:
            return {
                'recommendation': 'Task-focused teams z clear roles i responsibilities',
                'reasoning': 'Preferujesz teams gdzie każdy ma defined role i focus jest na execution'
            }
        else:
            return {
                'recommendation': 'Balanced teams z mix of collaboration i independent work',
                'reasoning': 'Versatile team environment pozwala na leveraging różnych working styles'
            }
    
    def _recommend_leadership_style(self, motivators: List[str]) -> Dict[str, str]:
        """Rekomendacja stylu przywództwa przełożonych"""
        
        if 'autonomy' in motivators:
            return {
                'recommendation': 'Delegating leadership style',
                'reasoning': 'Potrzebujesz leaders którzy dają freedom to execute while providing support when needed'
            }
        elif 'mastery' in motivators:
            return {
                'recommendation': 'Coaching leadership style',
                'reasoning': 'Leaders who focus on development i skill building będą best support your growth orientation'
            }
        elif 'achievement' in motivators:
            return {
                'recommendation': 'Transformational leadership style',
                'reasoning': 'Inspirational leaders who set high standards i provide recognition będą motivate your performance'
            }
        elif 'affiliation' in motivators:
            return {
                'recommendation': 'Servant leadership style',
                'reasoning': 'Leaders who prioritize team welfare i relationship building będą create optimal environment'
            }
        else:
            return {
                'recommendation': 'Adaptive leadership style',
                'reasoning': 'Leaders who can adjust their approach based on situation i individual needs'
            }
    
    def _recommend_physical_environment(self, big_five_scores: Dict[str, float]) -> Dict[str, str]:
        """Rekomendacja środowiska fizycznego"""
        extraversion = big_five_scores.get('extraversion', 3)
        openness = big_five_scores.get('openness', 3)
        conscientiousness = big_five_scores.get('conscientiousness', 3)
        
        if extraversion >= 4.0 and openness >= 3.5:
            return {
                'recommendation': 'Open, collaborative spaces z variety of work areas',
                'reasoning': 'Twoja ekstrawersja i otwartość thrive w dynamic environments z możliwością interaction'
            }
        elif conscientiousness >= 4.0 and extraversion <= 3.0:
            return {
                'recommendation': 'Quiet, organized workspace z minimal distractions',
                'reasoning': 'Potrzebujesz focused environment gdzie możesz concentrate i maintain high standards'
            }
        elif openness >= 4.0:
            return {
                'recommendation': 'Creative, inspiring spaces z artistic elements',
                'reasoning': 'Twoja otwartość na doświadczenia będzie stimulated przez visually interesting environment'
            }
        else:
            return {
                'recommendation': 'Comfortable, professional environment z flexible seating options',
                'reasoning': 'Balanced workspace który supports różne working styles i preferences'
            }
    
    def _assess_work_life_preferences(self, big_five_scores: Dict[str, float], motivators: List[str]) -> Dict[str, str]:
        """Ocena preferencji work-life balance"""
        conscientiousness = big_five_scores.get('conscientiousness', 3)
        emotional_stability = big_five_scores.get('emotional_stability', 3)
        
        if 'autonomy' in motivators and emotional_stability >= 3.5:
            return {
                'recommendation': 'Flexible work-life integration',
                'reasoning': 'Twoja potrzeba autonomii i stabilność emocjonalna pozwalają na effective self-management of boundaries'
            }
        elif conscientiousness >= 4.0 and 'achievement' in motivators:
            return {
                'recommendation': 'Structured work-life separation',
                'reasoning': 'Twoja sumienność i focus na achievement benefit from clear boundaries between work i personal time'
            }
        elif emotional_stability <= 3.0:
            return {
                'recommendation': 'Strong work-life boundaries z emphasis on recovery time',
                'reasoning': 'Important to maintain clear separation to prevent burnout i maintain emotional wellbeing'
            }
        else:
            return {
                'recommendation': 'Adaptive work-life balance based on project demands',
                'reasoning': 'Flexibility to adjust balance based on current priorities while maintaining overall wellbeing'
            }
    
    def _create_skill_development_plan(self, cognitive_profile: Dict, 
                                     recommended_paths: List[Dict], user_data: Dict) -> Dict[str, Any]:
        """Tworzenie planu rozwoju umiejętności"""
        
        # Identyfikacja gap-ów umiejętności
        skill_gaps = self._identify_skill_gaps(recommended_paths)
        
        # Priorityzacja umiejętności
        prioritized_skills = self._prioritize_skills(skill_gaps, recommended_paths)
        
        # Plan rozwoju na różnych horyzontach czasowych
        development_timeline = {
            'immediate_actions': self._create_immediate_actions(prioritized_skills),
            'short_term_plan': self._create_short_term_plan(prioritized_skills[:3]),
            'medium_term_plan': self._create_medium_term_plan(prioritized_skills[3:6]),
            'long_term_plan': self._create_long_term_plan(prioritized_skills[6:])
        }
        
        # Learning resources
        learning_resources = self._recommend_learning_resources(prioritized_skills)
        
        # Success metrics
        success_metrics = self._define_success_metrics(prioritized_skills)
        
        return {
            'skill_gaps': skill_gaps,
            'prioritized_skills': prioritized_skills,
            'development_timeline': development_timeline,
            'learning_resources': learning_resources,
            'success_metrics': success_metrics,
            'total_estimated_time': self._estimate_total_development_time(prioritized_skills),
            'quick_wins': self._identify_quick_wins(prioritized_skills)
        }
    
    def _identify_skill_gaps(self, recommended_paths: List[Dict]) -> List[Dict[str, Any]]:
        """Identyfikacja luk w umiejętnościach"""
        
        # Zbierz wszystkie wymagane umiejętności z top 3 rekomendacji
        required_skills = {}
        for i, path in enumerate(recommended_paths[:3]):
            weight = 1.0 - (i * 0.2)  # Większa waga dla lepiej dopasowanych ścieżek
            for skill in path['key_skills']:
                if skill not in required_skills:
                    required_skills[skill] = 0
                required_skills[skill] += weight
        
        skill_gaps = []
        for skill, importance in required_skills.items():
            # Mock current levels - w rzeczywistej aplikacji byłyby z user input
            current_level = np.random.randint(4, 8)  # Random dla demo
            target_level = 8
            
            if current_level < target_level:
                skill_gaps.append({
                    'skill': skill,
                    'current_level': current_level,
                    'target_level': target_level,
                    'gap_size': target_level - current_level,
                    'importance': round(importance, 2),
                    'priority_score': importance * (target_level - current_level)
                })
        
        return sorted(skill_gaps, key=lambda x: x['priority_score'], reverse=True)
    
    def _prioritize_skills(self, skill_gaps: List[Dict], recommended_paths: List[Dict]) -> List[Dict[str, Any]]:
        """Priorytetyzacja umiejętności do rozwoju"""
        
        # Skills już posortowane według priority score
        for skill in skill_gaps:
            # Dodaj learning difficulty
            skill['learning_difficulty'] = self._assess_learning_difficulty(skill['skill'])
            
            # Dodaj impact potential
            skill['impact_potential'] = self._assess_impact_potential(skill['skill'], recommended_paths)
            
            # Dodaj time to proficiency
            skill['time_to_proficiency'] = self._estimate_time_to_proficiency(
                skill['skill'], skill['gap_size'], skill['learning_difficulty']
            )
        
        return skill_gaps
    
    def _assess_learning_difficulty(self, skill: str) -> str:
        """Ocena trudności nauki umiejętności"""
        technical_skills = ['Programming', 'Data analysis', 'Machine learning', 'Statistics']
        leadership_skills = ['Leadership', 'Strategic thinking', 'Change management']
        communication_skills = ['Communication', 'Presentation', 'Negotiation']
        
        if any(tech in skill for tech in technical_skills):
            return 'High'
        elif any(lead in skill for lead in leadership_skills):
            return 'Medium-High'
        elif any(comm in skill for comm in communication_skills):
            return 'Medium'
        else:
            return 'Medium-Low'
    
    def _assess_impact_potential(self, skill: str, recommended_paths: List[Dict]) -> str:
        """Ocena potencjału wpływu umiejętności"""
        
        # Count how many top paths require this skill
        paths_requiring_skill = sum(1 for path in recommended_paths[:3] if skill in path['key_skills'])
        
        high_impact_skills = ['Strategic thinking', 'Leadership', 'Data analysis']
        
        if paths_requiring_skill >= 2 or any(high_skill in skill for high_skill in high_impact_skills):
            return 'Very High'
        elif paths_requiring_skill == 1:
            return 'High'
        else:
            return 'Medium'
    
    def _estimate_time_to_proficiency(self, skill: str, gap_size: int, difficulty: str) -> str:
        """Oszacowanie czasu do biegłości"""
        
        base_times = {
            'High': 6,
            'Medium-High': 4,
            'Medium': 3,
            'Medium-Low': 2
        }
        
        base_months = base_times.get(difficulty, 3)
        total_months = base_months * gap_size
        
        if total_months <= 2:
            return '1-2 miesiące'
        elif total_months <= 4:
            return '2-4 miesiące'
        elif total_months <= 8:
            return '4-8 miesięcy'
        else:
            return '8+ miesięcy'
    
    def _create_immediate_actions(self, prioritized_skills: List[Dict]) -> List[str]:
        """Natychmiastowe działania (następne 7 dni)"""
        top_skill = prioritized_skills[0] if prioritized_skills else None
        
        if not top_skill:
            return ['Przeprowadź detailed skills assessment']
        
        return [
            f"Zapisz się na online course: {top_skill['skill']}",
            f"Znajdź 3 articles/blogs o {top_skill['skill']}",
            "Zidentyfikuj potential mentor w wybranej dziedzinie",
            "Ustaw learning schedule (min. 5h tygodniowo)",
            "Join relevant professional groups na LinkedIn"
        ]
    
    def _create_short_term_plan(self, skills: List[Dict]) -> List[Dict[str, str]]:
        """Plan krótkoterminowy (1-3 miesiące)"""
        plan = []
        for skill in skills:
            plan.append({
                'skill': skill['skill'],
                'goal': f"Podnieś poziom z {skill['current_level']} do {min(skill['current_level'] + 2, skill['target_level'])}",
                'action': f"Intensywny kurs online + praktyczne projekty",
                'time_commitment': '6-8 godzin tygodniowo',
                'milestone': f"Ukończ certification lub complete practical project",
                'resources': 'Online courses, tutorials, practice projects'
            })
        return plan
    
    def _create_medium_term_plan(self, skills: List[Dict]) -> List[Dict[str, str]]:
        """Plan średnioterminowy (3-8 miesięcy)"""
        plan = []
        for skill in skills:
            plan.append({
                'skill': skill['skill'],
                'goal': f"Osiągnij poziom {skill['target_level']}",
                'action': f"Advanced training + real-world application",
                'time_commitment': '4-6 godzin tygodniowo',
                'milestone': f"Apply skill w professional context",
                'resources': 'Advanced courses, mentoring, project work'
            })
        return plan
    
    def _create_long_term_plan(self, skills: List[Dict]) -> List[Dict[str, str]]:
        """Plan długoterminowy (6-12 miesięcy)"""
        plan = []
        for skill in skills:
            plan.append({
                'skill': skill['skill'],
                'goal': f"Become proficient (level {skill['target_level']}+)",
                'action': f"Mastery through teaching i leadership",
                'time_commitment': '2-4 godziny tygodniowo',
                'milestone': f"Lead projekt requiring this skill",
                'resources': 'Advanced certifications, thought leadership, mentoring others'
            })
        return plan
    
    def _recommend_learning_resources(self, skills: List[Dict]) -> Dict[str, List[str]]:
        """Rekomendacje zasobów do nauki"""
        resources = {}
        
        resource_mapping = {
            'Strategic thinking': [
                'Good Strategy Bad Strategy - Richard Rumelt',
                'Harvard Business School Strategy courses',
                'BCG Strategy Institute publications',
                'McKinsey Strategy & Corporate Finance articles'
            ],
            'Leadership': [
                'The Leadership Challenge - Kouzes & Posner',
                'Google Manager Training certificates',
                'Executive coaching program',
                'Harvard ManageMentor Leadership modules'
            ],
            'Data analysis': [
                'Python for Data Analysis - Wes McKinney',
                'Coursera Data Science Specialization',
                'Kaggle Learn micro-courses',
                'Tableau/Power BI certification programs'
            ],
            'Communication': [
                'Toastmasters International program',
                'HBR Guide to Better Business Writing',
                'Public speaking workshops',
                'Communication coaching'
            ],
            'Programming': [
                'Codecademy Pro subscription',
                'LeetCode for interview prep',
                'GitHub for portfolio building',
                'Stack Overflow for community learning'
            ]
        }
        
        for skill in skills[:5]:  # Top 5 skills
            skill_name = skill['skill']
            resources[skill_name] = resource_mapping.get(skill_name, [
                'Industry-specific online courses',
                'Professional certification programs',
                'Mentorship i coaching',
                'Hands-on project experience'
            ])
        
        return resources
    
    def _define_success_metrics(self, skills: List[Dict]) -> Dict[str, List[str]]:
        """Definicja metryk sukcesu"""
        metrics = {}
        
        for skill in skills[:5]:
            skill_name = skill['skill']
            metrics[skill_name] = [
                f"Self-assessment improvement: {skill['current_level']} → {skill['target_level']}",
                "Successful application w real project",
                "Positive feedback from peers/supervisor",
                "Professional certification obtained",
                "Measurable business impact achieved"
            ]
        
        return metrics
    
    def _estimate_total_development_time(self, skills: List[Dict]) -> str:
        """Oszacowanie całkowitego czasu rozwoju"""
        if not skills:
            return "No development needed"
        
        total_priority_score = sum(skill['priority_score'] for skill in skills[:5])
        
        if total_priority_score >= 15:
            return "12-18 miesięcy intensive development"
        elif total_priority_score >= 10:
            return "8-12 miesięcy focused development"
        elif total_priority_score >= 5:
            return "4-8 miesięcy targeted improvement"
        else:
            return "2-4 miesiące skill enhancement"
    
    def _identify_quick_wins(self, skills: List[Dict]) -> List[str]:
        """Identyfikacja quick wins"""
        quick_wins = []
        
        for skill in skills:
            if (skill['gap_size'] <= 2 and 
                skill['learning_difficulty'] in ['Medium', 'Medium-Low'] and
                skill['impact_potential'] in ['High', 'Very High']):
                quick_wins.append(f"{skill['skill']} - high impact, relatively easy to improve")
        
        if not quick_wins:
            quick_wins = [
                "Focus na communication skills - universal applicability",
                "Strengthen project management - immediate workplace value",
                "Improve networking - career-long benefits"
            ]
        
        return quick_wins[:3]
    
    def _analyze_risk_opportunities(self, personality_profile: Dict, user_data: Dict) -> Dict[str, Any]:
        """Analiza ryzyk i możliwości"""
        
        # Extract Big Five scores
        big_five_scores = {}
        for trait in ['extraversion', 'agreeableness', 'conscientiousness', 'emotional_stability', 'openness']:
            if trait in personality_profile and isinstance(personality_profile[trait], dict):
                big_five_scores[trait] = personality_profile[trait].get('score', 3.0)
            else:
                big_five_scores[trait] = 3.0
        
        # Risk tolerance assessment
        risk_tolerance = self._assess_risk_tolerance(big_five_scores, user_data)
        
        # Opportunities identification
        opportunities = self._identify_career_opportunities(big_five_scores, user_data)
        
        # Threats analysis
        threats = self._identify_career_threats(big_five_scores, user_data)
        
        # Risk management strategy
        risk_strategy = self._develop_risk_management_strategy(risk_tolerance, opportunities, threats)
        
        return {
            'risk_tolerance_assessment': risk_tolerance,
            'career_opportunities': opportunities,
            'potential_threats': threats,
            'risk_management_strategy': risk_strategy,
            'opportunity_action_plan': self._create_opportunity_action_plan(opportunities),
            'threat_mitigation_plan': self._create_threat_mitigation_plan(threats)
        }
    
    def _assess_risk_tolerance(self, big_five_scores: Dict[str, float], user_data: Dict) -> Dict[str, Any]:
        """Ocena tolerancji ryzyka"""
        
        # Oblicz risk score na podstawie Big Five
        openness_contribution = big_five_scores['openness'] * 25
        stability_contribution = big_five_scores['emotional_stability'] * 20
        conscientiousness_contribution = (5 - big_five_scores['conscientiousness']) * 15  # Inverted
        extraversion_contribution = big_five_scores['extraversion'] * 10
        
        risk_score = (openness_contribution + stability_contribution + 
                     conscientiousness_contribution + extraversion_contribution)
        
        # Experience factor
        experience = user_data.get('experience', '0-1 lat')
        exp_factors = {
            '0-1 lat': 0.8,
            '2-3 lata': 0.9,
            '4-6 lat': 1.0,
            '7-10 lat': 1.1,
            'Powyżej 10 lat': 1.2
        }
        
        adjusted_risk_score = risk_score * exp_factors.get(experience, 1.0)
        
        # Categorization
        if adjusted_risk_score >= 75:
            level = "Bardzo wysoka"
            description = "Jesteś gotowa na high-risk, high-reward opportunities"
            recommendations = ["Consider entrepreneurship", "Explore emerging industries", "Take on stretch assignments"]
        elif adjusted_risk_score >= 60:
            level = "Wysoka"
            description = "Comfortable z calculated risks dla growth opportunities"
            recommendations = ["Join fast-growing companies", "Take on leadership challenges", "Explore new markets"]
        elif adjusted_risk_score >= 45:
            level = "Średnia"
            description = "Preferujesz balanced approach do risk-taking"
            recommendations = ["Gradual career transitions", "Build safety nets", "Pilot new initiatives"]
        else:
            level = "Niska"
            description = "Preferujesz stability i predictable career paths"
            recommendations = ["Focus na established companies", "Incremental skill building", "Strong financial planning"]
        
        return {
            'level': level,
            'score': round(adjusted_risk_score, 1),
            'description': description,
            'recommendations': recommendations,
            'risk_capacity': self._assess_risk_capacity(user_data)
        }
    
    def _assess_risk_capacity(self, user_data: Dict) -> str:
        """Ocena capacity do podejmowania ryzyka"""
        experience = user_data.get('experience', '0-1 lat')
        
        if experience in ['7-10 lat', 'Powyżej 10 lat']:
            return "High - doświadczenie i established network zwiększają capacity"
        elif experience in ['4-6 lat']:
            return "Medium-High - solid foundation z room for calculated risks"
        elif experience in ['2-3 lata']:
            return "Medium - developing expertise allows for moderate risk-taking"
        else:
            return "Lower - focus na building foundation i skills first"
    
    def _identify_career_opportunities(self, big_five_scores: Dict[str,# analysis_engine.py - Silnik analizy kariery
import numpy as np
from typing import Dict, List, Any, Tuple
from datetime import datetime, timedelta

class CareerAnalysisEngine:
    """Główny silnik analizy kariery"""
    
    def __init__(self):
        self.career_database = self._initialize_career_database()
        self.matching_weights = {
            'personality_fit': 0.30,
            'motivation_alignment': 0.25,
            'cognitive_match': 0.25,
            'skills_compatibility': 0.20
        }
        self.industry_trends = self._load_industry_trends()
    
    def comprehensive_analysis(self, personality_profile: Dict, motivation_profile: Dict,
                             cognitive_profile: Dict, user_data: Dict) -> Dict[str, Any]:
        """Kompleksowa analiza kariery"""
        
        # Generowanie rekomendacji ścieżek kariery
        recommended_paths = self._generate_career_recommendations(
            personality_profile, motivation_profile, cognitive_profile, user_data
        )
        
        # Analiza dopasowania do różnych środowisk pracy
        work_environments = self._analyze_work_environments(
            personality_profile, motivation_profile
        )
        
        # Plan rozwoju umiejętności
        skill_development_plan = self._create_skill_development_plan(
            cognitive_profile, recommended_paths, user_data
        )
        
        # Analiza ryzyka i możliwości
        risk_opportunity_analysis = self._analyze_risk_opportunities(
            personality_profile, user_data
        )
        
        # Prognozy zawodowe
        career_projections = self._generate_career_projections(
            recommended_paths, user_data
        )
        
        # Success probability
        success_analysis = self._calculate_success_probability(
            personality_profile, motivation_profile, cognitive_profile
        )
        
        return {
            'recommended_paths': recommended_paths,
            'work_environments': work_environments,
            'skill_development_plan': skill_development_plan,
            'risk_opportunity_analysis': risk_opportunity_analysis,
            'career_projections': career_projections,
            'success_analysis': success_analysis,
            'recommendations': self._generate_actionable_recommendations(
                recommended_paths, skill_development_plan
            )
        }
    
    def _initialize_career_database(self) -> Dict[str, Dict[str, Any]]:
        """Inicjalizacja bazy danych karier"""
        return {
            'Product Manager': {
                'personality_requirements': {
                    'extraversion': (3.0, 5.0),
                    'conscientiousness': (3.5, 5.0),
                    'openness': (3.0, 5.0),
                    'emotional_stability': (3.0, 5.0)
                },
                'key_motivators': ['mastery', 'achievement', 'autonomy'],
                'cognitive_requirements': ['strategic', 'analytical', 'creative'],
                'skills': ['Strategic thinking', 'Leadership', 'Communication', 'Data analysis'],
                'growth_potential': 95,
                'risk_level': 'Medium',
                'salary_range': (120000, 200000),
                'industry': 'Technology',
                'future_outlook': 'Very Positive',
                'automation_risk': 'Low'
            },
            'Strategy Consultant': {
                'personality_requirements': {
                    'extraversion': (3.0, 5.0),
                    'conscientiousness': (4.0, 5.0),
                    'openness': (3.5, 5.0),
                    'emotional_stability': (3.5, 5.0)
                },
                'key_motivators': ['mastery', 'achievement', 'autonomy'],
                'cognitive_requirements': ['strategic', 'analytical'],
                'skills': ['Problem solving', 'Client management', 'Business analysis', 'Presentation'],
                'growth_potential': 92,
                'risk_level': 'Medium-High',
                'salary_range': (100000, 180000),
                'industry': 'Consulting',
                'future_outlook': 'Positive',
                'automation_risk': 'Low'
            },
            'Data Scientist': {
                'personality_requirements': {
                    'conscientiousness': (3.5, 5.0),
                    'openness': (3.5, 5.0),
                    'extraversion': (2.0, 4.0)
                },
                'key_motivators': ['mastery', 'autonomy'],
                'cognitive_requirements': ['analytical', 'systemic'],
                'skills': ['Programming', 'Statistics', 'Machine learning', 'Data visualization'],
                'growth_potential': 98,
                'risk_level': 'Low',
                'salary_range': (110000, 190000),
                'industry': 'Technology',
                'future_outlook': 'Very Positive',
                'automation_risk': 'Very Low'
            },
            'UX Designer': {
                'personality_requirements': {
                    'openness': (4.0, 5.0),
                    'agreeableness': (3.0, 5.0),
                    'extraversion': (2.5, 4.5)
                },
                'key_motivators': ['mastery', 'purpose', 'autonomy'],
                'cognitive_requirements': ['creative', 'analytical'],
                'skills': ['Design thinking', 'User research', 'Prototyping', 'Communication'],
                'growth_potential': 88,
                'risk_level': 'Medium',
                'salary_range': (90000, 150000),
                'industry': 'Technology',
                'future_outlook': 'Positive',
                'automation_risk': 'Low'
            },
            'Innovation Director': {
                'personality_requirements': {
                    'extraversion': (3.5, 5.0),
                    'openness': (4.0, 5.0),
                    'conscientiousness': (3.0, 4.5),
                    'emotional_stability': (3.5, 5.0)
                },
                'key_motivators': ['mastery', 'purpose', 'autonomy'],
                'cognitive_requirements': ['creative', 'strategic'],
                'skills': ['Innovation management', 'Leadership', 'Change management', 'Strategic planning'],
                'growth_potential': 90,
                'risk_level': 'High',
                'salary_range': (140000, 220000),
                'industry': 'Technology',
                'future_outlook': 'Very Positive',
                'automation_risk': 'Very Low'
            },
            'Operations Manager': {
                'personality_requirements': {
                    'conscientiousness': (4.0, 5.0),
                    'emotional_stability': (3.5, 5.0),
                    'extraversion': (3.0, 5.0)
                },
                'key_motivators': ['achievement', 'security', 'mastery'],
                'cognitive_requirements': ['operational', 'analytical'],
                'skills': ['Process optimization', 'Team management', 'Project management', 'Problem solving'],
                'growth_potential': 85,
                'risk_level': 'Low',
                'salary_range': (95000, 160000),
                'industry': 'Operations',
                'future_outlook': 'Stable',
                'automation_risk': 'Medium'
            },
            'Sales Director': {
                'personality_requirements': {
                    'extraversion': (4.0, 5.0),
                    'emotional_stability': (3.5, 5.0),
                    'conscientiousness': (3.0, 5.0)
                },
                'key_motivators': ['achievement', 'autonomy', 'affiliation'],
                'cognitive_requirements': ['strategic', 'analytical'],
                'skills': ['Relationship building', 'Negotiation', 'Strategic selling', 'Leadership'],
                'growth_potential': 87,
                'risk_level': 'Medium-High',
                'salary_range': (120000, 250000),
                'industry': 'Sales',
                'future_outlook': 'Positive',
                'automation_risk': 'Low'
            },
            'Research Scientist': {
                'personality_requirements': {
                    'openness': (4.0, 5.0),
                    'conscientiousness': (3.5, 5.0),
                    'extraversion': (1.5, 3.5)
                },
                'key_motivators': ['mastery', 'purpose', 'autonomy'],
                'cognitive_requirements': ['analytical', 'creative', 'systemic'],
                'skills': ['Research methodology', 'Data analysis', 'Scientific writing', 'Critical thinking'],
                'growth_potential': 83,
                'risk_level': 'Low',
                'salary_range': (85000, 140000),
                'industry': 'Research',
                'future_outlook': 'Stable',
                'automation_risk': 'Low'
            }
        }
    
    def _load_industry_trends(self) -> Dict[str, Dict[str, Any]]:
        """Ładowanie trendów branżowych"""
        return {
            'Technology': {
                'growth_rate': 0.15,
                'hot_skills': ['AI/ML', 'Cloud computing', 'Cybersecurity', 'Data science'],
                'emerging_roles': ['AI Product Manager', 'MLOps Engineer', 'Prompt Engineer'],
                'outlook': 'Very Positive'
            },
            'Consulting': {
                'growth_rate': 0.08,
                'hot_skills': ['Digital transformation', 'Change management', 'Data analytics'],
                'emerging_roles': ['Digital Transformation Consultant', 'Sustainability Consultant'],
                'outlook': 'Positive'
            },
            'Healthcare': {
                'growth_rate': 0.12,
                'hot_skills': ['Digital health', 'Telemedicine', 'Health informatics'],
                'emerging_roles': ['Health Data Analyst', 'Digital Health Strategist'],
                'outlook': 'Very Positive'
            },
            'Finance': {
                'growth_rate': 0.06,
                'hot_skills': ['Fintech', 'Blockchain', 'Risk analytics', 'RegTech'],
                'emerging_roles': ['Fintech Product Manager', 'Crypto Analyst'],
                'outlook': 'Moderate'
            }
        }
    
    def _generate_career_recommendations(self, personality_profile: Dict, 
                                       motivation_profile: Dict, cognitive_profile: Dict,
                                       user_data: Dict) -> List[Dict[str, Any]]:
        """Generowanie rekomendacji ścieżek kariery"""
        recommendations = []
        
        for career_title, career_data in self.career_database.items():
            match_score = self._calculate_career_match_score(
                career_data, personality_profile, motivation_profile, cognitive_profile
            )
            
            if match_score >= 50:  # Threshold dla rekomendacji
                recommendations.append({
                    'title': career_title,
                    'match_score': round(match_score, 1),
                    'description': self._generate_career_description(career_title, career_data),
                    'reasoning': self._generate_match_reasoning(
                        career_data, personality_profile, motivation_profile, cognitive_profile
                    ),
                    'growth_potential': career_data['growth_potential'],
                    'risk_level': career_data['risk_level'],
                    'salary_range': career_data['salary_range'],
                    'key_skills': career_data['skills'],
                    'development_path': self._generate_development_path(career_title, user_data),
                    'industry': career_data['industry'],
                    'future_outlook': career_data['future_outlook'],
                    'automation_risk': career_data['automation_risk'],
                    'time_to_transition': self._estimate_transition_time(career_title, user_data)
                })
        
        # Sortuj według match score
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        return recommendations[:8]  # Top 8 rekomendacji
    
    def _calculate_career_match_score(self, career_data: Dict, personality_profile: Dict,
                                    motivation_profile: Dict, cognitive_profile: Dict) -> float:
        """Obliczanie score dopasowania do kariery"""
        
        # Dopasowanie osobowości
        personality_score = self._calculate_personality_fit(
            career_data['personality_requirements'], personality_profile
        )
        
        # Dopasowanie motywacji
        motivation_score = self._calculate_motivation_alignment(
            career_data['key_motivators'], motivation_profile
        )
        
        # Dopasowanie kognitywne
        cognitive_score = self._calculate_cognitive_match(
            career_data['cognitive_requirements'], cognitive_profile
        )
        
        # Dopasowanie umiejętności (bazowe)
        skills_score = 70  # Bazowy score, można rozwinąć
        
        # Weighted average
        total_score = (
            personality_score * self.matching_weights['personality_fit'] +
            motivation_score * self.matching_weights['motivation_alignment'] +
            cognitive_score * self.matching_weights['cognitive_match'] +
            skills_score * self.matching_weights['skills_compatibility']
        )
        
        return min(total_score, 100)
    
    def _calculate_personality_fit(self, requirements: Dict, personality_profile: Dict) -> float:
        """Obliczanie dopasowania osobowości"""
        fit_scores = []
        
        for trait, (min_req, max_req) in requirements.items():
            if trait in personality_profile and isinstance(personality_profile[trait], dict):
                trait_score = personality_profile[trait].get('score', 3.0)
                
                if min_req <= trait_score <= max_req:
                    fit_scores.append(100)
                else:
                    # Penalty za odchylenie od zakresu
                    if trait_score < min_req:
                        penalty = (min_req - trait_score) * 25
                    else:
                        penalty = (trait_score - max_req) * 25
                    fit_scores.append(max(0, 100 - penalty))
        
        return np.mean(fit_scores) if fit_scores else 60
    
    def _calculate_motivation_alignment(self, required_motivators: List[str], 
                                      motivation_profile: Dict) -> float:
        """Obliczanie zgodności motywacji"""
        top_motivators = motivation_profile.get('top_motivators', [])
        
        if not top_motivators:
            return 60  # Bazowy score
        
        alignment_scores = []
        motivator_names = [m.get('name', '') for m in top_motivators]
        
        for required_motivator in required_motivators:
            if required_motivator in motivator_names:
                # Znajdź score dla tego motywatora
                motivator_data = next(
                    (m for m in top_motivators if m.get('name') == required_motivator), 
                    None
                )
                if motivator_data:
                    score = motivator_data.get('score', 0.5) * 100
                    alignment_scores.append(score)
                else:
                    alignment_scores.append(50)
            else:
                alignment_scores.append(30)  # Penalty za missing motivator
        
        return np.mean(alignment_scores) if alignment_scores else 60
    
    def _calculate_cognitive_match(self, required_cognitive: List[str], 
                                 cognitive_profile: Dict) -> float:
        """Obliczanie dopasowania kognitywnego"""
        cognitive_analysis = cognitive_profile.get('cognitive_strengths_analysis', {})
        top_strengths = cognitive_analysis.get('top_strengths', [])
        
        if not top_strengths:
            return 60  # Bazowy score
        
        match_scores = []
        strength_names = [s.get('name', '').lower() for s in top_strengths]
        
        for requirement in required_cognitive:
            requirement_lower = requirement.lower()
            
            # Szukaj dopasowania w nazwach strengths
            match_found = False
            for strength_name in strength_names:
                if requirement_lower in strength_name or any(
                    keyword in strength_name for keyword in requirement_lower.split()
                ):
                    # Znajdź score dla tego strength
                    strength_data = next(
                        (s for s in top_strengths if requirement_lower in s.get('name', '').lower()),
                        None
                    )
                    if strength_data:
                        score = strength_data.get('score', 5) * 10  # Convert to percentage
                        match_scores.append(min(score, 100))
                        match_found = True
                        break
            
            if not match_found:
                match_scores.append(40)  # Penalty za missing cognitive requirement
        
        return np.mean(match_scores) if match_scores else 60
    
    def _generate_career_description(self, career_title: str, career_data: Dict) -> str:
        """Generowanie opisu kariery"""
        descriptions = {
            'Product Manager': 'Prowadzi strategię produktową, współpracuje z zespołami technicznymi i biznesowymi, analizuje potrzeby użytkowników i rynek.',
            'Strategy Consultant': 'Doradza firmom w zakresie strategii biznesowej, przeprowadza analizy rynkowe, opracowuje plany transformacji i wzrostu.',
            'Data Scientist': 'Analizuje duże zbiory danych, buduje modele predykcyjne i algorytmy ML, wspiera decyzje biznesowe insights.',
            'UX Designer': 'Projektuje doświadczenia użytkownika, przeprowadza badania UX, tworzy prototypy i testuje interfejsy.',
            'Innovation Director': 'Kieruje procesami innowacji w organizacji, rozwija nowe produkty i usługi, buduje kulturę innowacji.',
            'Operations Manager': 'Zarządza operacjami biznesowymi, optymalizuje procesy, kieruje zespołami operacyjnymi.',
            'Sales Director': 'Kieruje działaniami sprzedażowymi, buduje strategie sprzedaży, zarządza zespołami sales.',
            'Research Scientist': 'Prowadzi badania naukowe, publikuje wyniki, współpracuje z zespołami badawczymi.'
        }
        
        return descriptions.get(career_title, f'Specjalista w obszarze {career_title}')
    
    def _generate_match_reasoning(self, career_data: Dict, personality_profile: Dict,
                                motivation_profile: Dict, cognitive_profile: Dict) -> str:
        """Generowanie uzasadnienia dopasowania"""
        reasons = []
        
        # Analiza osobowości
        personality_reasons = []
        for trait, (min_req, max_req) in career_data['personality_requirements'].items():
            if trait in personality_profile and isinstance(personality_profile[trait], dict):
                trait_score = personality_profile[trait].get('score', 3.0)
                if min_req <= trait_score <= max_req:
                    trait_level = personality_profile[trait].get('level', 'medium')
                    personality_reasons.append(f"Twoja {trait} ({trait_level}) doskonale pasuje do wymagań roli")
        
        if personality_reasons:
            reasons.append(f"Profil osobowości: {'; '.join(personality_reasons[:2])}")
        
        # Analiza motywacji
        top_motivators = motivation_profile.get('top_motivators', [])
        matching_motivators = []
        for motivator_data in top_motivators[:3]:
            if motivator_data.get('name') in career_data['key_motivators']:
                matching_motivators.append(motivator_data['name'])
        
        if matching_motivators:
            reasons.append(f"Motywatory: {', '.join(matching_motivators)} są kluczowe w tej roli")
        
        # Analiza kognitywna
        cognitive_analysis = cognitive_profile.get('cognitive_strengths_analysis', {})
        top_strengths = cognitive_analysis.get('top_strengths', [])
        matching_cognitive = []
        
        for strength in top_strengths[:2]:
            strength_name = strength.get('name', '').lower()
            for req in career_data['cognitive_requirements']:
                if req.lower() in strength_name:
                    matching_cognitive.append(req)
                    break
        
        if matching_cognitive:
            reasons.append(f"Mocne strony kognitywne: {', '.join(matching_cognitive)} są fundamentalne")
        
        if not reasons:
            reasons.append("Solidne ogólne dopasowanie do wymagań i charakteru roli")
        
        return '. '.join(reasons)
    
    def _generate_development_path(self, career_title: str, user_data: Dict) -> str:
        """Generowanie ścieżki rozwoju"""
        experience = user_data.get('experience', '0-1 lat')
        
        development_paths = {
            'Product Manager': {
                '0-1 lat': 'Zdobądź podstawową wiedzę o product management, naucz się frameworków (Jobs-to-be-Done, OKRs), zbuduj portfolio case studies',
                '2-3 lata': 'Rozwijaj umiejętności user research i data analysis, weź udział w projektach produktowych, zdobądź certyfikat PM',
                '4-6 lat': 'Aplikuj na role Senior PM, rozwijaj strategic thinking, buduj network w branży tech, ucz się leadership',
                '7-10 lat': 'Przygotuj się do ról Principal/Director level, rozwijaj people management, strategię produktową na poziomie organizacji',
                'Powyżej 10 lat': 'Rozważ role VP Product lub CPO, fokus na organizational strategy i transformation'
            },
            'Strategy Consultant': {
                '0-1 lat': 'Zdobądź certyfikat consulting (np. od McKinsey), intensywnie ćwicz case studies, rozwijaj Excel/PowerPoint na advanced level',
                '2-3 lata': 'Aplikuj do top consulting firms, zbuduj portfolio business analysis, rozwijaj industry expertise',
                '4-6 lat': 'Awans do Senior Consultant, specjalizuj się w wybranej branży lub funkcji, rozwijaj client relationship skills',
                '7-10 lat': 'Manager/Principal level, prowadź duże projekty, rozwijaj business development, buduj thought leadership',
                'Powyżej 10 lat': 'Partner track lub założenie własnej firmy consultingowej, fokus na strategic advisory i industry expertise'
            },
            'Data Scientist': {
                '0-1 lat': 'Opanuj Python/R, SQL, podstawy ML, zbuduj portfolio projektów na GitHub, weź udział w Kaggle competitions',
                '2-3 lata': 'Rozwijaj domain expertise, naucz się advanced ML techniques, zdobądź doświadczenie w real-world projektach',
                '4-6 lat': 'Senior Data Scientist, rozwijaj MLOps skills, prowadź zespoły, fokus na business impact',
                '7-10 lat': 'Lead Data Scientist/ML Manager, strategy dla data science w organizacji, thought leadership',
                'Powyżej 10 lat': 'Chief Data Officer lub Head of AI, organizacyjna transformacja data-driven'
            }
        }
        
        career_paths = development_paths.get(career_title, {})
        path = career_paths.get(experience, 'Skonsultuj się z mentorem w branży dla spersonalizowanego planu rozwoju')
        
        return f"{path}. Timeline: 12-18 miesięcy preparation phase."
    
    def _estimate_transition_time(self, career_title: str, user_data:
