def show_strategic_analysis():
    """Głęboka analiza strategiczna z perspektywą przyszłości"""
    st.markdown("# 🔮 Analiza Strategiczna Kariery")
    
    if 'analysis_results' not in st.session_state:
        st.error("Brak danych analizy.")
        return
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;">
    <h3>🎯 Strategiczna Ocena Twojego Profilu</h3>
    <p>Głęboka analiza uwzględniająca trendy technologiczne, ewolucję rynku pracy i Twoje unikalne predyspozycje</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Analiza profilu strategicznego
    results = st.session_state.analysis_results
    personality = results['personality_profile']
    recommendations = results['career_recommendations']
    
    # Określ strategiczny archetyp
    strategic_archetype = determine_strategic_archetype(personality)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"## 🏛️ Twój Strategiczny Archetyp: **{strategic_archetype['name']}**")
        st.markdown(f"*{strategic_archetype['description']}*")
        
        st.markdown("### 🎯 Strategiczne Mocne Strony:")
        for strength in strategic_archetype['strategic_strengths']:
            st.markdown(f"• **{strength['area']}**: {strength['description']}")
        
        st.markdown("### ⚡ Twoja Unikalna Przewaga Konkurencyjna:")
        st.info(strategic_archetype['competitive_advantage'])
    
    with col2:
        # Strategic fit score
        st.metric("🎯 Strategic Fit Score", f"{strategic_archetype['fit_score']}%")
        st.metric("🚀 Future Readiness", f"{strategic_archetype['future_readiness']}/10")
        st.metric("🔮 Adaptability Index", f"{strategic_archetype['adaptability']}/10")
    
    # Market positioning analysis
    st.markdown("## 📈 Analiza Pozycjonowania Rynkowego")
    
    market_analysis = analyze_market_positioning(personality, recommendations)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 **BLUE OCEAN** Opportunities")
        st.markdown("*Niezaspokojena demand*")
        for opp in market_analysis['blue_ocean']:
            st.markdown(f"🌊 **{opp['role']}**")
            st.caption(f"Potential: {opp['potential']} | Competition: {opp['competition']}")
    
    with col2:
        st.markdown("### ⚔️ **COMPETITIVE** Markets")
        st.markdown("*Wysokie demand, wysoka competition*")
        for comp in market_analysis['competitive']:
            st.markdown(f"⚔️ **{comp['role']}**")
            st.caption(f"Growth: {comp['growth']} | Difficulty: {comp['difficulty']}")
    
    with col3:
        st.markdown("### 🔄 **TRANSFORMATION** Paths")
        st.markdown("*Emerging roles*")
        for trans in market_analysis['transformation']:
            st.markdown(f"🔄 **{trans['role']}**")
            st.caption(f"Timeline: {trans['timeline']} | Prep: {trans['preparation']}")

def show_ai_impact_analysis():
    """Analiza wpływu AI na karierę"""
    st.markdown("# 🤖 AI Impact Analysis")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%); 
                padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;">
    <h3>🤖 Jak AI Wpłynie na Twoją Karierę?</h3>
    <p>Analiza odporności na automatyzację i możliwości wykorzystania AI jako acceleratora kariery</p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'analysis_results' not in st.session_state:
        st.error("Brak danych analizy.")
        return
    
    results = st.session_state.analysis_results
    ai_analysis = analyze_ai_impact(results)
    
    # AI Resistance Score
    col1, col2, col3 = st.columns(3)
    
    with col1:
        resistance_score = ai_analysis['automation_resistance']
        color = "🟢" if resistance_score >= 80 else "🟡" if resistance_score >= 60 else "🔴"
        st.metric("🛡️ AI Resistance Score", f"{resistance_score}%", help="Odporność na automatyzację")
        st.markdown(f"{color} **{get_resistance_category(resistance_score)}**")
    
    with col2:
        ai_synergy = ai_analysis['ai_synergy_potential']
        st.metric("🤝 AI Synergy Potential", f"{ai_synergy}%", help="Potencjał współpracy z AI")
        synergy_icon = "🚀" if ai_synergy >= 80 else "✅" if ai_synergy >= 60 else "⚠️"
        st.markdown(f"{synergy_icon} **{get_synergy_category(ai_synergy)}**")
    
    with col3:
        future_score = ai_analysis['future_relevance']
        st.metric("🔮 Future Relevance", f"{future_score}/10", help="Relevantność w przyszłości")
        future_icon = "🌟" if future_score >= 8 else "👍" if future_score >= 6 else "🔄"
        st.markdown(f"{future_icon} **{get_future_category(future_score)}**")
    
    # Detailed AI Impact per career
    st.markdown("## 🎯 AI Impact na Twoje Top Karriery")
    
    for i, career in enumerate(results['career_recommendations'][:3]):
        with st.expander(f"🤖 {career['title']} - AI Impact Analysis", expanded=(i==0)):
            career_ai_impact = get_career_ai_impact(career['title'])
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**🔮 Przyszłość roli w erze AI:**")
                st.markdown(career_ai_impact['future_outlook'])
                
                st.markdown(f"**🤖 Jak AI zmieni tę rolę:**")
                for change in career_ai_impact['ai_changes']:
                    st.markdown(f"• {change}")
                
                st.markdown(f"**🚀 AI Superpowers - jak wykorzystać AI:**")
                for power in career_ai_impact['ai_superpowers']:
                    st.markdown(f"⚡ **{power['tool']}**: {power['application']}")
            
            with col2:
                st.metric("Automation Risk", f"{career_ai_impact['automation_risk']}%")
                st.metric("AI Enhancement", f"{career_ai_impact['ai_enhancement']}%")
                st.metric("Future Demand", career_ai_impact['future_demand'])
    
    # Strategic recommendations for AI era
    st.markdown("## 🎯 Strategiczne Rekomendacje dla Ery AI")
    
    st.markdown("### 🛡️ **DEFENSIVE** Strategies (Ochrona przed automatyzacją)")
    defensive_strategies = ai_analysis['defensive_strategies']
    for strategy in defensive_strategies:
        st.markdown(f"🛡️ **{strategy['category']}**: {strategy['action']}")
        st.caption(f"Timeline: {strategy['timeline']} | Impact: {strategy['impact']}")
    
    st.markdown("### 🚀 **OFFENSIVE** Strategies (Wykorzystanie AI jako accelerator)")
    offensive_strategies = ai_analysis['offensive_strategies']
    for strategy in offensive_strategies:
        st.markdown(f"🚀 **{strategy['category']}**: {strategy['action']}")
        st.caption(f"Tools: {strategy['tools']} | ROI: {strategy['roi']}")

def show_development_paths():
    """Szczegółowe ścieżki rozwoju"""
    st.markdown("# 🛣️ Personalizowane Ścieżki Rozwoju")
    
    if 'analysis_results' not in st.session_state:
        st.error("Brak danych analizy.")
        return
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2d3436 0%, #636e72 100%); 
                padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;">
    <h3>🛣️ Twoje Spersonalizowane Ścieżki Rozwoju</h3>
    <p>Konkretne roadmapy uwzględniające Twój profil, rynek pracy i trendy technologiczne</p>
    </div>
    """, unsafe_allow_html=True)
    
    results = st.session_state.analysis_results
    
    # Path selection
    path_type = st.selectbox(
        "Wybierz typ ścieżki rozwoju:",
        ["🚀 Fast Track (6-12 miesięcy)", "📈 Strategic Growth (1-2 lata)", "🔄 Career Pivot (2-3 lata)"]
    )
    
    # Generate detailed path based on selection
    if "Fast Track" in path_type:
        show_fast_track_path(results)
    elif "Strategic Growth" in path_type:
        show_strategic_growth_path(results)
    else:
        show_career_pivot_path(results)

def show_fast_track_path(results):
    """6-12 miesięczna ścieżka szybkiego rozwoju"""
    st.markdown("## 🚀 Ścieżka Ekspresowa (6-12 miesięcy)")
    
    top_career = results['career_recommendations'][0]
    
    st.info(f"**Rola Docelowa:** {top_career['title']} | **Wynik Dopasowania:** {top_career['match_score']:.0f}%")
    
    # 90-dniowe sprinty
    tab1, tab2, tab3, tab4 = st.tabs([
        "📅 Sprint 1 (0-90 dni)", 
        "📅 Sprint 2 (90-180 dni)", 
        "📅 Sprint 3 (180-270 dni)", 
        "📅 Sprint 4 (270-365 dni)"
    ])
    
    with tab1:
        st.markdown("### 🎯 Sprint 1: Fundament i Szybkie Sukcesy")
        show_sprint_details({
            'focus': 'Ocena Umiejętności i Szybki Rozwój Kompetencji',
            'goals': [
                'Przeprowadź kompleksową analizę luk w umiejętnościach',
                'Rozpocznij 2 kursy online o wysokim wpływie',
                'Zbuduj początkowe projekty portfolio',
                'Strategia mapowania sieci kontaktów'
            ],
            'deliverables': [
                '✅ Raport oceny umiejętności',
                '✅ 2 ukończone certyfikaty',
                '✅ Pierwszy projekt portfolio na żywo',
                '✅ 10 nowych kontaktów zawodowych'
            ],
            'tools': ['Coursera/Udemy', 'GitHub', 'LinkedIn', 'Strona osobista'],
            'time_investment': '15-20 godzin/tydzień'
        })
    
    with tab2:
        st.markdown("### 🎯 Sprint 2: Pogłębianie Umiejętności i Pozycjonowanie")
        show_sprint_details({
            'focus': 'Zaawansowane Umiejętności i Pozycjonowanie Rynkowe',
            'goals': [
                'Opanuj 1-2 kluczowe umiejętności dla roli docelowej',
                'Rozpocznij działania thought leadership',
                'Zbuduj strategiczne relacje zawodowe',
                'Stwórz znaczące elementy portfolio'
            ],
            'deliverables': [
                '✅ Zaawansowany certyfikat zdobyty',
                '✅ 3 artykuły thought leadership opublikowane',
                '✅ Strategiczna relacja mentorska nawiązana',
                '✅ Portfolio pokazuje expertise'
            ],
            'tools': ['Medium/Artykuły LinkedIn', 'Fora branżowe', 'Wystąpienia konferencyjne'],
            'time_investment': '20-25 godzin/tydzień'
        })
    
    with tab3:
        st.markdown("### 🎯 Sprint 3: Testowanie Rynku i Optymalizacja")
        show_sprint_details({
            'focus': 'Walidacja Rynkowa i Przygotowanie do Roli',
            'goals': [
                'Przetestuj gotowość rynkową poprzez aplikacje',
                'Dopracuj pozycjonowanie na podstawie feedbacku',
                'Intensywne przygotowanie do rozmów kwalifikacyjnych',
                'Optymalizuj wszystkie materiały (CV, LinkedIn, portfolio)'
            ],
            'deliverables': [
                '✅ 10+ aplikacji wysłanych',
                '✅ Feedback z rozmów wdrożony',
                '✅ Wszystkie materiały zoptymalizowane',
                '✅ Sieć referencji ustanowiona'
            ],
            'tools': ['Portale z ofertami pracy', 'Rekruterzy', 'Platformy do rozmów'],
            'time_investment': '25-30 godzin/tydzień'
        })
    
    with tab4:
        st.markdown("### 🎯 Sprint 4: Realizacja i Przejście")
        show_sprint_details({
            'focus': 'Finalne Natarcie i Przejście do Roli',
            'goals': [
                'Intensywna faza aplikacji i rozmów kwalifikacyjnych',
                'Negocjuj optymalną ofertę',
                'Przygotuj się do przejścia ról',
                'Zaplanuj strategię pierwszych 100 dni'
            ],
            'deliverables': [
                '✅ Oferta roli docelowej zabezpieczona',
                '✅ Plan przejścia stworzony',
                '✅ Strategia onboardingu gotowa',
                '✅ Plan ciągłego uczenia się ustanowiony'
            ],
            'tools': ['Zasoby negocjacji wynagrodzenia', 'Planowanie przejścia'],
            'time_investment': '30+ godzin/tydzień'
        })

def show_sprint_details(sprint_data):
    """Helper function wyświetlająca szczegóły sprintu"""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"**🎯 Fokus:** {sprint_data['focus']}")
        
        st.markdown("**📋 Kluczowe Cele:**")
        for goal in sprint_data['goals']:
            st.markdown(f"• {goal}")
        
        st.markdown("**🎯 Rezultaty:**")
        for deliverable in sprint_data['deliverables']:
            st.markdown(f"{deliverable}")
    
    with col2:
        st.markdown("**🛠️ Narzędzia i Zasoby:**")
        for tool in sprint_data['tools']:
            st.markdown(f"• {tool}")
        
        st.markdown(f"**⏰ Inwestycja Czasowa:**")
        st.markdown(f"{sprint_data['time_investment']}")

# Helper functions for strategic analysis
def determine_strategic_archetype(personality):
    """Określa strategiczny archetyp na podstawie osobowości"""
    
    # Extract scores
    extraversion = personality.get('extraversion', {}).get('score', 3)
    openness = personality.get('openness', {}).get('score', 3)
    conscientiousness = personality.get('conscientiousness', {}).get('score', 3)
    agreeableness = personality.get('agreeableness', {}).get('score', 3)
    emotional_stability = personality.get('emotional_stability', {}).get('score', 3)
    
    # Determine archetype based on combination
    if openness >= 4.0 and conscientiousness >= 4.0:
        return {
            'name': 'Innovation Catalyst',
            'description': 'Łączysz kreatywność z wykonawczością - idealna do prowadzenia transformacji',
            'strategic_strengths': [
                {'area': 'Visionary Thinking', 'description': 'Naturalnie widzisz przyszłość i trends'},
                {'area': 'Systematic Execution', 'description': 'Przekładasz wizje na konkretne działania'},
                {'area': 'Change Leadership', 'description': 'Prowadzisz organizacje przez transformacje'}
            ],
            'competitive_advantage': 'Rzadka kombinacja kreatywności i dyscypliny wykonawczej. W erze AI to kluczowa przewaga - możesz wymyślać innowacyjne zastosowania AI i skutecznie je implementować.',
            'fit_score': 92,
            'future_readiness': 9,
            'adaptability': 9
        }
    elif extraversion >= 4.0 and emotional_stability >= 4.0:
        return {
            'name': 'Strategic Leader',
            'description': 'Naturalny lider z wysoką odpornością na stres - born to lead',
            'strategic_strengths': [
                {'area': 'People Leadership', 'description': 'Inspirujesz i mobilizujesz zespoły'},
                {'area': 'Crisis Management', 'description': 'Thriving pod presją i w niepewności'},
                {'area': 'Stakeholder Management', 'description': 'Excellent w zarządzaniu relationships'}
            ],
            'competitive_advantage': 'AI może automatyzować wiele zadań, ale nie może zastąpić authentic human leadership. Twoje naturalne predyspozycje liderskie będą jeszcze bardziej cenne.',
            'fit_score': 88,
            'future_readiness': 8,
            'adaptability': 8
        }
    elif conscientiousness >= 4.0 and agreeableness >= 4.0:
        return {
            'name': 'Operational Excellence',
            'description': 'Master systematycznych procesów i budowania zespołów',
            'strategic_strengths': [
                {'area': 'Process Optimization', 'description': 'Doskonalisz operational efficiency'},
                {'area': 'Team Building', 'description': 'Budujesz strong, cohesive teams'},
                {'area': 'Quality Assurance', 'description': 'Zapewniasz highest standards'}
            ],
            'competitive_advantage': 'AI potrzebuje human oversight dla quality i ethics. Twoje predyspozycje do systematycznej pracy i współpracy czynią Cię idealną do supervisory roles nad AI systems.',
            'fit_score': 85,
            'future_readiness': 7,
            'adaptability': 7
        }
    else:
        return {
            'name': 'Adaptive Professional',
            'description': 'Balanced profile z flexibility do różnych ścieżek',
            'strategic_strengths': [
                {'area': 'Versatility', 'description': 'Adaptujesz się do różnych environments'},
                {'area': 'Learning Agility', 'description': 'Quickly acquiring new skills'},
                {'area': 'Cross-functional Collaboration', 'description': 'Bridging different departments'}
            ],
            'competitive_advantage': 'Twoja versatility jest huge asset w rapidly changing world. Możesz pivot między rolami i industries, co będzie crucial w AI-driven economy.',
            'fit_score': 80,
            'future_readiness': 8,
            'adaptability': 9
        }

def analyze_market_positioning(personality, recommendations):
    """Analiza pozycjonowania rynkowego"""
    return {
        'blue_ocean': [
            {'role': 'AI Ethics Specialist', 'potential': 'Very High', 'competition': 'Low'},
            {'role': 'Human-AI Interaction Designer', 'potential': 'High', 'competition': 'Low'},
            {'role': 'Digital Transformation Coach', 'potential': 'High', 'competition': 'Medium'}
        ],
        'competitive': [
            {'role': 'Product Manager', 'growth': 'High', 'difficulty': 'High'},
            {'role': 'Data Scientist', 'growth': 'Very High', 'difficulty': 'Very High'},
            {'role': 'UX Designer', 'growth': 'Medium', 'difficulty': 'High'}
        ],
        'transformation': [
            {'role': 'AI Prompt Engineer', 'timeline': '3-6 months', 'preparation': 'AI tools mastery'},
            {'role': 'Automation Consultant', 'timeline': '6-12 months', 'preparation': 'Process + AI knowledge'},
            {'role': 'Digital Experience Director', 'timeline': '12-18 months', 'preparation': 'Leadership + Digital'}
        ]
    }

def analyze_ai_impact(results):
    """Analiza wpływu AI na karierę"""
    
    # Base resistance calculation
    personality = results['personality_profile']
    openness = personality.get('openness', {}).get('score', 3)
    creativity_factor = openness * 20
    
    # Human-centric skills bonus
    agreeableness = personality.get('agreeableness', {}).get('score', 3)
    extraversion = personality.get('extraversion', {}).get('score', 3)
    human_skills_bonus = (agreeableness + extraversion) * 10
    
    automation_resistance = min(95, creativity_factor + human_skills_bonus + 30)
    
    return {
        'automation_resistance': int(automation_resistance),
        'ai_synergy_potential': int(75 + openness * 10),
        'future_relevance': min(10, int(6 + openness + agreeableness)),
        'defensive_strategies': [
            {
                'category': 'Human-Centric Skills',
                'action': 'Rozwijaj emotional intelligence, empathy, complex problem-solving',
                'timeline': '3-6 months',
                'impact': 'High'
            },
            {
                'category': 'Creative Thinking',
                'action': 'Master design thinking, innovation methodologies, creative problem-solving',
                'timeline': '6-12 months',
                'impact': 'Very High'
            },
            {
                'category': 'Strategic Leadership',
                'action': 'Develop systems thinking, strategic planning, change management',
                'timeline': '12-18 months',
                'impact': 'Critical'
            }
        ],
        'offensive_strategies': [
            {
                'category': 'AI Tool Mastery',
                'action': 'Become power user of AI tools in your domain',
                'tools': 'ChatGPT, Claude, Midjourney, Copilot',
                'roi': '300-500%'
            },
            {
                'category': 'AI-Human Collaboration',
                'action': 'Specialize in optimizing human-AI workflows',
                'tools': 'Prompt engineering, AI training, workflow design',
                'roi': '200-400%'
            },
            {
                'category': 'AI Strategy',
                'action': 'Become AI transformation consultant for your industry',
                'tools': 'Industry knowledge + AI understanding',
                'roi': '500-1000%'
            }
        ]
    }

def get_resistance_category(score):
    """Kategoryzacja odporności na automatyzację"""
    if score >= 80:
        return "AI-Proof"
    elif score >= 60:
        return "AI-Resistant"
    else:
        return "AI-Vulnerable"

def get_synergy_category(score):
    """Kategoryzacja synergii z AI"""
    if score >= 80:
        return "AI Superuser"
    elif score >= 60:
        return "AI Collaborator"
    else:
        return "AI Novice"

def get_future_category(score):
    """Kategoryzacja relevance w przyszłości"""
    if score >= 8:
        return "Future-Essential"
    elif score >= 6:
        return "Future-Relevant"
    else:
        return "Future-Uncertain"

def get_career_ai_impact(career_title):
    """Szczegółowy wpływ AI na konkretną karierę"""
    
    career_impacts = {
        'Product Manager': {
            'future_outlook': 'Product Management będzie jeszcze bardziej strategic. AI przejmie routine tasks jak data analysis, A/B testing, basic user research, pozwalając PM-om focus na vision, strategy i stakeholder management.',
            'automation_risk': 15,
            'ai_enhancement': 85,
            'future_demand': 'Very High',
            'ai_changes': [
                'AI automated user research i data analysis',
                'Predictive analytics dla product decisions',
                'Automated competitive intelligence',
                'AI-powered roadmap optimization'
            ],
            'ai_superpowers': [
                {'tool': 'ChatGPT/Claude', 'application': 'PRD writing, user story generation, stakeholder communication'},
                {'tool': 'Notion AI', 'application': 'Product documentation, meeting summaries, roadmap planning'},
                {'tool': 'Mixpanel/Amplitude AI', 'application': 'Automated insights, predictive analytics'},
                {'tool': 'Figma AI', 'application': 'Rapid prototyping, design iteration'}
            ]
        },
        'Data Scientist': {
            'future_outlook': 'Data Science ewoluuje w kierunku AI Engineering i MLOps. Routine data cleaning i basic modeling będzie automated, ale potrzeba domain experts którzy rozumieją business context i ethical implications.',
            'automation_risk': 35,
            'ai_enhancement': 95,
            'future_demand': 'High',
            'ai_changes': [
                'AutoML tools automate basic modeling',
                'AI-generated code dla standard analyses', 
                'Automated feature engineering',
                'Natural language interfaces dla data queries'
            ],
            'ai_superpowers': [
                {'tool': 'GitHub Copilot', 'application': 'Code generation, debugging, optimization'},
                {'tool': 'DataRobot/H2O', 'application': 'Automated machine learning, model selection'},
                {'tool': 'Tableau AI', 'application': 'Automated insights, natural language queries'},
                {'tool': 'ChatGPT Code Interpreter', 'application': 'Rapid prototyping, data exploration'}
            ]
        },
        'UX Designer': {
            'future_outlook': 'UX Design shifts toward strategy i research. AI handles wireframing, basic prototyping, design systems, ale human insight into user psychology i creative problem-solving becomes more valuable.',
            'automation_risk': 25,
            'ai_enhancement': 80,
            'future_demand': 'High',
            'ai_changes': [
                'AI-generated wireframes i mockups',
                'Automated usability testing',
                'AI-powered design systems',
                'Personalized user interfaces'
            ],
            'ai_superpowers': [
                {'tool': 'Figma AI', 'application': 'Rapid ideation, design variations, component generation'},
                {'tool': 'Midjourney/DALL-E', 'application': 'Concept visualization, mood boards, creative exploration'},
                {'tool': 'Maze AI', 'application': 'Automated user testing, insight generation'},
                {'tool': 'Framer AI', 'application': 'Interactive prototyping, animation generation'}
            ]
        },
        'Strategy Consultant': {
            'future_outlook': 'Strategy Consulting becomes more data-driven ale human judgment, industry expertise i client relationships remain critical. AI accelerates research i analysis, enabling focus na high-level strategic thinking.',
            'automation_risk': 20,
            'ai_enhancement': 90,
            'future_demand': 'Very High',
            'ai_changes': [
                'AI-powered market research i competitive analysis',
                'Automated financial modeling',
                'Predictive scenario planning',
                'AI-generated presentation materials'
            ],
            'ai_superpowers': [
                {'tool': 'ChatGPT/Claude', 'application': 'Research synthesis, hypothesis generation, client communication'},
                {'tool': 'Perplexity', 'application': 'Real-time market research, competitor analysis'},
                {'tool': 'Beautiful.ai', 'application': 'Automated presentation design, data visualization'},
                {'tool': 'Excel/Sheets AI', 'application': 'Advanced financial modeling, scenario analysis'}
            ]
        }
    }
    
    return career_impacts.get(career_title, {
        'future_outlook': 'Ta rola będzie ewoluować wraz z rozwojem AI, wymagając adaptacji i nowych umiejętności.',
        'automation_risk': 30,
        'ai_enhancement': 70,
        'future_demand': 'Medium',
        'ai_changes': [
            'Automatyzacja routine tasks',
            'AI-assisted decision making',
            'Enhanced productivity tools'
        ],
        'ai_superpowers': [
            {'tool': 'ChatGPT/Claude', 'application': 'Communication, analysis, ideation'},
            {'tool': 'Industry-specific AI tools', 'application': 'Domain-specific automation'}
        ]
    })

def show_strategic_growth_path(results):
    """1-2 letnia ścieżka strategicznego rozwoju"""
    st.markdown("## 📈 Strategic Growth Path (1-2 lata)")
    
    st.info("**Focus:** Becoming a strategic leader w wybranej dziedzinie z expertise w AI collaboration")
    
    # Year 1 vs Year 2
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📅 **ROK 1: Foundation & Specialization**")
        st.markdown("""
        **Q1: Strategic Foundation**
        - 🎯 Complete advanced strategic thinking certification
        - 📊 Master data-driven decision making
        - 🤖 Become proficient w AI tools ecosystem
        - 🌐 Build thought leadership platform
        
        **Q2: Domain Expertise**
        - 🏆 Achieve expert-level certification w target domain
        - 📝 Publish 5+ high-impact articles/posts
        - 🤝 Establish strategic mentoring relationships
        - 🎤 Begin speaking at industry events
        
        **Q3: Market Positioning**
        - 🚀 Launch signature project/initiative
        - 📈 Build measurable business impact case studies
        - 🌟 Establish personal brand w niche
        - 💼 Expand network strategically (50+ new connections)
        
        **Q4: Leadership Transition**
        - 👥 Take on team leadership responsibilities
        - 📊 Drive organizational change initiative
        - 🎯 Position dla promotion/role transition
        - 🔮 Develop 5-year strategic vision
        """)
    
    with col2:
        st.markdown("### 📅 **ROK 2: Leadership & Innovation**")
        st.markdown("""
        **Q1: Strategic Leadership**
        - 🏛️ Move into senior/director level role
        - 🌍 Expand influence beyond immediate team
        - 🤖 Pioneer AI adoption w organization
        - 📚 Complete executive leadership program
        
        **Q2: Innovation Driver**
        - 🚀 Launch breakthrough innovation project
        - 🔬 Establish R&D or innovation function
        - 🏆 Win industry recognition/award
        - 📊 Demonstrate significant ROI impact
        
        **Q3: External Recognition**
        - 🎤 Keynote major industry conference
        - 📰 Featured w industry publications
        - 👥 Advisory role dla startup/scale-up
        - 🌟 Industry "Top 40 Under 40" recognition
        
        **Q4: Future Positioning**
        - 🎯 C-suite readiness assessment
        - 🌐 International expansion opportunities
        - 💡 Intellectual property development
        - 🚀 Plan dla next career leap
        """)
    
    # Strategic milestones tracking
    st.markdown("### 🎯 Kluczowe Milestones & Success Metrics")
    
    milestones_data = {
        'Milestone': [
            'Strategic Thinking Mastery',
            'AI Collaboration Expertise', 
            'Thought Leadership Platform',
            'Team Leadership Experience',
            'Business Impact Demonstration',
            'Industry Recognition',
            'Innovation Project Success',
            'Executive Readiness'
        ],
        'Timeline': [
            '3 months',
            '6 months', 
            '9 months',
            '12 months',
            '15 months',
            '18 months',
            '21 months',
            '24 months'
        ],
        'Success Metric': [
            'Strategic Planning Certification + Applied Project',
            'AI Tool Proficiency + 3 Implemented Use Cases',
            '10k+ Followers + 50k+ Content Views',
            'Successfully Led 5+ Person Team for 6+ Months',
            'Demonstrable $500k+ Business Impact',
            'Industry Award or Top Professional List',
            'Launched Product/Service with >$1M Revenue',
            'C-suite Interview Ready + Executive Assessment'
        ]
    }
    
    df_milestones = pd.DataFrame(milestones_data)
    st.dataframe(df_milestones, use_container_width=True)

def show_career_pivot_path(results):
    """2-3 letnia ścieżka zmiany kariery"""
    st.markdown("## 🔄 Career Pivot Path (2-3 lata)")
    
    st.warning("**Focus:** Complete career transformation z strategicznym approach i minimal risk")
    
    # Three phases
    phase1, phase2, phase3 = st.tabs(["🌱 Phase 1: Exploration", "🚀 Phase 2: Transition", "🏆 Phase 3: Mastery"])
    
    with phase1:
        st.markdown("### 🌱 **PHASE 1: Exploration & Foundation (Months 1-12)**")
        st.markdown("*Cel: Validate new direction i build foundation bez burning bridges*")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **🔍 Market Research & Validation**
            - Deep dive into target industry/role
            - Informational interviews z professionals (50+)
            - Shadow professionals w target roles
            - Analyze market demand i salary expectations
            
            **📚 Skill Building Foundation**
            - Complete foundational courses w new domain
            - Build basic portfolio/projects
            - Start networking w target industry
            - Attend industry events i conferences
            
            **💼 Current Role Optimization**
            - Excel w current role dla strong references
            - Identify transferable skills i experiences
            - Take on projects aligned z new direction
            - Build internal support network
            
            **🎯 Personal Branding Start**
            - Create content bridging current → target domain
            - Start building online presence w new field
            - Join professional associations
            - Begin thought leadership journey
            """)
        
        with col2:
            st.markdown("**📊 Key Metrics:**")
            st.markdown("""
            - 50+ industry conversations
            - 3+ foundational certifications
            - Basic portfolio ready
            - 100+ new network connections
            - Strong performance w current role
            """)
            
            st.markdown("**⚠️ Risk Mitigation:**")
            st.markdown("""
            - Keep current job stable
            - Build emergency fund (6+ months)
            - Maintain current network
            - Gradual transition approach
            """)
    
    with phase2:
        st.markdown("### 🚀 **PHASE 2: Strategic Transition (Months 13-24)**")
        st.markdown("*Cel: Active transition z calculated risks i strong preparation*")
        
        st.markdown("""
        **🎯 Advanced Skill Development**
        - Complete advanced certifications w target domain
        - Build substantial portfolio demonstrating expertise
        - Gain practical experience through freelancing/consulting
        - Develop specialized expertise w AI-enhanced workflows
        
        **🌐 Strategic Positioning**
        - Position yourself as "hybrid expert" (current + new domain)
        - Leverage unique background jako competitive advantage
        - Build reputation jako bridge between industries
        - Establish thought leadership w niche intersection
        
        **💼 Transition Strategy Execution**
        - **Option A: Internal Transfer** - Move within current company
        - **Option B: Gradual Shift** - Consulting while employed
        - **Option C: Strategic Jump** - Direct role change
        - **Option D: Entrepreneurial** - Start own venture
        
        **📈 Market Testing**
        - Apply dla target roles (gauge market response)
        - Complete freelance/consulting projects
        - Measure market value of your unique profile
        - Adjust strategy based na real market feedback
        """)
    
    with phase3:
        st.markdown("### 🏆 **PHASE 3: Excellence & Leadership (Months 25-36)**")
        st.markdown("*Cel: Establish yourself jako leader w new domain*")
        
        st.markdown("""
        **🚀 Domain Mastery**
        - Achieve expert-level competency w new field
        - Develop proprietary methodologies or frameworks
        - Become go-to person dla specific expertise
        - Build reputation jako innovation leader
        
        **👥 Leadership Development**
        - Take on leadership responsibilities w new domain
        - Mentor others making similar transitions
        - Drive strategic initiatives w new field
        - Build i lead cross-functional teams
        
        **🌟 Market Recognition**
        - Speaking engagements at major conferences
        - Published articles w industry publications
        - Industry awards or recognition
        - Advisor/board positions
        
        **💡 Future Vision**
        - Develop 10-year strategic vision dla career
        - Plan dla next level advancement (C-suite, entrepreneurship)
        - Build sustainable competitive advantages
        - Create multiple career option paths
        """)
    
    # Risk vs Reward Analysis
    st.markdown("### ⚖️ Risk vs Reward Analysis dla Career Pivot")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🔴 **RISKS**")
        st.markdown("""
        - **Financial:** Potential income dip during transition
        - **Professional:** Loss of seniority/expertise
        - **Network:** Starting over w new industry
        - **Time:** 2-3 years of intensive effort
        - **Uncertainty:** Market changes during transition
        """)
    
    with col2:
        st.markdown("#### 🟡 **MITIGATION**")
        st.markdown("""
        - **Emergency fund:** 12+ months expenses
        - **Gradual transition:** Overlap periods
        - **Bridge strategy:** Hybrid positioning
        - **Continuous learning:** Stay adaptable
        - **Multiple options:** Plan A, B, C ready
        """)
    
    with col3:
        st.markdown("#### 🟢 **REWARDS**")
        st.markdown("""
        - **Fulfillment:** Work aligned z passion
        - **Growth:** Accelerated learning curve
        - **Uniqueness:** Rare skill combination
        - **Future-proofing:** AI-era relevance
        - **Leadership:** Pioneer w intersection
        """)

def show_recommendations():
    """Enhanced recommendations with strategic context"""
    st.markdown("# 🎯 Strategiczne Rekomendacje Kariery")
    
    if 'analysis_results' not in st.session_state:
        st.error("Brak danych analizy.")
        return
    
    recommendations = st.session_state.analysis_results['career_recommendations']
    
    # Strategic context
    st.markdown("""
    <div style="background: linear-gradient(135deg, #00b894 0%, #00a085 100%); 
                padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px;">
    <h3>🎯 Kontekst Strategiczny</h3>
    <p>Rekomendacje uwzględniają Twój profil psychologiczny, trendy rynkowe, wpływ AI i przyszłość poszczególnych ról</p>
    </div>
    """, unsafe_allow_html=True)
    
    for i, rec in enumerate(recommendations, 1):
        with st.expander(f"🎯 {rec['title']} - Match: {rec['match_score']:.0f}%", expanded=(i==1)):
            
            # Enhanced recommendation details
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"### 📋 Szczegółowa Analiza")
                st.write(f"**Opis roli:** {rec['description']}")
                
                # Strategic fit analysis
                strategic_fit = analyze_strategic_fit(rec['title'], st.session_state.analysis_results)
                
                st.markdown(f"**🎯 Dlaczego to idealne dopasowanie:**")
                st.markdown(strategic_fit['fit_reasons'])
                
                st.markdown(f"**🚀 Twoja unikalna przewaga:**")
                st.info(strategic_fit['unique_advantage'])
                
                st.markdown(f"**🛣️ Konkretna ścieżka rozwoju:**")
                st.markdown(strategic_fit['development_path'])
                
                # AI Impact Context
                ai_context = get_career_ai_impact(rec['title'])
                st.markdown(f"**🤖 Wpływ AI na tę rolę:**")
                st.markdown(f"• Automation Risk: {ai_context['automation_risk']}%")
                st.markdown(f"• AI Enhancement Potential: {ai_context['ai_enhancement']}%")
                st.markdown(f"• Future Outlook: {ai_context['future_outlook'][:100]}...")
            
            with col2:
                # Key metrics
                st.metric("Match Score", f"{rec['match_score']:.0f}%")
                st.metric("Growth Potential", f"{rec['growth_potential']}%")
                st.metric("AI Resistance", f"{100-get_career_ai_impact(rec['title'])['automation_risk']}%")
                
                # Salary progression
                st.markdown("**💰 Salary Progression:**")
                min_sal, max_sal = rec['salary_range']
                st.markdown(f"• Entry: ${min_sal:,}")
                st.markdown(f"• Senior: ${int(max_sal*1.3):,}")
                st.markdown(f"• Expert: ${int(max_sal*1.8):,}")
                
                # Time to competency
                st.markdown("**⏱️ Timeline:**")
                st.markdown("• Basic: 3-6 miesięcy")
                st.markdown("• Proficient: 12-18 miesięcy") 
                st.markdown("• Expert: 2-3 lata")
                
                # Skills breakdown
                st.markdown("**🎯 Key Skills:**")
                for skill in rec['skills']:
                    st.markdown(f"• {skill}")

def analyze_strategic_fit(career_title, analysis_results):
    """Analiza strategicznego dopasowania do kariery"""
    
    strategic_analyses = {
        'Product Manager': {
            'fit_reasons': """
            • **Strategic Thinking**: Twój profil wskazuje na naturalne predyspozycje do big-picture thinking
            • **Cross-functional Leadership**: Idealne dla osób łączących technical understanding z business acumen  
            • **User-Centric Approach**: Alignment z Twoją ugodowością i empathy
            • **Data-Driven Decisions**: Matches Twoje analytical strengths
            """,
            'unique_advantage': 'W erze AI, Product Managers muszą rozumieć zarówno human needs jak i AI capabilities. Twój balanced profile pozwala na bridging tego gap - jesteś natural translator między technical possibilities a human desires.',
            'development_path': """
            **Phase 1 (0-6 months):** Complete Google PM Certificate + build 2 product case studies  
            **Phase 2 (6-12 months):** Join product community, mentorship, intern/volunteer PM work  
            **Phase 3 (12-18 months):** Apply dla Associate PM roles, leverage unique background  
            **Advanced:** Specialize w AI Product Management - huge opportunity!
            """
        },
        'Data Scientist': {
            'fit_reasons': """
            • **Analytical Mindset**: Strong conscientiousness suggests systematic approach to analysis
            • **Problem-Solving**: Natural curiosity i openness to new methods
            • **Pattern Recognition**: Combines logical thinking z creative insights
            • **Continuous Learning**: Growth-oriented personality thrives w evolving field
            """,
            'unique_advantage': 'Data Science w erze AI shifts od pure technical skills do domain expertise + AI collaboration. Twoje background daje Ci context którego brakowo pure technical specialists.',
            'development_path': """
            **Phase 1:** Python/R + SQL fundamentals + statistics refresher (3 months)  
            **Phase 2:** Machine Learning + portfolio projects + Kaggle competitions (6 months)  
            **Phase 3:** Domain specialization + AI/LLM integration + job applications (6 months)  
            **Future:** Evolve into AI Engineering lub domain-specific AI consultant
            """
        },
        'UX Designer': {
            'fit_reasons': """
            • **Human-Centered Thinking**: High agreeableness suggests natural empathy dla users
            • **Creative Problem-Solving**: Openness to experience supports design thinking
            • **Systematic Approach**: Conscientiousness helps w research i testing methodologies
            • **Communication Skills**: Essential dla stakeholder management i user advocacy
            """,
            'unique_advantage': 'UX w AI era becomes more about designing human-AI interactions. Twoje understanding of both human psychology i systematic processes positions you perfectly dla emerging field of AI UX.',
            'development_path': """
            **Phase 1:** UX fundamentals + design tools + first portfolio pieces (4 months)  
            **Phase 2:** Advanced UX research + interaction design + real client projects (8 months)  
            **Phase 3:** AI/ML UX specialization + thought leadership + job search (6 months)  
            **Specialization:** Pioneer w Conversational AI UX lub AI Ethics Design
            """
        },
        'Strategy Consultant': {
            'fit_reasons': """
            • **Systems Thinking**: Natural ability to see connections i big picture
            • **Analytical Rigor**: Strong problem-solving skills i logical reasoning
            • **Communication Excellence**: Can distill complex ideas into clear recommendations
            • **Adaptability**: Thrives w diverse client environments i challenge variety
            """,
            'unique_advantage': 'Strategy Consulting w AI era requires professionals who can help organizations navigate AI transformation. Twoje combination of strategic thinking + AI awareness makes you ideal dla this emerging niche.',
            'development_path': """
            **Phase 1:** Case study practice + business fundamentals + consulting skills (6 months)  
            **Phase 2:** Apply do consulting firms or boutiques + build track record (12 months)  
            **Phase 3:** Develop AI strategy specialization + thought leadership (12 months)  
            **Leadership:** Launch own AI strategy consulting lub join top-tier firm
            """
        }
    }
    
    return strategic_analyses.get(career_title, {
        'fit_reasons': 'Strategic analysis dostępna po pogłębieniu profilu zawodowego.',
        'unique_advantage': 'Twój unique background tworzy interesting opportunities w tej dziedzinie.',
        'development_path': 'Standardowa ścieżka rozwoju z focus na AI integration i future trends.'
    })# app.py - Celestynka - Kompletna standalone aplikacja
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import json

# Konfiguracja strony
st.set_page_config(
    page_title="Celestynka",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #1e3c72;
        margin-bottom: 1rem;
    }
    
    .recommendation-card {
        background: #f8f9ff;
        border: 1px solid #1e3c72;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .step-container {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Simple Big Five Analyzer
class BigFiveAnalyzer:
    def analyze(self, scores):
        profile = {}
        trait_names = {
            'extraversion': 'Ekstrawersja',
            'agreeableness': 'Ugodowość', 
            'conscientiousness': 'Sumienność',
            'emotional_stability': 'Stabilność Emocjonalna',
            'openness': 'Otwartość'
        }
        
        for trait, score in scores.items():
            level = 'high' if score > 3.5 else 'medium' if score > 2.5 else 'low'
            profile[trait] = {
                'score': score,
                'level': level,
                'percentile': int((score / 5.0) * 100)
            }
        
        return profile

# Simple Career Analysis Engine
class CareerAnalysisEngine:
    def __init__(self):
        self.careers = {
            'Product Manager': {
                'match_factors': {'extraversion': 3.5, 'conscientiousness': 4.0, 'openness': 3.5},
                'salary_range': (120000, 200000),
                'growth_potential': 95,
                'skills': ['Strategic thinking', 'Leadership', 'Communication', 'Data analysis']
            },
            'Data Scientist': {
                'match_factors': {'conscientiousness': 4.0, 'openness': 4.0},
                'salary_range': (110000, 190000),
                'growth_potential': 98,
                'skills': ['Programming', 'Statistics', 'Machine learning', 'Analysis']
            },
            'UX Designer': {
                'match_factors': {'openness': 4.5, 'agreeableness': 3.5},
                'salary_range': (90000, 150000),
                'growth_potential': 88,
                'skills': ['Design thinking', 'User research', 'Prototyping', 'Communication']
            },
            'Strategy Consultant': {
                'match_factors': {'extraversion': 3.5, 'conscientiousness': 4.0, 'openness': 3.5},
                'salary_range': (100000, 180000),
                'growth_potential': 92,
                'skills': ['Problem solving', 'Client management', 'Business analysis']
            }
        }
    
    def analyze(self, personality_profile):
        recommendations = []
        
        for career, data in self.careers.items():
            match_score = self.calculate_match(personality_profile, data['match_factors'])
            
            recommendations.append({
                'title': career,
                'match_score': round(match_score, 1),
                'salary_range': data['salary_range'],
                'growth_potential': data['growth_potential'],
                'skills': data['skills'],
                'description': f"Kariera w {career} - dopasowanie {match_score:.0f}%"
            })
        
        return sorted(recommendations, key=lambda x: x['match_score'], reverse=True)
    
    def calculate_match(self, personality, factors):
        total_score = 0
        for trait, required_score in factors.items():
            if trait in personality:
                user_score = personality[trait]['score']
                # Calculate fit (closer to required = higher score)
                fit = max(0, 100 - abs(user_score - required_score) * 20)
                total_score += fit
        
        return total_score / len(factors) if factors else 50

# Visualization functions
def create_big_five_radar(personality_profile):
    traits = ['Ekstrawersja', 'Ugodowość', 'Sumienność', 'Stabilność Emocjonalna', 'Otwartość']
    
    trait_mapping = {
        'Ekstrawersja': 'extraversion',
        'Ugodowość': 'agreeableness', 
        'Sumienność': 'conscientiousness',
        'Stabilność Emocjonalna': 'emotional_stability',
        'Otwartość': 'openness'
    }
    
    scores = []
    for trait in traits:
        trait_key = trait_mapping[trait]
        if trait_key in personality_profile:
            scores.append(personality_profile[trait_key]['score'])
        else:
            scores.append(3.0)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=traits,
        fill='toself',
        fillcolor='rgba(30, 60, 114, 0.25)',
        line=dict(color='#1e3c72', width=3),
        name='Twój Profil'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickmode='linear',
                tick0=0,
                dtick=1
            )
        ),
        title="Profil Osobowości Big Five",
        height=500
    )
    
    return fig

def create_career_chart(recommendations):
    careers = [r['title'] for r in recommendations[:5]]
    scores = [r['match_score'] for r in recommendations[:5]]
    
    fig = go.Figure(go.Bar(
        x=scores,
        y=careers,
        orientation='h',
        marker=dict(color='#1e3c72'),
        text=[f'{score:.0f}%' for score in scores],
        textposition='auto'
    ))
    
    fig.update_layout(
        title="Dopasowanie do Ścieżek Kariery",
        xaxis=dict(title='Match Score (%)', range=[0, 100]),
        height=400
    )
    
    return fig

# Inicjalizacja session state
def init_session_state():
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 1
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    if 'analysis_complete' not in st.session_state:
        st.session_state.analysis_complete = False

def main():
    init_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🧠 Celestynka</h1>
        <p>Zaawansowana analiza psychologiczno-biznesowa kariery</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.markdown("## 🧭 Nawigacja")
    
    if st.session_state.analysis_complete:
        page = st.sidebar.selectbox(
            "Wybierz sekcję:",
            ["📊 Dashboard", "🔮 Analiza Strategiczna", "🤖 AI Impact Analysis", "🎯 Rekomendacje", "🛣️ Ścieżki Rozwoju", "📄 Raport", "🔄 Nowa Analiza"]
        )
    else:
        page = "📝 Analiza"
        st.sidebar.info("Wypełnij analizę, aby odblokować wszystkie funkcje")
    
    # Routing
    if page == "📝 Analiza" or not st.session_state.analysis_complete:
        show_analysis_form()
    elif page == "📊 Dashboard":
        show_dashboard()
    elif page == "🔮 Analiza Strategiczna":
        show_strategic_analysis()
    elif page == "🤖 AI Impact Analysis":
        show_ai_impact_analysis()
    elif page == "🎯 Rekomendacje":
        show_recommendations()
    elif page == "🛣️ Ścieżki Rozwoju":
        show_development_paths()
    elif page == "📄 Raport":
        show_report()
    elif page == "🔄 Nowa Analiza":
        reset_analysis()

def show_analysis_form():
    """Formularz analizy"""
    total_steps = 5
    progress = st.session_state.current_step / total_steps
    
    st.progress(progress)
    st.markdown(f"**Krok {st.session_state.current_step} z {total_steps}**")
    
    with st.container():
        st.markdown('<div class="step-container">', unsafe_allow_html=True)
        
        if st.session_state.current_step == 1:
            show_step_basic_info()
        elif st.session_state.current_step == 2:
            show_step_big_five()
        elif st.session_state.current_step == 3:
            show_step_motivation()
        elif st.session_state.current_step == 4:
            show_step_goals()
        elif st.session_state.current_step == 5:
            show_results()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.current_step > 1:
            if st.button("⬅️ Poprzedni", use_container_width=True):
                st.session_state.current_step -= 1
                st.rerun()
    
    with col3:
        if st.session_state.current_step < total_steps:
            if st.button("Następny ➡️", use_container_width=True):
                st.session_state.current_step += 1
                st.rerun()
        else:
            if st.button("🚀 Zobacz Wyniki", use_container_width=True, type="primary"):
                generate_analysis()
                st.session_state.analysis_complete = True
                st.rerun()

def show_step_basic_info():
    st.markdown("## 👤 Podstawowe Informacje")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Imię", value=st.session_state.user_data.get('name', ''))
        st.session_state.user_data['name'] = name
        
        position = st.text_input("Obecna pozycja", value=st.session_state.user_data.get('position', ''))
        st.session_state.user_data['position'] = position
    
    with col2:
        experience = st.selectbox(
            "Doświadczenie zawodowe",
            ["0-1 lat", "2-3 lata", "4-6 lat", "7-10 lat", "10+ lat"],
            index=0
        )
        st.session_state.user_data['experience'] = experience
        
        education = st.text_input("Wykształcenie", value=st.session_state.user_data.get('education', ''))
        st.session_state.user_data['education'] = education

def show_step_big_five():
    st.markdown("## 🧬 Test Osobowości Big Five")
    st.info("Oceń jak bardzo zgadzasz się z każdym stwierdzeniem w skali 1-5")
    
    # Ekstrawersja
    st.markdown("### 🎯 Ekstrawersja")
    ext1 = st.slider("Czuję się energetycznie po spotkaniach z ludźmi", 1, 5, 3, key="ext1")
    ext2 = st.slider("Lubię być w centrum uwagi", 1, 5, 3, key="ext2")
    extraversion = (ext1 + ext2) / 2
    
    # Ugodowość
    st.markdown("### 🤝 Ugodowość")
    agr1 = st.slider("Łatwo mi współczuć problemom innych", 1, 5, 3, key="agr1")
    agr2 = st.slider("Preferuję kompromis nad konfliktem", 1, 5, 3, key="agr2")
    agreeableness = (agr1 + agr2) / 2
    
    # Sumienność
    st.markdown("### 📋 Sumienność")
    con1 = st.slider("Zawsze kończę projekty przed deadline", 1, 5, 3, key="con1")
    con2 = st.slider("Mam uporządkowane miejsce pracy", 1, 5, 3, key="con2")
    conscientiousness = (con1 + con2) / 2
    
    # Stabilność emocjonalna
    st.markdown("### 🧘 Stabilność Emocjonalna")
    emo1 = st.slider("Dobrze radzę sobie ze stresem", 1, 5, 3, key="emo1")
    emo2 = st.slider("Rzadko się denerwuję", 1, 5, 3, key="emo2")
    emotional_stability = (emo1 + emo2) / 2
    
    # Otwartość
    st.markdown("### 🎨 Otwartość na Doświadczenia")
    ope1 = st.slider("Lubię eksperymentować z nowymi sposobami", 1, 5, 3, key="ope1")
    ope2 = st.slider("Interesują mnie abstrakcyjne koncepcje", 1, 5, 3, key="ope2")
    openness = (ope1 + ope2) / 2
    
    st.session_state.user_data['big_five'] = {
        'extraversion': extraversion,
        'agreeableness': agreeableness,
        'conscientiousness': conscientiousness,
        'emotional_stability': emotional_stability,
        'openness': openness
    }

def show_step_motivation():
    st.markdown("## 🚀 Motywacja i Wartości")
    
    energy_sources = st.multiselect(
        "Co daje Ci największą energię w pracy? (wybierz 3-5)",
        [
            "Rozwiązywanie problemów",
            "Pomaganie innym",
            "Tworzenie nowych rzeczy",
            "Praca w zespole",
            "Autonomia",
            "Uczenie się",
            "Osiąganie celów",
            "Uznanie"
        ]
    )
    st.session_state.user_data['energy_sources'] = energy_sources
    
    st.markdown("### 💰 Priorytet: Zarobki")
    salary_importance = st.slider("Jak ważne są wysokie zarobki?", 1, 10, 5)
    
    st.markdown("### ⚖️ Priorytet: Work-Life Balance")
    balance_importance = st.slider("Jak ważny jest work-life balance?", 1, 10, 7)
    
    st.markdown("### 🎯 Priorytet: Rozwój")
    growth_importance = st.slider("Jak ważny jest rozwój osobisty?", 1, 10, 8)
    
    st.session_state.user_data['priorities'] = {
        'salary': salary_importance,
        'balance': balance_importance,
        'growth': growth_importance
    }

def show_step_goals():
    st.markdown("## 🎯 Cele i Aspiracje")
    
    ideal_role = st.text_area(
        "Opisz swoją wymarzoną pracę:",
        placeholder="Co robiłabyś w idealnej pracy? Jak wyglądałby Twój dzień?"
    )
    st.session_state.user_data['ideal_role'] = ideal_role
    
    timeline = st.selectbox(
        "W jakim horyzoncie plansujesz zmianę kariery?",
        ["Natychmiast", "3-6 miesięcy", "6-12 miesięcy", "1-2 lata", "2+ lata"]
    )
    st.session_state.user_data['timeline'] = timeline
    
    interests = st.multiselect(
        "Które obszary Cię interesują?",
        [
            "Technologia", "Marketing", "Finanse", "HR",
            "Sprzedaż", "Operacje", "Strategia", "Design",
            "Analiza danych", "Zarządzanie projektami"
        ]
    )
    st.session_state.user_data['interests'] = interests

def show_results():
    st.markdown("## 🎉 Przygotowanie Analizy")
    
    st.success("Gratulacje! Wypełniłaś wszystkie sekcje analizy.")
    
    st.markdown("### 📊 Podsumowanie Twoich Odpowiedzi:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Podstawowe Info:**")
        st.write(f"• Imię: {st.session_state.user_data.get('name', 'N/A')}")
        st.write(f"• Pozycja: {st.session_state.user_data.get('position', 'N/A')}")
        st.write(f"• Doświadczenie: {st.session_state.user_data.get('experience', 'N/A')}")
    
    with col2:
        if 'big_five' in st.session_state.user_data:
            st.markdown("**Profil Big Five:**")
            big_five = st.session_state.user_data['big_five']
            for trait, score in big_five.items():
                st.write(f"• {trait.title()}: {score:.1f}/5")
    
    st.markdown("**Źródła energii:**")
    energy_sources = st.session_state.user_data.get('energy_sources', [])
    if energy_sources:
        st.write(", ".join(energy_sources))
    
    st.info("Kliknij 'Zobacz Wyniki' aby wygenerować swoją analizę kariery!")

def generate_analysis():
    """Generowanie analizy"""
    with st.spinner("🔄 Generuję analizę..."):
        # Initialize analyzers
        big_five_analyzer = BigFiveAnalyzer()
        career_engine = CareerAnalysisEngine()
        
        # Analyze personality
        big_five_data = st.session_state.user_data.get('big_five', {})
        personality_profile = big_five_analyzer.analyze(big_five_data)
        
        # Generate career recommendations
        career_recommendations = career_engine.analyze(personality_profile)
        
        # Store results
        st.session_state.analysis_results = {
            'personality_profile': personality_profile,
            'career_recommendations': career_recommendations,
            'generated_at': datetime.now().isoformat()
        }

def show_dashboard():
    st.markdown("# 📊 Dashboard Analizy Kariery")
    
    if 'analysis_results' not in st.session_state:
        st.error("Brak danych analizy. Proszę najpierw wypełnić formularz.")
        return
    
    results = st.session_state.analysis_results
    
    # Metryki
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🎯 Top Match", f"{results['career_recommendations'][0]['match_score']:.0f}%")
    with col2:
        st.metric("💰 Avg Salary", f"${np.mean([r['salary_range'] for r in results['career_recommendations'][:3]], axis=0)[0]/1000:.0f}k")
    with col3:
        st.metric("📈 Growth Potential", f"{np.mean([r['growth_potential'] for r in results['career_recommendations'][:3]]):.0f}%")
    with col4:
        st.metric("🧠 Profile Score", f"{np.mean(list(results['personality_profile'][trait]['score'] for trait in results['personality_profile'])):.1f}/5")
    
    # Wykresy
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("## 🧬 Profil Osobowości")
        radar_chart = create_big_five_radar(results['personality_profile'])
        st.plotly_chart(radar_chart, use_container_width=True)
    
    with col2:
        st.markdown("## 🎯 Dopasowanie Kariery")
        career_chart = create_career_chart(results['career_recommendations'])
        st.plotly_chart(career_chart, use_container_width=True)

def show_recommendations():
    st.markdown("# 🎯 Rekomendacje Kariery")
    
    if 'analysis_results' not in st.session_state:
        st.error("Brak danych analizy.")
        return
    
    recommendations = st.session_state.analysis_results['career_recommendations']
    
    for i, rec in enumerate(recommendations, 1):
        with st.expander(f"🎯 {rec['title']} - Match: {rec['match_score']:.0f}%", expanded=(i==1)):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**Opis:** {rec['description']}")
                st.write(f"**Kluczowe umiejętności:** {', '.join(rec['skills'])}")
            
            with col2:
                st.metric("Match Score", f"{rec['match_score']:.0f}%")
                st.metric("Growth Potential", f"{rec['growth_potential']}%")
                st.write(f"**Zarobki:** ${rec['salary_range'][0]:,} - ${rec['salary_range'][1]:,}")

def show_report():
    st.markdown("# 📄 Raport Analizy")
    
    if 'analysis_results' not in st.session_state:
        st.error("Brak danych analizy.")
        return
    
    name = st.session_state.user_data.get('name', 'Użytkownik')
    
    # Executive Summary
    st.markdown("## 📊 Executive Summary")
    
    top_career = st.session_state.analysis_results['career_recommendations'][0]
    
    st.markdown(f"""
    **Profil:** {name}
    
    **Top rekomendacja:** {top_career['title']} ({top_career['match_score']:.0f}% dopasowanie)
    
    **Kluczowe mocne strony osobowości:**
    """)
    
    personality = st.session_state.analysis_results['personality_profile']
    for trait, data in personality.items():
        if data['score'] >= 4.0:
            st.write(f"• {trait.title()}: {data['score']:.1f}/5 ({data['level']})")
    
    # Detailed recommendations
    st.markdown("## 🎯 Szczegółowe Rekomendacje")
    
    for rec in st.session_state.analysis_results['career_recommendations'][:3]:
        st.markdown(f"""
        ### {rec['title']}
        - **Match Score:** {rec['match_score']:.0f}%
        - **Growth Potential:** {rec['growth_potential']}%
        - **Salary Range:** ${rec['salary_range'][0]:,} - ${rec['salary_range'][1]:,}
        - **Key Skills:** {', '.join(rec['skills'])}
        """)
    
    # Download button (mock)
    if st.button("📥 Pobierz Pełny Raport PDF"):
        st.success("✅ Raport został wygenerowany! (W pełnej wersji byłby dostępny do pobrania)")

def reset_analysis():
    st.markdown("# 🔄 Nowa Analiza")
    
    if st.button("🗑️ Resetuj wszystkie dane", type="primary"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.success("✅ Dane zostały zresetowane!")
        st.rerun()

if __name__ == "__main__":
    main()
