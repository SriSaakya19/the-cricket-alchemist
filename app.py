import streamlit as st
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="The Cricket Alchemist - Pure Black Intelligence Lab",
    page_icon="🏏",
    layout="wide"
)

# Custom Dark Mode Styling with Interactive Red Active Tabs & Built by Sri Saakya Footer
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    
    /* Unselected tabs styling (Dark) */
    .stTabs [data-baseweb="tab"] {
        color: #A0AEC0 !important;
        background-color: #1a2234 !important;
        border-radius: 6px;
        padding: 10px 18px;
        font-weight: 600;
        border: 1px solid #2d3748 !important;
    }
    
    /* Active/Clicked tab styling (Turns Red dynamically) */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #FFFFFF !important;
        background-color: #9B2C2C !important;
        border-bottom: 3px solid #FF0000 !important;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.6);
    }

    /* Fix selectbox label and dropdown text color */
    .stSelectbox label, .stTextInput label {
        color: #00FFFF !important;
        font-weight: 700;
        font-size: 1.1rem;
    }
    
    div[data-baseweb="select"] > div {
        color: #FFFFFF !important;
        background-color: #1a2234 !important;
        border: 1px solid #00FFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header Title
st.markdown("<h1 style='color: #00FFFF; text-align: left;'>THE CRICKET ALCHEMIST — PURE BLACK INTELLIGENCE LAB</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #a0aec0;'>India vs West Indies 2026-27 | Next-Gen Tactical Warfare & Telemetry Dashboard</h4>", unsafe_allow_html=True)
st.markdown("---")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs([
    "1. PLAYER DNA & MATRIX", 
    "2. VENUE & PITCH TELEMETRY", 
    "3. CAPTAIN'S WINNING WAR ROOM"
])

# ---------------------------------------------------------
# TAB 1: PLAYER DNA & MATRIX (Complete ICC Squad List)
# ---------------------------------------------------------
with tab1:
    st.markdown("### Deep Squad Analytics & Vulnerability Mapping")
    
    # Complete Official Squad Database from Screenshot
    squad_database = {
        "SHUBMAN GILL (C)": {
            "role": "Opening Batter & Captain",
            "avg": 52.4,
            "sr": 95.6,
            "metrics": [80, 88, 92, 94, 85],
            "vulnerability": "Wide moving deliveries outside off-stump",
            "pitch_compatibility": "High-scoring flat decks with good bounce",
            "pros": ["Flawless textbook technique", "Rotates strike exceptionally well", "Anchors innings effortlessly"],
            "cons": ["Takes time to accelerate initially", "Prone to poking at deliveries outside off"],
            "strategy": "Focus on playing straight down the ground during powerplay."
        },
        "GURNOOR BRAR": {
            "role": "Fast Bowler",
            "avg": 14.5,
            "sr": 70.0,
            "metrics": [85, 55, 90, 76, 80],
            "vulnerability": "Length balls hit back over his head if pace drops",
            "pitch_compatibility": "Bounce-friendly tracks with initial zip",
            "pros": ["Extracts steep bounce from a height", "Aggressive enforcer role"],
            "cons": ["Can leak runs if line is slightly strayed"],
            "strategy": "Hit hard lengths on a back-of-a-length spot to test batter's ribcage."
        },
        "NAMAN DHIR": {
            "role": "Middle-Order All-Rounder",
            "avg": 35.0,
            "sr": 142.0,
            "metrics": [88, 75, 82, 74, 83],
            "vulnerability": "Sharp incoming spin from leg-spinners",
            "pitch_compatibility": "Batting paradises with even bounce",
            "pros": ["Destructive power-hitting capabilities", "Clears boundaries with ease"],
            "cons": ["Can get out playing rash strokes early on"],
            "strategy": "Capitalize on death overs with explosive pull and lofted shots."
        },
        "RUTURAJ GAIKWAD": {
            "role": "Opening Batter",
            "avg": 45.1,
            "sr": 98.2,
            "metrics": [82, 92, 85, 90, 84],
            "vulnerability": "Early swing movement into the pads",
            "pitch_compatibility": "True batting tracks with good stroke play",
            "pros": ["Elegant timing", "Patience to build mammoth innings"],
            "cons": ["Slower strike rate acceleration in initial 10 balls"],
            "strategy": "Anchor one end while exploiting gaps in the powerplay ring."
        },
        "RAVINDRA JADEJA": {
            "role": "All-Rounder",
            "avg": 32.6,
            "sr": 88.5,
            "metrics": [75, 95, 80, 92, 94],
            "vulnerability": "Lofted hits straight down the ground against flight",
            "pitch_compatibility": "Spin-friendly surfaces with variable bounce",
            "pros": ["Masterclass left-arm spin economy", "Lightning-fast fielding", "Clutch finisher"],
            "cons": ["Less effective on absolute flat highways"],
            "strategy": "Dart balls quickly into the pitch to restrict boundary options."
        },
        "YASHASVI JAISWAL": {
            "role": "Opening Batter",
            "avg": 48.0,
            "sr": 105.4,
            "metrics": [90, 82, 88, 80, 86],
            "vulnerability": "Sharp seam movement away and left-arm angle",
            "pitch_compatibility": "Bounce-friendly tracks with true carry",
            "pros": ["Fearless intent in powerplays", "High boundary percentage"],
            "cons": ["Prone to flashing outside off-stump"],
            "strategy": "Keep high intent while respecting first two overs of swing."
        },
        "DHRUV JUREL": {
            "role": "Wicket-Keeper Batter",
            "avg": 39.0,
            "sr": 96.0,
            "metrics": [78, 88, 84, 85, 91],
            "vulnerability": "Wide yorkers in death overs",
            "pitch_compatibility": "Balanced tracks offering steady bounce",
            "pros": ["Impeccable temperament under pressure", "Clean hitting against spin"],
            "cons": ["Limited international experience in finishing roles"],
            "strategy": "Rotate strike safely in middle overs before opening up."
        },
        "VIRAT KOHLI": {
            "role": "Top-Order Masterclass Batter",
            "avg": 57.3,
            "sr": 93.8,
            "metrics": [94, 96, 92, 99, 98],
            "vulnerability": "Wide fourth-stump deliveries asking for a push",
            "pitch_compatibility": "All conditions; master of chases",
            "pros": ["Legendary run-chase capability", "Stellar conversion rate", "Elite fitness"],
            "cons": ["Rarely vulnerable, minor weakness against sharp away spin early"],
            "strategy": "Run hard between wickets, anchor the innings and dictate chase tempos."
        },
        "PRASIDH KRISHNA": {
            "role": "Fast Bowler",
            "avg": 18.2,
            "sr": 72.0,
            "metrics": [86, 50, 88, 75, 82],
            "vulnerability": "Pitched up full deliveries on small grounds",
            "pitch_compatibility": "Extra bounce pitches allowing steep carry",
            "pros": ["Tall release point", "Generates uncomfortable bounce"],
            "cons": ["Can concede runs if line drifts down leg"],
            "strategy": "Hit a heavy length outside off-stump to force edge catches."
        },
        "AUQIB NABI": {
            "role": "Emerging Fast Bowler",
            "avg": 20.0,
            "sr": 75.0,
            "metrics": [82, 52, 85, 74, 79],
            "vulnerability": "Pace hitting down the ground by established anchors",
            "pitch_compatibility": "Seam-friendly helpful decks",
            "pros": ["Hungry for wickets", "Disciplined line and length control"],
            "cons": ["Lacks veteran death-over variations"],
            "strategy": "Concentrate on swing during powerplay spells."
        },
        "KL RAHUL": {
            "role": "Wicket-Keeper Batter",
            "avg": 49.8,
            "sr": 88.9,
            "metrics": [85, 94, 90, 88, 87],
            "vulnerability": "In-seaming deliveries targeting top of off-stump",
            "pitch_compatibility": "True batting tracks",
            "pros": ["Classy strokeplay", "Absorbs pressure masterfully in middle overs"],
            "cons": ["Can get stuck in a defensive shell occasionally"],
            "strategy": "Play proper cricketing shots through cover and mid-wicket."
        },
        "NITISH KUMAR REDDY": {
            "role": "Explosive All-Rounder",
            "avg": 38.5,
            "sr": 134.2,
            "metrics": [92, 70, 85, 78, 88],
            "vulnerability": "Wide slower-ball variations in death overs",
            "pitch_compatibility": "Pace-friendly tracks with initial zip",
            "pros": ["Massive lower-order power-hitting", "Medium-pace wicket-taker"],
            "cons": ["Inexperience against high-quality mystery spin"],
            "strategy": "Wait for length balls to launch straight; hit hard lengths when bowling."
        },
        "ROHIT SHARMA": {
            "role": "Opening Batter",
            "avg": 49.2,
            "sr": 92.1,
            "metrics": [85, 90, 75, 88, 80],
            "vulnerability": "Incoming Arm Pace / Short Ball targeting body",
            "pitch_compatibility": "True Batting Tracks",
            "pros": ["Destructive powerplay hitting", "Masterclass against spinners"],
            "cons": ["Vulnerable early on against sharp inswingers"],
            "strategy": "Attack powerplay field restrictions with lofted drives."
        },
        "MOHAMMED SIRAJ": {
            "role": "Lead Fast Bowler",
            "avg": 21.4,
            "sr": 74.0,
            "metrics": [95, 60, 92, 86, 90],
            "vulnerability": "Flat pitches with zero swing movement",
            "pitch_compatibility": "Overcast conditions with heavy swing",
            "pros": ["Fiery aggression", "Lethal first-spell seam movement"],
            "cons": ["Can leak runs if he searches too hard for wickets"],
            "strategy": "Target the seam aggressively to pick early breakthrough wickets."
        },
        "KULDEEP YADAV": {
            "role": "Wrist-Spinner (Mystery)",
            "avg": 12.1,
            "sr": 80.0,
            "metrics": [60, 98, 70, 86, 90],
            "vulnerability": "Using feet aggressively down the track against flight",
            "pitch_compatibility": "Dry surfaces offering turn and bounce",
            "pros": ["Genuine wicket-taker in middle overs", "Clever googlies"],
            "cons": ["Can concede boundaries if length is pushed short"],
            "strategy": "Maintain teasing loop just outside off-stump."
        }
    }

    selected_player = st.selectbox("Select Target Player for Telemetry Analysis", list(squad_database.keys()))
    player_info = squad_database[selected_player]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"### 📄 Dossier: {selected_player}")
        st.markdown(f"**Role:** {player_info['role']}")
        st.markdown(f"**Batting Average:** {player_info['avg']}")
        st.markdown(f"**Strike Rate:** {player_info['sr']}")
        st.markdown(f"**Vulnerability Vector:** `{player_info['vulnerability']}`")
        st.markdown(f"**Pitch Compatibility:** {player_info['pitch_compatibility']}")
        
        st.success(f"**Strengths (Pros):**\n" + "\n".join([f"- {p}" for p in player_info['pros']]))
        st.error(f"**Flaws & Weaknesses (Cons):**\n" + "\n".join([f"- {c}" for c in player_info['cons']]))

    with col2:
        st.markdown("### 📊 Player Efficiency Spectrum & Graph")
        
        categories = ['Powerplay', 'Spin Play', 'Pace Handling', 'Consistency', 'Pressure']
        fig = go.Figure(data=[
            go.Bar(
                x=categories,
                y=player_info['metrics'],
                marker_color='#00FFFF',
                text=player_info['metrics'],
                textposition='auto',
            )
        ])
        fig.update_layout(
            plot_bgcolor='#0b0f19',
            paper_bgcolor='#0b0f19',
            font=dict(color='white'),
            yaxis=dict(range=[0, 100], showgrid=True, gridcolor='#1a2234'),
            xaxis=dict(showgrid=False),
            margin=dict(t=20, b=20, l=20, r=20),
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.warning(f"**Custom Alchemist Execution Strategy:**\n{player_info['strategy']}")

# ---------------------------------------------------------
# TAB 2: VENUE & PITCH TELEMETRY
# ---------------------------------------------------------
with tab2:
    st.markdown("### Series Venues & Conditions Matrix (2026-27 Home Season)")
    
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        st.markdown("#### 🏟️ ODI Series Venues (Sept 27 - Oct 3)")
        st.markdown("- **Thiruvananthapuram:** Seam movement early, settles into true batting track.")
        st.markdown("- **Guwahati:** High-scoring deck, lights factor aids chasing teams.")
        st.markdown("- **Chandigarh:** Bounce-friendly pitch; pacers get initial zip.")

    with col_v2:
        st.markdown("#### ⚡ T20I Series Venues (Oct 6 - Oct 17)")
        st.markdown("- **Lucknow & Ranchi:** Grip for spinners in middle overs.")
        st.markdown("- **Indore & Hyderabad:** Pure batting paradises (200+ expected).")
        st.markdown("- **Bengaluru:** Electric atmosphere, short boundaries, high-thrill chase.")

# ---------------------------------------------------------
# TAB 3: CAPTAIN'S WINNING WAR ROOM
# ---------------------------------------------------------
with tab3:
    st.markdown("### Strategic Blueprint: How to Dominate & Win the Series")
    
    col_w1, col_w2 = st.columns(2)
    
    with col_w1:
        st.markdown("#### 🎯 Powerplay Control (Overs 1–10)")
        st.markdown("- **Tighten Lines:** Target off-stump channel to force false drives.")
        st.markdown("- **Aggressive Ring:** Vacuum up singles to build mounting dot-ball pressure.")
        st.markdown("- **Early Strikes:** Utilize new-ball swing to dismantle top-order anchors.")

    with col_w2:
        st.markdown("#### 🌪️ Middle-Overs Spin Choke (Overs 11–40)")
        st.markdown("- **Smart Rotation:** Alternate spin angles (Wrist-spin vs Finger-spin).")
        st.markdown("- **Pace Variations:** Mix slower balls and drift to starve boundary options.")
        st.markdown("- **Strategic Traps:** Set catchers in deep mid-wicket for aggressive lofts.")

# Footer info with Built by Sri Saakya
st.markdown("---")
st.markdown("<p style='text-align: center; color: #00FFFF; font-weight: 600;'>Built by Sri Saakya | @thecricketalchemist19 Intelligence Lab © 2026-27</p>", unsafe_allow_html=True)