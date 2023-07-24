from supabase_py import create_client

SUPABASE_URL = "https://ndkclxyzvcgqrhzxzouv.supabase.co"  
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5ka2NseHl6dmNncXJoenh6b3V2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTAxMjQ1MzYsImV4cCI6MjAwNTcwMDUzNn0.QZFmEan0WwIT1gnRDBvEmKTe1W0BlMiVBMI10FpSINY"
SUPABASE_HEADERS = {"apikey": SUPABASE_API_KEY}

# Función para crear y retornar el cliente de Supabase
def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_API_KEY)
