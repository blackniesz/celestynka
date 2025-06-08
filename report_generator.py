OGÓLNA TRWAŁOŚĆ: {sustainability.get('overall_sustainability', 0.7):.1f}/1.0

RATING: {sustainability.get('sustainability_rating', 'Wysoka stabilność motywacyjna')}

REKOMENDACJE DLA SUSTAINABILITY:
{chr(10).join([f'• {rec}' for rec in sustainability.get('recommendations', [])])}
        """
    
    def _format_work_environment_recommendations(self, motivation_profile: Dict) -> str:
        """Formatowanie rekomendacji środowiska pracy"""
        work_env = motivation_profile.get('ideal_work_environment', {})
        
        if not work_env:
            return "Rekomendacje środowiska pracy wymagają dalszej analizy."
        
        sections = []
        
        for category, recommendations in work_env.items():
            if recommendations:
                category_name = {
                    'culture_type': 'TYP KULTURY ORGANIZACYJNEJ',
                    'management_style': 'STYL ZARZĄDZANIA',
                    'work_structure': 'STRUKTURA PRACY',
                    'team_dynamics': 'DYNAMIKA ZESPOŁU',
                    'avoid': 'NALEŻY UNIKAĆ'
                }.get(category, category.upper())
                
                section = f"""
{category_name}:
{chr(10).join([f'• {rec}' for rec in recommendations])}
"""
                sections.append(section)
        
        return '\n'.join(sections)
    
    def _format_motivation_conflicts(self, motivation_profile: Dict) -> str:
        """Formatowanie konfliktów motywacyjnych"""
        conflicts = motivation_profile.get('potential_conflicts', [])
        
        if not conflicts:
            return "• Brak znaczących konfliktów motywacyjnych\n• Profil motywacyjny jest spójny i zbalansowany"
        
        conflict_sections = []
        for conflict in conflicts:
            conflict_section = f"""
⚠️ {conflict.get('type', 'Konflikt motywacyjny').upper()}
Opis: {conflict.get('description', '')}
Strategia zarządzania: {conflict.get('management_strategy', '')}
"""
            conflict_sections.append(conflict_section)
        
        return '\n'.join(conflict_sections)
    
    def _generate_cognitive_section(self, cognitive_profile: Dict) -> str:
        """Generowanie sekcji analizy kognitywnej"""
        
        return f"""
🧠 PROFIL KOGNITYWNY I STYLE MYŚLENIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analiza naturalnych wzorców przetwarzania informacji, podejmowania decyzji 
i rozwiązywania problemów.

{self._format_processing_style(cognitive_profile)}

{self._format_decision_style(cognitive_profile)}

{self._format_cognitive_strengths_analysis(cognitive_profile)}

{self._format_career_fit_analysis(cognitive_profile)}

{self._format_cognitive_development_recommendations(cognitive_profile)}
        """
    
    def _format_processing_style(self, cognitive_profile: Dict) -> str:
        """Formatowanie stylu przetwarzania"""
        processing = cognitive_profile.get('processing_style', {})
        
        if not processing:
            return "STYL PRZETWARZANIA: Wymagana dalsza analiza"
        
        return f"""
🔍 STYL PRZETWARZANIA INFORMACJI: {processing.get('type', '').upper()}

OPIS: {processing.get('description', '')}

NATURALNE MOCNE STRONY:
{chr(10).join([f'• {strength}' for strength in processing.get('strengths', [])])}

IDEALNE ZADANIA:
{chr(10).join([f'• {task}' for task in processing.get('ideal_tasks', [])])}
        """
    
    def _format_decision_style(self, cognitive_profile: Dict) -> str:
        """Formatowanie stylu decyzyjnego"""
        decision = cognitive_profile.get('decision_style', {})
        
        if not decision:
            return "STYL DECYZYJNY: Wymagana dalsza analiza"
        
        return f"""
⚖️ STYL PODEJMOWANIA DECYZJI: {decision.get('type', '').upper()}

OPIS: {decision.get('description', '')}
PODEJŚCIE: {decision.get('approach', '')}

NAJLEPSZE ZASTOSOWANIE:
{chr(10).join([f'• {application}' for application in decision.get('best_for', [])])}
        """
    
    def _format_cognitive_strengths_analysis(self, cognitive_profile: Dict) -> str:
        """Formatowanie analizy mocnych stron kognitywnych"""
        cog_analysis = cognitive_profile.get('cognitive_strengths_analysis', {})
        
        if not cog_analysis:
            return "ANALIZA MOCNYCH STRON: Wymagana dalsza analiza"
        
        top_strengths = cog_analysis.get('top_strengths', [])
        average_level = cog_analysis.get('average_level', 5.0)
        cognitive_balance = cog_analysis.get('cognitive_balance', {})
        
        strengths_text = ""
        for i, strength in enumerate(top_strengths, 1):
            strengths_text += f"""
{i}. {strength.get('name', '').upper()} - {strength.get('level', '')}
   Score: {strength.get('score', 5)}/10
   {strength.get('description', '')}
"""
        
        return f"""
🎯 ANALIZA MOCNYCH STRON KOGNITYWNYCH:

ŚREDNI POZIOM KOGNITYWNY: {average_level:.1f}/10

TOP MOCNE STRONY:
{strengths_text}

BALANS KOGNITYWNY:
Score: {cognitive_balance.get('balance_score', 5):.1f}/10
Ocena: {cognitive_balance.get('assessment', '')}
Rekomendacja: {cognitive_balance.get('recommendation', '')}
        """
    
    def _format_career_fit_analysis(self, cognitive_profile: Dict) -> str:
        """Formatowanie analizy dopasowania kariery"""
        career_fit = cognitive_profile.get('career_fit_analysis', {})
        
        if not career_fit:
            return "DOPASOWANIE KARIERY: Wymagana dalsza analiza"
        
        return f"""
🎯 DOPASOWANIE DO RÓL ZAWODOWYCH:

IDEALNE ROLE:
{chr(10).join([f'• {role}' for role in career_fit.get('ideal_roles', [])])}

DOBRE DOPASOWANIE:
{chr(10).join([f'• {role}' for role in career_fit.get('good_fit_roles', [])])}

WYZYWAJĄCE ROLE:
{chr(10).join([f'• {role}' for role in career_fit.get('challenging_roles', [])])}
        """
    
    def _format_cognitive_development_recommendations(self, cognitive_profile: Dict) -> str:
        """Formatowanie rekomendacji rozwoju kognitywnego"""
        dev_recs = cognitive_profile.get('development_recommendations', [])
        
        if not dev_recs:
            return "REKOMENDACJE ROZWOJU: Ogólny rozwój umiejętności kognitywnych"
        
        recommendations_text = ""
        for rec in dev_recs:
            recommendations_text += f"""
🎯 {rec.get('area', '').upper()}
Rekomendacja: {rec.get('recommendation', '')}
Metody: {', '.join(rec.get('methods', []))}
"""
        
        return f"""
💡 REKOMENDACJE ROZWOJU KOGNITYWNEGO:
{recommendations_text}
        """
    
    def _generate_career_recommendations_section(self, career_analysis: Dict) -> str:
        """Generowanie sekcji rekomendacji kariery"""
        
        recommended_paths = career_analysis.get('recommended_paths', [])
        
        if not recommended_paths:
            return "REKOMENDACJE KARIERY: Wymagana dalsza analiza profilu"
        
        paths_details = []
        for i, path in enumerate(recommended_paths[:5], 1):
            path_detail = f"""
{i}. {path.get('title', '').upper()}
   
   DOPASOWANIE: {path.get('match_score', 0):.1f}% | POTENCJAŁ WZROSTU: {path.get('growth_potential', 0)}%
   POZIOM RYZYKA: {path.get('risk_level', 'Medium')} | BRANŻA: {path.get('industry', 'General')}
   
   OPIS ROLI:
   {path.get('description', '')}
   
   DLACZEGO TO PASUJE:
   {path.get('reasoning', '')}
   
   KLUCZOWE UMIEJĘTNOŚCI:
   {', '.join(path.get('key_skills', []))}
   
   ŚCIEŻKA ROZWOJU:
   {path.get('development_path', '')}
   
   CZAS PRZEJŚCIA: {path.get('time_to_transition', 'N/A')}
   PRZYSZŁOŚĆ BRANŻY: {path.get('future_outlook', 'Stable')}
   RYZYKO AUTOMATYZACJI: {path.get('automation_risk', 'Medium')}
   
   PROJEKCJA ZAROBKÓW:
   ${path.get('salary_range', (0, 0))[0]:,} - ${path.get('salary_range', (0, 0))[1]:,}
"""
            paths_details.append(path_detail)
        
        return f"""
🎯 REKOMENDACJE ŚCIEŻEK KARIERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Następujące ścieżki kariery zostały zidentyfikowane jako najbardziej dopasowane 
do Twojego profilu psychologiczno-biznesowego:

{chr(10).join(paths_details)}

📊 ANALIZA PORÓWNAWCZA:

{self._generate_career_comparison_table(recommended_paths[:3])}
        """
    
    def _generate_career_comparison_table(self, top_paths: List[Dict]) -> str:
        """Generowanie tabeli porównawczej karier"""
        if not top_paths:
            return "Brak danych do porównania"
        
        table_header = "┌─────────────────────────┬─────────┬─────────┬──────────┬─────────────┐"
        table_separator = "├─────────────────────────┼─────────┼─────────┼──────────┼─────────────┤"
        table_footer = "└─────────────────────────┴─────────┴─────────┴──────────┴─────────────┘"
        
        header_row = "│ ŚCIEŻKA KARIERY         │ MATCH % │ GROWTH% │ RISK     │ TIMELINE    │"
        
        rows = [table_header, header_row, table_separator]
        
        for path in top_paths:
            title = path.get('title', '')[:23]  # Truncate długie nazwy
            match_score = path.get('match_score', 0)
            growth = path.get('growth_potential', 0)
            risk = path.get('risk_level', 'Medium')[:8]
            timeline = path.get('time_to_transition', 'N/A')[:11]
            
            row = f"│ {title:<23} │ {match_score:>5.0f}% │ {growth:>5.0f}% │ {risk:<8} │ {timeline:<11} │"
            rows.append(row)
        
        rows.append(table_footer)
        
        return '\n'.join(rows)
    
    def _generate_skill_development_section(self, skill_plan: Dict) -> str:
        """Generowanie sekcji planu rozwoju umiejętności"""
        
        return f"""
📈 PLAN ROZWOJU UMIEJĘTNOŚCI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{self._format_skill_gaps_analysis(skill_plan)}

{self._format_development_timeline(skill_plan)}

{self._format_learning_resources(skill_plan)}

{self._format_success_metrics(skill_plan)}

{self._format_quick_wins(skill_plan)}
        """
    
    def _format_skill_gaps_analysis(self, skill_plan: Dict) -> str:
        """Formatowanie analizy luk w umiejętnościach"""
        prioritized_skills = skill_plan.get('prioritized_skills', [])
        
        if not prioritized_skills:
            return "ANALIZA LUK: Wymagana ocena umiejętności"
        
        skills_analysis = "🎯 ANALIZA LUK W UMIEJĘTNOŚCIACH:\n\n"
        
        for i, skill in enumerate(prioritized_skills[:5], 1):
            skill_name = skill.get('skill', '')
            current_level = skill.get('current_level', 0)
            target_level = skill.get('target_level', 0)
            gap_size = skill.get('gap_size', 0)
            importance = skill.get('importance', 0)
            time_to_prof = skill.get('time_to_proficiency', 'N/A')
            
            progress_current = self._create_text_progress_bar(current_level, 10, 30)
            progress_target = self._create_text_progress_bar(target_level, 10, 30)
            
            skills_analysis += f"""
{i}. {skill_name.upper()}
   Obecny poziom: {current_level}/10  {progress_current}
   Poziom docelowy: {target_level}/10  {progress_target}
   Luka: {gap_size} punktów | Ważność: {importance:.1f} | Czas: {time_to_prof}
"""
        
        return skills_analysis
    
    def _format_development_timeline(self, skill_plan: Dict) -> str:
        """Formatowanie timeline rozwoju"""
        timeline = skill_plan.get('development_timeline', {})
        
        if not timeline:
            return "TIMELINE ROZWOJU: Wymagane szczegółowe planowanie"
        
        timeline_text = "📅 TIMELINE ROZWOJU UMIEJĘTNOŚCI:\n\n"
        
        phases = [
            ('immediate_actions', 'NATYCHMIASTOWE DZIAŁANIA (7 dni)'),
            ('short_term_plan', 'PLAN KRÓTKOTERMINOWY (1-3 miesiące)'),
            ('medium_term_plan', 'PLAN ŚREDNIOTERMINOWY (3-8 miesięcy)'),
            ('long_term_plan', 'PLAN DŁUGOTERMINOWY (8+ miesięcy)')
        ]
        
        for phase_key, phase_title in phases:
            if phase_key in timeline:
                timeline_text += f"{phase_title}:\n"
                
                phase_data = timeline[phase_key]
                if isinstance(phase_data, list):
                    if phase_key == 'immediate_actions':
                        # Lista stringów dla immediate actions
                        for action in phase_data:
                            timeline_text += f"• {action}\n"
                    else:
                        # Lista słowników dla planów
                        for item in phase_data:
                            if isinstance(item, dict):
                                timeline_text += f"• {item.get('skill', '')}: {item.get('goal', '')}\n"
                                timeline_text += f"  Action: {item.get('action', '')}\n"
                                timeline_text += f"  Time: {item.get('time_commitment', '')}\n"
                
                timeline_text += "\n"
        
        return timeline_text
    
    def _format_learning_resources(self, skill_plan: Dict) -> str:
        """Formatowanie zasobów do nauki"""
        resources = skill_plan.get('learning_resources', {})
        
        if not resources:
            return "ZASOBY ROZWOJU: Standardowe zasoby edukacyjne"
        
        resources_text = "📚 REKOMENDOWANE ZASOBY DO NAUKI:\n\n"
        
        for skill, resource_list in resources.items():
            resources_text += f"{skill.upper()}:\n"
            for resource in resource_list:
                resources_text += f"• {resource}\n"
            resources_text += "\n"
        
        return resources_text
    
    def _format_success_metrics(self, skill_plan: Dict) -> str:
        """Formatowanie metryk sukcesu"""
        metrics = skill_plan.get('success_metrics', {})
        
        if not metrics:
            return "METRYKI SUKCESU: Standardowe wskaźniki postępu"
        
        metrics_text = "📊 METRYKI SUKCESU I KPI:\n\n"
        
        for skill, metric_list in metrics.items():
            metrics_text += f"{skill.upper()}:\n"
            for metric in metric_list:
                metrics_text += f"• {metric}\n"
            metrics_text += "\n"
        
        return metrics_text
    
    def _format_quick_wins(self, skill_plan: Dict) -> str:
        """Formatowanie quick wins"""
        quick_wins = skill_plan.get('quick_wins', [])
        
        if not quick_wins:
            return "⚡ QUICK WINS: Focus na najbardziej impactful skills"
        
        return f"""
⚡ QUICK WINS - SZYBKIE SUKCESY:

{chr(10).join([f'• {win}' for win in quick_wins])}

ESTIMATED TOTAL DEVELOPMENT TIME: {skill_plan.get('total_estimated_time', '6-12 miesięcy')}
        """
    
    def _generate_risk_analysis_section(self, risk_analysis: Dict) -> str:
        """Generowanie sekcji analizy ryzyk"""
        
        return f"""
⚖️ ANALIZA RYZYK I MOŻLIWOŚCI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{self._format_risk_tolerance_assessment(risk_analysis)}

{self._format_career_opportunities(risk_analysis)}

{self._format_potential_threats(risk_analysis)}

{self._format_risk_management_strategy(risk_analysis)}
        """
    
    def _format_risk_tolerance_assessment(self, risk_analysis: Dict) -> str:
        """Formatowanie oceny tolerancji ryzyka"""
        risk_tolerance = risk_analysis.get('risk_tolerance_assessment', {})
        
        if not risk_tolerance:
            return "TOLERANCJA RYZYKA: Wymagana dalsza analiza"
        
        return f"""
🎲 OCENA TOLERANCJI RYZYKA:

POZIOM TOLERANCJI: {risk_tolerance.get('level', 'Średnia')}
SCORE: {risk_tolerance.get('score', 50):.1f}/100

OPIS: {risk_tolerance.get('description', '')}

CAPACITY DO RYZYKA: {risk_tolerance.get('risk_capacity', 'Medium')}

REKOMENDACJE:
{chr(10).join([f'• {rec}' for rec in risk_tolerance.get('recommendations', [])])}
        """
    
    def _format_career_opportunities(self, risk_analysis: Dict) -> str:
        """Formatowanie możliwości zawodowych"""
        opportunities = risk_analysis.get('career_opportunities', [])
        
        if not opportunities:
            return "MOŻLIWOŚCI: Standardowe możliwości rozwoju zawodowego"
        
        opportunities_text = "🚀 ZIDENTYFIKOWANE MOŻLIWOŚCI ZAWODOWE:\n\n"
        
        for i, opp in enumerate(opportunities, 1):
            opportunities_text += f"""
{i}. {opp.get('type', '').upper()}
   Opis: {opp.get('description', '')}
   Timeline: {opp.get('timeframe', 'N/A')}
   Wymagane działania: {opp.get('action_required', '')}
"""
        
        return opportunities_text
    
    def _format_potential_threats(self, risk_analysis: Dict) -> str:
        """Formatowanie potencjalnych zagrożeń"""
        threats = risk_analysis.get('potential_threats', [])
        
        if not threats:
            return "ZAGROŻENIA: Standardowe ryzyko branżowe"
        
        threats_text = "⚠️ POTENCJALNE ZAGROŻENIA:\n\n"
        
        for i, threat in enumerate(threats, 1):
            threats_text += f"""
{i}. {threat.get('type', '').upper()}
   Opis: {threat.get('description', '')}
   Prawdopodobieństwo: {threat.get('likelihood', 'Medium')}
   Mitigation: {threat.get('mitigation', '')}
"""
        
        return threats_text
    
    def _format_risk_management_strategy(self, risk_analysis: Dict) -> str:
        """Formatowanie strategii zarządzania ryzykiem"""
        strategy = risk_analysis.get('risk_management_strategy', {})
        
        if not strategy:
            return "STRATEGIA RYZYKA: Balanced approach do zarządzania ryzykiem zawodowym"
        
        strategy_text = "🛡️ STRATEGIA ZARZĄDZANIA RYZYKIEM:\n\n"
        
        strategy_categories = [
            ('diversification_strategies', 'STRATEGIE DYWERSYFIKACJI'),
            ('safety_net_building', 'BUDOWANIE SAFETY NETS'),
            ('opportunity_pursuit', 'PURSUIT OPPORTUNITIES'),
            ('threat_monitoring', 'MONITORING ZAGROŻEŃ')
        ]
        
        for category_key, category_title in strategy_categories:
            if category_key in strategy:
                strategy_text += f"{category_title}:\n"
                for item in strategy[category_key]:
                    strategy_text += f"• {item}\n"
                strategy_text += "\n"
        
        return strategy_text
    
    def _generate_implementation_roadmap(self, career_analysis: Dict) -> str:
        """Generowanie roadmapy implementacji"""
        
        recommendations = career_analysis.get('recommendations', [])
        
        return f"""
🗺️ ROADMAPA IMPLEMENTACJI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{self._format_actionable_recommendations(recommendations)}

{self._generate_90_day_action_plan()}

{self._generate_success_tracking_framework()}
        """
    
    def _format_actionable_recommendations(self, recommendations: List[Dict]) -> str:
        """Formatowanie wykonalnych rekomendacji"""
        if not recommendations:
            return "REKOMENDACJE: Wymagane szczegółowe planowanie działań"
        
        recs_text = "🎯 KLUCZOWE REKOMENDACJE DZIAŁAŃ:\n\n"
        
        for i, rec in enumerate(recommendations, 1):
            priority_symbol = {
                'Wysoki': '🔴',
                'Średni': '🟡', 
                'Niski': '🟢'
            }.get(rec.get('priority', 'Średni'), '🟡')
            
            recs_text += f"""
{i}. {priority_symbol} {rec.get('category', '').upper()}
   Działanie: {rec.get('action', '')}
   Uzasadnienie: {rec.get('rationale', '')}
   Timeline: {rec.get('timeline', 'N/A')}
   Priorytet: {rec.get('priority', 'Medium')}
"""
        
        return recs_text
    
    def _generate_90_day_action_plan(self) -> str:
        """Generowanie planu na 90 dni"""
        return """
📅 PLAN DZIAŁANIA NA PIERWSZE 90 DNI:

DNI 1-30: FOUNDATION & ASSESSMENT
• Przeprowadź comprehensive skills assessment
• Zidentyfikuj target companies i roles
• Rozpocznij networking activities
• Ustaw learning schedule i goals
• Update LinkedIn profile i resume

DNI 31-60: SKILL BUILDING & POSITIONING  
• Zapisz się na priority skills courses
• Start building portfolio projects
• Schedule informational interviews
• Attend industry events lub webinars
• Begin thought leadership activities

DNI 61-90: APPLICATION & ACCELERATION
• Apply dla target positions
• Complete first certification
• Expand professional network
• Seek stretch assignments w current role
• Evaluate progress i adjust strategy

🎯 90-DAY SUCCESS METRICS:
• Skills assessment completed z action plan
• Professional network expanded o 25+ contacts
• Portfolio zawiera 2-3 strong examples  
• First round interviews scheduled lub internal advancement opportunity identified
• Clear 6-month development plan established
        """
    
    def _generate_success_tracking_framework(self) -> str:
        """Generowanie frameworku śledzenia sukcesu"""
        return """
📊 FRAMEWORK ŚLEDZENIA POSTĘPÓW:

MONTHLY REVIEWS:
• Skills development progress (self-assessment 1-10)
• Network expansion (new connections, relationships depth)
• Learning achievements (courses, certifications, projects)
• Career opportunities (applications, interviews, offers)

QUARTERLY ASSESSMENTS:
• Goal achievement rate vs plan
• Market feedback (interviews, networking conversations)
• Skill gap reduction progress
• Personal brand development

ANNUAL EVALUATION:
• Career progression vs objectives
• Salary/compensation advancement
• Industry recognition i thought leadership
• Professional network quality i influence

KEY PERFORMANCE INDICATORS (KPIs):
• Time to interview dla target roles: <90 days
• Skills improvement rate: +2 points/quarter (1-10 scale)
• Network growth: +10 meaningful connections/quarter
• Learning completion rate: 100% dla priority skills
• Career transition success rate: binnen 12-18 months
        """
    
    def _generate_appendices(self, analysis_results: Dict) -> str:
        """Generowanie załączników"""
        
        return f"""
📎 ZAŁĄCZNIKI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{self._generate_methodology_appendix()}

{self._generate_resources_appendix()}

{self._generate_assessment_data_appendix(analysis_results)}
        """
    
    def _generate_methodology_appendix(self) -> str:
        """Metodologia analizy"""
        return """
📋 ZAŁĄCZNIK A: METODOLOGIA ANALIZY

MODELE PSYCHOLOGICZNE:
• Big Five (Five-Factor Model) - Costa & McCrae
• Self-Determination Theory (SDT) - Deci & Ryan  
• Cognitive Style Theory - Riding & Rayner
• Team Role Theory - Belbin

ALGORITMY DOPASOWANIA:
• Weighted scoring algorithm z personality fit (30%)
• Motivation alignment analysis (25%)
• Cognitive match assessment (25%)
• Skills compatibility evaluation (20%)

ŹRÓDŁA DANYCH RYNKOWYCH:
• Bureau of Labor Statistics (BLS)
• Industry salary surveys (Glassdoor, PayScale)
• Technology trend analysis (Gartner, McKinsey)
• Skills demand forecasting (LinkedIn, Indeed)

VALIDATION METHODOLOGY:
• Cross-validation z career success outcomes
• Predictive accuracy testing
• Expert review panel validation
• User feedback integration
        """
    
    def _generate_resources_appendix(self) -> str:
        """Załącznik zasobów"""
        return """
📚 ZAŁĄCZNIK B: DODATKOWE ZASOBY

CAREER DEVELOPMENT BOOKS:
• "What Color Is Your Parachute?" - Richard N. Bolles
• "Designing Your Life" - Bill Burnett & Dave Evans
• "The Startup of You" - Reid Hoffman
• "Mindset" - Carol Dweck

PROFESSIONAL ASSESSMENT TOOLS:
• StrengthsFinder 2.0 - Gallup
• DISC Assessment
• Myers-Briggs Type Indicator (MBTI)
• Emotional Intelligence Assessment

ONLINE LEARNING PLATFORMS:
• Coursera - University courses i specializations
• LinkedIn Learning - Professional skills
• Udemy - Practical skills training
• edX - Academic i professional programs

NETWORKING PLATFORMS:
• LinkedIn - Professional networking
• Industry associations i conferences
• Meetup groups - Local professional events
• Alumni networks - University connections

CAREER COACHING RESOURCES:
• International Coach Federation (ICF)
• Career Development Institute (CDI)
• Local career centers i employment services
• Professional coaching platforms
        """
    
    def _generate_assessment_data_appendix(self, analysis_results: Dict) -> str:
        """Załącznik danych z oceny"""
        
        # Simplified data summary dla załącznika
        return f"""
📊 ZAŁĄCZNIK C: DANE Z OCENY

PERSONALITY SCORES (Big Five):
{self._format_raw_personality_data(analysis_results.get('personality_profile', {}))}

MOTIVATION PROFILE:
{self._format_raw_motivation_data(analysis_results.get('motivation_profile', {}))}

COGNITIVE ASSESSMENT:
{self._format_raw_cognitive_data(analysis_results.get('cognitive_profile', {}))}

CAREER MATCHING RESULTS:
{self._format_raw_career_data(analysis_results.get('career_analysis', {}))}

DISCLAIMER:
Te wyniki są oparte na self-assessment i algorytmach predykcyjnych. 
Nie stanowią profesjonalnej porady psychologicznej ani gwarancji sukcesu zawodowego.
Zaleca się konsultacje z qualified career counselor dla personalized guidance.
        """
    
    def _format_raw_personality_data(self, personality_profile: Dict) -> str:
        """Formatowanie surowych danych osobowości"""
        if not personality_profile:
            return "Brak danych osobowości"
        
        data_text = ""
        traits = ['extraversion', 'agreeableness', 'conscientiousness', 'emotional_stability', 'openness']
        
        for trait in traits:
            if trait in personality_profile and isinstance(personality_profile[trait], dict):
                score = personality_profile[trait].get('score', 3.0)
                percentile = personality_profile[trait].get('percentile', 60)
                data_text += f"• {trait.title()}: {score:.1f}/5.0 (Percentyl: {percentile}%)\n"
        
        return data_text
    
    def _format_raw_motivation_data(self, motivation_profile: Dict) -> str:
        """Formatowanie surowych danych motywacji"""
        top_motivators = motivation_profile.get('top_motivators', [])
        
        if not top_motivators:
            return "Brak danych motywacji"
        
        data_text = ""
        for motivator in top_motivators:
            name = motivator.get('name', '')
            score = motivator.get('score', 0.5)
            data_text += f"• {name.title()}: {score:.2f} ({score*100:.0f}%)\n"
        
        return data_text
    
    def _format_raw_cognitive_data(self, cognitive_profile: Dict) -> str:
        """Formatowanie surowych danych kognitywnych"""
        processing_style = cognitive_profile.get('processing_style', {}).get('type', 'N/A')
        decision_style = cognitive_profile.get('decision_style', {}).get('type', 'N/A')
        
        cognitive_analysis = cognitive_profile.get('cognitive_strengths_analysis', {})
        average_level = cognitive_analysis.get('average_level', 5.0)
        
        return f"""• Processing Style: {processing_style}
• Decision Style: {decision_style}
• Average Cognitive Level: {average_level:.1f}/10
        """
    
    def _format_raw_career_data(self, career_analysis: Dict) -> str:
        """Formatowanie surowych danych kariery"""
        recommended_paths = career_analysis.get('recommended_paths', [])
        
        if not recommended_paths:
            return "Brak rekomendacji kariery"
        
        data_text = ""
        for path in recommended_paths[:3]:
            title = path.get('title', '')
            match_score = path.get('match_score', 0)
            data_text += f"• {title}: {match_score:.1f}% match\n"
        
        return data_text
    
    def _generate_report_footer(self) -> str:
        """Generowanie stopki raportu"""
        generation_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📞 WSPARCIE I KONTAKT

Masz pytania dotyczące raportu lub potrzebujesz dodatkowej pomocy?

🔗 DALSZE KROKI:
• Skonsultuj się z career counselor dla personalized guidance
• Rozważ professional coaching dla accelerated development  
• Join professional associations w target industry
• Build mentor relationships dla ongoing support

⚖️ DISCLAIMER:
Ten raport jest generowany przez algorytmy AI i nie zastępuje profesjonalnej 
porady psychologicznej, career counseling lub innych professional services.
Wyniki są oparte na self-assessment i powinny być traktowane jako guidance,
nie jako definitive career direction.

📊 RAPORT STATISTICS:
• Wygenerowany: {generation_time}
• Wersja algorytmu: CareerScope Pro v2.0
• Confidence level: High (based na comprehensive assessment)
• Validity period: 12-18 miesięcy (recommended re-assessment)

╔══════════════════════════════════════════════════════════════════════════════╗
║                     🧠 CAREERSCOPE PRO                                      ║
║            "Unlock Your Professional Potential"                             ║
║                                                                              ║ 
║     © 2024 CareerScope Pro. All rights reserved.                           ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """

    def generate_summary_report(self, analysis_results: Dict, user_data: Dict) -> str:
        """Generowanie skróconego raportu (executive summary only)"""
        
        report_sections = [
            self._generate_report_header(user_data),
            self._generate_executive_summary(analysis_results, user_data),
            self._generate_quick_action_plan(),
            self._generate_report_footer()
        ]
        
        return '\n\n'.join(report_sections)
    
    def _generate_quick_action_plan(self) -> str:
        """Szybki plan działania dla skróconego raportu"""
        return """
⚡ QUICK ACTION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 IMMEDIATE NEXT STEPS (Next 7 Days):
1. Review i internalize key findings z tego raportu
2. Identify 1-2 priority skills dla immediate development
3. Update LinkedIn profile z target career w mind  
4. Research 5 companies w recommended industries
5. Reach out do 3 people w your network dla advice

📅 30-DAY SPRINT:
• Complete detailed skills assessment
• Enroll w online course dla top priority skill
• Schedule 3 informational interviews
• Begin networking w target industry
• Start building portfolio/examples portfolio

🚀 90-DAY TRANSFORMATION:
• Apply skills learnings w current role
• Complete first certification lub course
• Attend industry event lub conference
• Build relationships z 5+ new professional contacts
• Evaluate progress i adjust strategy based na market feedback

SUCCESS METRIC: W 90 dni powinieneś mieć clear path forward 
i measurable progress towards your target career direction.
        """
    
    def generate_skills_focused_report(self, analysis_results: Dict, user_data: Dict) -> str:
        """Generowanie raportu focused na skills development"""
        
        career_analysis = analysis_results.get('career_analysis', {})
        skill_plan = career_analysis.get('skill_development_plan', {})
        
        report_sections = [
            self._generate_report_header(user_data),
            "🎯 SKILLS DEVELOPMENT FOCUS REPORT",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            self._generate_skill_development_section(skill_plan),
            self._generate_report_footer()
        ]
        
        return '\n\n'.join(report_sections)
    
    def export_data_for_external_tools(self, analysis_results: Dict, user_data: Dict) -> Dict[str, Any]:
        """Export danych dla external tools (JSON format)"""
        
        export_data = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'version': 'CareerScope Pro v2.0',
                'user_name': user_data.get('name', 'Anonymous'),
                'user_position': user_data.get('position', 'Professional')
            },
            'personality_profile': analysis_results.get('personality_profile', {}),
            'motivation_profile': analysis_results.get('motivation_profile', {}),
            'cognitive_profile': analysis_results.get('cognitive_profile', {}),
            'career_analysis': {
                'recommended_paths': analysis_results.get('career_analysis', {}).get('recommended_paths', []),
                'skill_development_plan': analysis_results.get('career_analysis', {}).get('skill_development_plan', {}),
                'success_analysis': analysis_results.get('career_analysis', {}).get('success_analysis', {})
            }
        }
        
        return export_data
    
    def create_presentation_slides_content(self, analysis_results: Dict, user_data: Dict) -> List[Dict[str, str]]:
        """Tworzenie contentu dla presentation slides"""
        
        slides = [
            {
                'title': '🧠 CareerScope Pro Analysis',
                'subtitle': f'Personalized Career Assessment dla {user_data.get("name", "Professional")}',
                'content': f'Generated: {datetime.now().strftime("%B %d, %Y")}'
            },
            {
                'title': '📊 Executive Summary',
                'content': self._create_slide_summary(analysis_results)
            },
            {
                'title': '🧬 Personality Profile',
                'content': self._create_personality_slide(analysis_results.get('personality_profile', {}))
            },
            {
                'title': '🚀 Career Recommendations',
                'content': self._create_career_slide(analysis_results.get('career_analysis', {}))
            },
            {
                'title': '📈 Development Plan',
                'content': self._create_development_slide(analysis_results.get('career_analysis', {}))
            },
            {
                'title': '🎯 Next Steps',
                'content': self._create_next_steps_slide()
            }
        ]
        
        return slides
    
    def _create_slide_summary(self, analysis_results: Dict) -> str:
        """Tworzenie slide summary"""
        career_analysis = analysis_results.get('career_analysis', {})
        recommended_paths = career_analysis.get('recommended_paths', [])
        success_analysis = career_analysis.get('success_analysis', {})
        
        top_career = recommended_paths[0]['title'] if recommended_paths else 'N/A'
        success_score = success_analysis.get('overall_success_probability', 75)
        
        return f"""
• PRIMARY RECOMMENDATION: {top_career}
• SUCCESS PROBABILITY: {success_score}%
• KEY STRENGTHS: Analytical thinking, Strong communication
• DEVELOPMENT FOCUS: Leadership skills, Industry expertise
• TIMELINE: 12-18 months dla career transition
        """
    
    def _create_personality_slide(self, personality_profile: Dict) -> str:
        """Tworzenie personality slide"""
        if not personality_profile:
            return "• Personality assessment requires completion"
        
        traits_summary = []
        for trait, data in personality_profile.items():
            if isinstance(data, dict) and 'level' in data:
                level = data['level']
                if level == 'high':
                    traits_summary.append(f"• {trait.title()}: High - Natural strength")
        
        return '\n'.join(traits_summary) if traits_summary else "• Balanced personality profile"
    
    def _create_career_slide(self, career_analysis: Dict) -> str:
        """Tworzenie career slide"""
        recommended_paths = career_analysis.get('recommended_paths', [])
        
        if not recommended_paths:
            return "• Career recommendations require profile completion"
        
        career_content = []
        for path in recommended_paths[:3]:
            title = path.get('title', '')
            match_score = path.get('match_score', 0)
            career_content.append(f"• {title}: {match_score:.0f}% match")
        
        return '\n'.join(career_content)
    
    def _create_development_slide(self, career_analysis: Dict) -> str:
        """Tworzenie development slide"""
        skill_plan = career_analysis.get('skill_development_plan', {})
        prioritized_skills = skill_plan.get('prioritized_skills', [])
        
        if not prioritized_skills:
            return "• Skills development plan requires assessment"
        
        dev_content = []
        for skill in prioritized_skills[:4]:
            skill_name = skill.get('skill', '')
            time_to_prof = skill.get('time_to_proficiency', 'N/A')
            dev_content.append(f"• {skill_name}: {time_to_prof}")
        
        return '\n'.join(dev_content)
    
    def _create_next_steps_slide(self) -> str:
        """Tworzenie next steps slide"""
        return """
• Complete priority skills assessment
• Network w target industry professionals
• Apply dla stretch assignments w current role
• Build portfolio demonstrating key capabilities
• Schedule follow-up assessment w 6 months
        """# report_generator.py - Generator raportów PDF
from typing import Dict, List, Any
from datetime import datetime
import json

class ReportGenerator:
    """Generator komprehensywnych raportów PDF z analizy kariery"""
    
    def __init__(self):
        self.report_template = {
            'header': {
                'title': 'CareerScope Pro - Analiza Psychologiczno-Biznesowa',
                'subtitle': 'Personalizowany Raport Rozwoju Kariery',
                'logo': '🧠',
                'colors': {
                    'primary': '#1e3c72',
                    'secondary': '#2a5298',
                    'accent': '#667eea'
                }
            },
            'sections': [
                'executive_summary',
                'personality_analysis', 
                'motivation_profile',
                'cognitive_assessment',
                'career_recommendations',
                'skill_development_plan',
                'risk_opportunity_analysis',
                'implementation_roadmap',
                'appendices'
            ]
        }
    
    def generate_comprehensive_report(self, analysis_results: Dict, user_data: Dict) -> str:
        """Generowanie komprehensywnego raportu"""
        
        report_sections = []
        
        # Header i metadata
        report_sections.append(self._generate_report_header(user_data))
        
        # Executive Summary
        report_sections.append(self._generate_executive_summary(analysis_results, user_data))
        
        # Detailed sections
        if 'personality_profile' in analysis_results:
            report_sections.append(self._generate_personality_section(analysis_results['personality_profile']))
        
        if 'motivation_profile' in analysis_results:
            report_sections.append(self._generate_motivation_section(analysis_results['motivation_profile']))
        
        if 'cognitive_profile' in analysis_results:
            report_sections.append(self._generate_cognitive_section(analysis_results['cognitive_profile']))
        
        if 'career_analysis' in analysis_results:
            career_analysis = analysis_results['career_analysis']
            
            report_sections.append(self._generate_career_recommendations_section(career_analysis))
            
            if 'skill_development_plan' in career_analysis:
                report_sections.append(self._generate_skill_development_section(career_analysis['skill_development_plan']))
            
            if 'risk_opportunity_analysis' in career_analysis:
                report_sections.append(self._generate_risk_analysis_section(career_analysis['risk_opportunity_analysis']))
            
            report_sections.append(self._generate_implementation_roadmap(career_analysis))
        
        # Appendices
        report_sections.append(self._generate_appendices(analysis_results))
        
        # Footer
        report_sections.append(self._generate_report_footer())
        
        return '\n\n'.join(report_sections)
    
    def _generate_report_header(self, user_data: Dict) -> str:
        """Generowanie nagłówka raportu"""
        
        name = user_data.get('name', 'Użytkownik')
        position = user_data.get('position', 'Profesjonalista')
        generation_date = datetime.now().strftime('%d %B %Y')
        
        return f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                          🧠 CAREERSCOPE PRO                                 ║
║                    ANALIZA PSYCHOLOGICZNO-BIZNESOWA                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  PROFIL ZAWODOWY: {name:<58} ║
║  OBECNA POZYCJA:  {position:<58} ║
║  DATA ANALIZY:    {generation_date:<58} ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

INFORMACJE O RAPORCIE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ten raport zawiera kompleksową analizę Twojego profilu zawodowego opartą na:
• Naukowo zwalidowanych modelach psychologicznych (Big Five, SDT)
• Zaawansowanych algorytmach dopasowania kariery
• Analizie trendów rynkowych i projekcjach branżowych
• Spersonalizowanych rekomendacjach rozwoju

STRUKTURA RAPORTU:
• Executive Summary - kluczowe wnioski i rekomendacje
• Analiza Osobowości - profil Big Five z implikacjami zawodowymi
• Profil Motywacyjny - analiza drivers i sustainability
• Ocena Kognitywna - style myślenia i mocne strony
• Rekomendacje Kariery - dopasowane ścieżki zawodowe
• Plan Rozwoju - konkretne kroki i timeline
• Analiza Ryzyk - możliwości i zagrożenia
• Roadmapa Implementacji - praktyczny plan działania
        """
    
    def _generate_executive_summary(self, analysis_results: Dict, user_data: Dict) -> str:
        """Generowanie executive summary"""
        
        name = user_data.get('name', 'Użytkownik')
        
        # Extract key insights
        personality_profile = analysis_results.get('personality_profile', {})
        career_analysis = analysis_results.get('career_analysis', {})
        recommended_paths = career_analysis.get('recommended_paths', [])
        success_analysis = career_analysis.get('success_analysis', {})
        
        # Determine dominant personality traits
        dominant_traits = self._get_dominant_traits(personality_profile)
        
        # Get top career recommendations
        top_careers = [path['title'] for path in recommended_paths[:3]] if recommended_paths else ['Brak rekomendacji']
        
        # Success probability
        success_prob = success_analysis.get('overall_success_probability', 75)
        
        return f"""
📊 EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 PROFIL ZAWODOWY: {name}

KLUCZOWE WNIOSKI:
┌─────────────────────────────────────────────────────────────────────────────┐
│ PERSONALNOŚĆ:  {dominant_traits:<59} │
│ SUKCES SCORE:  {success_prob}% - {'Bardzo wysoki potencjał' if success_prob >= 85 else 'Wysoki potencjał' if success_prob >= 75 else 'Dobry potencjał'}                               │
│ GOTOWOŚĆ:      {'Gotowy do advancement' if success_prob >= 80 else 'Wymaga rozwoju w kluczowych obszarach'}                                        │
└─────────────────────────────────────────────────────────────────────────────┘

🚀 TOP 3 REKOMENDOWANE ŚCIEŻKI KARIERY:

1. {top_careers[0] if len(top_careers) > 0 else 'N/A'}
   → Match Score: {recommended_paths[0]['match_score'] if recommended_paths else 'N/A'}% | Growth Potential: {recommended_paths[0]['growth_potential'] if recommended_paths else 'N/A'}%

2. {top_careers[1] if len(top_careers) > 1 else 'N/A'}
   → Match Score: {recommended_paths[1]['match_score'] if len(recommended_paths) > 1 else 'N/A'}% | Growth Potential: {recommended_paths[1]['growth_potential'] if len(recommended_paths) > 1 else 'N/A'}%

3. {top_careers[2] if len(top_careers) > 2 else 'N/A'}
   → Match Score: {recommended_paths[2]['match_score'] if len(recommended_paths) > 2 else 'N/A'}% | Growth Potential: {recommended_paths[2]['growth_potential'] if len(recommended_paths) > 2 else 'N/A'}%

💪 KLUCZOWE MOCNE STRONY:
{self._format_strengths(analysis_results)}

🎯 PRIORYTETOWE OBSZARY ROZWOJU:
{self._format_development_areas(analysis_results)}

⏰ TIMELINE IMPLEMENTACJI:
• NASTĘPNE 30 DNI:   Skills assessment i goal setting
• 1-3 MIESIĄCE:      Intensywny rozwój top-priority skills
• 3-6 MIESIĘCY:      Network building i market positioning
• 6-12 MIESIĘCY:     Career transition lub advancement

💰 PROJEKCJA FINANSOWA (dla top rekomendacji):
• Obecny potencjał:  ${self._get_current_salary_projection(recommended_paths):,} - ${self._get_current_salary_projection(recommended_paths, 'max'):,}
• Za 3 lata:         ${self._get_future_salary_projection(recommended_paths, 3):,} - ${self._get_future_salary_projection(recommended_paths, 3, 'max'):,}
• Za 5 lat:          ${self._get_future_salary_projection(recommended_paths, 5):,} - ${self._get_future_salary_projection(recommended_paths, 5, 'max'):,}

🎖️ SUCCESS FACTORS:
{self._format_success_factors(success_analysis)}
        """
    
    def _get_dominant_traits(self, personality_profile: Dict) -> str:
        """Identyfikacja dominujących cech osobowości"""
        if not personality_profile:
            return "Profil wymagający pogłębienia"
        
        high_traits = []
        for trait, data in personality_profile.items():
            if isinstance(data, dict) and data.get('level') == 'high':
                trait_names = {
                    'extraversion': 'Ekstrawertyczny',
                    'agreeableness': 'Współpracujący', 
                    'conscientiousness': 'Sumienny',
                    'emotional_stability': 'Stabilny emocjonalnie',
                    'openness': 'Otwarty na doświadczenia'
                }
                high_traits.append(trait_names.get(trait, trait))
        
        if high_traits:
            return f"{', '.join(high_traits[:2])} Leader"
        else:
            return "Balanced Professional"
    
    def _format_strengths(self, analysis_results: Dict) -> str:
        """Formatowanie mocnych stron"""
        strengths = []
        
        # Z analizy osobowości
        personality_profile = analysis_results.get('personality_profile', {})
        if 'overall_assessment' in personality_profile:
            overall_strengths = personality_profile['overall_assessment'].get('strengths_summary', [])
            strengths.extend(overall_strengths[:2])
        
        # Z analizy kognitywnej
        cognitive_profile = analysis_results.get('cognitive_profile', {})
        if 'cognitive_strengths_analysis' in cognitive_profile:
            cog_analysis = cognitive_profile['cognitive_strengths_analysis']
            top_strengths = cog_analysis.get('top_strengths', [])
            for strength in top_strengths[:2]:
                strengths.append(f"{strength.get('name', '')} ({strength.get('level', '')})")
        
        if not strengths:
            strengths = ['Strong foundation dla professional growth', 'Balanced skill portfolio']
        
        return '\n'.join([f"• {strength}" for strength in strengths[:4]])
    
    def _format_development_areas(self, analysis_results: Dict) -> str:
        """Formatowanie obszarów rozwoju"""
        development_areas = []
        
        # Z skill development plan
        career_analysis = analysis_results.get('career_analysis', {})
        if 'skill_development_plan' in career_analysis:
            skill_plan = career_analysis['skill_development_plan']
            prioritized_skills = skill_plan.get('prioritized_skills', [])
            for skill in prioritized_skills[:3]:
                development_areas.append(f"{skill.get('skill', '')} (Gap: {skill.get('gap_size', 0)} points)")
        
        if not development_areas:
            development_areas = ['Strategic thinking enhancement', 'Leadership skills development', 'Industry expertise deepening']
        
        return '\n'.join([f"• {area}" for area in development_areas[:3]])
    
    def _get_current_salary_projection(self, recommended_paths: List[Dict], range_type: str = 'min') -> int:
        """Aktualna projekcja zarobków"""
        if not recommended_paths:
            return 80000 if range_type == 'min' else 120000
        
        salary_range = recommended_paths[0].get('salary_range', (80000, 120000))
        return salary_range[0] if range_type == 'min' else salary_range[1]
    
    def _get_future_salary_projection(self, recommended_paths: List[Dict], years: int, range_type: str = 'min') -> int:
        """Przyszła projekcja zarobków"""
        current = self._get_current_salary_projection(recommended_paths, range_type)
        growth_rate = 0.08  # 8% annual growth
        return int(current * (1 + growth_rate) ** years)
    
    def _format_success_factors(self, success_analysis: Dict) -> str:
        """Formatowanie czynników sukcesu"""
        factors = success_analysis.get('key_success_drivers', [])
        if not factors:
            factors = ['Strong analytical capabilities', 'Good interpersonal skills', 'Adaptability i learning agility']
        
        return '\n'.join([f"• {factor}" for factor in factors[:3]])
    
    def _generate_personality_section(self, personality_profile: Dict) -> str:
        """Generowanie sekcji analizy osobowości"""
        
        return f"""
🧬 ANALIZA OSOBOWOŚCI (MODEL BIG FIVE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Model Big Five to naukowo zwalidowany framework analizy osobowości, który 
przewiduje zachowania zawodowe i sukces w różnych rolach.

{self._format_big_five_traits(personality_profile)}

🔗 KOMBINACJE CECH I IMPLIKACJE ZAWODOWE:

{self._format_trait_combinations(personality_profile)}

📈 OGÓLNA OCENA PROFILU:

{self._format_overall_assessment(personality_profile)}

💡 REKOMENDACJE ROZWOJU OSOBOWOŚCI:

{self._format_personality_development_recommendations(personality_profile)}
        """
    
    def _format_big_five_traits(self, personality_profile: Dict) -> str:
        """Formatowanie cech Big Five"""
        
        trait_sections = []
        
        trait_names = {
            'extraversion': ('🎯 EKSTRAWERSJA', 'Źródło energii i style interakcji'),
            'agreeableness': ('🤝 UGODOWOŚĆ', 'Podejście do współpracy i relacji'),
            'conscientiousness': ('📋 SUMIENNOŚĆ', 'Organizacja, dyscyplina i niezawodność'),
            'emotional_stability': ('🧘 STABILNOŚĆ EMOCJONALNA', 'Radzenie sobie ze stresem'),
            'openness': ('🎨 OTWARTOŚĆ', 'Kreatywność i otwartość na nowe doświadczenia')
        }
        
        for trait_key, (trait_title, trait_subtitle) in trait_names.items():
            if trait_key in personality_profile and isinstance(personality_profile[trait_key], dict):
                trait_data = personality_profile[trait_key]
                score = trait_data.get('score', 3.0)
                level = trait_data.get('level', 'medium')
                description = trait_data.get('description', '')
                percentile = trait_data.get('percentile', 60)
                
                # Progress bar visualization
                progress_bar = self._create_text_progress_bar(score, 5.0)
                
                trait_section = f"""
{trait_title} ({trait_subtitle})
Wynik: {score:.1f}/5.0 ({level.upper()}) | Percentyl: {percentile}%
{progress_bar}

INTERPRETACJA: {description}

IMPLIKACJE ZAWODOWE:
{self._format_career_implications(trait_data)}
"""
                trait_sections.append(trait_section)
        
        return '\n'.join(trait_sections)
    
    def _create_text_progress_bar(self, value: float, max_value: float, length: int = 50) -> str:
        """Tworzenie tekstowego paska postępu"""
        filled_length = int(length * value / max_value)
        bar = '█' * filled_length + '░' * (length - filled_length)
        return f"[{bar}] {value:.1f}/{max_value}"
    
    def _format_career_implications(self, trait_data: Dict) -> str:
        """Formatowanie implikacji zawodowych"""
        implications = trait_data.get('career_implications', [])
        if implications:
            return '\n'.join([f"• {implication}" for implication in implications[:3]])
        else:
            return "• Uniwersalne zastosowanie w różnych rolach zawodowych"
    
    def _format_trait_combinations(self, personality_profile: Dict) -> str:
        """Formatowanie kombinacji cech"""
        combinations = personality_profile.get('combinations', [])
        
        if not combinations:
            return "Profil osobowości wskazuje na balanced approach do różnych sytuacji zawodowych."
        
        combination_texts = []
        for combo in combinations:
            combo_text = f"""
🎭 {combo.get('type', 'Kombinacja cech').upper()}
{combo.get('description', '')}

Implikacje: {combo.get('implications', '')}
"""
            combination_texts.append(combo_text)
        
        return '\n'.join(combination_texts)
    
    def _format_overall_assessment(self, personality_profile: Dict) -> str:
        """Formatowanie ogólnej oceny"""
        overall = personality_profile.get('overall_assessment', {})
        
        if not overall:
            return "Profil osobowości wymaga dalszej analizy dla pełnej oceny."
        
        return f"""
PROFIL OGÓLNY: {overall.get('overall_profile', 'Balanced Professional')}

ŚREDNI WYNIK: {overall.get('average_score', 3.5):.1f}/5.0
BALANS OSOBOWOŚCI: {overall.get('personality_balance', 3.5):.1f}/5.0

DOMINUJĄCA CECHA: {overall.get('dominant_trait', 'conscientiousness').title()}
OBSZAR ROZWOJU: {overall.get('development_area', 'extraversion').title()}

MOCNE STRONY:
{chr(10).join([f'• {strength}' for strength in overall.get('strengths_summary', [])])}
        """
    
    def _format_personality_development_recommendations(self, personality_profile: Dict) -> str:
        """Rekomendacje rozwoju osobowości"""
        overall = personality_profile.get('overall_assessment', {})
        recommendations = overall.get('development_recommendations', [])
        
        if not recommendations:
            return "• Regularnie seek feedback od colleagues i supervisors\n• Work on building self-awareness through reflection\n• Consider personality-based coaching"
        
        return '\n'.join([f"• {rec}" for rec in recommendations])
    
    def _generate_motivation_section(self, motivation_profile: Dict) -> str:
        """Generowanie sekcji analizy motywacji"""
        
        return f"""
🚀 PROFIL MOTYWACYJNY (TEORIA AUTODETERMINACJI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Analiza oparta na Self-Determination Theory (SDT), które identyfikuje kluczowe 
drivers długoterminowej motywacji i zaangażowania w pracy.

{self._format_top_motivators(motivation_profile)}

📊 ANALIZA TRWAŁOŚCI MOTYWACJI:

{self._format_sustainability_analysis(motivation_profile)}

🏢 REKOMENDACJE ŚRODOWISKA PRACY:

{self._format_work_environment_recommendations(motivation_profile)}

⚠️ POTENCJALNE KONFLIKTY MOTYWACYJNE:

{self._format_motivation_conflicts(motivation_profile)}

🎯 PROFIL MOTYWACYJNY - PODSUMOWANIE:

{motivation_profile.get('motivation_profile_summary', 'Unique motivational profile requiring individual approach')}
        """
    
    def _format_top_motivators(self, motivation_profile: Dict) -> str:
        """Formatowanie głównych motywatorów"""
        top_motivators = motivation_profile.get('top_motivators', [])
        
        if not top_motivators:
            return "Profil motywacyjny wymaga pogłębionej analizy."
        
        motivator_sections = []
        
        for i, motivator in enumerate(top_motivators, 1):
            name = motivator.get('name', '').title()
            score = motivator.get('score', 0.5)
            strength_level = motivator.get('strength_level', 'Umiarkowany')
            description = motivator.get('description', '')
            
            score_percentage = score * 100
            progress_bar = self._create_text_progress_bar(score_percentage, 100)
            
            motivator_section = f"""
{i}. {name.upper()} - {strength_level}
   Siła: {score_percentage:.0f}% {progress_bar}
   
   OPIS: {description}
"""
            motivator_sections.append(motivator_section)
        
        return '\n'.join(motivator_sections)
    
    def _format_sustainability_analysis(self, motivation_profile: Dict) -> str:
        """Formatowanie analizy trwałości"""
        sustainability = motivation_profile.get('sustainability_analysis', {})
        
        if not sustainability:
            return "Analiza trwałości motywacji niedostępna."
        
        return f"""
INTRINSIC MOTIVATION: {sustainability.get('intrinsic_motivation_level', 0.6):.1f}/1.0
EXTRINSIC MOTIVATION: {sustainability.get('extrinsic_motivation_level', 0.4):.1f}/1.0
OGÓLNA TRWAŁOŚĆ: {sustainability.get('overall_sustainability', 0.7):.1f
