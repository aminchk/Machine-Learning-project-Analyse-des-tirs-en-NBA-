import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

@st.cache_data
def load_data(fichier):
    df = pd.read_csv(fichier)
    L=['LeBron James','Kobe Bryant','Tim Duncan', "Shaquille O'Neal", 'Stephen Curry','Kevin Durant','Dwyane Wade','Giannis Antetokounmpo','Kevin Garnett','Dirk Nowitzki', 'Kawhi Leonard','Allen Iverson','Steve Nash','Nikola Jokic', 'Chris Paul','Paul Pierce', 'Dwight Howard', 'Jason Kidd', 'Ray Allen', 'James Harden']
    df = df[df['Player Name'].isin(L)]
    df = df.replace(to_replace = ["Shaquille O'Neal",'Jason Kidd','Kevin Garnett','Kobe Bryant','Ray Allen','Steve Nash','Allen Iverson'],value = ["*Shaquille O'Neal",'*Jason Kidd','*Kevin Garnett','*Kobe Bryant','*Ray Allen','*Steve Nash','*Allen Iverson'])
    return df
    
nba_shot = load_data("nba_shot_location.csv")

@st.cache_data
def load_data_2(fichier):
    df = pd.read_csv(fichier, index_col= 0)
    return df
    
df_num_orig = load_data_2("df_num_orig.csv")
df_num = load_data_2("df_num.csv")

@st.cache_data
def load_data_3(fichier):
    df = pd.read_csv(fichier)
    return df

nba_shot_2 = load_data_3("nba_shot_2.csv")

@st.cache_data
def load_data_4(fichier):
    df = pd.read_csv(fichier)
    return df

season_stat = load_data_4("season_stat.csv")

with st.sidebar:
    selected = option_menu(
        "Menu",
        [
            "Description et objectif du projet",
            'Données',
            'Analyse exploratoire',
            'Visualisation des données',
            'Préparation des données',
            'Méthodologie',
            'Modélisation',
            'Meilleur modèle',
            'Conclusion et Perspectives',
            'Remerciement'
        ],
        default_index=1,
    )
    selected

if selected == "Description et objectif du projet":
    st.title("Analyse des tirs de joueurs NBA :basketball:")
    st.markdown('Projet réalisé par : Amine Chakli, Pierre Ndjiki et David Tewodrose')
    st.markdown('20 Juin 2023')
    video_file = open('shot.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    st.header('Description et objectif du projet :')
    st.markdown("\n")
    st.write(
        '''Le développement constant des nouvelles technologies et des outils numériques permet désormais de suivre en temps réel les déplacements de tous les joueurs sur un terrain de basketball. Les données recueillies sont ainsi très nombreuses et riches.'''
    )
    st.markdown("\n")
    st.write('''Le but de ce projet est de :''')
    st.markdown(
        """
    * Comparer les tirs (fréquence et efficacité par situation de jeu et par localisation sur le terrain) des 20 meilleurs joueurs de NBA du 21ème siècle selon un classement ESPN
    * Pour chacun de ces 20 joueurs, estimer à l'aide d'un modèle la probabilité de réussite de leurs tirs en fonction de différents paramètres"""
    )
    st.markdown("\n")
    st.write("Nos 20 joueurs sont :")
    st.markdown(
        """
    * LeBron James
    * Kobe Bryant
    * Tim Duncan
    * Shaquille O'Neal
    * Stephen Curry
    * Kevin Durant
    * Dwyane Wade
    * Giannis Antetokounmpo
    * Kevin Garnett
    * Dirk Nowitzki
    * Kawhi Leonard
    * Allen Iverson
    * Steve Nash
    * Nikola Jokic
    * Chris Paul
    * Paul Pierce
    * Dwight Howard
    * Jason Kidd
    * Ray Allen
    * James Harden \n
    """)

    st.markdown("\n")
    st.write('Nous avons deux jeux de données à notre disposition :')
    st.markdown(
        """
    * NBA Shot Locations 1997 - 2020.csv
    * Seasons Stats.csv
    """
    )
if selected == "Données":
    st.title('Les données :')
    st.markdown("\n")
    st.info("""Les données proviennent du site Kaggle https://www.kaggle.com/jonathangmwl/nba-shot-locations.""")
    st.markdown("\n")
    st.write(
        "Nous restreignons notre étude au panel de 20 joueurs désignés précédemment. Nous avons donc filtré nos données à l'aide de la variable 'Player Name'."
    )
    st.markdown("\n")
    st.info(
        """Le classement des 20 meilleurs joueurs du 21ème siècle est disponible sur le site ESPN  https://www.espn.com/nba/story/_/id/34552302/nbarank-2022-ranking-best-players-2022-23-100-26."""
    )
    st.markdown("\n")
    st.write("""Le tableau suivant récapitule les données présentes :""")
    st.markdown("\n") 

    st.dataframe(nba_shot.head())

    st.markdown("\n")
    st.write(
        "Ce jeu de données contient des informations sur chacun des **4729512 tirs** qui ont été tentés en match NBA de 1997 à 2020. Pour chaque tir, **22 variables** sont renseignées."
    )
    st.markdown("\n")
    st.write("La figure suivante représente le pourcentage de données associées à chaque joueur :")
    
    fig = px.histogram(nba_shot, y="Player Name", title="Modalités de la variable Player Name :", histnorm='percent')
    fig.update_yaxes(categoryorder="total ascending", showline=True, linewidth=2, linecolor='black')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey', showline=True, linewidth=2, linecolor='black')
    fig.update_layout(bargap=0.2, title={"x": 0.5}, grid_xaxes=list('x'), plot_bgcolor='white')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("\n")
    st.write("Nous n’avons pas trouvé de doublons ni de données manquantes.")

if selected == "Analyse exploratoire":
    st.title('Analyse exploratoire des données :')
    st.markdown("\n")
    st.info("""Dans cette section, nous faisons une analyse non exhaustive en portant une attention particulière aux variables les plus représentatives du jeu de données. L'analyse exploratoire complète est traitée dans notre rapport technique d'évaluation.""")
    st.markdown("\n")
    st.header("Les variables quantitatives : ")
    st.markdown("\n")

    
    fig00 = px.imshow(df_num_orig.corr(), x= list(df_num_orig.corr().columns), y= list(df_num_orig.corr().columns),color_continuous_scale='RdBu_r')
    fig1 = px.imshow(df_num.corr(), x= list(df_num.corr().columns), y= list(df_num.corr().columns),color_continuous_scale='RdBu_r')

    quant = st.checkbox('Afficher la description des variables')
    if quant:
        st.dataframe(df_num_orig.describe().round(1))
    
    quant2 = st.checkbox('Afficher les matrices de corrélations')
    if quant2:
        st.plotly_chart(fig00, use_container_width=True)
        st.write("Suite à la matrice de corrélation présentée précédemment, il est important de considérer les variables les plus décorrélées possibles afin d'améliorer la fiabilité de nos modèles. La variable Shot Distance a donc été supprimée et nous avons également supprimé les lignes pour lesquelles la valeur de Shot Distance différait de plus de 7 pieds de la racine carrée de (X Location)^2 + (Y Location )^2. En effet, ces lignes sont aberrantes du point de vue de l'équation suivante :")
        st.latex(r'''(X Location)^2 +(Y Location)^2 = (Shot Distance)^2''')
        st.markdown("\n")
        st.write("Bien qu'elles soient décorrélées, les variables Minutes Remaining et Seconds Remaining ne contiennent chacune qu'une information partielle sur le moment du match où le tir est effectué. Nous avons donc choisi de les fusionner en une seule variable appelée Time Remaining qui donne le nombre de secondes restantes dans le quart-temps considéré au moment où le tir est tenté.")
        st.plotly_chart(fig1, use_container_width=True)

    quant3 = st.checkbox('Afficher la description des variables après préprocessing')
    if quant3:
        st.dataframe(df_num.describe().round(1))
    st.markdown("\n")
    st.header("Les variables qualitatives : ")
    st.markdown("\n")

    st.write("La figure suivante représente les modalités de notre variable cible :")
    fig3 = px.histogram(nba_shot, y="Shot Made Flag", title = "Modalités de la variable Shot Made Flag :", histnorm='percent')
    fig3.update_yaxes(categoryorder = "total ascending",nticks=3, showline=True, linewidth=2, linecolor='black')
    fig3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey',showline=True, linewidth=2, linecolor='black')
    fig3.update_layout(bargap=0.2, title = {"x" : 0.5}, grid_xaxes=list('x'),plot_bgcolor = 'white')
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("\n")

    st.write("La figure suivante représente les modalités de la variable Action type :")
    fig11 = px.histogram(nba_shot, y="Action Type", title = "Modalités de la variable Action Type :", histnorm='percent')
    fig11.update_yaxes(categoryorder = "total ascending", showline=True, linewidth=2, linecolor='black')
    fig11.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey',showline=True, linewidth=2, linecolor='black')
    fig11.update_layout(bargap=0.2, title = {"x" : 0.5}, grid_xaxes=list('x'),plot_bgcolor = 'white')
    st.plotly_chart(fig11, use_container_width=True)
    st.markdown("\n")
    st.write("Afin de rendre cette variable exploitable, nous avons choisi de regrouper ses modalités en 4 catégories et de renommer la variable en 'technique_shot' :")
    listacty = list(nba_shot['Action Type'].value_counts().index)
    listdunk = [string for string in listacty if "Dunk" in string]
    listlayup = [string for string in listacty if "Layup" in string or "Finger Roll" in string or "Tip Shot" in string]
    listhook = [string for string in listacty if "Hook" in string]
    listjump = [string for string in listacty if "Jump" in string or "Shot" in string or "shot" in string]
    nba_shot['technique_shot'] = nba_shot['Action Type'].replace(to_replace = listdunk,value='Dunk')
    nba_shot['technique_shot'] = nba_shot['technique_shot'].replace(to_replace = listlayup,value='Layup')
    nba_shot['technique_shot'] = nba_shot['technique_shot'].replace(to_replace = listhook,value='Hook')
    nba_shot['technique_shot'] = nba_shot['technique_shot'].replace(to_replace = listjump,value='Jump Shot')
    fig12 = px.histogram(nba_shot, y="technique_shot", title = "Modalités de la variable Technique Shot :", histnorm='percent')
    fig12.update_yaxes(categoryorder = "total ascending", showline=True, linewidth=2, linecolor='black')
    fig12.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey',showline=True, linewidth=2, linecolor='black')
    fig12.update_layout(bargap=0.2, title = {"x" : 0.5}, grid_xaxes=list('x'),plot_bgcolor = 'white')
    st.plotly_chart(fig12, use_container_width=True)
    st.markdown("\n")

    st.write("La figure suivante représente les modalités de la variable Shot Type :")
    fig5 = px.histogram(nba_shot, y="Shot Type", title = "Modalités de la variable Shot Type :", histnorm='percent')
    fig5.update_yaxes(categoryorder = "total ascending", showline=True, linewidth=2, linecolor='black')
    fig5.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey',showline=True, linewidth=2, linecolor='black')
    fig5.update_layout(bargap=0.2, title = {"x" : 0.5}, grid_xaxes=list('x'),plot_bgcolor = 'white')
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("\n")
    st.write("La figure suivante représente les modalités de la variable Season Type :")
    fig6 = px.histogram(nba_shot, y="Season Type", title = "Modalités de la variable Season Type :", histnorm='percent')
    fig6.update_yaxes(categoryorder = "total ascending", showline=True, linewidth=2, linecolor='black')
    fig6.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey',showline=True, linewidth=2, linecolor='black')
    fig6.update_layout(bargap=0.2, title = {"x" : 0.5}, grid_xaxes=list('x'),plot_bgcolor = 'white')
    st.plotly_chart(fig6, use_container_width=True)

if selected == "Visualisation des données":
    st.title('Data Visualisation')
    st.markdown("\n")
    st.info("""Dans cette section, nous présentons les différentes visualisations réalisées de façon non exhaustive. La data visualisation complète est traitée dans notre rapport technique d'évaluation.""")
    st.markdown("\n")

    st.write("La figure suivante représente le pourcentage de réussite de tir par joueur :")
    image2 = Image.open("reussite.png")  
    st.image(image2)
    st.markdown("\n")

    st.write("Cartes des tirs des joueurs de la NBA :")
   
    court_shapes = []
    #Outer Lines
    outer_lines_shape = dict(
        type='rect',
        xref='x',
        yref='y',
        x0='-250',
        y0='-47.5',
        x1='250',
        y1='422.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )
    )
    court_shapes.append(outer_lines_shape)

    #Hoop Shape
    hoop_shape = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='7.5',
        y0='7.5',
        x1='-7.5',
        y1='-7.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )   
    )
    court_shapes.append(hoop_shape)

    #Basket Backboard
    backboard_shape = dict(
        type='rect',
        xref='x',
        yref='y',
        x0='-30',
        y0='-7.5',
        x1='30',
        y1='-6.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        ),
        fillcolor='rgba(10, 10, 10, 1)'
    )
    court_shapes.append(backboard_shape)

    #Outer Box of Three-Second Area
    outer_three_sec_shape = dict(
        type='rect',
        xref='x',
        yref='y',
        x0='-80',
        y0='-47.5',
        x1='80',
        y1='143.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )
    )
    court_shapes.append(outer_three_sec_shape)

    #Inner Box of Three-Second Area
    inner_three_sec_shape = dict(
        type='rect',
        xref='x',
        yref='y',
        x0='-60',
        y0='-47.5',
        x1='60',
        y1='143.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )
    )
    court_shapes.append(inner_three_sec_shape)
    
    #Three Point Line (Left)
    left_line_shape = dict(
        type='line',
        xref='x',
        yref='y',
        x0='-220',
        y0='-47.5',
        x1='-220',
        y1='92.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )
    )
    court_shapes.append(left_line_shape)

    #Three Point Line (Right)
    right_line_shape = dict(
        type='line',
        xref='x',
        yref='y',
        x0='220',
        y0='-47.5',
        x1='220',
        y1='92.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )   
    )
    court_shapes.append(right_line_shape)

    #Three Point Line Arc
    three_point_arc_shape = dict(
        type='path',
        xref='x',
        yref='y',
        path='M -220 92.5 C -70 300, 70 300, 220 92.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )
    )
    court_shapes.append(three_point_arc_shape)

    #Center Circle
    center_circle_shape = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='60',
        y0='482.5',
        x1='-60',
        y1='362.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )
    )
    court_shapes.append(center_circle_shape)

    #Restraining Circle
    res_circle_shape = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='20',
        y0='442.5',
        x1='-20',
        y1='402.5',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )
    )
    court_shapes.append(res_circle_shape)

    #Free Throw Circle
    free_throw_circle_shape = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='60',
        y0='200',
        x1='-60',
        y1='80',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1
        )
    )
    court_shapes.append(free_throw_circle_shape)

    #Restricted Area
    res_area_shape = dict(
        type='circle',
        xref='x',
        yref='y',
        x0='40',
        y0='40',
        x1='-40',
        y1='-40',
        line=dict(
            color='rgba(10, 10, 10, 1)',
            width=1,
            dash='dot'
        )
    )
    court_shapes.append(res_area_shape)

    saison = st.selectbox(label = "Choisissez la saison :" , options = ['1997/1998', '2020/2021'])
    if saison == '1997/1998':
        season19971998 = nba_shot_2[(nba_shot_2['Season'] == '1997/1998')]
        def updateVisibility(selectedPlayer):
            visibilityValues = []
            for player in list(season19971998['Player Name'].unique()):
                if player == selectedPlayer:
                    visibilityValues.append(True)
                    visibilityValues.append(True)
                else:
                    visibilityValues.append(False)
                    visibilityValues.append(False)
            return visibilityValues

        data = []
        buttons_data = []
        for player in list(season19971998['Player Name'].unique()):
            shot_trace_made = go.Scatter(
                x = season19971998[(season19971998['Shot Made Flag'] == 1) & (season19971998['Player Name'] == player)]['X Location'],
                y = season19971998[(season19971998['Shot Made Flag'] == 1) & (season19971998['Player Name'] == player)]['Y Location'],
                mode = 'markers',
                marker = dict(
                size = 10,
                color = 'rgba(63, 191, 63, 0.9)',
                ), 
                name = 'Made',
                text = season19971998[(season19971998['Shot Made Flag'] == 1) & (season19971998['Player Name'] == player)],
                textfont = dict(
                color = 'rgba(75, 85, 102,0.7)'
                ),
                visible = (player =='Tim Duncan')
            )
    
    
            shot_trace_missed = go.Scatter(
                x = season19971998[(season19971998['Shot Made Flag'] == 0) & (season19971998['Player Name'] == player)]['X Location'],
                y = season19971998[(season19971998['Shot Made Flag'] == 0) & (season19971998['Player Name'] == player)]['Y Location'],
                mode = 'markers',
                marker = dict(
                    size = 10,
                    color = 'rgba(241, 18, 18, 0.9)',
                    ), 
                name = 'Missed',
                text = season19971998[(season19971998['Shot Made Flag'] == 1) & (season19971998['Player Name'] == player)],
                textfont = dict(
                color = 'rgba(75, 85, 102,0.7)'
                ),
                visible = (player =='Tim Duncan')
            )

            data.append(shot_trace_made)
            data.append(shot_trace_missed)
    
            buttons_data.append(
            dict(
                label = player,
                method = 'update',
                args = [{'visible': updateVisibility(player)}]
                )
            )
    
        updatemenus = list([
            dict(active=0,
            buttons = buttons_data,
            direction = 'down',
            pad = {'r': 10, 't': 10},
            showactive = True,
            x = 0.65,
            xanchor = 'left',
            y = 1.2,
            yanchor = 'top',
            font = dict (
                size = 14
                )
            )
        ])

        layout = go.Layout(
            title='<b>Shot Chart - Season 1997/1998</b>',
            titlefont=dict(
                size=17
            ),
            hovermode = 'closest',
            updatemenus = updatemenus,
            showlegend = True,
            height = 600,
            width = 600, 
            shapes = court_shapes,
            xaxis = dict(
                showticklabels = False
            ),
            yaxis = dict(
                showticklabels = False
            )
        )
 
        fig = go.Figure(data=data, layout=layout)
        fig.update_layout(plot_bgcolor='rgba(255,255,255,1)')
        st.write(fig)

    if saison == '2020/2021':
        season20202021 = nba_shot_2[(nba_shot_2['Season'] == '2020/2021')]
        def updateVisibility(selectedPlayer):
            visibilityValues = []
            for player in list(season20202021['Player Name'].unique()):
                if player == selectedPlayer:
                    visibilityValues.append(True)
                    visibilityValues.append(True)
                else:
                    visibilityValues.append(False)
                    visibilityValues.append(False)
            return visibilityValues

        data = []
        buttons_data = []
        for player in list(season20202021['Player Name'].unique()):
            shot_trace_made = go.Scatter(
                x = season20202021[(season20202021['Shot Made Flag'] == 1) & (season20202021['Player Name'] == player)]['X Location'],
                y = season20202021[(season20202021['Shot Made Flag'] == 1) & (season20202021['Player Name'] == player)]['Y Location'],
                mode = 'markers',
                marker = dict(
                size = 10,
                color = 'rgba(63, 191, 63, 0.9)',
                ), 
                name = 'Made',
                text = season20202021[(season20202021['Shot Made Flag'] == 1) & (season20202021['Player Name'] == player)],
                textfont = dict(
                color = 'rgba(75, 85, 102,0.7)'
                ),
                visible = (player =='James Harden')
            )
    
    
            shot_trace_missed = go.Scatter(
                x = season20202021[(season20202021['Shot Made Flag'] == 0) & (season20202021['Player Name'] == player)]['X Location'],
                y = season20202021[(season20202021['Shot Made Flag'] == 0) & (season20202021['Player Name'] == player)]['Y Location'],
                mode = 'markers',
                marker = dict(
                    size = 10,
                    color = 'rgba(241, 18, 18, 0.9)',
                    ), 
                name = 'Missed',
                text = season20202021[(season20202021['Shot Made Flag'] == 1) & (season20202021['Player Name'] == player)],
                textfont = dict(
                color = 'rgba(75, 85, 102,0.7)'
                ),
                visible = (player =='Tim Duncan')
            )

            data.append(shot_trace_made)
            data.append(shot_trace_missed)
    
            buttons_data.append(
            dict(
                label = player,
                method = 'update',
                args = [{'visible': updateVisibility(player)}]
                )
            )
    
        updatemenus = list([
            dict(active=0,
            buttons = buttons_data,
            direction = 'down',
            pad = {'r': 10, 't': 10},
            showactive = True,
            x = 0.65,
            xanchor = 'left',
            y = 1.2,
            yanchor = 'top',
            font = dict (
                size = 14
                )
            )
        ])

        layout = go.Layout(
            title='<b>Shot Chart - Season 2020/2021</b>',
            titlefont=dict(
                size=17
            ),
            hovermode = 'closest',
            updatemenus = updatemenus,
            showlegend = True,
            height = 600,
            width = 600, 
            shapes = court_shapes,
            xaxis = dict(
                showticklabels = False
            ),
            yaxis = dict(
                showticklabels = False
            )
        )
 
        fig = go.Figure(data=data, layout=layout)
        fig.update_layout(plot_bgcolor='rgba(255,255,255,1)')
        st.write(fig)

    
    st.write("La figure suivante représente le type de tir par joueur :")
    image3 = Image.open("tir.png")  
    st.image(image3)

    st.markdown("\n")
    st.write("La figure suivante représente les différentes aires de tirs en fonction joueur :")
    image5 = Image.open("aire.png")  
    st.image(image5)

    st.markdown("\n")
    st.write("Ratio tirs tentés / tirs réussis par joueur en fonction de la technique de tir :")
    image6 = Image.open("ratio.png")  
    st.image(image6)

if selected == "Préparation des données":
    st.title('Préparation des données :')
    st.markdown("\n")
    st.write("Voici le jeu de données que nous avions initialement : ")
    image6 = Image.open("donnee.png")  
    st.image(image6)
    st.markdown("\n")
    st.header("Modification des variables :")
    st.markdown("\n")

    st.subheader("La variable Period :")
    st.write("Elle correspond aux différentes périodes ou quart-temps d'un match de basket. Un match de basket se joue en 4 périodes de 12 minutes. Si à la fin de la quatrième période les deux équipes sont à égalité, on joue une prolongation de 5 minutes, puis une autre prolongation de 5 minutes si le score est toujours à égalité, et ainsi de suite. Voici les modalités de cette variable avant préprocessing :")
    fig9 = px.histogram(nba_shot, y="Period", title = "Modalités de la variable Period :", histnorm='percent')
    fig9.update_yaxes(showline=True, linewidth=2, linecolor='black')
    fig9.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey',showline=True, linewidth=2, linecolor='black')
    fig9.update_layout(bargap=0.2, title = {"x" : 0.5}, grid_xaxes=list('x'),plot_bgcolor = 'white')
    st.plotly_chart(fig9, use_container_width=True)
    st.write("Étant donné que les prolongations sont assez rares au basket, nous avons rassemblé les périodes 5, 6 et 7 en une seule modalité appelée “P+” et nous avons renommé les périodes 1, 2, 3, 4 en “P1”, “P2”, “P3”, “P4”. Voici les modalités de la variable Period après préprocessing :")
    nba_shot['Period'] = nba_shot['Period'].replace(to_replace = [1,2,3,4,5,6,7], value = ['P1','P2','P3','P4','P+','P+','P+'])
    fig10 = px.histogram(nba_shot, y="Period", title = "Modalités de la variable Period :", histnorm='percent')
    fig10.update_yaxes(categoryorder = "total ascending",showline=True, linewidth=2, linecolor='black')
    fig10.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey',showline=True, linewidth=2, linecolor='black')
    fig10.update_layout(bargap=0.2, title = {"x" : 0.5}, grid_xaxes=list('x'),plot_bgcolor = 'white')
    st.plotly_chart(fig10, use_container_width=True)

    st.subheader("La variable Team Name :")
    st.write("Nous avons modifié la variable Team Name pour n’avoir que des sigles correspondant aux sigles présents dans la variable Home Team. À partir de la variable Team Name, nous avons créé une nouvelle variable intitulée “Home”")
    A=['San Antonio Spurs', 'Los Angeles Lakers', 'Phoenix Suns','Minnesota Timberwolves',
   'Philadelphia 76ers', 'Milwaukee Bucks','Dallas Mavericks', 'Boston Celtics',
   'New Jersey Nets','Seattle SuperSonics', 'Cleveland Cavaliers', 'Miami Heat',
   'Orlando Magic','New Orleans/Oklahoma City Hornets','Denver Nuggets',
   'New Orleans Hornets', 'Oklahoma City Thunder','Detroit Pistons', 'Golden State Warriors',
   'Memphis Grizzlies','Los Angeles Clippers', 'Houston Rockets', 'New York Knicks',
   'Brooklyn Nets', 'Washington Wizards', 'LA Clippers','Chicago Bulls',
   'Atlanta Hawks', 'Charlotte Hornets','Toronto Raptors']
    B=['SAS','LAL','PHX','MIN','PHI','MIL','DAL','BOS','NJN','SEA','CLE','MIA','ORL','NOK','DEN',
   'NOH','OKC','DET','GSW','MEM','LAC','HOU','NYK','BKN','WAS','LAC','CHI','ATL','CHA','TOR']
    nba_shot = nba_shot.replace(to_replace=A,value=B)
    nba_shot['Home'] = 0
    nba_shot['Home'][nba_shot['Team Name']==nba_shot['Home Team']] = 1
    fig12 = px.histogram(nba_shot, y="Home", title = "Modalités de la variable Home:", histnorm='percent')
    fig12.update_yaxes(categoryorder = "total ascending", showline=True, linewidth=2, linecolor='black')
    fig12.update_xaxes(showgrid=True, gridwidth=1, gridcolor='Lightgrey',showline=True, linewidth=2, linecolor='black')
    fig12.update_layout(bargap=0.2, title = {"x" : 0.5}, grid_xaxes=list('x'),plot_bgcolor = 'white')
    st.plotly_chart(fig12, use_container_width=True)
    st.markdown("\n")

    st.subheader("La variable Game Date :")
    st.write("La variable Game Date nous fournit la date du match considéré. En cherchant sur Internet les dates de naissance de chacun de nos joueurs, nous avons pu utiliser cette variable pour en créer une nouvelle, appelée Age, fournissant l’âge du joueur au moment du match.")
    st.markdown("\n")

    st.header("Suppression de variables :")
    st.markdown("\n")
    st.write("Voici la liste des variables que nous supprimons :")
    st.markdown("\n")
    st.markdown(
        """
        * Player ID
        * Game ID
        * Game Event ID
        * Team ID
        * Team Name
        * Game Date
        """
    )
    st.markdown("\n")

    st.write("Les variables qui nous restent à la fin de l'étape de préparation des données apparaissent dans la figure ci-dessous :")
    image7 = Image.open("donneepp.png")  
    st.image(image7)

if selected == "Méthodologie":
    st.header("Approche :")
    st.write("Notre projet de recherche s'apparente à un problème de Machine Learning et plus précisément de la classification :")
    st.markdown("""
    * La classe 1 : Tir réussi
    * La classe 0 : Tir raté
    """)
    st.markdown("\n")

    st.header("Exploitation des données :")
    st.write("Il est nécéssaire d'effectuer les étapes suivantes afin d'assurer l'exploitation des données pour les modèles de Machine Learning :")
    st.write("1. Dichotomisation des variables catégorielles suivantes :")
    st.markdown("""
    * Period
    * Shot Type
    * Shot Zone Basic
    * Shot Zone Area
    * Shot Zone Range
    * technique_shot
    * Home
    """)
    st.write("2. Suppression des variables catégorielles les moins représentées :")
    st.markdown("""
    * Period_P+
    * technique_shot_Hook
    * Shot Type_3PT Field Goal
    * Shot Zone Basic_Backcourt
    * Shot Zone Range_Back Court Shot
    * Shot Zone Area_Back Court(BC)
    * Home_0.
    """)
    st.write("3. Normalisation des données avec standard scaler")
    st.write("4. Nos données étant soumises à une évolution temporelle, lors de la séparation des données, nous avons fixé le paramètre “Shuffle” sur “False”.")
    st.markdown("\n")
    st.write("Voici les variables qui vont nous permettre d'élaborer nos modèles :")
    image8 = Image.open("donneeml.png")  
    st.image(image8)
    st.markdown("\n")

    st.header("Les modèles :")
    st.write("Nous avons utilisé quatre modèles :")
    st.write("* Modèle par joueur sans les données concernant les playoffs")
    st.write("* Modèle par joueur avec les données concernant les playoffs")
    st.write("* Modèle par joueur sans les données concernant les playoffs avec une PCA et un SelectPercentile")
    st.write("* Modèle par joueur avec les données concernant les playoffs avec une PCA et un SelectPercentile")
    st.info("L'intérêt d'utiliser la PCA est de réduire considérablement le temps d'apprentissage des modèles tout en améliorant la performance. Nous avons choisi ici de réduire la taille du dataset tout en conservant 95% de la variance de nos données.")
    st.info("L'intérêt d'utiliser la sélection de variable (Select Percentile) consiste à choisir de façon automatisée les variables les plus importantes et d’oublier les autres. La sélection des variables se fait selon un pourcentage de pertinence que nous avons fixé ici à 90%.")

    st.header("Mise en place des algorithmes :")
    st.write("Nous avons utilisé les modèles suivants pour chacun des 20 joueurs selon le classement ESPN :")
    st.write("* Régression Logistique") 
    st.write("* Arbres de décision")
    st.write("* Forêts aléatoires")
    st.write("* K-plus proches voisins (KNN)")
    st.write("* Machines à Vecteurs de Support (SVM)")
    st.write("* Boosting sur des arbres de décisions")
    st.write("* Bagging")
    st.markdown("\n")

    st.write("Nous avons cherché à optimiser les paramètres afin d'avoir les meilleures performances. Pour cela, nous avons utilisé un outil appelé Grid Search. Voici les paramètres des différents modèles quand cela était possible : ")
    st.write("* Pour les arbres de décision, les forêts aléatoires et le boosting on doit choisir entre deux critères : Entropy ou Gini")
    st.write("* Pour KNN, on doit choisir un nombre de voisins que l’on prend ici entre 2 et 40, et entre trois métriques : Minkowski, Manhattan ou Chebyshev")
    st.write("* Pour SVM, on doit choisir entre trois Kernel : linear, sigmoid, rbf ou poly")
    st.markdown("\n")

    st.write("Afin de se faire une idée plus précise des performances de nos modèles, nous avons affiché plusieurs éléments pour chaque joueur et pour chaque modèle, voici un exemple d'affichage des performances pour James Harden sur un Random Forest :")
    st.markdown("\n")
    image50 = Image.open("jamesharden.png")  
    st.image(image50)

if selected == "Modélisation":
    st.header("1. Modèle par joueur sans les données concernant les playoffs :")
    st.write("Nous restreignons notre étude aux matchs de la saison régulière qui représentent environ 87% des données dont nous disposons.")
    image9 = Image.open("modele1.png")  
    st.image(image9)
    st.markdown("\n")
    st.write("On observe que les performances se situent globalement entre 52% et 69%. Elles sont assez variables selon les joueurs et le modèle choisi. De plus, bien que les forêts aléatoires soient toujours le modèle le moins efficace, on remarque que le modèle le plus efficace varie d’un joueur à un autre et qu’il s’agit toujours de la régression logistique ou de SVM.")
    st.markdown("\n")
    exemple = st.checkbox("Exemple d'un modèle appliqué sur l'un des joueurs")
    if exemple:
        st.write("Régression logistique appliqué sur Tim Duncan :")
        image20 = Image.open("modele1ex.png")  
        st.image(image20)
    st.markdown("\n")

    st.header("2. Modèle par joueur avec les données concernant les playoffs :")
    st.write("Nous incluons maintenant les données concernant les playoffs.")
    image10 = Image.open("modele2.png")  
    st.image(image10)
    st.write("On observe que les performances se situent globalement entre 52% et 67%. Elles sont assez variables selon les joueurs et le modèle choisi. Comme dans le modèle précédent, les forêts aléatoires sont le modèle le moins efficace et le modèle le plus efficace diffère d’un joueur à un autre et est toujours la régression logistique ou le SVM.")
    st.markdown("\n")
    exemple2 = st.checkbox("Exemple d'un modèle appliqué sur l'un des joueurs ")
    if exemple2:
        st.write("KNN appliqué sur LeBron James :")
        image21 = Image.open("modele2ex.png")  
        st.image(image21)

    st.header("3. Modèle par joueur sans les données concernant les playoffs avec une PCA et un SelectPercentile :")
    st.write("Nous reprenons ici notre premier modèle qui incluait uniquement les données de la saison régulière et nous lui appliquons deux méthodes pour tenter d’améliorer les performances : Une analyse en composante principale et une sélection de variable.")
    st.write("Nous avons réalisé des modèles de classifications simples et cette fois-ci des modèles de clasification avancées tels que le boosting et le bagging. Nous avons lancé les modèles avancées uniquement lorsque nous utilisions la PCA ce qui a permi de considérablement réduire le temps d'exécution des algorithmes.")
    image11 = Image.open("modele3.png")  
    st.image(image11)
    st.markdown("\n")
    st.write("On observe une diminution significative des performances avec les modèles de classifications avancées. L’utilisation de modèles avancés tels que le boosting et le bagging n’ont pas eu d’impact significatif sur nos performances.")
    exemple3 = st.checkbox("Exemple d'un modèle appliqué sur l'un des joueurs  ")
    if exemple3:
        st.write("Boosting appliqué sur Stephen Curry :")
        image22 = Image.open("modele3ex.png")  
        st.image(image22)


    st.header("4. Modèle par joueur avec les données concernant les playoffs avec une PCA et un SelectPercentile :")
    st.write("Nous avons procédé de la même manière que pour le modèle précédent mais en incluant cette fois les données concernant les playoffs.")
    image12 = Image.open("modele4.png")  
    st.image(image12)
    st.markdown("\n")
    st.write("De la même façon, on observe une diminution significative des performances avec les modèles de classifications avancées")
    exemple4 = st.checkbox("Exemple d'un modèle appliqué sur l'un des joueurs   ")
    if exemple4:
        st.write("Bagging appliqué sur Shaquille O'Neal :")
        image23 = Image.open("modele4ex.png")  
        st.image(image23)

if selected == "Meilleur modèle":
    st.header("Analyse des performances des différents modèles dans le but de rechercher le meilleur modèle :")
    st.markdown("\n")
    st.subheader("Comparaison des performances avec et sans playoffs :")
    st.markdown("\n")
    image25 = Image.open("modele1vs2.png")  
    st.image(image25)
    st.markdown("\n")
    image26 = Image.open("modele1vs2_2.png")  
    st.image(image26)
    st.markdown("\n")
    st.write("On obtient des scores similaires pour tous les joueurs")
    st.markdown("\n")
    st.write("La régression logistique et le SVM étaient nos deux modèles les plus efficaces")
    st.markdown("\n")

    st.subheader("Comparaison des performances sans les playoffs et avec une PCA et la sélection de variable :")
    st.markdown("\n")
    image27 = Image.open("modele1vs3.png")  
    st.image(image27)
    st.markdown("\n")
    image28 = Image.open("modele1vs3_2.png")  
    st.image(image28)
    st.markdown("\n")
    st.write("Les indicateurs de performances se sont très légèrement améliorés.")
    st.write("Ces méthodes sont donc pertinentes dans notre étude puisqu'elles nous ont permis de réduire considérablement le temps d'exécution") 
    
    st.subheader("Comparaison des performances avec les playoffs et avec une PCA et la sélection de variable :")
    st.markdown("\n")
    image29 = Image.open("modele2vs4.png")  
    st.image(image29)
    st.markdown("\n")
    image30 = Image.open("modele2vs4_2.png")  
    st.image(image30)
    st.markdown("\n")
    st.write("Les indicateurs de performances sont globalement restés assez similaires.")

if selected == "Conclusion et Perspectives":
    st.header("Bilan :")
    st.markdown("\n")
    image001 = Image.open("nba.jpg")  
    st.image(image001)
    st.markdown("\n")
    #st.write("L'objectif du projet était d'estimer à l'aide d'un modèle la probabilité de réussite des tirs des 20 meilleurs joueurs de la NBA selon le classement ESPN en fonction de différents paramètres. Passionné par le sport, ce projet nous a tout de suite intéressé et nous étions motivé à l'idée d'apporter de nouvelles perspectives au sport et notamment au basket. Pouvoir démontrer un réelle apport de la Data Science dans le sport était un vrai défi pour nous.")
    st.write("Nos analyses ont mis évidence plusieurs résultats :")
    st.markdown("""
    * En fonction des joueurs et des modèles, nous avons une précision minimale de 55% et maximale de 70%
    * La réduction de dimension (PCA) et la sélection de variable ont considérablement réduit les temps d'exécution
    * Ces méthodes n'ont pas eu d'impacts significatifs sur les performances
    * L'utilisation de modèles avancés (Bagging et Boosting) n’a pas eu d’impact révélateur sur les performances
    * Nos modèles prédisent mieux les tirs ratés que les tirs réussis
    """)
    st.markdown("\n")
    st.write("Les résultats sont assez correctes mais nous pouvons faire plusieurs critiques :")
    st.write("")
    st.markdown(
        """
    * La différence de données disponibles selon les joueurs
    * Les performances des modèles sont très dépendantes du profil du joueur
    """)

    st.header("Pistes d'amélioration :")
    st.markdown("\n")
    st.write("Dans l'immédiat, nous aurions voulu jouer sur les métriques de chaque joueur pour chaque modèle. Nos résultats ont montré une grande variabilité dans les recalls pour les tirs réussis. L'objectif aurait été d'améliorer les modèles afin qu'ils prédisent mieux les tirs réussis que les tirs manqués.")
    st.markdown("\n")
    st.write("Pour aller plus loin, nous aurions souhaité effectuer des modélisations sur le dataset 2 et la variable cible quantitative “pts” (point) dans le but de faire des modèles capables de prédire le nombre de points en fonction par exemple du poste du joueur.")
    st.markdown("\n")
    st.dataframe(season_stat.head())
    st.markdown("\n")
    st.write("Nous aurions également pu utiliser le Webscraping afin d’augmenter nos données dans le but d’obtenir une homogénéité des données disponibles en fonction des joueurs.")
    st.markdown("\n")
    st.write("Enfin, si le projet s'inscrivait un peu plus dans la durée, nous aurions pu interroger différents joueurs de basket amateur par exemple dans le but de recueillir des pistes de variables supplémentaires se rapprochant plus de la réalité du jeu.")
    st.markdown("\n")   

if selected == "Remerciement":
    st.header("Remerciement :")
    st.markdown("\n")
    st.write("Nous tenons tout d'abord à remercier l'équipe de Datascientest pour sa réactivité et son expertise, et en particulier notre chef de cohorte Antoine qui nous a guidé tout au long de notre travail et s'est rendu constamment disponible.")
    st.markdown("\n")
    st.header("A propos de la team :")
    st.info("""Le projet a été réalisé par trois futures Data Scientist (Promotion continue Septembre 2022) \n
    Amine Chakli : https://www.linkedin.com/in/amine-chakli-41878b1b8/ \n
    Pierre Ndjiki : https://www.linkedin.com/in/pierrendjiki/  \n
    David Tewodrose : https://www.linkedin.com/in/david-tewodrose-85a59195/""")
    st.markdown("\n")
    st.write("Si jamais vous avez des question n'hésitez pas à nous contacter !")
