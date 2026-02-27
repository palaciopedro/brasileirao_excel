from services.api_service import get_standings
from services.excel_service import export_to_excel

standings = get_standings()
export_to_excel(standings)