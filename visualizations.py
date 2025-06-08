# visualizations.py - Interaktywne wizualizacje i dashboard
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Dict, List, Any

class CareerDashboard:
    """Klasa do tworzenia profesjonalnych wizualizacji dashboard"""
    
    def __init__(self):
        self.color_palette = {
            'primary': '#1e3c72',
            'secondary': '#2a5298', 
            'accent': '#667eea',
            'highlight': '#764ba2',
            'success': '#28a745',
            'warning': '#ffc107',
            'danger': '#dc3545',
            'info': '#17a2b8',
            'light': '#f8f9fa',
            'dark': '#343a40'
        }
        
        self.gradient_colors = [
            '#1e3c72', '#2a5298', '#667eea', '#764ba2'
        ]
    
    def create_big_five_radar(self, personality_profile: Dict) -> go.Figure:
        """Tworzenie zaawansowanego wykresu radarowego Big Five"""
        
        # Przygotowanie danych
        traits = ['Ekstrawersja', 'Ugodowość', 'Sumienność', 'Stabilność Emocjonalna', 'Otwartość']
        
        trait_mapping = {
            'Ekstrawersja': 'extraversion',
            'Ugodowość': 'agreeableness', 
            'Sumienność': 'conscientiousness',
            'Stabilność Emocjonalna': 'emotional_stability',
            'Otwartość': 'openness'
        }
        
        # Wyciągnij scores
        user_scores = []
        for trait in traits:
            trait_key = trait_mapping[trait]
            if trait_key in personality_profile and isinstance(personality_profile[trait_key], dict):
                score = personality_profile[trait_key].get('score', 3.0)
                user_scores.append(score)
            else:
                user_scores.append(3.0)
        
        # Średnie populacyjne dla porównania
        population_avg = [3.5, 3.4, 3.6, 3.3, 3.7]
        
        # Tworzenie wykresu
        fig = go.Figure()
        
        # User profile
        fig.add_trace(go.Scatterpolar(
            r=user_scores,
            theta=traits,
            fill='toself',
            fillcolor=f'rgba(30, 60, 114, 0.25)',
            line=dict(color=self.color_palette['primary'], width=3),
            marker=dict(size=10, color=self.color_palette['primary']),
            name='Twój Profil',
            hovertemplate='<b>%{theta}</b><br>Twój wynik: %{r:.1f}/5.0<extra></extra>'
        ))
        
        # Population average
        fig.add_trace(go.Scatterpolar(
            r=population_avg,
            theta=traits,
            fill='toself',
            fillcolor='rgba(150, 150, 150, 0.1)',
            line=dict(color='gray', width=2, dash='dash'),
            marker=dict(size=6, color='gray'),
            name='Średnia populacyjna',
            hovertemplate='<b>%{theta}</b><br>Średnia: %{r:.1f}/5.0<extra></extra>'
        ))
        
        # Ideal profile dla career success (research-based)
        ideal_profile = [3.8, 3.2, 4.2, 4.0, 3.9]
        fig.add_trace(go.Scatterpolar(
            r=ideal_profile,
            theta=traits,
            fill=None,
            line=dict(color=self.color_palette['success'], width=2, dash='dot'),
            marker=dict(size=8, color=self.color_palette['success']),
            name='Profil sukcesu zawodowego',
            hovertemplate='<b>%{theta}</b><br>Ideal dla sukcesu: %{r:.1f}/5.0<extra></extra>'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5],
                    tickmode='linear',
                    tick0=0,
                    dtick=1,
                    gridcolor='lightgray',
                    gridwidth=1
                ),
                angularaxis=dict(
                    tickfont=dict(size=12, color=self.color_palette['dark']),
                    gridcolor='lightgray'
                )
            ),
            showlegend=True,
            title=dict(
                text="Profil Osobowości Big Five",
                x=0.5,
                font=dict(size=18, color=self.color_palette['primary'], family="Arial Black")
            ),
            xaxis=dict(title='Horyzont Czasowy'),
            yaxis=dict(title='Zarobki (USD)', tickformat='$,.0f'),
            height=450,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        return fig
    
    def create_risk_opportunity_matrix(self, risk_analysis: Dict) -> go.Figure:
        """Macierz ryzyk i możliwości"""
        
        opportunities = risk_analysis.get('career_opportunities', [])
        threats = risk_analysis.get('potential_threats', [])
        
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=['🚀 Możliwości Zawodowe', '⚠️ Potencjalne Zagrożenia'],
            vertical_spacing=0.15
        )
        
        # Opportunities
        if opportunities:
            opp_names = [opp['type'] for opp in opportunities[:5]]
            opp_timeframes = [opp.get('timeframe', '6-12 miesięcy') for opp in opportunities[:5]]
            
            # Convert timeframes to numeric values for visualization
            timeframe_values = []
            for tf in opp_timeframes:
                if '3-6' in tf:
                    timeframe_values.append(4.5)
                elif '6-12' in tf:
                    timeframe_values.append(9)
                elif '12-18' in tf:
                    timeframe_values.append(15)
                elif '12-24' in tf:
                    timeframe_values.append(18)
                else:
                    timeframe_values.append(9)
            
            fig.add_trace(
                go.Bar(
                    x=opp_names,
                    y=timeframe_values,
                    name='Czas realizacji (miesiące)',
                    marker=dict(color=self.color_palette['success'], opacity=0.7),
                    hovertemplate='<b>%{x}</b><br>Czas realizacji: %{y} miesięcy<extra></extra>'
                ),
                row=1, col=1
            )
        
        # Threats
        if threats:
            threat_names = [threat['type'] for threat in threats[:5]]
            
            # Mock likelihood values
            likelihood_mapping = {'High': 3, 'Medium-High': 2.5, 'Medium': 2, 'Low': 1}
            threat_likelihoods = [likelihood_mapping.get(threat.get('likelihood', 'Medium'), 2) for threat in threats[:5]]
            
            fig.add_trace(
                go.Bar(
                    x=threat_names,
                    y=threat_likelihoods,
                    name='Prawdopodobieństwo',
                    marker=dict(color=self.color_palette['danger'], opacity=0.7),
                    hovertemplate='<b>%{x}</b><br>Prawdopodobieństwo: %{y}/3<extra></extra>'
                ),
                row=2, col=1
            )
        
        fig.update_layout(
            title=dict(
                text="Analiza Ryzyk i Możliwości Zawodowych",
                x=0.5,
                font=dict(size=18, color=self.color_palette['primary'], family="Arial Black")
            ),
            height=600,
            showlegend=False,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        return fig
    
    def create_competency_radar(self, user_data: Dict, recommended_paths: List[Dict]) -> go.Figure:
        """Radar chart kompetencji względem wymagań ról"""
        
        if not recommended_paths:
            return go.Figure().add_annotation(text="Brak danych o ścieżkach kariery")
        
        # Mock current competencies (w rzeczywistej aplikacji z user assessment)
        competencies = [
            'Strategic Thinking', 'Leadership', 'Communication', 
            'Data Analysis', 'Problem Solving', 'Project Management'
        ]
        
        current_levels = [7, 6, 8, 5, 7, 6]  # Mock user levels
        
        # Requirements dla top recommended path
        top_path = recommended_paths[0]
        required_skills = top_path.get('key_skills', [])
        
        # Map required skills to competencies (simplified)
        required_levels = []
        for comp in competencies:
            if any(skill.lower() in comp.lower() or comp.lower() in skill.lower() 
                   for skill in required_skills):
                required_levels.append(8)  # High requirement
            else:
                required_levels.append(6)  # Medium requirement
        
        fig = go.Figure()
        
        # Current competencies
        fig.add_trace(go.Scatterpolar(
            r=current_levels,
            theta=competencies,
            fill='toself',
            fillcolor=f'rgba(30, 60, 114, 0.3)',
            line=dict(color=self.color_palette['primary'], width=3),
            name='Twoje kompetencje',
            hovertemplate='<b>%{theta}</b><br>Twój poziom: %{r}/10<extra></extra>'
        ))
        
        # Required for target role
        fig.add_trace(go.Scatterpolar(
            r=required_levels,
            theta=competencies,
            fill='toself',
            fillcolor=f'rgba(40, 167, 69, 0.2)',
            line=dict(color=self.color_palette['success'], width=2, dash='dash'),
            name=f'Wymagania: {top_path["title"]}',
            hovertemplate='<b>%{theta}</b><br>Wymagany poziom: %{r}/10<extra></extra>'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10],
                    tickmode='linear',
                    tick0=0,
                    dtick=2
                )
            ),
            title=dict(
                text="Profil Kompetencji vs Wymagania Roli",
                x=0.5,
                font=dict(size=18, color=self.color_palette['primary'], family="Arial Black")
            ),
            height=500,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
            paper_bgcolor='white'
        )
        
        return fig['primary'], family="Arial Black")
            ),
            height=550,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.1,
                xanchor="center",
                x=0.5
            ),
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        return fig
    
    def create_motivation_chart(self, motivation_profile: Dict) -> go.Figure:
        """Zaawansowany wykres motywatorów z insights"""
        
        top_motivators = motivation_profile.get('top_motivators', [])
        
        if not top_motivators:
            # Fallback data
            motivators = ['Autonomy', 'Mastery', 'Purpose', 'Achievement', 'Affiliation']
            scores = [85, 78, 72, 68, 55]
            strength_levels = ['Bardzo silny', 'Silny', 'Silny', 'Umiarkowany', 'Słaby']
        else:
            motivators = [m.get('name', '').title() for m in top_motivators]
            scores = [m.get('score', 0.5) * 100 for m in top_motivators]
            strength_levels = [m.get('strength_level', 'Umiarkowany') for m in top_motivators]
        
        # Color mapping based on strength
        color_mapping = {
            'Bardzo silny': self.color_palette['success'],
            'Silny': self.color_palette['primary'],
            'Umiarkowany': self.color_palette['warning'],
            'Słaby': self.color_palette['danger']
        }
        
        colors = [color_mapping.get(level, self.color_palette['info']) for level in strength_levels]
        
        # Tworzenie horizontal bar chart
        fig = go.Figure(go.Bar(
            y=motivators,
            x=scores,
            orientation='h',
            marker=dict(
                color=colors,
                line=dict(color='white', width=2)
            ),
            text=[f'{score:.0f}%' for score in scores],
            textposition='auto',
            textfont=dict(color='white', size=12, family="Arial Black"),
            hovertemplate='<b>%{y}</b><br>Siła motywacji: %{x:.0f}%<br>Poziom: %{customdata}<extra></extra>',
            customdata=strength_levels
        ))
        
        fig.update_layout(
            title=dict(
                text="Profil Motywacyjny - Główne Drivers",
                x=0.5,
                font=dict(size=18, color=self.color_palette['primary'], family="Arial Black")
            ),
            xaxis=dict(
                title='Siła Motywacji (%)', 
                range=[0, 100],
                gridcolor='lightgray',
                tickfont=dict(size=11)
            ),
            yaxis=dict(
                title='',
                tickfont=dict(size=12, color=self.color_palette['dark'])
            ),
            height=400,
            showlegend=False,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        # Dodaj annotations dla interpretacji
        for i, (score, level) in enumerate(zip(scores, strength_levels)):
            if score >= 80:
                annotation_text = "🚀"
            elif score >= 60:
                annotation_text = "✅"
            elif score >= 40:
                annotation_text = "⚠️"
            else:
                annotation_text = "🔄"
            
            fig.add_annotation(
                x=score + 5,
                y=i,
                text=annotation_text,
                showarrow=False,
                font=dict(size=16)
            )
        
        return fig
    
    def create_cognitive_strengths_chart(self, cognitive_profile: Dict) -> go.Figure:
        """Wykres mocnych stron kognitywnych w stylu polar bar"""
        
        cognitive_analysis = cognitive_profile.get('cognitive_strengths_analysis', {})
        top_strengths = cognitive_analysis.get('top_strengths', [])
        
        if not top_strengths:
            # Fallback data
            strengths = ['Strategic', 'Creative', 'Analytical', 'Operational', 'Systemic']
            scores = [8.5, 7.8, 9.2, 6.5, 7.0]
            levels = ['Expert', 'Proficient', 'Expert', 'Developing', 'Proficient']
        else:
            strengths = [s.get('name', '').replace('Myślenie ', '') for s in top_strengths]
            scores = [s.get('score', 5) for s in top_strengths]
            levels = [s.get('level', 'Proficient') for s in top_strengths]
        
        # Color mapping dla poziomów
        level_colors = {
            'Expert': self.color_palette['success'],
            'Proficient': self.color_palette['primary'],
            'Developing': self.color_palette['warning'],
            'Novice': self.color_palette['danger']
        }
        
        colors = [level_colors.get(level, self.color_palette['info']) for level in levels]
        
        # Polar bar chart
        fig = go.Figure()
        
        fig.add_trace(go.Barpolar(
            r=scores,
            theta=strengths,
            marker=dict(
                color=colors,
                line=dict(color='white', width=2),
                opacity=0.8
            ),
            hovertemplate='<b>%{theta}</b><br>Poziom: %{r:.1f}/10<br>Kategoria: %{customdata}<extra></extra>',
            customdata=levels
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    range=[0, 10], 
                    showticklabels=True,
                    tickfont=dict(size=10),
                    gridcolor='lightgray'
                ),
                angularaxis=dict(
                    showticklabels=True,
                    tickfont=dict(size=12, color=self.color_palette['dark'])
                )
            ),
            title=dict(
                text="Profil Kognitywny - Mocne Strony",
                x=0.5,
                font=dict(size=18, color=self.color_palette['primary'], family="Arial Black")
            ),
            height=450,
            showlegend=False,
            paper_bgcolor='white'
        )
        
        return fig
    
    def create_career_fit_matrix(self, recommended_paths: List[Dict]) -> go.Figure:
        """Macierz dopasowania kariery - risk vs reward"""
        
        if not recommended_paths:
            return go.Figure().add_annotation(text="Brak danych o ścieżkach kariery")
        
        # Przygotowanie danych
        careers = [path['title'] for path in recommended_paths[:6]]
        match_scores = [path['match_score'] for path in recommended_paths[:6]]
        growth_potentials = [path['growth_potential'] for path in recommended_paths[:6]]
        
        # Risk mapping
        risk_mapping = {'Low': 1, 'Medium': 2, 'Medium-High': 2.5, 'High': 3}
        risk_scores = [risk_mapping.get(path['risk_level'], 2) for path in recommended_paths[:6]]
        
        # Bubble sizes based on match score
        bubble_sizes = [score * 0.8 for score in match_scores]
        
        # Colors based on growth potential
        colors = growth_potentials
        
        fig = go.Figure(go.Scatter(
            x=risk_scores,
            y=growth_potentials,
            mode='markers+text',
            marker=dict(
                size=bubble_sizes,
                color=colors,
                colorscale='RdYlBu_r',
                showscale=True,
                colorbar=dict(title="Growth Potential"),
                line=dict(width=2, color='white'),
                opacity=0.8
            ),
            text=careers,
            textposition='middle center',
            textfont=dict(size=10, color='white', family="Arial Black"),
            hovertemplate='<b>%{text}</b><br>Risk Level: %{x}<br>Growth Potential: %{y}%<br>Match Score: %{customdata}%<extra></extra>',
            customdata=match_scores
        ))
        
        fig.update_layout(
            title=dict(
                text="Macierz Risk-Reward dla Ścieżek Kariery",
                x=0.5,
                font=dict(size=18, color=self.color_palette['primary'], family="Arial Black")
            ),
            xaxis=dict(
                title='Poziom Ryzyka',
                range=[0.5, 3.5],
                tickvals=[1, 2, 3],
                ticktext=['Niski', 'Średni', 'Wysoki'],
                gridcolor='lightgray'
            ),
            yaxis=dict(
                title='Potencjał Wzrostu (%)',
                range=[75, 100],
                gridcolor='lightgray'
            ),
            height=500,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        # Dodaj quadrant lines
        fig.add_hline(y=90, line_dash="dash", line_color="gray", opacity=0.5)
        fig.add_vline(x=2, line_dash="dash", line_color="gray", opacity=0.5)
        
        return fig
    
    def create_skills_gap_analysis(self, skill_development_plan: Dict) -> go.Figure:
        """Analiza luk w umiejętnościach"""
        
        prioritized_skills = skill_development_plan.get('prioritized_skills', [])
        
        if not prioritized_skills:
            return go.Figure().add_annotation(text="Brak danych o umiejętnościach")
        
        # Przygotowanie danych dla top 8 skills
        skills_data = prioritized_skills[:8]
        skill_names = [skill['skill'] for skill in skills_data]
        current_levels = [skill['current_level'] for skill in skills_data]
        target_levels = [skill['target_level'] for skill in skills_data]
        gap_sizes = [skill['gap_size'] for skill in skills_data]
        importance_scores = [skill['importance'] for skill in skills_data]
        
        fig = go.Figure()
        
        # Current levels
        fig.add_trace(go.Bar(
            name='Obecny poziom',
            y=skill_names,
            x=current_levels,
            orientation='h',
            marker=dict(color=self.color_palette['info'], opacity=0.7),
            hovertemplate='<b>%{y}</b><br>Obecny poziom: %{x}/10<extra></extra>'
        ))
        
        # Target levels
        fig.add_trace(go.Bar(
            name='Poziom docelowy',
            y=skill_names,
            x=target_levels,
            orientation='h',
            marker=dict(color=self.color_palette['success'], opacity=0.7),
            hovertemplate='<b>%{y}</b><br>Poziom docelowy: %{x}/10<extra></extra>'
        ))
        
        # Gap indicators
        for i, (skill, gap, importance) in enumerate(zip(skill_names, gap_sizes, importance_scores)):
            if gap > 2:
                symbol = "🚨"
            elif gap > 1:
                symbol = "⚠️"
            else:
                symbol = "✅"
            
            fig.add_annotation(
                x=max(current_levels[i], target_levels[i]) + 0.3,
                y=i,
                text=f"{symbol} Gap: {gap}",
                showarrow=False,
                font=dict(size=10)
            )
        
        fig.update_layout(
            title=dict(
                text="Analiza Luk w Umiejętnościach",
                x=0.5,
                font=dict(size=18, color=self.color_palette['primary'], family="Arial Black")
            ),
            xaxis=dict(title='Poziom Umiejętności (1-10)', range=[0, 10]),
            yaxis=dict(title=''),
            height=500,
            barmode='overlay',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        return fig
    
    def create_development_timeline(self, skill_development_plan: Dict) -> go.Figure:
        """Timeline rozwoju umiejętności"""
        
        # Mock timeline data - w rzeczywistej aplikacji z skill_development_plan
        timeline_data = [
            {'date': '2024-07', 'milestone': 'Skills Assessment Complete', 'category': 'Foundation', 'progress': 100},
            {'date': '2024-08', 'milestone': 'Python Basics Mastery', 'category': 'Technical', 'progress': 80},
            {'date': '2024-09', 'milestone': 'Leadership Training Start', 'category': 'Soft Skills', 'progress': 30},
            {'date': '2024-10', 'milestone': 'Data Analysis Certification', 'category': 'Technical', 'progress': 60},
            {'date': '2024-11', 'milestone': 'Strategic Thinking Workshop', 'category': 'Cognitive', 'progress': 0},
            {'date': '2024-12', 'milestone': 'Portfolio Project Complete', 'category': 'Application', 'progress': 0},
            {'date': '2025-01', 'milestone': 'Industry Networking Event', 'category': 'Professional', 'progress': 0},
            {'date': '2025-02', 'milestone': 'Mentor Relationship Established', 'category': 'Professional', 'progress': 0}
        ]
        
        # Color mapping dla kategorii
        category_colors = {
            'Foundation': self.color_palette['dark'],
            'Technical': self.color_palette['primary'],
            'Soft Skills': self.color_palette['success'],
            'Cognitive': self.color_palette['warning'],
            'Application': self.color_palette['highlight'],
            'Professional': self.color_palette['info']
        }
        
        fig = go.Figure()
        
        for i, item in enumerate(timeline_data):
            # Progress indicator
            if item['progress'] == 100:
                symbol = '✅'
                opacity = 1.0
            elif item['progress'] > 0:
                symbol = '🔄'
                opacity = 0.8
            else:
                symbol = '⏳'
                opacity = 0.5
            
            fig.add_trace(go.Scatter(
                x=[item['date']],
                y=[i],
                mode='markers+text',
                marker=dict(
                    size=25,
                    color=category_colors[item['category']],
                    opacity=opacity,
                    line=dict(width=3, color='white')
                ),
                text=symbol,
                textfont=dict(size=14),
                textposition='middle center',
                name=item['category'],
                showlegend=False,
                hovertemplate=f'<b>{item["milestone"]}</b><br>Data: {item["date"]}<br>Kategoria: {item["category"]}<br>Postęp: {item["progress"]}%<extra></extra>'
            ))
            
            # Milestone labels
            fig.add_annotation(
                x=item['date'],
                y=i,
                text=item['milestone'],
                yshift=25,
                showarrow=False,
                font=dict(size=10, color=self.color_palette['dark']),
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor=category_colors[item['category']],
                borderwidth=1
            )
        
        # Connect timeline
        dates = [item['date'] for item in timeline_data]
        y_positions = list(range(len(timeline_data)))
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=y_positions,
            mode='lines',
            line=dict(color=self.color_palette['primary'], width=3, dash='dot'),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        fig.update_layout(
            title=dict(
                text="Timeline Rozwoju Zawodowego",
                x=0.5,
                font=dict(size=18, color=self.color_palette['primary'], family="Arial Black")
            ),
            xaxis=dict(title='Timeline', tickangle=45),
            yaxis=dict(showticklabels=False, title=''),
            height=600,
            showlegend=False,
            paper_bgcolor='white',
            plot_bgcolor='white'
        )
        
        return fig
    
    def create_success_probability_gauge(self, success_analysis: Dict) -> go.Figure:
        """Gauge chart prawdopodobieństwa sukcesu"""
        
        overall_probability = success_analysis.get('overall_success_probability', 75)
        
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = overall_probability,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Prawdopodobieństwo Sukcesu Zawodowego", 
                    'font': {'size': 18, 'color': self.color_palette['primary']}},
            delta = {'reference': 70, 'increasing': {'color': self.color_palette['success']}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': self.color_palette['primary']},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "gray",
                'steps': [
                    {'range': [0, 50], 'color': self.color_palette['danger']},
                    {'range': [50, 70], 'color': self.color_palette['warning']},
                    {'range': [70, 85], 'color': self.color_palette['info']},
                    {'range': [85, 100], 'color': self.color_palette['success']}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        
        fig.update_layout(
            height=400,
            paper_bgcolor='white',
            font={'color': self.color_palette['dark'], 'family': "Arial"}
        )
        
        return fig
    
    def create_comprehensive_dashboard(self, analysis_results: Dict) -> Dict[str, go.Figure]:
        """Tworzenie kompletnego dashboard z wszystkimi wykresami"""
        
        dashboard_charts = {}
        
        # Big Five Radar
        if 'personality_profile' in analysis_results:
            dashboard_charts['big_five_radar'] = self.create_big_five_radar(
                analysis_results['personality_profile']
            )
        
        # Motivation Chart
        if 'motivation_profile' in analysis_results:
            dashboard_charts['motivation_chart'] = self.create_motivation_chart(
                analysis_results['motivation_profile']
            )
        
        # Cognitive Strengths
        if 'cognitive_profile' in analysis_results:
            dashboard_charts['cognitive_chart'] = self.create_cognitive_strengths_chart(
                analysis_results['cognitive_profile']
            )
        
        # Career analysis charts
        if 'career_analysis' in analysis_results:
            career_analysis = analysis_results['career_analysis']
            
            # Career fit matrix
            if 'recommended_paths' in career_analysis:
                dashboard_charts['career_fit_matrix'] = self.create_career_fit_matrix(
                    career_analysis['recommended_paths']
                )
            
            # Skills gap analysis
            if 'skill_development_plan' in career_analysis:
                dashboard_charts['skills_gap_chart'] = self.create_skills_gap_analysis(
                    career_analysis['skill_development_plan']
                )
                
                dashboard_charts['development_timeline'] = self.create_development_timeline(
                    career_analysis['skill_development_plan']
                )
            
            # Success probability gauge
            if 'success_analysis' in career_analysis:
                dashboard_charts['success_gauge'] = self.create_success_probability_gauge(
                    career_analysis['success_analysis']
                )
        
        return dashboard_charts
    
    def create_salary_projection_chart(self, career_projections: Dict) -> go.Figure:
        """Wykres projekcji zarobków dla różnych ścieżek"""
        
        if not career_projections:
            return go.Figure().add_annotation(text="Brak danych o projekcjach kariery")
        
        fig = go.Figure()
        
        years = ['Obecnie', '3 lata', '5 lat', '10 lat']
        
        for i, (career_title, projection_data) in enumerate(list(career_projections.items())[:3]):
            salary_data = projection_data.get('salary_projections', {})
            
            salary_values = [
                (salary_data.get('current_range_min', 0) + salary_data.get('current_range_max', 0)) / 2,
                (salary_data.get('3_year_projection_min', 0) + salary_data.get('3_year_projection_max', 0)) / 2,
                (salary_data.get('5_year_projection_min', 0) + salary_data.get('5_year_projection_max', 0)) / 2,
                (salary_data.get('10_year_projection_min', 0) + salary_data.get('10_year_projection_max', 0)) / 2
            ]
            
            fig.add_trace(go.Scatter(
                x=years,
                y=salary_values,
                mode='lines+markers',
                name=career_title,
                line=dict(width=3, color=self.gradient_colors[i % len(self.gradient_colors)]),
                marker=dict(size=8),
                hovertemplate=f'<b>{career_title}</b><br>Rok: %{{x}}<br>Średnie zarobki: %{{y:$,.0f}}<extra></extra>'
            ))
        
        fig.update_layout(
            title=dict(
                text="Projekcja Zarobków - Porównanie Ścieżek Kariery",
                x=0.5,
                font=dict(size=18, color=self.color_palette
