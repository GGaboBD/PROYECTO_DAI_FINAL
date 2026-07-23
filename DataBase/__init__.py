from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

from .db_ventas import *
#from .db_sucursal import *
#from .db_servicio import *
# ...etc