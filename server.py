from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
ROOT=Path(__file__).resolve().parent
os.chdir(ROOT)
if __name__=="__main__":
    port=8000
    print(f"FOLIÉ running at http://localhost:{port}")
    ThreadingHTTPServer(("0.0.0.0",port),SimpleHTTPRequestHandler).serve_forever()
