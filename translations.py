language = 'en'
en = 'en'
fi = 'fi'

def toggle_language():
    """Toggles the language of the program between the two available languages"""
    global language
    current_language = language
    language = 'fi' if current_language == 'en' else 'en'

def get_string(string: str) -> str:
    """Provides the string to be printed with the chosen translation
        Args:
            string (str): A string that is linked to the string to be printed
        Returns:
            A string"""
    if string not in strings:
        return string
    if language not in strings[string]:
        return strings[string]['en']
    return strings[string][language]
    

strings = {
    'menu': {
        en: f'''
            1. Begin review     5. New deck
            2. Card operations  6. Options
            3. View cards       7. Statistics
            4. Choose deck      8. Quit
            ''',
        fi: f'''
            1. Aloita kertaus       5. Uusi pakka
            2. Käsittele kortteja   6. Asetukset
            3. Tarkastele kortteja  7. Statistiikkaa
            4. Valitse pakka        8. Sulje ohjelma
            '''
    },
    'cardMenu': {
        en: f'''
        Card operations
            1. Add cards
            2. View cards
            3. Update cards
            4. Delete cards
            ''',
        fi: f'''
        Korttien käsittely
            1. Lisää kortteja
            2. Tarkastele kortteja
            3. Muokkaa kortteja
            4. Poista kortteja'''
    },
    'search': {
        en: f'''
            1. Search by text
            2. Search by ID
            ''',
        fi: f'''
            1. Etsi tekstillä
            2. Etsi ID:llä
            '''
    },
    'options': {
        en: f'''
            ----USER OPTIONS----
            1. Toggle language (English | Finnish)
            2. Return
            ''',
        fi: f'''
            ----KÄYTTÄJÄASETUKSET----
            1. Vaihda kieltä (Englanti | Suomi)
            2. Palaa takaisin
            '''
    },
    'toggledLanguage': { 
        en: 'Language set to English', 
        fi: 'Kieli vaihdettu Suomeksi'
    },
    'currentlyActiveDeck': {
        en: 'Currently active deck: ',
        fi: 'Nykyinen pakka: '
    },
    'goodbye': {
        en: 'Goodbye',
        fi: 'Heihei'
    },
    'card': {
        en: 'Card',
        fi: 'Kortti'
    },
    'deckName': {
        en: 'Deck name',
        fi: 'Pakan nimi'
    },
    'selectAction': {
        en: 'Select action',
        fi: 'Valitse toiminto'
    },
    'correct': {
        en: 'Correct',
        fi: 'Oikein'
    },
    'incorrectAnswer': {
        en: 'Incorrect. Correct answer is',
        fi: 'Väärin. Oikea vastaus on'
    },
    'markAsCorrect': {
        en: 'Mark as correct?',
        fi: 'Merkitse vastaus oikeaksi?'
    },
    'markedAsCorrect': {
        en: 'Answer was marked as correct',
        fi: 'Vastaus merkittiin oikeaksi'
    },
    'markedAsIncorrect': {
        en: 'Answer was marked as incorrect',
        fi: 'Vastaus merkittiin vääräksi'
    },
    'score': {
        en: 'Score',
        fi: 'Pistetilanne'
    },
    'beginReview': {
        en: 'The review has begun. You may quit by typing the command "!quit"',
        fi: 'Harjoitus on alkanut. Voit lopettaa komennolla "!quit"'
    },
    'endOfReview': {
        en: 'The review has ended',
        fi: 'Harjoitus on ohi'
    },
    'typeAnswer': {
        en: 'Type your answer',
        fi: 'Kirjoita vastauksesi'
    },
    'reviewCancelled': {
        en: 'Review cancelled',
        fi: 'Harjoitus keskeytetty'
    },
    'front': {
        en: 'Front',
        fi: 'Etupuoli'
    },
    'back': {
        en: 'Back',
        fi: 'Takapuoli'
    },
    'errorExclamationMark': {
        en: 'A card may not start with an exclamation mark (!)',
        fi: 'Kortin tekstiä ei voi aloittaa huutomerkillä (!)'
    },
    'errorCardTooSimilar': {
        en: 'Card is too similar to another card',
        fi: 'Kortti muistuttaa liikaa aikaisemmin lisättyä korttia'
    },
    'continueAdding': {
        en: 'Continue adding cards',
        fi: 'Jatka korttien lisäystä'
    },
    'finishAdding': {
        en: 'Finished adding cards',
        fi: 'Korttien lisääminen lopetettu'
    },
    'createdDeck': {
        en: 'Created a new deck named',
        fi: 'Luotu uusi korttipakka nimeltään'
    },
    'returnToMenu': {
        en: 'Return to main menu by pressing enter',
        fi: 'Palaa takaisin päävalikkoon painamalla enter-painiketta'
    }
}