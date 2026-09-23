import sys
from Services import PersonaService

# Register alias in sys.modules so both Services.personaService and Services.PersonaService work
sys.modules['Services.personaService'] = PersonaService
personaService = PersonaService
