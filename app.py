# app.py - CareerScope Pro - Kompletna standalone aplikacja
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import json

# Konfiguracja strony
st.set_page_config(
    page_title="CareerScope Pro",
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
        <h1>🧠 CareerScope Pro</h1>
        <p>Zaawansowana analiza psychologiczno-biznesowa kariery</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.markdown("## 🧭 Nawigacja")
    
    if st.session_state.analysis_complete:
        page = st.sidebar.selectbox(
            "Wybierz sekcję:",
            ["📊 Dashboard", "🎯 Rekomendacje", "📄 Raport", "🔄 Nowa Analiza"]
        )
    else:
        page = "📝 Analiza"
        st.sidebar.info("Wypełnij analizę, aby odblokować wszystkie funkcje")
    
    # Routing
    if page == "📝 Analiza" or not st.session_state.analysis_complete:
        show_analysis_form()
    elif page == "📊 Dashboard":
        show_dashboard()
    elif page == "🎯 Rekomendacje":
        show_recommendations()
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
