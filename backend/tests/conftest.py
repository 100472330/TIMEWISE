import sys
from pathlib import Path
# Añade la raíz del proyecto al sys.path para que 'backend' se pueda importar
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
