import streamlit as st

st.title("VAK Quiz")

# Initialize counters
v, a, k = 0, 0, 0

qs1 = st.radio("1. What comes to your mind when you hear the word 'bike'?",
               ['The feeling of riding', 'Sound of bike', 'Picture of bike'], index=None)
if qs1 == 'Picture of bike':
    v += 1
elif qs1 == 'Sound of bike':
    a += 1
elif qs1 == 'The feeling of riding':
    k += 1

# --- Question 2 ---
qs2 = st.radio("2. When you are learning a new skill, you prefer:",
               ['Listening to instructions', 'Watching a demo', 'Trying it yourself'], index=None)
if qs2 == 'Watching a demo':
    v += 1
elif qs2 == 'Listening to instructions':
    a += 1 
elif qs2 == 'Trying it yourself':
    k += 1

# --- Question 3 ---
qs3 = st.radio("3. When you are lost, what helps you most?",
               ['A physical map', 'Asking someone for directions', 'Walking until it feels right'], index=None)
if qs3 == 'A physical map':
    v += 1
elif qs3 == 'Asking someone for directions':
    a += 1
elif qs3 == 'Walking until it feels right':
    k += 1

# --- Question 4 ---
qs4 = st.radio("4. How do you prefer to relax?",
               ['Doing exercise or a hobby', 'Watching a movie', 'Listening to music'], index=None)
if qs4 == 'Watching a movie':
    v += 1
elif qs4 == 'Listening to music':
    a += 1
elif qs4 == 'Doing exercise or a hobby':
    k += 1

# --- Question 5 ---
qs5 = st.radio("5. When you spell a word, you usually:",
               ['Sound it out', 'Write it down to feel it', 'Visualize it in your head'], index=None)
if qs5 == 'Visualize it in your head':
    v += 1
elif qs5 == 'Sound it out':
    a += 1
elif qs5 == 'Write it down to feel it':
    k += 1

# --- Question 6 ---
qs6 = st.radio("6. Which environment distracts you most?",
               ['A messy room', 'Uncomfortable seating', 'Background noise'], index=None)
if qs6 == 'A messy room':
    v += 1
elif qs6 == 'Background noise':
    a += 1
elif qs6 == 'Uncomfortable seating':
    k += 1

# --- Question 7 ---
qs7 = st.radio("7. When meeting someone new, you first notice:",
               ['Their voice/accent', 'Their handshake/vibe', 'Their clothes/face'], index=None)
if qs7 == 'Their clothes/face':
    v += 1
elif qs7 == 'Their voice/accent':
    a += 1
elif qs7 == 'Their handshake/vibe':
    k += 1

# --- Question 8 ---
qs8 = st.radio("8. To remember a phone number, you:",
               ['See the numbers in your mind', 'Call it out loud', 'Feel the pattern on the keypad'], index=None)
if qs8 == 'See the numbers in your mind':
    v += 1
elif qs8 == 'Call it out loud':
    a += 1
elif qs8 == 'Feel the pattern on the keypad':
    k += 1

# --- Question 9 ---
qs9 = st.radio("9. When reading, you enjoy:",
               ['Action-packed plots', 'Descriptive imagery', 'Character dialogue'], index=None)
if qs9 == 'Descriptive imagery':
    v += 1
elif qs9 == 'Character dialogue':
    a += 1
elif qs9 == 'Action-packed plots':
    k += 1

# --- Question 10 ---
qs10 = st.radio("10. When assembling furniture, you:",
                ['Read the manual aloud', 'Follow the pictures', 'Start building immediately'], index=None)
if qs10 == 'Follow the pictures':
    v += 1
elif qs10 == 'Read the manual aloud':
    a += 1
elif qs10 == 'Start building immediately':
    k += 1

# --- Question 11 ---
qs11 = st.radio("11. Your favorite type of gift is:",
                ['Something useful/physical', 'Something beautiful to look at', 'A music/audio gift'], index=None)
if qs11 == 'Something beautiful to look at':
    v += 1
elif qs11 == 'A music/audio gift':
    a += 1
elif qs11 == 'Something useful/physical':
    k += 1

# --- Question 12 ---
qs12 = st.radio("12. When you are angry, you tend to:",
                ['Pace or slam doors', 'Go silent and stare', 'Shout or vent verbally'], index=None)
if qs12 == 'Go silent and stare':
    v += 1
elif qs12 == 'Shout or vent verbally':
    a += 1
elif qs12 == 'Pace or slam doors':
    k += 1

# --- Question 13 ---
qs13 = st.radio("13. In a classroom, you prefer:",
                ['Hands-on activities', 'Slides and diagrams', 'Lectures and discussions'], index=None)
if qs13 == 'Slides and diagrams':
    v += 1
elif qs13 == 'Lectures and discussions':
    a += 1
elif qs13 == 'Hands-on activities':
    k += 1

# --- Question 14 ---
qs14 = st.radio("14. When you are happy, you:",
                ['Sing or talk a lot', 'Jump for joy/hug', 'Smile a lot'], index=None)
if qs14 == 'Smile a lot':
    v += 1
elif qs14 == 'Sing or talk a lot':
    a += 1
elif qs14 == 'Jump for joy/hug':
    k += 1

# --- Question 15 ---
qs15 = st.radio("15. To memorize a speech, you:",
                ['Walk around while speaking', 'Read it over and over', 'Record it and listen back'], index=None)
if qs15 == 'Read it over and over':
    v += 1
elif qs15 == 'Record it and listen back':
    a += 1
elif qs15 == 'Walk around while speaking':
    k += 1

# --- Question 16 ---
qs16 = st.radio("16. When choosing food, you care about:",
                ['The texture and heat', 'The presentation/color', 'What people recommend'], index=None)
if qs16 == 'The presentation/color':
    v += 1
elif qs16 == 'What people recommend':
    a += 1
elif qs16 == 'The texture and heat':
    k += 1

# --- Question 17 ---
qs17 = st.radio("17. When you think of a beach, you first think of:",
                ['The blue water/sand', 'The sound of waves', 'The feel of sand and sun'], index=None)
if qs17 == 'The blue water/sand':
    v += 1
elif qs17 == 'The sound of waves':
    a += 1
elif qs17 == 'The feel of sand and sun':
    k += 1

# --- Question 18 ---
qs18 = st.radio("18. You find it easiest to focus when:",
                ['You are moving/fidgeting', 'It is very quiet', 'The lighting is perfect'], index=None)
if qs18 == 'The lighting is perfect':
    v += 1
elif qs18 == 'It is very quiet':
    a += 1
elif qs18 == 'You are moving/fidgeting':
    k += 1

# --- Question 19 ---
qs19 = st.radio("19. When solving a problem, you:",
                ['Make a list/diagram', 'Talk it out', 'Try different movements/actions'], index=None)
if qs19 == 'Make a list/diagram':
    v += 1
elif qs19 == 'Talk it out':
    a += 1
elif qs19 == 'Try different movements/actions':
    k += 1

# --- Question 20 ---
qs20 = st.radio("20. When you dream, you remember:",
                ['The conversations', 'The physical sensations', 'The colors and scenes'], index=None)
if qs20 == 'The colors and scenes':
    v += 1
elif qs20 == 'The conversations':
    a += 1
elif qs20 == 'The physical sensations':
    k += 1

# --- Question 21 ---
qs21 = st.radio("21. In a museum, you prefer:",
                ['Audio guides', 'Looking at the exhibits', 'Interactive displays'], index=None)
if qs21 == 'Looking at the exhibits':
    v += 1
elif qs21 == 'Audio guides':
    a += 1
elif qs21 == 'Interactive displays':
    k += 1

# --- Question 22 ---
qs22 = st.radio("22. When buying a car, you look for:",
                ['The engine sound/stereo', 'Comfortable seats/drive', 'The sleek design'], index=None)
if qs22 == 'The sleek design':
    v += 1
elif qs22 == 'The engine sound/stereo':
    a += 1
elif qs22 == 'Comfortable seats/drive':
    k += 1

# --- Question 23 ---
qs23 = st.radio("23. When teaching others, you:",
                ['Explain it verbally', 'Guide them physically', 'Draw a picture'], index=None)
if qs23 == 'Draw a picture':
    v += 1
elif qs23 == 'Explain it verbally':
    a += 1
elif qs23 == 'Guide them physically':
    k += 1

# --- Question 24 ---
qs24 = st.radio("24. When you are bored, you:",
                ['Doodle on paper', 'Talk to yourself', 'Fidget or walk around'], index=None)
if qs24 == 'Doodle on paper':
    v += 1
elif qs24 == 'Talk to yourself':
    a += 1
elif qs24 == 'Fidget or walk around':
    k += 1

# --- Question 25 ---
qs25 = st.radio("25. To remember a movie, you recall:",
                ['The music and lines', 'The emotions/action', 'The visual scenes'], index=None)
if qs25 == 'The visual scenes':
    v += 1
elif qs25 == 'The music and lines':
    a += 1
elif qs25 == 'The emotions/action':
    k += 1

# --- Question 26 ---
qs26 = st.radio("26. When learning a dance, you:",
                ['Watch the instructor', 'Listen to the rhythm', 'Feel the body movement'], index=None)
if qs26 == 'Watch the instructor':
    v += 1
elif qs26 == 'Listen to the rhythm':
    a += 1
elif qs26 == 'Feel the body movement':
    k += 1

# --- Question 27 ---
qs27 = st.radio("27. Which describes your memory best?",
                ['Faces', 'Names', 'Experiences'], index=None)
if qs27 == 'Faces':
    v += 1
elif qs27 == 'Names':
    a += 1
elif qs27 == 'Experiences':
    k += 1

# --- Question 28 ---
qs28 = st.radio("28. When you work on a computer, you dislike:",
                ['Bad screen resolution', 'Noisy fans/keyboards', 'An uncomfortable desk'], index=None)
if qs28 == 'Bad screen resolution':
    v += 1
elif qs28 == 'Noisy fans/keyboards':
    a += 1
elif qs28 == 'An uncomfortable desk':
    k += 1

# --- Question 29 ---
qs29 = st.radio("29. When thinking of a song, you think of:",
                ['The music video', 'The lyrics/melody', 'How it makes you dance'], index=None)
if qs29 == 'The music video':
    v += 1
elif qs29 == 'The lyrics/melody':
    a += 1
elif qs29 == 'How it makes you dance':
    k += 1

# --- Question 30 ---
qs30 = st.radio("30. Your main way of processing info is:",
                ['Reading/Seeing', 'Hearing/Speaking', 'Doing/Feeling'], index=None)
if qs30 == 'Reading/Seeing':
    v += 1
elif qs30 == 'Hearing/Speaking':
    a += 1
elif qs30 == 'Doing/Feeling':
    k += 1

if st.button("get result"):

    st.success(f"Visual: {v/30*100}%")

    st.success(f"Auditory: {a/30*100}%")

    st.success(f"Kinaesthetic: {k/30*100}%")