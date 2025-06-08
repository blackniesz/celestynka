# app.py - Główna aplikacja Streamlit
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
import json

# Import własnych modułów z error handling
try:
    from psychology_models import BigFiveAnalyzer, MotivationAnalyzer, CognitiveProfiler
    from analysis_engine import CareerAnalysisEngine
    from report_generator import ReportGenerator
    from visualizations import CareerDashboard
except ImportError as e:
    st.error(f"Błąd importu modułów: {e}")
    st.info("Upewnij się, że wszystkie pliki są w tym samym folderze co app.py")

# Konfiguracja strony
st.set_page_config(
    page_title="CareerScope Pro",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS dla profesjonalnego wyglądu
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
    
    .personality-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        display: inline-block;
        font-weight: 600;
    }
    
    .recommendation-card {
        background: #f8f9ff;
        border: 1px solid #1e3c72;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .section-divider {
        height: 2px;
        background: linear-gradient(90deg, #1e3c72, #2a5298);
        margin: 2rem 0;
        border-radius: 1px;
    }
    
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #1e3c72, #2a5298);
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

# Inicjalizacja session state
def init_session_state():
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 1
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    if 'analysis_complete' not in st.session_state:
        st.session_state.analysis_complete = False
    if 'analysis_results' not in st.session_state:
        st.session_state.analysis_results = None

def main():
    init_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🧠 CareerScope Pro</h1>
        <p>Zaawansowana analiza psychologiczno-biznesowa kariery</p>
        <p><em>Powered by AI & Advanced Psychology Models</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Navigation
    st.sidebar.markdown("## 🧭 Nawigacja")
    
    if st.session_state.analysis_complete:
        page = st.sidebar.selectbox(
            "Wybierz sekcję:",
            ["📊 Dashboard", "🧠 Profil Psychologiczny", "🎯 Rekomendacje", 
             "📈 Plan Rozwoju", "📄 Raport PDF", "🔄 Nowa Analiza"]
        )
    else:
        page = "📝 Analiza"
        st.sidebar.info("Wypełnij analizę, aby odblokować wszystkie funkcje")
    
    # Routing
    if page == "📝 Analiza" or not st.session_state.analysis_complete:
        show_analysis_form()
    elif page == "📊 Dashboard":
        show_dashboard()
    elif page == "🧠 Profil Psychologiczny":
        show_psychology_profile()
    elif page == "🎯 Rekomendacje":
        show_recommendations()
    elif page == "📈 Plan Rozwoju":
        show_development_plan()
    elif page == "📄 Raport PDF":
        show_pdf_report()
    elif page == "🔄 Nowa Analiza":
        reset_analysis()

def show_analysis_form():
    """Wieloetapowy formularz analizy"""
    total_steps = 8
    progress = st.session_state.current_step / total_steps
    
    # Progress bar
    st.progress(progress)
    st.markdown(f"**Krok {st.session_state.current_step} z {total_steps}**")
    
    # Kontener dla kroku
    with st.container():
        st.markdown('<div class="step-container">', unsafe_allow_html=True)
        
        if st.session_state.current_step == 1:
            show_step_basic_info()
        elif st.session_state.current_step == 2:
            show_step_big_five()
        elif st.session_state.current_step == 3:
            show_step_motivation()
        elif st.session_state.current_step == 4:
            show_step_cognitive()
        elif st.session_state.current_step == 5:
            show_step_team_roles()
        elif st.session_state.current_step == 6:
            show_step_risk_profile()
        elif st.session_state.current_step == 7:
            show_step_competencies()
        elif st.session_state.current_step == 8:
            show_step_vision()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.current_step > 1:
            if st.button("⬅️ Poprzedni", use_container_width=True):
                st.session_state.current_step -= 1
                st.rerun()
    
    with col3:
        if st.session_state.current_step < total_steps:
            if st.button("Następny ➡️", use_container_width=True):
                if validate_current_step():
                    st.session_state.current_step += 1
                    st.rerun()
                else:
                    st.error("Proszę wypełnić wszystkie wymagane pola.")
        else:
            if st.button("🚀 Generuj Analizę", use_container_width=True, type="primary"):
                if validate_current_step():
                    generate_analysis()
                    st.session_state.analysis_complete = True
                    st.success("✅ Analiza została wygenerowana!")
                    st.rerun()

def show_step_basic_info():
    """Krok 1: Podstawowe informacje"""
    st.markdown("## 👤 Podstawowe Informacje")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Imię", value=st.session_state.user_data.get('name', ''))
        st.session_state.user_data['name'] = name
        
        position = st.text_input(
            "Obecna pozycja zawodowa", 
            value=st.session_state.user_data.get('position', '')
        )
        st.session_state.user_data['position'] = position
    
    with col2:
        experience = st.selectbox(
            "Lata doświadczenia zawodowego",
            ["0-1 lat", "2-3 lata", "4-6 lat", "7-10 lat", "Powyżej 10 lat"],
            index=0 if 'experience' not in st.session_state.user_data else 
                  ["0-1 lat", "2-3 lata", "4-6 lat", "7-10 lat", "Powyżej 10 lat"].index(st.session_state.user_data['experience'])
        )
        st.session_state.user_data['experience'] = experience
        
        education = st.text_input(
            "Wykształcenie/kierunek", 
            value=st.session_state.user_data.get('education', '')
        )
        st.session_state.user_data['education'] = education

def show_step_big_five():
    """Krok 2: Analiza Big Five"""
    st.markdown("## 🧬 Profil Osobowości (Big Five)")
    st.info("Oceń jak bardzo zgadzasz się z każdym stwierdzeniem w skali 1-5")
    
    # Ekstrawersja
    st.markdown("### 🎯 Ekstrawersja")
    ext_questions = [
        "Czuję się energetycznie po spotkaniach z ludźmi",
        "Preferuję pracę w zespole nad pracą samodzielną", 
        "Łatwo nawiązuję kontakty z nowymi ludźmi",
        "Lubię być w centrum uwagi"
    ]
    
    extraversion_scores = []
    for i, question in enumerate(ext_questions):
        score = st.slider(question, 1, 5, 3, key=f"ext_{i}")
        extraversion_scores.append(score)
    
    # Ugodowość
    st.markdown("### 🤝 Ugodowość")
    agr_questions = [
        "Unikam konfliktów, nawet kosztem swoich potrzeb",
        "Łatwo mi współczuć problemom innych ludzi",
        "Preferuję kompromis nad narzucaniem swojego zdania",
        "Mam tendencję do ufania ludziom"
    ]
    
    agreeableness_scores = []
    for i, question in enumerate(agr_questions):
        score = st.slider(question, 1, 5, 3, key=f"agr_{i}")
        agreeableness_scores.append(score)
    
    # Zapisz wyniki
    st.session_state.user_data['big_five'] = {
        'extraversion': np.mean(extraversion_scores),
        'agreeableness': np.mean(agreeableness_scores),
        # Dodaj pozostałe wymiary...
    }

def show_step_motivation():
    """Krok 3: Analiza motywacji"""
    st.markdown("## 🚀 Głębokie Motywatory i Wartości")
    
    st.markdown("### ⚡ Źródła Energii")
    energy_sources = st.multiselect(
        "Co daje Ci największą energię w pracy? (wybierz 3-5)",
        [
            "Rozwiązywanie skomplikowanych problemów",
            "Pomaganie innym ludziom",
            "Tworzenie czegoś nowego",
            "Optymalizacja procesów",
            "Budowanie relacji",
            "Uczenie się nowych rzeczy",
            "Osiąganie celów",
            "Współpraca w zespole",
            "Autonomia w działaniu",
            "Uznanie za osiągnięcia"
        ],
        default=st.session_state.user_data.get('energy_sources', [])
    )
    st.session_state.user_data['energy_sources'] = energy_sources

def show_step_cognitive():
    """Krok 4: Profil kognitywny"""
    st.markdown("## 🧠 Profil Kognitywny i Styl Myślenia")
    
    st.markdown("### 🔍 Styl Przetwarzania Informacji")
    processing_style = st.radio(
        "Jak najczęściej przetwarzasz informacje?",
        [
            "📋 Sekwencyjnie - krok po kroku, logicznie",
            "🌐 Holistycznie - widzę całościowy obraz",
            "👁️ Wizualnie - myślę obrazami i diagramami",
            "🤲 Praktycznie - uczę się przez działanie"
        ]
    )
    st.session_state.user_data['processing_style'] = processing_style

def show_step_team_roles():
    """Krok 5: Role zespołowe"""
    st.markdown("## 👥 Profil Zespołowy i Przywództwo")
    
    team_roles = st.multiselect(
        "Twoje naturalne role w zespole (wybierz 3):",
        [
            "🎯 Koordynator - moderuję dyskusje, dbam o cele",
            "🌱 Kreator - generuję nowe pomysły", 
            "🔍 Poszukiwacz zasobów - buduję sieci, zbieramy informacje",
            "⚙️ Realizator - przekształcam pomysły w działania",
            "✅ Finalizator - doprowadzam sprawy do końca"
        ],
        default=st.session_state.user_data.get('team_roles', [])
    )
    st.session_state.user_data['team_roles'] = team_roles

def show_step_risk_profile():
    """Krok 6: Profil ryzyka"""
    st.markdown("## ⚖️ Profil Ryzyka i Adaptacyjności")
    
    risk_tolerance = st.slider(
        "Tolerancja ryzyka zawodowego (1-10)",
        1, 10, 5,
        help="1 = Preferuję stabilność, 10 = Gotowość na wysokie ryzyko"
    )
    st.session_state.user_data['risk_tolerance'] = risk_tolerance

def show_step_competencies():
    """Krok 7: Kompetencje"""
    st.markdown("## 📈 Mapa Kompetencji i Rozwoju")
    
    achievements = st.text_area(
        "Opisz swoje 3 największe sukcesy zawodowe z ostatnich 3 lat",
        height=120
    )
    st.session_state.user_data['achievements'] = achievements

def show_step_vision():
    """Krok 8: Wizja przyszłości"""
    st.markdown("## 🔮 Wizja Przyszłości")
    
    ten_year_vision = st.text_area(
        "Opisz, jak wyglądałby Twój idealny dzień za 10 lat",
        height=120
    )
    st.session_state.user_data['ten_year_vision'] = ten_year_vision

def validate_current_step():
    """Walidacja obecnego kroku"""
    step = st.session_state.current_step
    
    if step == 1:
        return (st.session_state.user_data.get('name') and 
                st.session_state.user_data.get('position'))
    # Inne kroki zawsze są valide dla demo
    return True

def generate_analysis():
    """Generowanie kompletnej analizy"""
    with st.spinner("🔄 Generuję zaawansowaną analizę psychologiczno-biznesową..."):
        # Inicjalizacja modułów analizy
        big_five_analyzer = BigFiveAnalyzer()
        motivation_analyzer = MotivationAnalyzer()
        cognitive_profiler = CognitiveProfiler()
        analysis_engine = CareerAnalysisEngine()
        
        # Analiza Big Five (z mock data jeśli nie ma pełnych danych)
        big_five_data = st.session_state.user_data.get('big_five', {
            'extraversion': 3.5,
            'agreeableness': 3.8,
            'conscientiousness': 4.2,
            'emotional_stability': 3.9,
            'openness': 4.1
        })
        personality_profile = big_five_analyzer.analyze(big_five_data)
        
        # Analiza motywacji
        energy_sources = st.session_state.user_data.get('energy_sources', [])
        values_importance = {'autonomy': 8, 'mastery': 9, 'purpose': 7}  # Mock data
        motivation_profile = motivation_analyzer.analyze(energy_sources, values_importance)
        
        # Profil kognitywny
        processing_style = st.session_state.user_data.get('processing_style', 'Holistycznie')
        decision_style = 'Analitycznie'  # Mock
        cognitive_strengths = {'strategic': 8, 'creative': 7, 'analytical': 9}  # Mock
        cognitive_profile = cognitive_profiler.analyze(processing_style, decision_style, cognitive_strengths)
        
        # Kompleksowa analiza kariery
        career_analysis = analysis_engine.comprehensive_analysis(
            personality_profile,
            motivation_profile, 
            cognitive_profile,
            st.session_state.user_data
        )
        
        # Zapisanie wyników
        st.session_state.analysis_results = {
            'personality_profile': personality_profile,
            'motivation_profile': motivation_profile,
            'cognitive_profile': cognitive_profile,
            'career_analysis': career_analysis,
            'generated_at': datetime.now().isoformat()
        }

def show_dashboard():
    """Główny dashboard z metrykami"""
    if not st.session_state.analysis_results:
        st.error("Brak danych analizy. Proszę najpierw wypełnić formularz.")
        return
    
    st.markdown("# 📊 Dashboard Analizy Kariery")
    
    # Kluczowe metryki
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎯 Compatibility Score", "87%", "↗️ +5%")
    with col2:
        st.metric("📈 Growth Potential", "92%", "↗️ +12%")
    with col3:
        st.metric("⚖️ Risk Profile", "Medium", "→ stable")
    with col4:
        st.metric("🧠 Cognitive Fit", "95%", "↗️ +8%")
    
    # Wizualizacje
    dashboard = CareerDashboard()
    results = st.session_state.analysis_results
    
    # Big Five radar chart
    st.markdown("## 🧬 Profil Osobowości")
    big_five_chart = dashboard.create_big_five_radar(results['personality_profile'])
    st.plotly_chart(big_five_chart, use_container_width=True)
    
    # Rekomendowane ścieżki
    st.markdown("## 🛤️ Top Rekomendacje Kariery")
    career_paths = results['career_analysis']['recommended_paths']
    
    for i, path in enumerate(career_paths[:3]):
        with st.expander(f"🎯 {path['title']} - Match: {path['match_score']}%", expanded=(i==0)):
            col1, col2 = st.columns([2, 1])
            with col1:
                st.write(f"**Opis:** {path['description']}")
                st.write(f"**Dlaczego pasuje:** {path['reasoning']}")
            with col2:
                st.metric("Growth Potential", f"{path['growth_potential']}%")
                st.metric("Risk Level", path['risk_level'])

def show_psychology_profile():
    """Szczegółowy profil psychologiczny"""
    if not st.session_state.analysis_results:
        st.error("Brak danych analizy.")
        return
    
    st.markdown("# 🧠 Szczegółowy Profil Psychologiczny")
    
    profile = st.session_state.analysis_results['personality_profile']
    
    # Wyświetl interpretacje Big Five
    traits = {
        'Ekstrawersja': profile.get('extraversion', {}),
        'Ugodowość': profile.get('agreeableness', {}),
        'Sumienność': profile.get('conscientiousness', {}),
        'Stabilność Emocjonalna': profile.get('emotional_stability', {}),
        'Otwartość': profile.get('openness', {})
    }
    
    for trait_name, trait_data in traits.items():
        if isinstance(trait_data, dict) and 'score' in trait_data:
            st.markdown(f"### {trait_name}")
            score = trait_data['score']
            
            # Progress bar
            progress_html = f"""
            <div style="background: #e0e0e0; border-radius: 10px; height: 20px; margin: 10px 0;">
                <div style="background: linear-gradient(90deg, #1e3c72, #2a5298); 
                           width: {score*20}%; height: 100%; border-radius: 10px;
                           display: flex; align-items: center; justify-content: center;
                           color: white; font-weight: bold;">
                    {score:.1f}/5.0
                </div>
            </div>
            """
            st.markdown(progress_html, unsafe_allow_html=True)
            
            if 'description' in trait_data:
                st.write(f"**Interpretacja:** {trait_data['description']}")

def show_recommendations():
    """Dynamiczne rekomendacje kariery"""
    if not st.session_state.analysis_results:
        st.error("Brak danych analizy.")
        return
    
    st.markdown("# 🎯 Personalizowane Rekomendacje Kariery")
    
    # Filtry w sidebar
    st.sidebar.markdown("## 🔍 Filtry")
    industry_filter = st.sidebar.multiselect(
        "Branże",
        ["Technology", "Consulting", "Healthcare", "Finance"],
        default=["Technology", "Consulting"]
    )
    
    # Główne rekomendacje
    career_paths = st.session_state.analysis_results['career_analysis']['recommended_paths']
    
    for path in career_paths[:3]:
        st.markdown(f"""
        <div class="recommendation-card">
            <h3>🎯 {path['title']} - Match: {path['match_score']}%</h3>
            <p><strong>Opis:</strong> {path['description']}</p>
            <p><strong>Dlaczego pasuje:</strong> {path['reasoning']}</p>
            <p><strong>Rozwój:</strong> {path['development_path']}</p>
        </div>
        """, unsafe_allow_html=True)

def show_development_plan():
    """Plan rozwoju zawodowego"""
    st.markdown("# 📈 Plan Rozwoju Zawodowego")
    
    # Plan 90 dni
    st.markdown("## 🎯 Plan na Pierwsze 90 Dni")
    
    tab1, tab2, tab3 = st.tabs(["📅 Dni 1-30", "📅 Dni 31-60", "📅 Dni 61-90"])
    
    with tab1:
        st.markdown("""
        ### 🎯 Focus: Foundation & Assessment
        **Zadania:**
        - [ ] Skill gap analysis
        - [ ] Industry research
        - [ ] Network mapping
        - [ ] Learning plan creation
        
        **Milestone:** Complete comprehensive skills assessment
        """)
    
    with tab2:
        st.markdown("""
        ### 🎯 Focus: Skill Building
        **Zadania:**
        - [ ] Start online courses
        - [ ] Join professional groups
        - [ ] Begin side projects
        - [ ] Schedule informational interviews
        
        **Milestone:** Complete first certification
        """)
    
    with tab3:
        st.markdown("""
        ### 🎯 Focus: Application & Practice
        **Zadania:**
        - [ ] Apply learnings in current role
        - [ ] Build portfolio
        - [ ] Update LinkedIn/CV
        - [ ] First job applications
        
        **Milestone:** Portfolio ready, interviews scheduled
        """)

def show_pdf_report():
    """Generowanie raportu PDF"""
    st.markdown("# 📄 Kompletny Raport PDF")
    
    if st.button("📥 Generuj Raport PDF", type="primary"):
        with st.spinner("Generuję raport..."):
            # Mock PDF generation
            report_generator = ReportGenerator()
            
            if st.session_state.analysis_results:
                report_content = report_generator.generate_comprehensive_report(
                    st.session_state.analysis_results, 
                    st.session_state.user_data
                )
                
                st.success("✅ Raport został wygenerowany!")
                
                # Display preview
                st.markdown("## 👀 Podgląd Raportu")
                st.text_area("", report_content, height=300)
                
                # Mock download
                st.download_button(
                    "⬇️ Pobierz PDF",
                    data=report_content.encode(),
                    file_name="CareerScope_Report.txt",  # W rzeczywistości byłby PDF
                    mime="text/plain"
                )

def reset_analysis():
    """Reset analizy"""
    st.markdown("# 🔄 Nowa Analiza")
    
    if st.button("🗑️ Resetuj i zacznij od nowa", type="primary"):
        # Clear session state
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        
        st.success("✅ Dane zostały zresetowane!")
        st.rerun()

if __name__ == "__main__":
    main()
